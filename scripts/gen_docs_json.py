#!/usr/bin/env python3
"""Generate docs.json for Mintlify from the converted MDX file tree.

Usage:
    python3 scripts/gen_docs_json.py --root . --out docs.json
"""

import argparse
import json
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("Missing dependency: pip install pyyaml")

# Only language codes Mintlify actually supports (from their schema enum)
# Maps directory name → Mintlify language code
SUPPORTED_LANGS = {
    "en":      "en",
    "vi":      "vi",
    "fr":      "fr",
    "de":      "de",
    "pt":      "pt",
    "es":      "es",
    "zh-Hans": "zh-Hans",
    "ar":      "ar",
    "id":      "id",
    "hi":      "hi",
    "ru":      "ru",
    "zh-Hant": "zh-Hant",
    "ko":      "ko",
    "ja":      "ja",
    "it":      "it",
    "nl":      "nl",
    "tr":      "tr",
    "uk":      "uk",
    "no":      "no",
    "sv":      "sv",
    "pl":      "pl",
    "cs":      "cs",
    "hu":      "hu",
    "lv":      "lv",
    "pt-BR":   "pt-BR",
}

# Placeholder folder to skip from navigation
SKIP_DIRS = {"section-subfolder"}


def read_title(path: Path):
    """Read the title from an MDX file's front matter."""
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    try:
        data = yaml.safe_load(text[3:end]) or {}
        return data.get("title")
    except yaml.YAMLError:
        return None


def humanize(name: str) -> str:
    return name.replace("-", " ").replace("_", " ").title()


def build_pages(directory: Path, root: Path) -> list:
    """Recursively build a Mintlify pages array for a directory."""
    items = []

    # Index page first
    idx = directory / "index.mdx"
    if idx.exists():
        items.append(str(idx.relative_to(root)).replace(".mdx", ""))

    # Non-index .mdx files, sorted
    for f in sorted(directory.iterdir()):
        if f.is_file() and f.suffix == ".mdx" and f.stem != "index":
            items.append(str(f.relative_to(root)).replace(".mdx", ""))

    # Subdirectories as nested groups
    for d in sorted(directory.iterdir()):
        if d.is_dir() and d.name not in SKIP_DIRS:
            sub_idx = d / "index.mdx"
            title = read_title(sub_idx) or humanize(d.name)
            sub_pages = build_pages(d, root)
            if sub_pages:
                items.append({"group": title, "pages": sub_pages})

    return items


def build_lang_groups(lang_dir: str, root: Path) -> list:
    """Build navigation groups for one language directory."""
    base = root / lang_dir
    if not base.exists():
        return []

    section_order = [
        "getting-started",
        "user-interface",
        "project-management",
        "survey-design",
        "data-collection",
        "data-management",
        "analysis",
        "api-integration",
        "troubleshooting-support",
        "release-update",
    ]

    groups = []
    for section in section_order:
        section_dir = base / section
        if not section_dir.exists():
            continue
        idx = section_dir / "index.mdx"
        title = read_title(idx) if lang_dir == "en" else None
        if not title:
            title = humanize(section)
        pages = build_pages(section_dir, root)
        if pages:
            groups.append({"group": title, "pages": pages})

    return groups


def main():
    parser = argparse.ArgumentParser(description="Generate Mintlify docs.json")
    parser.add_argument("--root", default=".", help="Repo root directory")
    parser.add_argument("--out", default="docs.json", help="Output file path")
    args = parser.parse_args()

    root = Path(args.root).resolve()

    languages = []
    for lang_dir, lang_code in SUPPORTED_LANGS.items():
        groups = build_lang_groups(lang_dir, root)
        if not groups:
            print(f"  {lang_dir:<10} SKIPPED (no content)")
            continue

        # Prepend root index page as the home page for this language
        root_index = root / lang_dir / "index.mdx"
        if root_index.exists():
            home_page = str(root_index.relative_to(root)).replace(".mdx", "")
            groups = [{"group": "Home", "pages": [home_page]}] + groups

        # Each language entry needs "tabs" wrapping the groups
        lang_entry = {"language": lang_code}
        if lang_code == "en":
            lang_entry["default"] = True
        lang_entry["tabs"] = [{"tab": "Documentation", "groups": groups}]
        languages.append(lang_entry)

        total_pages = sum(len(g["pages"]) for g in groups)
        print(f"  {lang_dir:<10} {total_pages:>4} nav items")

    docs = {
        "$schema": "https://mintlify.com/docs.json",
        "name": "rtSurvey Documentation",
        "theme": "mint",
        "logo": {
            "light": "/images/logo-light.png",
            "dark": "/images/logo-dark.png",
            "href": "https://rtsurvey.com"
        },
        "favicon": "/favicon.svg",
        "colors": {
            "primary": "#2563EB",
            "light": "#3B82F6",
            "dark": "#1D4ED8"
        },
        "navbar": {
            "links": [{"label": "rtSurvey", "href": "https://rtsurvey.com"}]
        },
        "footer": {
            "socials": {"github": "https://github.com/rtsurvey"}
        },
        "navigation": {
            "languages": languages
        }
    }

    out_path = root / args.out
    out_path.write_text(json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nWrote {out_path}  ({out_path.stat().st_size // 1024} KB)")
    print(f"Languages: {len(languages)}")


if __name__ == "__main__":
    main()
