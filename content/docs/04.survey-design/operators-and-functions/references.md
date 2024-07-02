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