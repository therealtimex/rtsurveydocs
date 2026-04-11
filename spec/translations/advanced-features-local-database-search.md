# Translation Spec — Local Database Search

## Source
`pages/survey-design/advanced-features/local-database-search.mdx`

## Target path pattern
`_locales/{locale}/survey-design/advanced-features/local-database-search.mdx`

## Summary of changes
New page. Documents rawquery-backed autocomplete for offline SQLite lookups. Covers: appearance variants (search-autocomplete-noedit, search-autocomplete-noedit-v2, search()), rawquery data source signature (6 parameters), db_path convention using family_path, basic province lookup example, parameterized queries with ? placeholders (single and two-parameter cascade examples), UNION SELECT for 888/999 special values, multi-language display with if() on display column, selected-at(., 0) != -997 constraint for validating real selection, comparison table (rawquery vs search-api vs search() vs plain CSV choices), limitations.

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
