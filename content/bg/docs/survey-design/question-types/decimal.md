---
title: "Десетично число"
description: "Въпросите от тип decimal позволяват числови входове с дробни части в анкетата."
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 223
---

The decimal question type in XLSForms and rtSurvey is used to collect numeric responses that may include fractional parts. This question type is essential for gathering precise numerical data such as measurements, prices, or percentages.

## Basic XLSForm Specification

| type    | name   | label                    |
|---------|--------|--------------------------|
| decimal | weight | Enter your weight in kg  |

For more details on the basic decimal question type, see the [XLSForm specification](https://xlsform.org/en/#question-types).

## Uses

Decimal questions are commonly used for:

1. Measurements (e.g., weight, height, distance)
2. Financial data (e.g., prices, salaries)
3. Percentages
4. Scientific data collection
5. Any numeric data that requires precision beyond whole numbers

## Best Practices

1. Use clear and concise labels to specify the expected input and unit of measurement.
2. Implement range constraints to prevent unrealistic or erroneous inputs.
3. Consider using hint text to provide examples or clarify the expected format.
4. Specify the desired number of decimal places in the label or hint if precision is important.

## Constraints and Validation

You can add constraints to ensure the entered value falls within a specific range:

| type    | name   | label                    | constraint        | constraint_message                    |
|---------|--------|--------------------------|-------------------|---------------------------------------|
| decimal | height | Enter your height in meters | .>0 and .<=3    | Height must be between 0 and 3 meters |

## Example Usage

Here's an example of how you might use decimal questions in a health survey:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| decimal | weight         | Enter your weight in kg                   | .>0 and .<=500 | Weight must be between 0 and 500 kg |
| decimal | height         | Enter your height in meters               | .>0 and .<=3 | Height must be between 0 and 3 meters |
| decimal | body_temp      | Enter your body temperature in Celsius    | .>=35 and .<=42 | Temperature must be between 35°C and 42°C |
| calculate | bmi          |                                           |            |                                   |

In the calculate row for BMI, you can use:

```
calculation | ${weight} / (${height} * ${height})
```

This will calculate the BMI using the entered weight and height.

## rtSurvey Extensions

While the basic XLSForm specification for decimal questions is straightforward, rtSurvey may offer additional features or customizations:

1. Precision control (number of decimal places)
2. Custom input formats (e.g., percentage, currency)
3. Advanced validation rules

(Note: The specific extensions available in rtSurvey for decimal questions would need to be confirmed and detailed here.)

## Limitations

- The precision of decimal numbers may be limited by the underlying system or database.
- Users may need guidance on the expected decimal separator (period or comma) depending on their locale.
- Large decimal numbers may be difficult to read or input accurately on mobile devices.

