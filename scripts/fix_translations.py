#!/usr/bin/env python3
"""
fix_translations.py
For every non-English language:
  1. Rename numbered files/folders to match the clean en structure (via git mv)
  2. Delete files that no longer exist in en (e.g. try-rtsurvey.md)
  3. Stub missing files by copying the English version

Usage:
  python3 scripts/fix_translations.py [--lang LANG] [--dry-run]
"""

import os
import re
import sys
import shutil
import subprocess
import argparse

REPO_DIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT    = os.path.join(REPO_DIR, "content")
SOURCE     = "en"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def strip_number_prefix(name: str) -> str:
    """'01.getting-started' → 'getting-started',  '1.overview.md' → 'overview.md'"""
    m = re.match(r'^\d+\.(.+)$', name)
    return m.group(1) if m else name


def normalize_rel(rel: str) -> str:
    """Normalize every path component of a relative path."""
    parts = rel.replace("\\", "/").split("/")
    return "/".join(strip_number_prefix(p) for p in parts)


def get_files(lang_dir: str) -> dict:
    """Return {rel_path: abs_path} for all .md files under lang_dir."""
    result = {}
    for root, _, files in os.walk(lang_dir):
        for f in files:
            if f.endswith(".md"):
                abs_path = os.path.join(root, f)
                rel = os.path.relpath(abs_path, lang_dir).replace("\\", "/")
                result[rel] = abs_path
    return result


def git_mv(src: str, dst: str, dry_run: bool) -> bool:
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if dry_run:
        print(f"  [mv]  {src}  →  {dst}")
        return True
    r = subprocess.run(["git", "mv", src, dst], cwd=REPO_DIR, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  [ERROR git mv] {r.stderr.strip()}")
        return False
    return True


def git_rm(path: str, dry_run: bool) -> bool:
    if dry_run:
        print(f"  [rm]  {path}")
        return True
    r = subprocess.run(["git", "rm", "-f", path], cwd=REPO_DIR, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  [ERROR git rm] {r.stderr.strip()}")
        return False
    return True


def copy_stub(en_abs: str, dst_abs: str, dry_run: bool):
    if dry_run:
        print(f"  [stub] {dst_abs}")
        return
    os.makedirs(os.path.dirname(dst_abs), exist_ok=True)
    shutil.copy2(en_abs, dst_abs)
    subprocess.run(["git", "add", dst_abs], cwd=REPO_DIR, capture_output=True)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_lang(lang: str, en_files: dict, dry_run: bool):
    lang_dir = os.path.join(CONTENT, lang)
    lang_files = get_files(lang_dir)

    renames  = 0
    deletes  = 0
    stubs    = 0

    print(f"\n{'='*60}")
    print(f"  {lang}")
    print(f"{'='*60}")

    # --- Step 1: rename numbered files to normalized names ---
    # Collect renames first (avoid moving into a path we haven't created yet)
    moves = []
    for rel, abs_src in sorted(lang_files.items()):
        norm = normalize_rel(rel)
        if norm == rel:
            continue  # already clean
        abs_dst = os.path.join(lang_dir, norm)
        if norm in en_files:
            moves.append((abs_src, abs_dst, rel, norm))
        else:
            # Normalized name doesn't exist in en → delete
            print(f"  [del-obsolete] {rel}  (not in en after normalising)")
            git_rm(abs_src, dry_run)
            deletes += 1

    # Sort: deeper paths first so parent renames don't break children
    moves.sort(key=lambda x: -x[2].count("/"))
    for abs_src, abs_dst, rel, norm in moves:
        if os.path.exists(abs_src) or dry_run:
            print(f"  [mv] {rel}  →  {norm}")
            git_mv(abs_src, abs_dst, dry_run)
            renames += 1

    # --- Step 2: delete numbered files with no en equivalent ---
    # (already handled above; catch any remaining numbered files
    #  whose normalized form is also not in en)
    lang_files_now = get_files(lang_dir) if not dry_run else lang_files
    for rel, abs_src in sorted(lang_files_now.items()):
        norm = normalize_rel(rel)
        if norm not in en_files and rel not in en_files:
            print(f"  [del-extra] {rel}  (no en equivalent)")
            git_rm(abs_src, dry_run)
            deletes += 1

    # --- Step 3: stub missing files from en ---
    # Refresh file list after renames
    lang_files_final = get_files(lang_dir) if not dry_run else {
        normalize_rel(r): p for r, p in lang_files.items()
    }
    for en_rel, en_abs in sorted(en_files.items()):
        if en_rel not in lang_files_final:
            dst_abs = os.path.join(lang_dir, en_rel)
            print(f"  [stub] {en_rel}")
            copy_stub(en_abs, dst_abs, dry_run)
            stubs += 1

    print(f"  → renamed: {renames}  deleted: {deletes}  stubbed: {stubs}")
    return renames + deletes + stubs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang",    help="Process only this language")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, no changes")
    args = parser.parse_args()

    en_dir   = os.path.join(CONTENT, SOURCE)
    en_files = get_files(en_dir)

    all_langs = sorted(
        d for d in os.listdir(CONTENT)
        if os.path.isdir(os.path.join(CONTENT, d)) and d not in (SOURCE, "docs")
    )

    langs = [args.lang] if args.lang else all_langs
    for l in langs:
        if not os.path.isdir(os.path.join(CONTENT, l)):
            print(f"Language '{l}' not found.")
            sys.exit(1)

    total = 0
    for lang in langs:
        total += process_lang(lang, en_files, args.dry_run)

    print(f"\n{'='*60}")
    print(f"Total operations: {total}  ({'DRY RUN — no changes made' if args.dry_run else 'done'})")
    print(f"{'='*60}")

    if not args.dry_run and total > 0:
        print("\nRun: git commit -m 'chore: normalize translation file structure'")


if __name__ == "__main__":
    main()
