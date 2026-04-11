# Translation Spec — family_path

## Source
`pages/survey-design/advanced-features/family-path.mdx`

## Target path pattern
`_locales/{locale}/survey-design/advanced-features/family-path.mdx`

## Summary of changes
New page. Documents the family_path convention calculate field required for all local database lookups. Covers: the calculate field definition (pulldata('app-api', 'family_path')), why it is needed (platform-specific media directory path, cannot be hard-coded), example resolved value, how to build paths with concat(${family_path}, '/file.db::tableName'), where family_path is used (rawquery autocomplete, pulldata rawquery, search()), placement in form (before first field that references it, recommended position after meta group), warning callout (silent empty return if missing or placed after referencing fields), multiple database files pattern, development verification with temporary note field.

## Locales

| Locale | Status |
|--------|--------|
| ar | not_implemented |
| bg | not_implemented |
| cs | not_implemented |
| da | not_implemented |
| de | not_implemented |
| el | not_implemented |
| es | not_implemented |
| fi | not_implemented |
| fr | not_implemented |
| hi | not_implemented |
| hu | not_implemented |
| id | not_implemented |
| it | not_implemented |
| ja | not_implemented |
| km | not_implemented |
| ko | not_implemented |
| lt | not_implemented |
| lv | not_implemented |
| nb | not_implemented |
| nl | not_implemented |
| pl | not_implemented |
| pt | not_implemented |
| pt-br | not_implemented |
| ru | not_implemented |
| sk | not_implemented |
| sq | not_implemented |
| sr | not_implemented |
| sv | not_implemented |
| te | not_implemented |
| th | not_implemented |
| tr | not_implemented |
| uk | not_implemented |
| vi | not_implemented |
| zh-hans | not_implemented |
| zh-hant | not_implemented |
