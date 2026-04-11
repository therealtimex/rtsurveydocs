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
