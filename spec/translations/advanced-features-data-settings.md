# Translation Spec — Data Settings

## Source
`pages/survey-design/advanced-features/data-settings.mdx`

## Target path pattern
`_locales/{locale}/survey-design/advanced-features/data-settings.mdx`

## Summary of changes
New page. Documents the `dataSetting.csv` remote database download configuration file. Covers: purpose (auto-download remote SQLite files at form open, queryable offline via rawquery), how to include (upload as family media with exact filename `dataSetting.csv`, converted to `dataSetting.db` on device), column reference table (filepath, service_url, option, frequency, primary_key, where, dynamic_part), downloaded file requirements (SQLite with one table named `externalData`, system columns max_order and marked_as_deleted), `##key##` substitution rules (what columns support openArgs vs App API, failure behavior), where vs dynamic_part difference (join behavior with AND, override behavior), example with two rows (filtered staff list + static facility list), querying after download with rawquery + family_path, when-to-use comparison table (static bundled vs dataSetting.csv vs search-api()).

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
