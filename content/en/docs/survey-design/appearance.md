---
title: "Appearance"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

The `appearance` column in rtSurvey allows you to customize the visual presentation and behavior of questions in your surveys. This feature enhances user experience and can significantly improve data collection efficiency. rtSurvey supports standard XLSForm appearance attributes and extends them with additional options.

## Standard XLSForm Appearance Attributes

rtSurvey supports the following standard XLSForm appearance attributes:

| Appearance Attribute | Question Types | Description |
|----------------------|----------------|-------------|
| multiline | text | Creates a multi-line text box (best for web clients) |
| minimal | select_one, select_multiple | Displays choices in a dropdown menu |
| quick | select_one | Auto-advances to next question after selection (mobile only) |
| no-calendar | date | Suppresses the calendar display (mobile only) |
| month-year | date | Allows selection of month and year only |
| year | date | Allows selection of year only |
| horizontal-compact | select_one, select_multiple | Displays choices horizontally (web only) |
| horizontal | select_one, select_multiple | Displays choices horizontally in columns (web only) |
| likert | select_one | Presents choices as a Likert scale |
| compact | select_one, select_multiple | Displays choices side by side with minimal padding |
| quickcompact | select_one | Combines compact display with auto-advance (mobile only) |
| field-list | groups | Displays entire group on one screen (mobile only) |
| label | select_one, select_multiple | Shows choice labels without inputs |
| list-nolabel | select_one, select_multiple | Shows inputs without labels (use with `label`) |
| table-list | groups | Displays questions in a table format |
| signature | image | Enables signature capture (mobile only) |
| draw | image | Allows freehand drawing (mobile only) |
| map, quick map | select_one, select_one_from_file | Enables selection from map features |

## Best Practices for Using Appearance

1. **Consistency**: Use appearance attributes consistently across your survey for a uniform look.
2. **Mobile vs. Web**: Consider how appearances will render on different devices and platforms.
3. **Performance**: Be cautious with appearance attributes that might slow down form loading (e.g., `table-list` for large groups).
4. **User Experience**: Choose appearances that make data entry easier and more intuitive for respondents.
5. **Testing**: Always test your form on target devices to ensure appearances work as expected.

## Advanced Techniques

### Combining Appearances

