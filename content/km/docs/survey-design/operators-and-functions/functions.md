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
ន ៅ ព េ ល ធ ្ វ ើ ជ ា មួ យ strings ក ្ ន ុ ង expressions, ប ្ រ ើ single quotes ('') ។ Exception: ប ្ រ ស ិ ន ប ើ ចង ់ include single quotes ក ្ ន ុ ង string, ប ្ រ ើ double quotes ("") ។
{{% /alert %}}

rtSurvey គ ា ំ ទ ្ រ functions ផ ្ ស េ ង ៗ:

1. `string(field)`: Convert field ទ ៅ string ។
2. `string-length(field)`: Return length ន ៃ string field ។
3. `substr(fieldorstring, startindex, endindex)`: Return substring ។
4. `concat(a, b, c, ...)`: Concatenate fields ។
5. `linebreak()`: Return linebreak character ។
6. `lower()`: Convert string ទ ៅ lowercase ។
7. `upper()`: Convert string ទ ៅ uppercase ។

### select_one and select_multiple functions

1. `count-selected(field)`: Return ចំ នួ ន items ដ ែ ល selected ក ្ ន ុ ង select_multiple field ។
2. `selected(field, value)`: Return true ឬ false ។
3. `selected-at(field, number)`: Return selected item ន ៅ position ជ ាក ់ ល ា ក ់ ។
4. `choice-label(field, value)`: Return label ស ម ្ រ ា ប ់ choice ។

### Repeated field functions

1. `join(string, repeatedfield)`: Generate string-separated list ន ៃ values ។
2. `join-if(string, repeatedfield, expression)`: ដ ូ ច `join()` ប ្ រ ស ិ ន ប ើ expression true ។
3. `count(repeatgroup)`: Return ចំ នួ ន times ដ ែ ល repeat group ត ្ រ ូ វ ប ា ន repeated ។
4. `count-if(repeatgroup, expression)`: ដ ូ ច `count()` ជ ា ម ួ យ expression ។
5. `sum(repeatedfield)`: គ ណ ន ា sum ន ៃ values ទ ា ំ ង អ ស ់ ។
6. `sum-if(repeatedfield, expression)`: ដ ូ ច `sum()` ជ ា ម ួ យ expression ។
7. `min(repeatedfield)`: គ ណ ន ា minimum ។
8. `max(repeatedfield)`: គ ណ ន ា maximum ។
9. `index()`: Return index number ន ៃ current group instance ។
10. `indexed-repeat(repeatedfield, repeatgroup, index)`: Reference field ក ្ ន ុ ង repeat group ពី ក ្ រ ោ ម ។

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

- `number(field)`: Convert value ទ ៅ number ។
- `int(field)`: Convert value ទ ៅ integer ។
- `round(field, digits)`: Round numeric field ។
- `abs(number)`: Return absolute value ។
- `pow(base, exponent)`: Return value ្ ល ើ ក ។
- `sqrt(fieldorvalue)`: Return square root ។
- `pi()`: Return value ន ៃ pi ។

### Date and time functions

{{% alert icon=" " context="warning" %}}
Date values ក ្ ន ុ ង rtSurvey ត ្ រ ូ វ ប ា ន store ជ ា strings ក ្ ន ុ ង format `YYYY-MM-DD` ។ ប ្ រ ើ `decimal-date-time()` ដើ ម ្ ប ី convert ទ ៅ number ស ម ្ រ ា ប ់ arithmetic ។
{{% /alert %}}

1. `today()`: Return today's date ជ ា string `YYYY-MM-DD` ។
2. `now()`: Return current date and time ជ ា ISO 8601 string ។
3. `date(value)`: Convert value ទ ៅ date string ។
4. `date-time(value)`: Convert value ទ ៅ datetime string ។
5. `decimal-date-time(value)`: Convert date/datetime string ទ ៅ decimal number ។
6. `format-date(date, format)`: Format date value ។
   - Format tokens: `%Y` (4-digit year), `%m` (month), `%d` (day)
   - Example: `format-date(today(), '%d/%m/%Y')` → `'15/03/2024'`
