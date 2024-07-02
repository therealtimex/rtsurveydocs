---
title: "Text"
description: ""
icon: "text_fields"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 221
---

The "text" question type in XLSForm prompts the user to enter text. To limit the entries to numeric input and prompt the numeric keypad to show, you can use the "numbers", "numbers_decimal", or "numbers_phone" appearance in the appearance column. The appearance column allows you to modify the appearance or behavior of the question.

Here are the appearances you can use for numeric input:

- **numbers**: This appearance shows a numeric keypad for entering whole numbers. It may not allow hyphens or may only allow hyphens in the first position, depending on the device.
- **numbers_decimal**: This appearance shows a numeric keypad for entering decimal numbers. It allows the user to enter decimal points.
- **numbers_phone**: This appearance shows a numeric keypad optimized for entering phone numbers. It may include additional symbols specific to phone number input.

You can try using these appearances to see which one works best for your specific device and requirements. For example, if you want to accept a number greater than nine digits in length or a hyphen-separated list of numbers, you can use a text field with one of the "numbers" appearances.

Remember to specify the appearance in the appearance column of the survey worksheet for the respective question to apply the desired behavior.