Some appearance attributes can be combined for more complex layouts:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Select one: | minimal compact |
```

### Dynamic Appearances

rtSurvey allows for dynamic appearance changes based on form logic:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Enter time: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Mobile App Considerations

- Some appearances (e.g., `quick`, `signature`) are specific to mobile devices.
- Test thoroughly on both Android and iOS to ensure consistent behavior.

## rtSurvey Extended Appearance Attributes

In addition to standard XLSForm appearances, rtSurvey supports the following platform-specific options:

### Data and display control

| Appearance Attribute | Question Types | Description |
|----------------------|----------------|-------------|
| `invisible` | any | Hides the field from view while still collecting or calculating its value. Different from `hidden` type — the field still participates in logic. |
| `displaytitle` | any | Forces display of the field's label/title even when it would otherwise be suppressed. |
| `autopull` | select_one, select_multiple | Automatically fetches external data to populate choices when the form loads or a trigger field changes. |
| `floating_hint` | text, integer, decimal | Shows the hint text as a floating label above the input field rather than below it. |
| `calculate-button` | calculate | Adds a visible button that triggers recalculation of the field on demand, rather than computing automatically. |

### Layout

| Appearance Attribute | Question Types | Description |
|----------------------|----------------|-------------|
| `1screen` | group | Forces the entire group to display on a single screen regardless of group size. |
| `columns(n)` | select_one, select_multiple | Displays choices in `n` columns. Example: `columns(3)` shows three columns of radio buttons. |
| `gridformat<row=R col=C colspan=S align=center>` | any | Positions the field in a CSS-grid layout at row `R`, column `C`, spanning `S` columns. Used with `advanced-extension/grid-layout`. |
| `ignore-simplify` | any | Instructs the form renderer to skip automatic simplification or condensing of this field's layout. |
| `required-but-simplify` | any | Field is required but its layout is still simplified by the renderer (overrides the default behaviour where required fields are excluded from simplification). |
| `embed` | any | Renders the field in embedded/inline display mode, suppressing its outer wrapper and label container — used when a question is nested inside custom HTML. |
| `popup` | select_one, select_multiple | Renders the choice list in a popup/modal overlay instead of inline. |
| `auto-hide-empty` | boxtag, select | Hides the entire question widget when the choice list is empty (e.g., no API results returned). |
| `text-nolabel` | select_one, select_multiple | Hides the text label for each choice, showing only the input control. Similar to `list-nolabel` but applied per-choice rather than as a column split. |

### Widgets

| Appearance Attribute | Question Types | Description |
|----------------------|----------------|-------------|
| `likert` | select_one | Presents choices as a Likert scale row (already in standard table above; confirmed supported). |
| `distress` | select_one | Renders choices as the Kessler Psychological Distress Scale (K10) visual widget with emotional icons. |

### Select visual widgets

These appearances change the entire rendering of select choice lists.

| Appearance Attribute | Question Types | Description |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | Choices render as pill-shaped clickable tag chips. |
| `boxtag` | select_one, select_multiple | Choices render as rectangular styled boxes the user taps. |
| `boxtag -search` | select_one, select_multiple | Boxtag layout with a live search/filter input above the boxes. |
| `duolingo-style1` | select_one, select_multiple | Large card layout inspired by Duolingo — suited for short lists with icons. |
| `rating_box` | select_one, select_multiple | Grid of tappable numbered boxes — suited for scale or NPS questions. |
| `star_rating` | select_one | Choices render as stars; the star count equals the number of choices. |
| `choices-noshow` | select_one, select_multiple | Initially shows only the first 10 choices with a "Show more" control. |
| `noshow` | select_one, select_multiple | Hides the choice list entirely; the value is set programmatically via `calculate` or API. |
| `checkall` | select_multiple | Adds a "Select all" shortcut at the top of the choice list. |
| `max-items(N)` | select_one, select_multiple | Caps the visible choice list to N items. Example: `max-items(5)`. |

### Text visual widgets

| Appearance Attribute | Question Types | Description |
|----------------------|----------------|-------------|
| `richtext` | text | Replaces the plain text box with a rich text editor (bold, italic, lists, links). Stores HTML. |
| `typingtest` | text | Typing test widget — the label text is the passage; the widget records the typed response and timing. |

### Media extensions

| Appearance Attribute | Question Types | Description |
|----------------------|----------------|-------------|
| `watermark("expression")` | image | Overlays a text watermark on captured photos. The argument is an XPath expression evaluated at capture time. Example: `watermark("${id} ${today()}")`. |
| `editable` | image | Enables annotation/drawing over the captured photo before saving. |

### Inline display configuration

The `display{}` and `results{}` modifiers can be appended to `inline` appearances to control icon alignment and result display. These are used together with the `inline` time input extension on `text` fields and with media capture widgets.

#### `display{}` parameters

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| Parameter | Values | Description |
|-----------|--------|-------------|
| Alignment | `left`, `right`, `top`, `bottom`, `center` | Position of the icon relative to the input field |
| Size | `small`, `medium`, `large` | Icon size (maps to 2.5 rem, 5 rem, 8 rem respectively) |
| Mode | `inline-icon` | Renders the trigger as an icon only (no button border) |
| Mode | `inline-button` | Renders the trigger as a full button |

#### `results{}` parameters

```
inline results{right}
inline results{left,hide(seconds)}
```

| Parameter | Values | Description |
|-----------|--------|-------------|
| Alignment | `left`, `right`, `top`, `bottom`, `center` | Position of the result value display |
| `hide(field)` | any sub-field name | Hides a specific component of the result (e.g., `hide(seconds)`) |

### API integration

| Appearance Attribute | Question Types | Description |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Enables API call integration for this field. The calculation column should contain a `callapi()` expression. See [Call API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Triggers an API verification call using static parameters. The form blocks progress until the API confirms the value. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Same as `callapi-verify` but with parameters derived from other field values at runtime. |

### Inline date/time format

For `date`, `time`, and `datetime` fields, you can specify a custom display format using a format string appended to the appearance:

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

Format tokens are the same as `format-date()` and `format-date-time()`. See [Functions — Date and time functions](operators-and-functions/functions#date-and-time-functions).

Example:

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Event date and time | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Date of birth | inline-[%d/%m/%Y] |

## Known Limitations

- Complex appearances may not render identically across all platforms.
- Some advanced rtSurvey appearances may not be supported in offline mode.

## Troubleshooting Appearance Issues

1. **Appearance Not Applied**: Check for typos in the appearance column.
2. **Inconsistent Rendering**: Verify compatibility with the question type and platform.
3. **Performance Issues**: Consider simplifying complex appearances, especially for large surveys.
