#!/bin/sh
# Build the docs site into dist/
# Usage:
#   ./build.sh           — English only (fast, ~2 min)
#   ./build.sh all       — All 35 locales (~70 min sequential, or use CI for parallel)
#   ./build.sh vi fr de  — Specific locales only

set -e

LOCALES="${1:-}"

echo "=== Building English ==="
NODE_OPTIONS='--max-old-space-size=6144' yarn build

if [ -n "$LOCALES" ]; then
  if [ "$LOCALES" = "all" ]; then
    echo "=== Building all locales ==="
    node scripts/build-split.mjs
  else
    echo "=== Building locales: $@ ==="
    node scripts/build-split.mjs "$@"
  fi
fi

echo "=== Merging into dist/ ==="
node scripts/merge-output.mjs

echo "=== Done. Run: docker compose build && docker compose up -d ==="
