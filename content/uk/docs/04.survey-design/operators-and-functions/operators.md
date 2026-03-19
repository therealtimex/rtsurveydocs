---
title: "Оператори"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### Оператори порівняння

{{< table >}}
Operator | Operation      | Example              | Example Answer
-------- | -------------- | -------------------- | --------------
`=`        | Equal          | ${age} = 25     | true or false
`!=`       | Not equal      | ${age} != 25    | true or false
`>`        | Greater-than   | ${age} > 25     | true or false
`>=`       | Greater-than or equal | ${age} >= 25 | true or false
`<`        | Less-than      | ${age} < 25     | true or false
`<=`       | Less-than or equal | ${age} <= 25  | true or false
{{< /table >}}

У наведених прикладах ${age} представляє значення поточного поля, а оператор використовується для порівняння його зі значенням 25. Обмеження оцінюватиметься як true або false залежно від того, чи виконується порівняння чи ні.

### Логічні оператори

Логічні оператори використовуються для об'єднання кількох виразів в обмеженнях. Ось деякі часто використовувані логічні оператори разом з їх операціями та прикладами:

Operator | Operation      | Example                                           
-------- | -------------- | --------------------------------------------------
`or`       | Returns true if either expression is true          | ${age} = 3 or ${age} = 4
`and`      | Returns true only if both expressions are true    | ${age} > 3 and ${age} < 5
`not()`    | Returns true if the expression is not true        | not(${age} > 3 and ${age} < 5)

У наведених прикладах ${age} представляє значення поточного поля, а логічні оператори використовуються для об'єднання виразів. Обмеження оцінюватиметься як true або false на основі зазначених умов.

Приклад 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` поверне `true`, якщо вік дорівнює 3 або 4." />}}

Приклад 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` поверне `true`, якщо вік між 3 і 5." />}}

Приклад 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` поверне `true`, якщо вік не між 3 і 5." />}}
