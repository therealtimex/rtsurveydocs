---
title: "Advanced extensions"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 289
---

The `appearance` column in rtSurvey allows you to customize the visual presentation and behavior of questions in your surveys. This feature enhances user experience and can significantly improve data collection efficiency. rtSurvey supports standard XLSForm appearance attributes and extends them with additional options.

## rtSurvey-Specific Appearance Extensions

rtSurvey extends the standard appearance options with the following:

### Time Input Customization

For `text` type questions used for time input:

- `appearance:` - Displays a clock for selecting hours and minutes
- `appearance: inline` - Displays the clock as an icon
- `appearance: inline-1line` - Displays the clock in a single row format
- `appearance: inline-onlyresult` - Displays clock icon, disappears after selection
- `appearance: inline-[FORMAT]` - Customizes time format display (e.g., `[%H:%M]`, `[%h:%M:%S]`)

### Color Customization

rtSurvey allows color customization for various appearances:

- `appearance: inline colors("0099FF")` - Customizes icon color
- `appearance: inline-1line colors("0000FF","FFFF00")` - Customizes colors in single-line format

### Grid Layout

rtSurvey introduces a grid layout for compact, table-like displays:

- `appearance: grid` - Applies to groups to create a grid layout

### Collapsible Groups

- `appearance: collapsible` - Creates expandable/collapsible groups

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
