---
title: "ការ Reference Values"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 291
---

Syntax `${fieldname}` ប ្ រ ើ ដើ ម ្ ប ី refer ទ ៅ value current ន ៃ field ផ ្ ស េ ង ក ្ ន ុ ង form ។

ឧទាហរណ៍:
ប ្ រ ស ិ ន ប ើ អ ្ ន ក ម ា ន field ដ ែ ល ហ ៅ ថ ា "age" ហ ើ យ ចង ់ retrieve value, ប ្ រ ើ `${age}` ។

ក ្ ន ុ ង constraints, "." symbol ប ្ រ ើ ដើ ម ្ ប ី refer ទ ៅ proposed entry ន ៃ user ។

ឧទាហរណ៍:
ប ្ រ ស ិ ន ប ើ ចង ់ ពិ ន ិ ត ្ យ ថ ា value ត ូ ច ជ ា ង 3: `. < 3` ។

---

## `..` — Parent group reference

ក ្ ន ុ ង group ឬ repeat group, `..` refer ទ ៅ **parent context** ។

---

## Where references ត ្ រ ូ វ ប ្ រ ើ

| Column | Reference type | Example |
|--------|---------------|---------|
| `relevant` | `${fieldname}` | `${consent} = 'yes'` |
| `constraint` | `.` field current, `${fieldname}` ផ ្ ស េ ង | `. > 0 and . <= ${max_value}` |
| `calculation` | `${fieldname}` | `${adults} + ${children}` |
| `required` | `${fieldname}` | `${has_income} = 'yes'` |
| `default` | `${fieldname}` | `${previous_answer}` |
| `label` | `${fieldname}` ក ្ ន ុ ង text | `"Your age is ${age} years"` |
| `choice_filter` | Column name (ម ិ ន ប ្ រ ើ `${}`) | `district = ${district}` |

{{% alert icon=" " context="warning" %}}
ក ្ ន ុ ង column `choice_filter`, reference **choice column names** ដ ោ យ ផ ្ ទ ា ល ់ (ម ិ ន ប ្ រ ើ `${}`), ហ ើ យ reference **form fields** ជ ា ម ួ យ `${}` ។
{{% /alert %}}

---

## Referencing values inside repeat groups

ក ្ ន ុ ង repeat, `${fieldname}` refer ទ ៅ field ក ្ ន ុ ង **instance ដ ូ ច គ ្ ន ា** ន ៃ repeat ។

ដើ ម ្ ប ី reference field ក ្ ន ុ ង **instance ជ ាក ់ ល ា ក ់** ពី ក ្ រ ោ ម repeat, ប ្ រ ើ `indexed-repeat()`:

```
indexed-repeat(${member_name}, ${household_members}, 1)
```

---

## Empty value checks

```
${fieldname} != ''       (field ម ិ ន ទ ទ េ)
${fieldname} = ''        (field ទ ទ េ)
```

---

## Type coercion in references

ន ៅ ព េ ល ប ្ រ ើ `${fieldname}` ក ្ ន ុ ង numeric context, rtSurvey coerce string value ទ ៅ number ដ ោ យ ស ្ វ ័ យ ប ្ រ វ ត ្ ត ិ ។ ប ្ រ ើ `coalesce(${field}, 0)` ដ ើ ម ្ ប ី default empty numeric field ទ ៅ zero ។
