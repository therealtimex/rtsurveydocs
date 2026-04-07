#!/usr/bin/env python3
"""
check-translations.py
Checks _meta.json files across all locales for untranslated menu titles.
Compares against English (pages/) as the reference.

Usage:
  python3 scripts/check-translations.py              # all locales
  python3 scripts/check-translations.py vi fr de     # specific locales
  python3 scripts/check-translations.py --verbose vi # show each untranslated key
"""

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "pages"
LOCALES_DIR = ROOT / "_locales"

# Values that intentionally stay untranslated (proper nouns, brand names, tech terms)
KEEP_AS_IS = {
    # Brand names
    "DigitalOcean", "Linode", "Linode (Akamai)", "Docker", "GitHub", "Keycloak",
    "rtSurvey", "rtCloud", "rtSurvey Cloud", "XForm", "ODK", "KoBoToolbox",
    "WebBox",
    # Acronyms / tech terms kept in English
    "SSL", "SSL Setup", "SSO", "SSO Authentication",
    "HTTPS", "HTTP", "API", "Call API", "HTML Styling",
    "PDF", "CSV", "JSON", "XLSForm", "XML",
    "Android", "iOS", "Power BI", "AWS", "GCP", "Azure",
    "Ubuntu", "MySQL", "PHP", "Apache", "Nginx", "Shiny", "Beanstalkd",
    # Common cognates — identical spelling in many European languages
    "Home", "Support", "Sponsor", "Media",
    "Installation", "Configuration", "Maintenance",
    "Mobile App", "Images", "Analysis",
    "Relevant (Skip Logic)",
    # XForm question type names (international standard — always English)
    "text", "integer", "decimal",
    "select_one", "select_multiple", "select_one_from_file",
    "date / time / datetime",
    "image", "audio", "video", "file",
    "geopoint", "geotrace", "geoshape",
    "barcode", "range", "rank", "note", "hidden",
    "calculate", "trigger", "meta",
}

def load_meta(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}

def extract_strings(meta: dict) -> dict[str, str]:
    """Return {key: title_string} for all translatable entries."""
    result = {}
    for k, v in meta.items():
        if isinstance(v, str):
            result[k] = v
        elif isinstance(v, dict) and "title" in v and isinstance(v["title"], str):
            result[k] = v["title"]
    return result

def find_en_metas() -> list[Path]:
    return sorted(PAGES.rglob("_meta.json"))

def get_locale_meta_path(locale: str, en_meta: Path) -> Path:
    rel = en_meta.relative_to(PAGES)
    return LOCALES_DIR / locale / rel

def check_locale(locale: str, verbose: bool = False) -> dict[str, list[str]]:
    """Returns {rel_path: [untranslated_key, ...]} for a locale."""
    issues: dict[str, list[str]] = {}
    locale_dir = LOCALES_DIR / locale
    if not locale_dir.is_dir():
        return issues

    for en_meta in find_en_metas():
        locale_meta_path = get_locale_meta_path(locale, en_meta)
        if not locale_meta_path.exists():
            continue

        en_strings = extract_strings(load_meta(en_meta))
        locale_strings = extract_strings(load_meta(locale_meta_path))

        untranslated = []
        for key, en_val in en_strings.items():
            locale_val = locale_strings.get(key, "")
            if en_val == locale_val and en_val not in KEEP_AS_IS:
                untranslated.append(key)

        if untranslated:
            rel = str(en_meta.relative_to(PAGES).parent)
            if rel == ".":
                rel = "root"
            issues[rel] = untranslated

    return issues

def main():
    args = sys.argv[1:]
    verbose = "--verbose" in args or "-v" in args
    args = [a for a in args if not a.startswith("-")]

    if args:
        locales = args
    else:
        locales = sorted(d.name for d in LOCALES_DIR.iterdir() if d.is_dir())

    col_w = 12
    print(f"{'LOCALE':<{col_w}}  {'FILE':<30}  {'COUNT':>5}  UNTRANSLATED KEYS")
    print(f"{'-'*col_w}  {'-'*30}  {'-'*5}  {'-'*40}")

    total_issues = 0

    for locale in locales:
        issues = check_locale(locale, verbose)
        locale_total = sum(len(v) for v in issues.values())
        total_issues += locale_total

        if locale_total == 0:
            print(f"{locale:<{col_w}}  {'(all files)':<30}  {'0':>5}  ✓ fully translated")
        elif verbose:
            for path, keys in sorted(issues.items()):
                keys_str = ", ".join(keys)
                print(f"{locale:<{col_w}}  {path:<30}  {len(keys):>5}  {keys_str}")
        else:
            print(f"{locale:<{col_w}}  {'(all files)':<30}  {locale_total:>5}")

    print()
    print(f"Total untranslated menu entries: {total_issues}")
    print(f"Across {len(locales)} locale(s), {len(find_en_metas())} _meta.json files each")
    print()
    print("Tip: python3 scripts/check-translations.py --verbose <locale>")

if __name__ == "__main__":
    main()
