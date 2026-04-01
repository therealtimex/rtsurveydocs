---
title: "Referencing values"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 291
---

The `${fieldname}` syntax is used to refer to the current value of a different field in your form. It can represent the value that was entered, selected, or calculated, and it will be displayed exactly as it appears in the submitted data.

Example:
If you have a field named "age" and you want to retrieve the exact value that was entered in that field, you can use `${age}`.

When it comes to constraints, the "." symbol is used to refer to the user's proposed entry or selection for the current field. It allows you to apply conditions or limits based on the value the user is entering or selecting at that moment.

Example:
If you want to check if the proposed value for the current field is less than 3, you can use the constraint `. < 3`.

---

## `..` — Parent group reference

Inside a group or repeat group, `..` refers to the **parent context**. This is rarely needed in practice but is used in advanced XPath expressions to navigate the form hierarchy.

---

## Where references are used

| Column | Reference type | Example |
|--------|---------------|---------|
| `relevant` | `${fieldname}` | `${consent} = 'yes'` |
| `constraint` | `.` for current field, `${fieldname}` for others | `. > 0 and . <= ${max_value}` |
| `calculation` | `${fieldname}` | `${adults} + ${children}` |
| `required` | `${fieldname}` | `${has_income} = 'yes'` |
| `default` | `${fieldname}` | `${previous_answer}` |
| `label` | `${fieldname}` in text | `"Your age is ${age} years"` |
| `choice_filter` | Column name (no `${}`) | `district = ${district}` |

{{% alert icon=" " context="warning" %}}
In the `choice_filter` column, reference **choice column names** directly (without `${}`), and reference **form fields** with `${}`. Mixing these up is a common source of errors.
{{% /alert %}}

---

## Referencing values inside repeat groups

Inside a repeat, `${fieldname}` refers to the field in the **same instance** of the repeat:

```
relevant: ${member_age} < 18
```

This uses the `member_age` value for the current repeat instance, not all instances.

To reference a field in a **specific** repeat instance from outside the repeat, use `indexed-repeat()`:

```
indexed-repeat(${member_name}, ${household_members}, 1)
```

See [Functions — Repeated field functions](functions#repeated-field-functions) for full details.

---

## Empty value checks

Test whether a field has been answered:

```
${fieldname} != ''       (field is not empty)
${fieldname} = ''        (field is empty)
```

For numbers, also check:
```
${age} > 0               (age has a positive value — implicitly not empty for numeric context)
```

---

## Type coercion in references

When you use `${fieldname}` in a numeric context (e.g., `${age} + 1`), rtSurvey automatically coerces the string value to a number. An empty field coerces to `0` or `NaN` depending on the operation — use `coalesce(${field}, 0)` to safely default an empty numeric field to zero.
