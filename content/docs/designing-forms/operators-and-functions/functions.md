---
title: "Functions"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

### String functions

{{% alert icon=" " context="warning" %}}
When working with strings within expressions, it's important to use single quotes ('') to enclose literal strings. However, an exception arises when you want to include single quotes within a literal string. In such cases, you can use double quotes ("") to enclose the entire string.

For example:
- Correct: if(${yesno} = 1, "a string with 'single quotes' in it", "no single quotes here")
- Incorrect: if(${yesno} = 1, 'a string with 'single quotes' in it', 'no single quotes here')

Regarding smart quotes, it's crucial to be aware of their presence, as they can cause issues in expressions. Many rich text editors automatically convert straight quotes ("" or '') into smart quotes or curly quotes (“” or ‘’), which may result in syntax errors or unexpected behavior. To avoid this, ensure that you are using straight quotes ('') consistently in your expressions.

Please let me know if you have any further questions or need additional assistance!
{{% /alert %}}

rtSurvey supports various functions, including:

1. `string(field)`: Converts a field to a string.
   - Example: `string(34.8)` will be converted to `'34.8'`.

2. `string-length(field)`: Returns the length of a string field.
   - Example: `string-length(.) > 3 and string-length(.) < 10` can be used to ensure the current field is between 3 and 10 characters.

3. `substr(fieldorstring, startindex, endindex)`: Returns a substring starting at `startindex` and ending just before `endindex`. Indexes start at 0 for the first character in the string.
   - Example: `substr(${phone}, 0, 3)` will return the first three digits of a phone number.

4. `concat(a, b, c, ...)`: Concatenates fields (and/or strings) together.
   - Example: `concat(${firstname}, ' ', ${lastname})` will return a full name by combining the values in the `firstname` and `lastname` fields.

5. `linebreak()`: Returns a linebreak character.
   - Example: `concat(${field1}, linebreak(), ${field2}, linebreak(), ${field3})` will return a list of three field values with linebreaks between them.

6. `lower()`: Converts a string to all lowercase characters.
   - Example: `lower('Street Name')` will return "street name".

7. `upper()`: Converts a string to all uppercase characters.
   - Example: `upper('Street Name')` will return "STREET NAME".

### select_one and select_multiple functions

1. `count-selected(field)`: Returns the number of items selected in a select_multiple field.
   - Example: `count-selected(.) = 3` can be used as a constraint expression to ensure exactly three choices are selected.

2. `selected(field, value)`: Returns true or false depending on whether the specified value was selected in the select_one or select_multiple field.
   - Example: `selected(${color}, 'Blue')` can be used as a relevance expression to show a group or field only if the respondent selected "Blue" as their favorite color.
   - Note: The second parameter should always specify the choice value, not the choice label. Use the value from the value column in the choices worksheet of the form definition.

3. `selected-at(field, number)`: Returns the selected item at the specified position in a select_multiple field. When the passed number is 0, it returns the first selected item; when the number is 1, it returns the second selected item, and so on.
   - Example: `selected-at(${fruits}, 0) = 'Apple'` can be used as a relevance expression to show a group or field only if the first selected choice is "Apple".
   - Note: The returned value will be the choice value, not the choice label. Use the value from the value column in the choices worksheet of the form definition.

4. `choice-label(field, value)`: Returns the label for a select_one or select_multiple field choice, as defined in the choices worksheet of the form definition.
   - Example 1: `choice-label(${country}, ${country})` will return the choice label for the currently selected choice in the field named `country`.
   - Example 2: `choice-label(${languages}, selected-at(${languages}, 0))` will return the label for the first selected choice in the field named `languages`.
   - Note: This function retrieves the choice label, not the value. It uses the label column from the choices worksheet of the form definition.

### Repeated field functions

In rtSurvey, if you want to ask the same question(s) multiple times, you can put a field inside a repeat group. This results in multiple instances of the same field. The following functions can help you deal with these repeated fields and the repeated data they produce. See the help topic on repeating fields for more details.

1. `join(string, repeatedfield)`: For a field within a repeat group, generates a string-separated list of values. The first parameter specifies the delimiter to use to separate the values.
   - Example: `join(', ', ${member_name})` will generate a single comma-separated list from all entered names.

2. `join-if(string, repeatedfield, expression)`: Functions exactly like `join()`, except that it checks each instance in the repeat group using the supplied expression. If the expression evaluates to false, the item will be omitted from the output.
   - Example: `join-if(', ', ${member_name}, ${age} >= 18)` will generate a comma-separated list of names of only adult members (those with ages 18 and over).

3. `count(repeatgroup)`: Returns the current number of times that a repeat group has repeated.
   - Example: `count(${groupname})` will return the number of instances of the group.

4. `count-if(repeatgroup, expression)`: Functions exactly like `count()`, except that it checks each instance in the repeat group using the supplied expression. If the expression evaluates to false, the item will be omitted from the output.
   - Example: `count-if(${members}, ${age} >= 18)` will return the count of adult members based on the age field within the "members" repeat group.

5. `sum(repeatedfield)`: For a field within a repeat group, calculates the sum of all values.
   - Example: `sum(${loan_amount})` will return the total value of all loans.

6. `sum-if(repeatedfield, expression)`: Functions exactly like `sum()`, except that it checks each instance in the repeat group using the supplied expression. If the expression evaluates to false, the item will be omitted from the output.
   - Example: `sum-if(${loan_amount}, ${loan_amount} > 500)` will return the total value of all loans that are over 500. Smaller loans will be ignored.

