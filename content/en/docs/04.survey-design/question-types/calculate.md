---
title: "Calculate"
description: ""
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 235
---

Calculate questions in XLSForms and rtSurvey are used to perform computations based on other fields or values in your form. These questions don't display to the user but instead run in the background, storing their results for later use or submission.

## Syntax

In the XLSForm, a calculate question is defined as follows:

| type      | name     | label | calculation |
|-----------|----------|-------|-------------|
| calculate | calc_q1  |       | ${q1} + ${q2} |

- **type**: Always "calculate" for this question type.
- **name**: A unique name for the calculate question.
- **label**: Usually left blank as calculate questions are not displayed to users.
- **calculation**: The formula to be evaluated.

## Uses

Calculate questions are commonly used for:

1. Performing arithmetic operations
2. Concatenating strings
3. Applying complex logic or functions
4. Storing intermediate results for later use

## Examples

### Basic Arithmetic

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | total    | ${price} * ${quantity} |
```

### String Concatenation

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | full_name| concat(${first_name}, ' ', ${last_name}) |
```

### Using Functions

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | age      | int((today() - ${date_of_birth}) / 365.25) |
```

## Advanced Usage in rtSurvey

### pulldata() Function

rtSurvey supports the `pulldata()` function in calculate fields, allowing you to retrieve data from external CSV files:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | city     | pulldata('cities', 'city_name', 'zip_code', ${zip_input}) |
```

#### Syntax

The basic syntax for pulldata() is:

```
pulldata('csv_filename', 'column_to_return', 'key_column', ${matching_value})
```

- 'csv_filename': Name of the CSV file (without .csv extension)
- 'column_to_return': Column name containing the data you want to pull
- 'key_column': Column name to match against
- ${matching_value}: Value to look up in the key column (often a variable from the form)

#### Important Notes

1. The CSV file must be uploaded along with your XLSForm when deploying the survey.
2. Use commas as separators in your CSV file, not semicolons.
3. Avoid commas within the data fields of your CSV, as they can cause parsing issues.
4. pulldata() only supports 1-to-1 relationships. If multiple matches are found, it returns only the first one.
5. There may be limitations on text length that can be pulled (around 76 characters).
6. You can use pulldata() in constraints to validate entries against the CSV data.

### Conditional Calculations

You can use if() statements for conditional calculations:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | discount | if(${total} > 1000, ${total} * 0.1, 0) |
```

## Best Practices

1. Use meaningful names for calculate fields to improve form readability.
2. Avoid overly complex calculations in a single field; break them down if necessary.
3. Test your calculations thoroughly, especially when using complex formulas or external data.
4. Remember that calculate fields run each time the form is evaluated, which can impact performance for very complex or numerous calculations.
5. When using pulldata(), ensure your CSV files are correctly formatted and test thoroughly with your specific data and form structure.

## Limitations

- Calculate fields are not directly editable by users.
- The result of a calculate field is not immediately visible unless referenced in a display field or used in form logic.
