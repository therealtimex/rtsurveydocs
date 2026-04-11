# Translation Spec — Advanced Repeats

## Source
`pages/survey-design/advanced-features/repeats.mdx`

## Target path pattern
`_locales/{locale}/survey-design/advanced-features/repeats.mdx`

## Summary of changes
Added three sections before Best Practices, and updated Best Practices item 5. (1) "1screen appearance": sets one-screen-per-instance layout on begin_repeat, auto-adds circular + button when no repeat_count and no add_repeat child present, comparison table vs field-list. (2) "add_repeat custom add button": note/text field inside repeat with appearance add_repeat renders full-width Add button (label from field label column), suppresses default + button from 1screen; color via <#RRGGBB/> or RRGGBB-RRGGBB (bg-text), icon variant with "add_repeat icon". (3) "Delete buttons delete-repeat-current and delete-repeat-last": split button (trash icon + label text), -icon suffix for circular trash icon, same color format as add_repeat, full pattern example combining 1screen + delete-current-icon + add_repeat. Updated Best Practices item 5 to reference 1screen + add_repeat instead of field-list.

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
