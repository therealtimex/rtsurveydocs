---
title: "Цяло число"
description: "Въпросите от тип integer позволяват въвеждане на цели числа в анкетата."
icon: "123"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 222
---

The integer question type in XLSForms and rtSurvey is used to collect whole number responses. This question type is essential for gathering numerical data without decimal places, such as counts, ages, or years.

## Basic XLSForm Specification

| type    | name  | label                 |
|---------|-------|------------------------|
| integer | age   | Enter your age in years|

For more details on the basic integer question type, see the [XLSForm specification](https://xlsform.org/en/#question-types).

## Uses

Integer questions are commonly used for:

1. Age inputs
2. Counting items (e.g., number of children, household members)
3. Year inputs (e.g., year of birth)
4. Ratings on a numerical scale
5. Any whole number data collection

## rtSurvey Extensions

While the basic XLSForm specification for integer questions is straightforward, rtSurvey may offer additional features or customizations:

1. Range validation
2. Custom error messages
3. Appearance options for number input

(Note: The specific extensions available in rtSurvey for integer questions would need to be confirmed and detailed here.)

## Best Practices

1. Use clear and concise labels to specify the expected input.
2. Implement range constraints to prevent unrealistic or erroneous inputs.
3. Consider using hint text to provide examples or clarify the expected format.
4. For large numbers, consider using commas or spaces in the label to improve readability (e.g., "Enter the population (up to 1,000,000)").

## Constraints and Validation

You can add constraints to ensure the entered value falls within a specific range:

| type    | name  | label                 | constraint        | constraint_message                    |
|---------|-------|------------------------|-------------------|---------------------------------------|
| integer | age   | Enter your age in years| .>0 and .<=120    | Age must be between 1 and 120 years   |

## Example Usage

Here's an example of how you might use integer questions in a household survey:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| integer | household_size | How many people live in your household?   | .>0        | Household size must be at least 1 |
| integer | num_children   | How many children under 18 in the household? | .>=0    | Number of children cannot be negative |
| integer | year_built     | In what year was your house built?        | .>1800 and .<=2023 | Year must be between 1800 and 2023 |

## Calculation with Integer Values

Integer values can be used in calculations. Here's an example:

| type    | name           | label                                     |
|---------|----------------|-------------------------------------------|
| integer | num_adults     | Number of adults in the household         |
| integer | num_children   | Number of children in the household       |
| calculate | total_members | | 

In the calculate row, you can use:

```
calculation | ${num_adults} + ${num_children}
```

This will sum the number of adults and children to get the total household members.

