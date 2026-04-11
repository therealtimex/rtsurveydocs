# Translation Spec — Functions

## Source
`pages/survey-design/operators-and-functions/functions.mdx`

## Target path pattern
`_locales/{locale}/survey-design/operators-and-functions/functions.mdx`

## Summary of changes
Expanded substr-jsonpath() entry with: return type (string), empty-string behavior on no match, array indexing example ($.items[0].name), and cross-reference link to call-api for the json: extract pattern.

Also added: (1) Cascade dependency pattern sub-note under string-length() — string-length(${field}) >= 0 always returns true but forces re-evaluation when field changes, use in relevant to trigger cascade refresh for search()/rawquery appearances. (2) New item 8 STRFTIME(format, datetime) under Date functions — SQLite-style date formatting available only inside rawquery SQL strings (not in XLSForm calculation/label columns), with example and note to use format-date-time() for XLSForm expressions instead.

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
