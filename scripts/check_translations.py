#!/usr/bin/env python3
"""
check_translations.py
Compares content/en against every other language directory and reports missing files.
Usage: python3 scripts/check_translations.py [--lang LANG]
"""

import os
import sys
import argparse

CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")
SOURCE_LANG = "en"


def get_md_files(lang_dir):
    result = []
    for root, _, files in os.walk(lang_dir):
        for f in files:
            if f.endswith(".md"):
                full = os.path.join(root, f)
                rel = os.path.relpath(full, lang_dir)
                result.append(rel)
    return set(result)


def main():
    parser = argparse.ArgumentParser(description="Check missing translation files")
    parser.add_argument("--lang", help="Check only this language (e.g. vi, fr)")
    args = parser.parse_args()

    source_dir = os.path.join(CONTENT_DIR, SOURCE_LANG)
    source_files = get_md_files(source_dir)

    all_langs = sorted(
        d for d in os.listdir(CONTENT_DIR)
        if os.path.isdir(os.path.join(CONTENT_DIR, d)) and d != SOURCE_LANG and d != "docs"
    )

    if args.lang:
        if args.lang not in all_langs:
            print(f"Language '{args.lang}' not found. Available: {', '.join(all_langs)}")
            sys.exit(1)
        langs_to_check = [args.lang]
    else:
        langs_to_check = all_langs

    total_missing = 0
    summary = []

    for lang in langs_to_check:
        lang_dir = os.path.join(CONTENT_DIR, lang)
        lang_files = get_md_files(lang_dir)
        missing = sorted(source_files - lang_files)
        extra = sorted(lang_files - source_files)
        total_missing += len(missing)
        summary.append((lang, missing, extra))

    # Print results
    for lang, missing, extra in summary:
        if missing or extra:
            print(f"\n{'='*60}")
            print(f"  {lang}  —  {len(missing)} missing, {len(extra)} extra")
            print(f"{'='*60}")
            if missing:
                print("  MISSING (exists in en, not in this lang):")
                for f in missing:
                    print(f"    - {f}")
            if extra:
                print("  EXTRA (exists here, not in en):")
                for f in extra:
                    print(f"    + {f}")
        else:
            print(f"  {lang}  ✓  complete")

    print(f"\n{'='*60}")
    print(f"Total missing files across {len(langs_to_check)} language(s): {total_missing}")
    print(f"Source (en) has {len(source_files)} files")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
