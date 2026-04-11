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
| ar | implemented |
| bg | implemented |
| cs | implemented |
| da | implemented |
| de | implemented |
| el | implemented |
| es | implemented |
| fi | implemented |
| fr | implemented |
| hi | implemented |
| hu | implemented |
| id | implemented |
| it | implemented |
| ja | implemented |
| km | implemented |
| ko | implemented |
| lt | implemented |
| lv | implemented |
| nb | implemented |
| nl | implemented |
| pl | implemented |
| pt | implemented |
| pt-br | implemented |
| ru | implemented |
| sk | implemented |
| sq | implemented |
| sr | implemented |
| sv | implemented |
| te | implemented |
| th | implemented |
| tr | implemented |
| uk | implemented |
| vi | implemented |
| zh-hans | implemented |
| zh-hant | implemented |
