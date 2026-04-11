# Translation Spec — Multi-Language

## Source
`pages/survey-design/multi-language.mdx`

## Target path pattern
`_locales/{locale}/survey-design/multi-language.mdx`

## Summary of changes
Added two sections before Best Practices. (1) "HTML formatting in bilingual labels": combining HTML tags with <en>/<vi> language wrappers in a single label cell, supported inline tags (b, i, u, big, small, font color, br, span style), colored text per language example. (2) "Language-aware calculations": using if(${language_use} = 'en', label_en, label_vi) pattern when a change_language widget is present, full example with pulldata('rawquery',...) returning label_en or label_vi based on language_use field, note about language_use being set by change_language appearance.

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
