---
title: "Read-only"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

Read-only fields បង្ហាញ ព័ ត ៌ ម ាន ដោយ មិន អនុញ្ញាតឱ្យ user input ។ ប្រើ `readonly` column ក្នុង XLSForm ។

## Basic Usage

```
| type    | name | label | read_only |
|---------|------|-------|-----------|
| integer | age  | Age   | yes       |
```

## ការ ប្រើ ជាមួយ calculate

```
| type      | name | label | appearance | calculation          |
|-----------|------|-------|------------|----------------------|
| calculate | bmi  | BMI   | readonly   | ${weight} / (${height} * ${height}) |
```
