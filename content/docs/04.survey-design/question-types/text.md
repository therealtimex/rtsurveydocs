---
title: "Text"
description: "Free text response question type in rtSurvey"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

## Overview

The "text" question type in rtSurvey allows for free text responses, providing flexibility for collecting various types of textual data. It is based on the standard XLSForm specification but includes rtSurvey-specific extensions for enhanced functionality.

## XLSForm Specification

In XLSForm, the text question type is specified as:

```
type: text
```

For more details on the standard XLSForm syntax, refer to the [official XLSForm documentation](https://xlsform.org/en/#question-types).

## rtSurvey-specific Extensions

rtSurvey extends the functionality of the text question type through various appearance options, particularly for time input:

### Time Input Extensions

- `appearance:` - Displays a clock for selecting hours and minutes
- `appearance: inline` - Displays the clock as an icon
- `appearance: inline colors("0099FF")` - Displays the clock as an icon with customizable color
- `appearance: inline-1line` - Displays the clock for selection in a single row format
- `appearance: inline-1line-0000FF` - Single row format with customizable color
- `appearance: inline-1line colors("0000FF","FFFF00")` - Single row format with multiple color options
- `appearance: inline-onlyresult` - Displays the clock as an icon at the end of the line, disappearing after selection
- `appearance: inline-onlyresult colors("0099FF")` - Same as above, with customizable icon color

### Time Format Extensions

- `appearance: inline-[%3]` - Displays milliseconds
- `appearance: inline-[%S]` - Displays seconds
- `appearance: inline-[%M]` - Displays minutes
- `appearance: inline-[%h]` - Displays hours (12-hour format)
- `appearance: inline-[%H]` - Displays hours (24-hour format)
- `appearance: inline-[%H-%M-%S]` - Displays time in HH-MM-SS format
- `appearance: inline-[%H:%M:%3]` - Displays time in HH:MM:milliseconds format
- `appearance: inline-[%h:%M:%S]` - Displays time in 12-hour format with seconds
- `appearance: inline-[%H:%M]` - Displays time in 24-hour format
- `appearance: inline-[%h:%M]` - Displays time in 12-hour format
- `appearance: inline-[%M:%S]` - Displays minutes and seconds
- `appearance: inline-[%M:%3]` - Displays minutes and milliseconds

## Data Format

Text data is stored and exported as text. For time-based inputs, the data is stored in a text-based datetime format.

## Mobile App Considerations

The text question type, including all its variants and appearances, is fully supported on iOS, Android, and Web platforms.

## Related Question Types

- Integers
- Datetime

## Best Practices

- Use clear and concise labels for text questions to guide respondents.
- Consider using constraints or validation rules to ensure data quality.
- For time inputs, choose the appropriate appearance option based on the level of precision required for your survey.

## Known Limitations

Currently, there are no known limitations for the text question type in rtSurvey.

## Screenshots

[Note: Include relevant screenshots to illustrate different appearances and variants of the text question type.]
