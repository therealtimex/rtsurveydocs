# Translation Spec — Elasticsearch

## Source
`pages/survey-design/advanced-features/elasticsearch.mdx`

## Target path pattern
`_locales/{locale}/survey-design/advanced-features/elasticsearch.mdx`

## Summary of changes
New page. Documents how to use Elasticsearch data in RTSurvey forms from a form designer's perspective. Covers: (1) Real-time search via search-api() pointing at ES _search endpoint — data_path=$.hits.hits, ##_source.fieldname## display template, pulldata() after selection; (2) Offline via dataSetting.csv + rawquery — server exports ES snapshot as SQLite externalData table, query with marked_as_deleted filter; (3) When-to-use comparison table (real-time vs offline vs static bundled); (4) Security note — HTTP Basic Auth is server-side only, search-api() sends no auth headers to ES, use offline mode for sensitive data.

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
