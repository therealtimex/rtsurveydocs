---
title: "Skipping questions"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

Skip logic, also known as branching or conditional logic, allows you to create dynamic surveys that adapt to respondents' answers. In rtSurvey, skip logic is implemented using the `relevant` column in your XLSForm.

## Basic Skip Logic

To implement basic skip logic, use the `relevant` column to specify a condition:

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|--------------------|
| select_one y_n | likes_pizza   | Do you like pizza?          |                    |
| select_multiple pizza_toppings | favorite_topping | Favorite toppings | ${likes_pizza} = 'yes' |
```

In this example, the "Favorite toppings" question only appears if the respondent answers "yes" to liking pizza.

## Syntax for Relevant Expressions

- Use `${ }` to reference other question variables.
- For `select_one` questions, compare directly: `${question_name} = 'answer'`
- For `select_multiple` questions, use the `selected()` function.

## Advanced Skip Logic

### Multiple Conditions

You can combine multiple conditions using `and`, `or`, and parentheses:

```
| type    | name  | label                   | relevant                                  |
|---------|-------|-------------------------|-------------------------------------------|
| integer | age   | What is your age?       |                                           |
| text    | school| What school do you attend? | ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### Using select_multiple Questions

For `select_multiple` questions, use the `selected()` function:

```
| type           | name          | label                       | relevant                               |
|----------------|---------------|-----------------------------|-----------------------------------------|
| select_multiple pizza_toppings | favorite_topping | Favorite toppings |                                         |
| text           | cheese_type   | Favorite type of cheese     | selected(${favorite_topping}, 'cheese') |
```

### "Other" Option in Multiple Choice

Implement a free-text "Other" option using `relevant`:

```
| type           | name                  | label                               | relevant                               |
|----------------|----------------------|-------------------------------------|---------------------------------------|
| select_multiple pizza_toppings | favorite_toppings | What are your favorite pizza toppings? |                                       |
| text           | favorite_toppings_other | What other toppings do you like?   | selected(${favorite_toppings}, 'other') |
```

Remember to include 'other' as an option in your choices worksheet.

## rtSurvey-Specific Features

### Dynamic Relevance

rtSurvey allows for dynamic relevance based on calculated fields:

```
| type      | name       | label              | calculation                   |
|-----------|------------|--------------------|-----------------------------|
| calculate | total_score| Total Score        | ${score1} + ${score2} + ${score3} |
| text      | feedback   | Feedback           | ${total_score} > 75             |
```

### Relevance in Repeats

rtSurvey supports relevance within repeat groups:

```
| type         | name         | label            | relevant               |
|--------------|--------------|------------------|------------------------|
| begin repeat | child_info   | Child Information|                        |
| integer      | child_age    | Child's Age      |                        |
| text         | school_name  | School Name      | ${child_age} >= 5      |
| end repeat   |              |                  |                        |
```

### Cascading Relevance

rtSurvey efficiently handles cascading relevance, where the relevance of one question depends on another, which in turn depends on a third:

```
| type           | name        | label                  | relevant               |
|----------------|-------------|------------------------|------------------------|
| select_one y_n | has_car     | Do you own a car?      |                        |
| select_one car_type | car_type | What type of car?    | ${has_car} = 'yes'     |
| text           | model       | Specific model         | ${car_type} = 'sedan'  |
```

## Best Practices for Skip Logic in rtSurvey

1. **Keep it Simple**: Avoid overly complex relevance conditions when possible.
2. **Test Thoroughly**: Use rtSurvey's preview feature to test all possible paths through your survey.
3. **Consider Performance**: Very complex skip logic can impact survey performance, especially on mobile devices.
4. **Use Clear Variable Names**: This makes your relevance expressions easier to read and maintain.
5. **Document Your Logic**: Add notes to explain complex skip patterns, especially for team collaboration.
6. **Be Mindful of Data Analysis**: Skipped questions will result in missing data. Plan your analysis accordingly.

## Troubleshooting Skip Logic

- **Syntax Errors**: Ensure all `${ }` are properly closed and spelled correctly.
- **Circular References**: Avoid creating loops where questions depend on each other.
- **Case Sensitivity**: Remember that answer choices are case-sensitive in relevance expressions.
- **Numeric Comparisons**: Use appropriate operators (`<`, `>`, `=`) for numeric comparisons.

## Conclusion

Effective use of skip logic can significantly improve the respondent experience and data quality in your rtSurvey projects. By leveraging rtSurvey's advanced features and following best practices, you can create dynamic, efficient surveys that adapt to each respondent's unique situation.

