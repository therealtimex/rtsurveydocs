---
title: "引用值"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 291
---

`${fieldname}` 语法用于引用表单中另一个字段的当前值。它可以表示输入、选择或计算的值，并将与提交数据中显示的完全一致。

示例：
如果您有一个名为"age"的字段，想检索该字段中输入的确切值，可以使用 `${age}`。

对于约束，"."符号用于引用用户对当前字段的建议输入或选择。它允许您根据用户此时输入或选择的值应用条件或限制。

示例：
如果您想检查当前字段建议值是否小于 3，可以使用约束 `. < 3`。

---

## `..` — 父组引用

在组或重复组内，`..` 引用**父上下文**。在实践中很少需要，但在高级 XPath 表达式中用于导航表单层次结构。

---

## 引用的使用位置

| 列 | 引用类型 | 示例 |
|--------|---------------|---------|
| `relevant` | `${fieldname}` | `${consent} = 'yes'` |
| `constraint` | 当前字段用 `.`，其他字段用 `${fieldname}` | `. > 0 and . <= ${max_value}` |
| `calculation` | `${fieldname}` | `${adults} + ${children}` |
| `required` | `${fieldname}` | `${has_income} = 'yes'` |
| `default` | `${fieldname}` | `${previous_answer}` |
| `label` | 文本中的 `${fieldname}` | `"您的年龄是 ${age} 岁"` |
| `choice_filter` | 列名（不带 `${}`） | `district = ${district}` |

{{% alert icon=" " context="warning" %}}
在 `choice_filter` 列中，直接引用**选项列名**（不带 `${}`），使用 `${}` 引用**表单字段**。混淆这两者是常见的错误来源。
{{% /alert %}}

---

## 在重复组内引用值

在重复组内，`${fieldname}` 引用**同一重复实例**中的字段：

```
relevant: ${member_age} < 18
```

这使用当前重复实例的 `member_age` 值，而不是所有实例。

要从重复组外部引用**特定**重复实例中的字段，请使用 `indexed-repeat()`：

```
indexed-repeat(${member_name}, ${household_members}, 1)
```

完整详情请参见[函数 — 重复字段函数](functions#repeated-field-functions)。

---

## 空值检查

测试字段是否已回答：

```
${fieldname} != ''       （字段不为空）
${fieldname} = ''        （字段为空）
```

对于数字，还要检查：
```
${age} > 0               （年龄有正值——在数值上下文中隐式非空）
```

---

## 引用中的类型强制

当您在数值上下文中使用 `${fieldname}`（例如 `${age} + 1`），rtSurvey 会自动将字符串值强制转换为数字。空字段根据操作强制转换为 `0` 或 `NaN`——使用 `coalesce(${field}, 0)` 将空数值字段安全地默认为零。
