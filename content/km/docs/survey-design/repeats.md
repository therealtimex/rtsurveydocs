---
title: "Repeats"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

Repeats អនុញ្ញាតឱ្យ group នៃ questions ត្រូវ ឆ្លើយ ច ្ រ ើ ន ដ ង ។

## Basic Repeat Structure

```
| type         | name             | label            |
|--------------|------------------|------------------|
| begin_repeat | household_member | Household member |
| text         | member_name      | Name             |
| integer      | member_age       | Age              |
| end_repeat   |                  |                  |
```

## Dynamic Repeat Count

```
| type         | name             | label            | repeat_count   |
|--------------|------------------|------------------|----------------|
| begin_repeat | household_members| Household member | ${num_members} |
| text         | member_name      | Member name      |                |
| end_repeat   |                  |                  |                |
```

## `indexed-repeat()` Function

```
| type      | name       | label | calculation                                          |
|-----------|------------|-------|------------------------------------------------------|
| calculate | first_name |       | indexed-repeat(${member_name}, ${household_members}, 1) |
```

## Best Practices

1. ប្រើ `repeat_count` ពេល ចំ នួ ន repetitions ត្រូវ បាន ដ ឹ ង ។
2. ដ ា ក ់ ឈ្មោះ repeat groups ដោយ ច ា ស ់ ។
3. Test ជ ា ម ួ យ ចំ នួ ន instances ច ្ រ ើ ន ។
