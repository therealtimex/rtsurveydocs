---
title: "运算符"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 292
---

### 比较运算符

{{< table >}}
运算符 | 操作      | 示例              | 示例答案
-------- | -------------- | -------------------- | --------------
`=`        | 等于          | ${age} = 25     | true 或 false
`!=`       | 不等于      | ${age} != 25    | true 或 false
`>`        | 大于   | ${age} > 25     | true 或 false
`>=`       | 大于或等于 | ${age} >= 25 | true 或 false
`<`        | 小于      | ${age} < 25     | true 或 false
`<=`       | 小于或等于 | ${age} <= 25  | true 或 false
{{< /table >}}

在上面的示例中，${age} 表示当前字段的值，运算符用于将其与值 25 进行比较。约束将评估为 true 或 false，取决于比较是否满足。

### 逻辑运算符

逻辑运算符用于在约束中组合多个表达式。以下是一些常用的逻辑运算符及其操作和示例：

运算符 | 操作      | 示例                                           
-------- | -------------- | --------------------------------------------------
`or`       | 如果任一表达式为真则返回 true          | ${age} = 3 or ${age} = 4
`and`      | 仅当两个表达式都为真时才返回 true    | ${age} > 3 and ${age} < 5
`not()`    | 如果表达式不为真则返回 true        | not(${age} > 3 and ${age} < 5)

在上面的示例中，${age} 表示当前字段的值，逻辑运算符用于组合表达式。约束将根据指定的条件评估为 true 或 false。

示例 1：
{{< alert icon=" " context="info" text="`${age} = 3 or ${age} = 4` 如果年龄为 3 或 4，则返回 `true`。" />}}

示例 2：
{{< alert icon=" " context="info" text="`${age} > 3 and ${age} < 5` 如果年龄在 3 到 5 之间，则返回 `true`。" />}}

示例 3：
{{< alert icon=" " context="info" text="`not(${age} > 3 and ${age} < 5)` 如果年龄不在 3 到 5 之间，则返回 `true`。" />}}
