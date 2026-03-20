#!/usr/bin/env python3
"""Convert Hugo (Lotus Docs) content to Mintlify MDX format.

Usage:
    python3 scripts/convert.py --src ./content --dst /tmp/mintlify-output
"""

import argparse
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("Missing dependency: pip install pyyaml")

# Hugo front matter keys to drop
REMOVE_KEYS = {"weight", "date", "lastmod", "author", "publishdate", "tags", "toc", "draft"}

# Alert context → MDX component name
CONTEXT_MAP = {
    "warning": "Warning",
    "info": "Info",
    "light": "Note",
    "danger": "Warning",
    "success": "Tip",
    "primary": "Info",
    "secondary": "Note",
}


def normalise_name(name: str) -> str:
    """Strip leading numeric prefix and normalise spaces → hyphens.

    Examples:
        01.getting-started  → getting-started
        1.overview          → overview
        04.survey-design    → survey-design
        my folder           → my-folder
        _index              → (unchanged — handled separately)
    """
    name = re.sub(r"^\d+\.", "", name)   # strip 01. / 1. etc.
    name = re.sub(r"^\d+_", "", name)   # strip 01_ / 1_ etc.
    name = re.sub(r"^\d+-", "", name)   # strip 01- / 1- etc.
    name = name.replace(" ", "-")
    return name


def convert_front_matter(raw_yaml: str) -> str:
    """Keep only allowed front matter keys, return cleaned YAML string."""
    try:
        data = yaml.safe_load(raw_yaml) or {}
    except yaml.YAMLError:
        return raw_yaml  # malformed — return as-is

    cleaned = {k: v for k, v in data.items() if k not in REMOVE_KEYS and v is not None}
    if not cleaned:
        return ""
    return yaml.dump(cleaned, allow_unicode=True, default_flow_style=False).rstrip()


def mdx_component(context: str) -> str:
    return CONTEXT_MAP.get(context.lower(), "Note")


def convert_table_shortcodes(text: str) -> str:
    """Remove {{< table >}} / {{< /table >}} wrapper tags."""
    text = re.sub(r"\{\{<\s*/?table\s*>\}\}\n?", "", text)
    return text


def convert_self_closing_alerts(text: str) -> str:
    """Convert {{< alert ... text="..." />}} to MDX components."""
    pattern = re.compile(r"\{\{<\s*alert\s+(.*?)/>\}\}", re.DOTALL)

    def replace(m):
        attrs = m.group(1)
        ctx_m = re.search(r'context="([^"]*)"', attrs)
        context = ctx_m.group(1) if ctx_m else "info"
        component = mdx_component(context)

        # Extract text="..." value — use \b to avoid matching "context=..." substring
        text_m = re.search(r'\btext="((?:[^"\\]|\\.)*)"', attrs)
        inner = text_m.group(1).replace('\\"', '"') if text_m else ""

        return f"<{component}>{inner}</{component}>"

    return pattern.sub(replace, text)


def convert_block_alerts(text: str) -> str:
    """Convert {{% alert ... %}}...{{% /alert %}} to MDX components."""
    pattern = re.compile(r"\{\{%\s*alert\s+(.*?)%\}\}(.*?)\{\{%\s*/alert\s*%\}\}", re.DOTALL)

    def replace(m):
        attrs = m.group(1)
        inner = m.group(2)
        ctx_m = re.search(r'context="([^"]*)"', attrs)
        context = ctx_m.group(1) if ctx_m else "info"
        component = mdx_component(context)
        return f"<{component}>\n{inner.strip()}\n</{component}>"

    return pattern.sub(replace, text)


def convert_image_paths(text: str) -> str:
    """Convert relative image paths to absolute /images/<filename>."""

    def replace(m):
        alt = m.group(1)
        img_path = m.group(2)
        filename = Path(img_path).name
        return f"![{alt}](/images/{filename})"

    # Matches: ![alt](images/possibly/nested/file.ext)
    return re.sub(r"!\[([^\]]*)\]\(images/([^\)]+)\)", replace, text)


def convert_file(src: Path, dst: Path) -> None:
    """Read a Hugo .md file, convert it, write .mdx to dst."""
    text = src.read_text(encoding="utf-8")

    # Parse and rewrite YAML front matter
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm_raw = text[3:end]
            body = text[end + 4:]
            fm_cleaned = convert_front_matter(fm_raw)
            if fm_cleaned:
                text = f"---\n{fm_cleaned}\n---\n{body}"
            else:
                text = body

    # Shortcode conversions
    text = convert_table_shortcodes(text)
    text = convert_self_closing_alerts(text)
    text = convert_block_alerts(text)

    # Image path fix
    text = convert_image_paths(text)

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8")


def normalise_path(rel: Path) -> Path:
    """Normalise each path component by stripping numeric prefixes.

    _index.md → index.mdx
    1.overview.md → overview.mdx
    01.getting-started/ → getting-started/
    """
    parts = list(rel.parts)
    new_parts = []
    for i, part in enumerate(parts):
        is_last = i == len(parts) - 1
        if is_last and part.endswith(".md"):
            stem = part[:-3]
            if stem == "_index":
                stem = "index"
            else:
                stem = normalise_name(stem)
            new_parts.append(stem + ".mdx")
        else:
            new_parts.append(normalise_name(part))
    return Path(*new_parts)


def main():
    parser = argparse.ArgumentParser(description="Hugo → Mintlify MDX converter")
    parser.add_argument("--src", required=True, help="Path to Hugo content/ directory")
    parser.add_argument("--dst", required=True, help="Output directory for MDX files")
    args = parser.parse_args()

    src = Path(args.src)
    dst = Path(args.dst)
    dst.mkdir(parents=True, exist_ok=True)

    total = 0
    errors = []

    for lang_dir in sorted(src.iterdir()):
        if not lang_dir.is_dir():
            continue
        lang = lang_dir.name
        if lang == "docs":
            # content/docs/ contains shared images, not language content
            continue

        docs_dir = lang_dir / "docs"
        if not docs_dir.exists():
            continue

        lang_count = 0
        for md_file in sorted(docs_dir.rglob("*.md")):
            rel = md_file.relative_to(docs_dir)
            norm_rel = normalise_path(rel)
            dst_file = dst / lang / norm_rel
            try:
                convert_file(md_file, dst_file)
                lang_count += 1
            except Exception as e:
                errors.append(f"{md_file}: {e}")

        print(f"  {lang:<10} {lang_count:>4} files")
        total += lang_count

    print(f"\nTotal: {total} files converted")
    if errors:
        print(f"\n{len(errors)} errors:")
        for e in errors:
            print(f"  {e}")


if __name__ == "__main__":
    main()
