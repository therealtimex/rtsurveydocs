#!/usr/bin/env bash
# Translates ssl-setup.mdx into all 35 locales using Gemini CLI.
# Run from the repo root:
#   bash scripts/gemini_translate_ssl_setup.sh

set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SPEC="$REPO_DIR/spec/translations/deployment-ssl-setup.md"
SOURCE="$REPO_DIR/pages/deployment/ssl-setup.mdx"

PROMPT="You are a documentation translator.

Read the translation spec at: $SPEC
Read the English source file at: $SOURCE

For each locale listed in the spec with status 'not_implemented':
1. Translate the full content of the English source into that language
2. Keep all MDX syntax, image paths, code blocks, links, and frontmatter keys in English — only translate human-readable text
3. Write the translated file to: $REPO_DIR/_locales/{locale}/deployment/ssl-setup.mdx
   (replace {locale} with the actual locale code)
4. After writing each file, update the spec at $SPEC — change that locale's status from 'not_implemented' to 'implemented'

Work through all 35 locales. Do not skip any."

echo "Running Gemini CLI translation for ssl-setup..."
gemini --yolo -p "$PROMPT"

echo "Done. Check spec/translations/deployment-ssl-setup.md for status."
