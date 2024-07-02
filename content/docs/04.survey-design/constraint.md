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


### Soft alert

