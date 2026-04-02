#!/usr/bin/env python3
"""
translate_cloud_pages.py
Translates cloud deployment pages (digitalocean.md, linode.md) into all 35 languages
using Google Translate via deep-translator.

Usage:
    pip install deep-translator
    python3 scripts/translate_cloud_pages.py
"""
import os
import re
import time
from deep_translator import GoogleTranslator

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT  = os.path.join(REPO_DIR, "content")

LANG_MAP = {
    "ar":      "ar",
    "bg":      "bg",
    "cs":      "cs",
    "da":      "da",
    "de":      "de",
    "el":      "el",
    "es":      "es",
    "fi":      "fi",
    "fr":      "fr",
    "hi":      "hi",
    "hu":      "hu",
    "id":      "id",
    "it":      "it",
    "ja":      "ja",
    "km":      "km",
    "ko":      "ko",
    "lt":      "lt",
    "lv":      "lv",
    "nb":      "no",
    "nl":      "nl",
    "pl":      "pl",
    "pt":      "pt",
    "pt-br":   "pt",
    "ru":      "ru",
    "sk":      "sk",
    "sq":      "sq",
    "sr":      "sr",
    "sv":      "sv",
    "te":      "te",
    "th":      "th",
    "tr":      "tr",
    "uk":      "uk",
    "vi":      "vi",
    "zh-hans": "zh-CN",
    "zh-hant": "zh-TW",
}

SOURCE_FILES = [
    "docs/getting-started/self-hosting/cloud-deployment/digitalocean.md",
    "docs/getting-started/self-hosting/cloud-deployment/linode.md",
]

# Lines/patterns that must never be translated
SKIP_PATTERNS = [
    re.compile(r'^!\['),                          # images
    re.compile(r'^<!--'),                         # HTML comments
    re.compile(r'^\s*```'),                       # code fence lines
    re.compile(r'^\s*$'),                         # blank lines
    re.compile(r'^---\s*$'),                      # horizontal rules / frontmatter delimiters
    re.compile(r'^\*\*Download'),                 # download links
    re.compile(r'^\[Deploy'),                     # deploy links
    re.compile(r'^\*\*\[Deploy'),                 # bold deploy links
    re.compile(r'https?://'),                     # lines that are raw URLs
]

FRONTMATTER_TRANSLATE_KEYS = {"title", "description"}

# Brand/product names that must never be translated
PROTECTED_NAMES = [
    "DigitalOcean", "Linode", "Akamai Cloud", "Akamai",
    "rtSurvey", "rtCloud", "Keycloak",
    "Docker", "Nginx", "Ubuntu", "Let's Encrypt",
    "Droplet", "StackScript", "Weblish", "LISH",
]

def protect(text):
    """Replace brand names with stable placeholders before translation."""
    tokens = {}
    for name in PROTECTED_NAMES:
        placeholder = f"XPROTX{len(tokens)}X"
        if name in text:
            tokens[placeholder] = name
            text = text.replace(name, placeholder)
    return text, tokens

def restore(text, tokens):
    """Restore brand name placeholders after translation."""
    for placeholder, name in tokens.items():
        text = text.replace(placeholder, name)
    return text


def safe_translate(text, translator):
    """Translate text, returning original on failure. Protects brand names."""
    stripped = text.strip()
    if not stripped:
        return text
    protected, tokens = protect(stripped)
    try:
        result = translator.translate(protected)
        time.sleep(0.05)
        if result:
            result = restore(result, tokens)
            leading = len(text) - len(text.lstrip())
            return text[:leading] + result
        return text
    except Exception:
        return restore(text, tokens)


def translate_frontmatter(fm_text, translator):
    """Translate only title and description in frontmatter block."""
    lines = fm_text.split("\n")
    result = []
    for line in lines:
        match = re.match(r'^(title|description):\s*"(.+)"', line)
        if match:
            key = match.group(1)
            val = match.group(2)
            translated = safe_translate(val, translator)
            result.append(f'{key}: "{translated}"')
        else:
            result.append(line)
    return "\n".join(result)


def should_skip(line):
    """Return True if this line should not be translated."""
    return any(p.search(line) for p in SKIP_PATTERNS)


def translate_body(body_text, translator):
    """
    Translate text body, preserving code blocks, images, comments, and URLs.
    Works by splitting on code fences and translating text segments line-by-line.
    """
    # Split into code and non-code segments
    segments = re.split(r'(```[\s\S]*?```)', body_text)

    result_parts = []
    for i, seg in enumerate(segments):
        if i % 2 == 1:
            # Code block — preserve verbatim
            result_parts.append(seg)
            continue

        # Text segment — translate line by line
        lines = seg.split("\n")
        translated_lines = []
        for line in lines:
            if should_skip(line):
                translated_lines.append(line)
            else:
                translated_lines.append(safe_translate(line, translator))
        result_parts.append("\n".join(translated_lines))

    return "".join(result_parts)


def translate_file(rel_path, hugo_lang, google_lang):
    """Read English source, translate, write to target language directory."""
    src = os.path.join(CONTENT, "en", rel_path)
    dst = os.path.join(CONTENT, hugo_lang, rel_path)

    with open(src, "r", encoding="utf-8") as f:
        content = f.read()

    translator = GoogleTranslator(source="en", target=google_lang)

    # Separate frontmatter from body
    fm_match = re.match(r'^(---\n[\s\S]*?\n---\n)', content)
    if fm_match:
        fm = fm_match.group(1)
        body = content[fm_match.end():]
        fm_translated = translate_frontmatter(fm, translator)
    else:
        fm_translated = ""
        body = content

    body_translated = translate_body(body, translator)

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(fm_translated + body_translated)


def main():
    import sys
    # Accept optional language filter: python3 translate_cloud_pages.py ar,bg,cs
    if len(sys.argv) > 1:
        langs = sys.argv[1].split(",")
        lang_subset = {k: v for k, v in LANG_MAP.items() if k in langs}
    else:
        lang_subset = LANG_MAP

    for rel_path in SOURCE_FILES:
        filename = os.path.basename(rel_path)
        print(f"\n=== {filename} ===")
        for hugo_lang, google_lang in lang_subset.items():
            print(f"  {hugo_lang} ...", end=" ", flush=True)
            try:
                translate_file(rel_path, hugo_lang, google_lang)
                print("done")
            except Exception as e:
                print(f"ERROR: {e}")

    print(f"\nDone — {len(SOURCE_FILES)} files × {len(lang_subset)} languages")


if __name__ == "__main__":
    main()
