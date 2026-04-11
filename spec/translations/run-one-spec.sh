#!/usr/bin/env bash
# Called by run-translations.sh — processes one spec file.
# Usage: run-one-spec.sh <spec-file>
set -euo pipefail

SPEC="$1"
NAME="$(basename "$SPEC" .md)"
LOG="/tmp/gemini-translations/$NAME.log"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

PROMPT='Read spec/translations/README.md to understand the process.
Then process the translation spec provided on stdin:
1. Find the Source path and read the English source file.
2. Find the Target path pattern.
3. For each locale row with status "not_implemented":
   a. Translate the full English source into that language.
   b. Write the translated MDX to _locales/{locale}/{target_path} (create if missing).
   c. Update that locale row in the spec file from "not_implemented" to "implemented".
4. Keep code blocks, XLSForm column names, function names, and appearance values in English.
5. Translate all prose, callout text, table description cells, frontmatter title and description.
Work through all 35 locales before finishing.'

echo "[START] $NAME"
cd "$ROOT"
cat "$SPEC" | gemini --yolo -p "$PROMPT" > "$LOG" 2>&1
CODE=$?
if [ $CODE -eq 0 ]; then
  echo "[DONE]  $NAME"
else
  echo "[FAIL]  $NAME (exit $CODE) — see $LOG"
fi
