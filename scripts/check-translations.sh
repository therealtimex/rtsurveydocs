#!/usr/bin/env bash
# check-translations.sh
# Compares each locale's _meta.json files against English to find untranslated entries.
#
# Usage:
#   ./scripts/check-translations.sh            — check all 35 locales
#   ./scripts/check-translations.sh vi fr de   — check specific locales
#
# Output modes:
#   Default: summary table (locale | files checked | untranslated entries)
#   VERBOSE=1 ./scripts/check-translations.sh vi  — show each untranslated key

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PAGES="$ROOT/pages"
LOCALES_DIR="$ROOT/_locales"

# Nouns that should NOT be translated (brand names, proper nouns, tech terms)
KEEP_AS_IS=(
  "DigitalOcean" "Linode" "Docker" "GitHub" "Keycloak" "SSL" "SSO"
  "HTTPS" "HTTP" "API" "PDF" "CSV" "JSON" "XLSForm" "XML"
  "Android" "iOS" "Power BI" "AWS" "GCP" "Azure" "Ubuntu"
  "MySQL" "PHP" "Apache" "Nginx" "Shiny" "Beanstalkd"
  "rtSurvey" "rtCloud" "XForm" "ODK" "KoBoToolbox"
)

# Build jq filter to extract all string values from a _meta.json
# Returns "key\tvalue" pairs, skipping object values (like {"display":"hidden"})
extract_strings() {
  local file="$1"
  python3 -c "
import json, sys
data = json.load(open('$file'))
for k, v in data.items():
    if isinstance(v, str):
        print(f'{k}\t{v}')
    elif isinstance(v, dict) and 'title' in v and isinstance(v['title'], str):
        print(f'{k}\t{v[\"title\"]}')
" 2>/dev/null
}

# Check if a value is likely untranslated (same as English and not a kept noun)
is_untranslated() {
  local en_val="$1"
  local locale_val="$2"

  # If values differ, it's translated
  [[ "$en_val" != "$locale_val" ]] && return 1

  # Same value — check if it's a kept noun (intentionally unchanged)
  for noun in "${KEEP_AS_IS[@]}"; do
    [[ "$en_val" == "$noun" ]] && return 1
  done

  return 0
}

# Collect locales to check
if [[ $# -gt 0 ]]; then
  LOCALES=("$@")
else
  LOCALES=($(ls "$LOCALES_DIR"))
fi

VERBOSE="${VERBOSE:-0}"

# Header
printf "%-10s  %-20s  %-6s  %s\n" "LOCALE" "FILE" "COUNT" "UNTRANSLATED KEYS"
printf "%-10s  %-20s  %-6s  %s\n" "----------" "--------------------" "------" "-----------------"

TOTAL_ISSUES=0

for locale in "${LOCALES[@]}"; do
  locale_dir="$LOCALES_DIR/$locale"
  [[ -d "$locale_dir" ]] || { echo "  [$locale] not found in _locales/"; continue; }

  locale_total=0

  # Walk all English _meta.json files
  while IFS= read -r -d '' en_meta; do
    rel="${en_meta#$PAGES/}"          # e.g. deployment/_meta.json
    locale_meta="$locale_dir/$rel"

    [[ -f "$locale_meta" ]] || continue

    untranslated_keys=()

    while IFS=$'\t' read -r key en_val; do
      locale_val=$(python3 -c "
import json, sys
data = json.load(open('$locale_meta'))
v = data.get('$key', '')
if isinstance(v, str): print(v)
elif isinstance(v, dict): print(v.get('title',''))
else: print('')
" 2>/dev/null)

      if is_untranslated "$en_val" "$locale_val"; then
        untranslated_keys+=("$key")
      fi
    done < <(extract_strings "$en_meta")

    count="${#untranslated_keys[@]}"
    if [[ $count -gt 0 ]]; then
      locale_total=$((locale_total + count))
      TOTAL_ISSUES=$((TOTAL_ISSUES + count))
      short_rel="${rel%/_meta.json}"
      short_rel="${short_rel:-root}"
      if [[ "$VERBOSE" == "1" ]]; then
        printf "%-10s  %-20s  %-6s  %s\n" "$locale" "$short_rel" "$count" "${untranslated_keys[*]}"
      fi
    fi
  done < <(find "$PAGES" -name "_meta.json" -print0)

  if [[ $locale_total -gt 0 ]]; then
    if [[ "$VERBOSE" != "1" ]]; then
      printf "%-10s  %-20s  %-6s\n" "$locale" "(all files)" "$locale_total"
    fi
  else
    printf "%-10s  %-20s  %-6s  %s\n" "$locale" "(all files)" "0" "✓ fully translated"
  fi
done

echo ""
echo "Total untranslated entries across all checked locales: $TOTAL_ISSUES"
echo ""
echo "Tip: VERBOSE=1 $0 <locale> — show per-file breakdown"
