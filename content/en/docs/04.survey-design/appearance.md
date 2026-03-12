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

## Known Limitations

- Complex appearances may not render identically across all platforms.
- Some advanced rtSurvey appearances may not be supported in offline mode.

## Troubleshooting Appearance Issues

1. **Appearance Not Applied**: Check for typos in the appearance column.
2. **Inconsistent Rendering**: Verify compatibility with the question type and platform.
3. **Performance Issues**: Consider simplifying complex appearances, especially for large surveys.
