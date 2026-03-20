#!/usr/bin/env python3
"""Generate docs.json for Mintlify from the converted MDX file tree.

Usage:
    python3 scripts/gen_docs_json.py --root . --out docs.json
"""

import argparse
import json
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("Missing dependency: pip install pyyaml")

# Language code → display name (from hugo.toml)
LANG_NAMES = {
    "en": "English",
    "vi": "Tiếng Việt",
    "fr": "Français",
    "de": "Deutsch",
    "pt": "Português",
    "es": "Español",
    "zh-hans": "简体中文",
    "ar": "العربية",
    "th": "ไทย",
    "id": "Bahasa Indonesia",
    "km": "ភាសាខ្មែរ",
    "hi": "हिन्दी",
    "ru": "Русский",
    "zh-hant": "繁體中文",
    "ko": "한국어",
    "ja": "日本語",
    "it": "Italiano",
    "nl": "Nederlands",
    "tr": "Türkçe",
    "uk": "Українська",
    "nb": "Norsk Bokmål",
    "da": "Dansk",
    "sv": "Svenska",
    "fi": "Suomi",
    "el": "Ελληνικά",
    "pl": "Polski",
    "cs": "Čeština",
    "sk": "Slovenčina",
    "hu": "Magyar",
    "bg": "Български",
    "sr": "Srpski",
    "sq": "Shqip",
    "lv": "Latviešu",
    "lt": "Lietuvių",
    "te": "తెలుగు",
    "pt-br": "Português (Brasil)",
}

RTL_LANGS = {"ar", "he", "fa", "ur"}

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
    """Convert a slug to a title."""
    return name.replace("-", " ").replace("_", " ").title()


def build_pages(directory: Path, lang: str, root: Path) -> list:
    """Recursively build a Mintlify pages array for a directory."""
    items = []

    # Include index page first
    idx = directory / "index.mdx"
    if idx.exists():
        rel = idx.relative_to(root)
        page_path = str(rel).replace(".mdx", "")
        items.append(page_path)

    # Then all non-index .mdx files, sorted
    for f in sorted(directory.iterdir()):
        if f.is_file() and f.suffix == ".mdx" and f.stem != "index":
            rel = f.relative_to(root)
            page_path = str(rel).replace(".mdx", "")
            items.append(page_path)

    # Then subdirectories as nested groups
    for d in sorted(directory.iterdir()):
        if d.is_dir() and d.name not in SKIP_DIRS:
            sub_idx = d / "index.mdx"
            title = read_title(sub_idx) or humanize(d.name)
            sub_pages = build_pages(d, lang, root)
            if sub_pages:
                items.append({"group": title, "pages": sub_pages})

    return items


def build_lang_navigation(lang: str, root: Path) -> list:
    """Build top-level navigation groups for one language."""
    lang_dir = root / lang
    if not lang_dir.exists():
        return []

    groups = []

    # Section order (matches original Hugo weight order)
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

    for section in section_order:
        section_dir = lang_dir / section
        if not section_dir.exists():
            continue

        idx = section_dir / "index.mdx"
        title = read_title(idx) if lang == "en" else None
        if not title:
            title = humanize(section)

        pages = build_pages(section_dir, lang, root)
        if pages:
            groups.append({"group": title, "pages": pages})

    return groups


def main():
    parser = argparse.ArgumentParser(description="Generate Mintlify docs.json")
    parser.add_argument("--root", default=".", help="Repo root directory")
    parser.add_argument("--out", default="docs.json", help="Output file path")
    args = parser.parse_args()

    root = Path(args.root).resolve()

    # Build navigation for all languages
    languages = []
    for lang_code in LANG_NAMES:
        lang_dir = root / lang_code
        if not lang_dir.exists():
            continue

        groups = build_lang_navigation(lang_code, root)
        if not groups:
            continue

        lang_entry = {
            "language": lang_code,
        }
        if lang_code == "en":
            lang_entry["default"] = True

        lang_entry["groups"] = groups
        languages.append(lang_entry)

        print(f"  {lang_code:<10} {sum(len(g['pages']) for g in groups):>4} nav items")

    # Build complete docs.json
    docs = {
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
            "links": [
                {
                    "label": "rtSurvey",
                    "href": "https://rtsurvey.com"
                }
            ]
        },
        "footer": {
            "socials": {
                "github": "https://github.com/rtsurvey"
            }
        },
        "navigation": {
            "languages": languages
        }
    }

    out_path = root / args.out
    out_path.write_text(json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nWrote {out_path}")
    print(f"Total languages: {len(languages)}")


if __name__ == "__main__":
    main()
