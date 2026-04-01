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

### Comparison operators

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

In the examples above, ${age} represents the current field's value, and the operator is used to compare it with the value 25. The constraint will evaluate to either true or false, depending on whether the comparison is satisfied or not.

### Logical operators

Logical operators are used to combine multiple expressions in constraints. Here are some commonly used logical operators along with their operations and examples:

Operator | Operation      | Example                                           
-------- | -------------- | --------------------------------------------------
`or`       | Returns true if either expression is true          | ${age} = 3 or ${age} = 4
`and`      | Returns true only if both expressions are true    | ${age} > 3 and ${age} < 5
`not()`    | Returns true if the expression is not true        | not(${age} > 3 and ${age} < 5)

In the examples above, ${age} represents the current field's value, and the logical operators are used to combine expressions. The constraint will evaluate to true or false based on the conditions specified.

Example 1:
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` will return `true` if the age is either 3 or 4." />}}

Example 2:
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` will return `true` if the age is between 3 and 5." />}}

Example 3:
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` will return `true` if the age is not between 3 and 5." />}}