7. `min(repeatedfield)`: For a field within a repeat group, calculates the minimum of all values.
   - Example: `min(${member_age})` will return the age of the youngest member in the group.

8. `min-if(repeatedfield, expression)`: Functions exactly like `min()`, except that it checks each instance in the repeat group using the supplied expression. If the expression evaluates to false, the item will be omitted from the output.
   - Example: `min-if(${member_age}, ${member_age} >= 18)` will return the age of the youngest adult in the group. Those younger than 18 will be ignored.

9. `max(repeatedfield)`: For a field within a repeat group, calculates the maximum of all values.
   - Example: `max(${member_age})` will return the age of the oldest member in the group.

10. `max-if(repeatedfield, expression)`: Functions exactly like `max()`, except that it checks each instance in the repeat group using the supplied expression. If the expression evaluates to false, the item will be omitted from the output.
    - Example: `max-if(${member_age}, ${member_age} >= 18)` will return the age of the oldest adult in the group. Those younger than 18 will be ignored.

11. `index()`: Called within a repeat group, returns the index number for the current group or instance.
    - Example: `index()` when used within a repeat group will return 1 for the first instance, 2 for the second, and so on.

12. `indexed-repeat(repeatedfield, repeatgroup, index)`: References a field or group that is inside a repeat group from outside that repeat group. The first parameter specifies the repeated field or group of interest, the second specifies the repeat group within which the field or group is located, and the third specifies the instance number within the repeat group to use.
    - Example 1: `indexed-repeat(${name}, ${names}, 1)` will return the first name available when the name field is inside a prior repeat group named "names".
    - Example 2: `indexed-repeat(${name}, ${names}, index())` will pull the name corresponding to the instance number of the current repeat group.

13. `rank-index(index, repeatedfield)`: This function calculates the ordinal rank of the specified instance of a repeated field for use outside the repeat group. The rank of 1 is assigned to the instance with the highest value, the rank of 2 to the instance with the next-highest value, and so on. If you pass an invalid index or an index to an instance with a non-numeric value, a rank of 999 will be returned.
    - Example: `rank-index(1, ${random_draw})` calculates the rank of the first instance based on the value of its `random_draw` field compared to other instances' values.

14. `rank-index-if(index, repeatedfield, expression)`: This function works similarly to `rank-index()`, but it checks each instance in the repeated field's repeat group using the supplied expression. If the expression evaluates to false, the item will be omitted from the calculation. The index used is based on the full set of instances before evaluating the expression for each instance. If you pass an index for an instance that was ignored due to not satisfying the expression, it is considered an invalid index, and a rank of 999 will be returned.
    - Example: `rank-index-if(1, ${age}, ${age} >= 18)` calculates the age rank within the set of adults, considering only instances where the age is greater than or equal to 18.

### Number functions 

{{< table >}}
| Operator | Operation | Example | Example answer |
|----------|-----------|---------|----------------|
| `+` | Addition | 1 + 1 | 2 |
| `-` | Subtraction | 3 - 2 | 1 |
| `*` | Multiplication | 3 * 2 | 6 |
| `div` | Division | 10 div 2 | 5 |
| `mod` | Modulus | 9 mod 2 | 1 |
{{< /table >}}

rtSurvey supports number functions, including:
- `number(field)`: Converts the value of the field to a number.
  - Example: `number('34.8')` = 34.8

- `int(field)`: Converts the value of the field to an integer.
  - Example: `int('39.2')` = 39

- `min(field1, ..., fieldx)`: Returns the minimum value among the passed fields.
  - Example: `min(${father_age}, ${mother_age})` will return the age of either the mother or the father, whichever is smaller.

- `max(field1, ..., fieldx)`: Returns the maximum value among the passed fields.
  - Example: `max(${father_age}, ${mother_age})` will return the age of either the mother or the father, whichever is larger.

- `format-number(field)`: Formats the value of an integer or decimal field according to the user's locale settings.
  - Example: `format-number(${income})` This expression might format "120000" as "120,000".

- `round(field, digits)`: Rounds the numeric field value to the specified number of digits after the decimal place.
  - Example: `round(${interest_rate}, 2)`

- `abs(number)`: Returns the absolute value of a number.
  
- `pow(base, exponent)`: Returns the value of the first parameter raised to the power of the second parameter.
  - Each parameter can be a field, number, or expression.

- `log10(fieldorvalue)`: Returns the base-ten logarithm of the field or value passed in.

- `sin(fieldorvalue)`: Returns the sine of the field or value passed in, expressed in radians.
  
- `cos(fieldorvalue)`: Returns the cosine of the field or value passed in, expressed in radians.

- `tan(fieldorvalue)`: Returns the tangent of the field or value passed in, expressed in radians.

- `asin(fieldorvalue)`: Returns the arcsine of the field or value passed in, expressed in radians.

- `acos(fieldorvalue)`: Returns the arccosine of the field or value passed in, expressed in radians.

- `atan(fieldorvalue)`: Returns the arctangent of the field or value passed in, expressed in radians.

- `atan2(x, y)`: Returns the angle in radians subtended at the origin by the point with coordinates (x, y) and the positive x-axis. The result is in the range -pi() to pi().

- `sqrt(fieldorvalue)`: Returns the non-negative square root of the field or value passed in.

- `exp(x)`: Returns the value of e^x.

- `pi()`: Returns the value of pi.
