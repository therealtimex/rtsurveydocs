---
title: "Validating responses"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 270
---

One way to ensure data quality is to add constraints to the data fields in your form. Constraints help prevent users from entering invalid or impossible answers. For example, when asking for a person's income, you want to avoid unrealistic values, such as negative numbers or extremely high values. Adding data constraints in your form is easy to do. Simply follow the steps below:

1. Add a new column called "constraint" to your form.
2. In the "constraint" column, enter a formula that specifies the limits on the answer.

### Example

Let's consider an example where we want to add a constraint for the person's income. The constraint requires the income to be between $0 and $1,000,000. Here's how you can set up the constraint:

{{< table >}}
| `name`      | `constraint`                  |
|---------------|-----------------------------|
| Income        | . >= 0 & . <= 1000000      |
{{< /table >}}

In the example above, the "." in the formula refers back to the question variable, which represents the value entered by the user for the "Income" question. The constraint ". >= 0 && . <= 1000000" ensures that the income entered is greater than or equal to 0 and less than or equal to 1,000,000.


### Hard constraint

A **hard constraint** blocks form submission entirely if the entered value does not satisfy the expression. The enumerator cannot proceed until they enter a valid value.

To add a hard constraint, enter your expression in the `constraint` column. Optionally add a human-readable message in `constraint_message`:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | age | Age of respondent | `. > 0 and . <= 120` | Age must be between 1 and 120 |
| decimal | temperature | Body temperature (°C) | `. >= 35 and . <= 42` | Temperature must be between 35°C and 42°C |
| text | phone | Phone number | `regex(., '^[0-9]{10}$')` | Enter a 10-digit phone number |
{{< /table >}}

#### Multiple conditions

Combine conditions with `and` / `or`:

```
. >= 0 and . <= 100
```

```
. = 'yes' or . = 'no'
```

#### Using `regex()` for pattern validation

The `regex(value, pattern)` function tests a value against a regular expression:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| text | email | Email address | `regex(., '^[^@]+@[^@]+\.[^@]+$')` | Enter a valid email address |
| text | zip_code | ZIP code | `regex(., '^[0-9]{5}$')` | Enter a 5-digit ZIP code |
{{< /table >}}

#### Referencing other fields in a constraint

Use `${fieldname}` to reference values from other questions:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | end_year | End year | `. >= ${start_year}` | End year must be after start year |
| decimal | loan_repaid | Amount repaid | `. <= ${loan_amount}` | Cannot repay more than the loan amount |
{{< /table >}}

### Soft alert

A **soft alert** (also called a soft constraint or warning) warns the enumerator that a value looks unusual, but still allows them to proceed. This is useful when a value is technically valid but statistically unlikely.

rtSurvey supports soft alerts using the `constraint` column with a special `constraint_type` approach, or via the appearance `soft` combined with a note field.

The most common pattern is to use a **note** with a `relevant` expression that flags the suspicious value, paired with an **acknowledge** question to confirm:

{{< table >}}
| `type` | `name` | `label` | `relevant` |
|--------|--------|---------|------------|
| integer | children | Number of children | |
| note | children_warning | Warning: You entered ${children} children. Please confirm this is correct. | `. > 15` |
| trigger | children_confirm | Confirm the number of children is correct | `${children} > 15` |
{{< /table >}}

#### Soft alert with constraint_message only

For a simpler soft warning, you can phrase the constraint to warn on extreme values but still allow a wide range:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | children | Number of children | `. >= 0 and . <= 30` | This value seems very high. Please verify. |
{{< /table >}}

{{% alert icon=" " context="warning" %}}
The distinction between hard and soft constraints matters for data quality. Use **hard constraints** for logically impossible values (negative ages, temperatures above 100°C). Use **soft alerts** for statistically unlikely but not impossible values — you don't want to block legitimate edge cases.
{{% /alert %}}
