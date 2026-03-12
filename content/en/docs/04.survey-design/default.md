---
title: "Default"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Default values in rtSurvey allow you to pre-populate questions with answers when a respondent first encounters them. This feature can significantly enhance survey efficiency and data quality by providing initial values that are either commonly selected or serve as examples of expected input.

## Basic Usage

To set a default value, use the `default` column in your XLSForm:

```
| type    | name        | label                         | default    |
|---------|-------------|-------------------------------|------------|
| date    | survey_date | Survey date                   | 2024-07-04 |
| decimal | weight      | Respondent's weight? (in kgs) | 51.3       |
```

In this example, the survey date will be pre-filled with July 4, 2024, and the weight field will start with 51.3 kg.

## Dynamic Defaults

rtSurvey supports dynamic default values using functions:

```
| type | name | label                              | default  |
|------|------|------------------------------------| ---------|
| date | d    | Enter the date the event occurred? | today()  |
```

Here, the `today()` function automatically sets the default to the current date.

## rtSurvey-Specific Features

### Context-Aware Defaults

rtSurvey extends the default functionality with context-aware defaults:

```
| type    | name     | label           | default            |
|---------|----------|-----------------|---------------------|
| text    | location | Current location| ${current_location} |
```

This uses rtSurvey's `${current_location}` variable to pre-fill the location based on the device's GPS.

### Cascading Defaults

rtSurvey allows defaults based on previous answers:

```
| type    | name     | label           | default         |
|---------|----------|-----------------|-----------------|
| text    | city     | City            |                 |
| text    | district | District        | ${city}-district|
```

Here, the district field is pre-filled based on the city entered.

### Default in Repeats

For questions inside a repeat group, the default is calculated when the repeat is added:

```
| type         | name      | label        | default                |
|--------------|-----------|--------------|------------------------|
| begin repeat | visits    | Clinic Visits|                        |
| date         | visit_date| Visit Date   | ${previous_visit_date} |
| end repeat   |           |              |                        |
```

This sets the default visit date to the previous visit's date.

## Best Practices for Using Defaults

1. **Use Sparingly**: Only use defaults where they significantly improve efficiency or data quality.
2. **Ensure Accuracy**: Regularly review and update static default values.
3. **Test Thoroughly**: Especially when using dynamic or calculated defaults.
4. **Consider User Experience**: Ensure defaults don't mislead respondents or introduce bias.
5. **Document Clearly**: Make sure all team members understand the rationale behind default values.

## Advanced Default Techniques

### Randomized Defaults

rtSurvey supports randomized defaults for certain question types:

```
| type              | name    | label        | default           |
|-------------------|---------|--------------|-------------------|
| select_one options| choice  | Select one:  | random(options)   |
```

This randomly selects a default option from the 'options' list.

### Conditional Defaults

Use relevance to set conditional defaults:

```
| type    | name     | label    | default | relevant        |
|---------|----------|----------|---------|-----------------|
| text    | other    | Specify  | N/A     | ${q1} = 'other' |
```

Here, 'N/A' is the default only when 'other' is selected in a previous question.

## Data Management Considerations

- Default values are included in data exports, typically with a flag indicating they were default values.
- rtSurvey's audit trail feature tracks when default values are changed by respondents.

## Mobile App Behavior

- The rtSurvey mobile app supports all default functionalities, including dynamic and context-aware defaults.
- Offline mode may affect some dynamic defaults that rely on real-time data.

## Known Limitations

- Complex calculated defaults may impact form loading time, especially on lower-end devices.
- Some dynamic defaults may not work as expected in preview mode.

## Troubleshooting Default Values

1. **Default Not Appearing**: Check for syntax errors in the default expression.
2. **Unexpected Values**: Verify the calculation logic and test with various scenarios.
3. **Performance Issues**: Optimize complex default calculations or consider alternative approaches.

