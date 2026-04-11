#!/usr/bin/env bash
# Run up to 5 gemini translation jobs concurrently.

set -euo pipefail

SPECS_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="/tmp/gemini-translations"
MAX_JOBS=5

mkdir -p "$LOG_DIR"
chmod +x "$SPECS_DIR/run-one-spec.sh"

find "$SPECS_DIR" -maxdepth 1 -name '*.md' ! -name 'README.md' \
  | sort \
  | xargs grep -l "not_implemented" \
  | xargs -P "$MAX_JOBS" -I{} "$SPECS_DIR/run-one-spec.sh" {}

echo ""
echo "All translation jobs finished. Logs in $LOG_DIR"
