# Translation Specs

Each file in this folder tracks the translation status of one English source page across all 35 locales.

## Status values

- `not_implemented` — locale file exists but content is outdated / not yet translated from the new English source
- `implemented` — locale file has been updated to match the current English source

## Source files (English)

All source pages live in `pages/`. Locale translations live in `_locales/{locale}/` mirroring the same path.

## Locales (35 total)

`ar` `bg` `cs` `da` `de` `el` `es` `fi` `fr` `hi` `hu` `id` `it` `ja` `km` `ko` `lt` `lv` `nb` `nl` `pl` `pt` `pt-br` `ru` `sk` `sq` `sr` `sv` `te` `th` `tr` `uk` `vi` `zh-hans` `zh-hant`

## How to use with Gemini

For each spec file:
1. Read the English source file listed under `source`
2. For each locale with status `not_implemented`, translate the source into that language
3. Write the translated content to `_locales/{locale}/{path}`
4. Update the status to `implemented`
