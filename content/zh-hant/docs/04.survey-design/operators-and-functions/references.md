---
title: "參考值"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 291
---

`${fieldname}` 語法用於參考表單中另一個字段的當前值。它可以代表已輸入、選取或計算的值，並將完全按照提交資料中的顯示方式顯示。

範例：
如果您有一個名為「age」的字段，並且想要擷取該字段中輸入的確切值，您可以使用 `${age}`。

在約束條件方面，「.」符號用於參考使用者對當前字段的建議輸入或選取。它允許您根據使用者當時正在輸入或選取的值應用條件或限制。

範例：
如果您想要檢查當前字段的建議值是否小於 3，您可以使用約束條件 `. < 3`。

---

## `..` — 父群組參考

在群組或重複群組中，`..` 指的是**父上下文**。這在實踐中很少需要，但在高級 XPath 表達式中用於導航表單階層。

---

## 使用參考的位置

| 欄位 | 參考類型 | 範例 |
|--------|---------------|---------|
| `relevant` | `${fieldname}` | `${consent} = 'yes'` |
| `constraint` | `.` 用於當前字段，`${fieldname}` 用於其他字段 | `. > 0 and . <= ${max_value}` |
| `calculation` | `${fieldname}` | `${adults} + ${children}` |
| `required` | `${fieldname}` | `${has_income} = 'yes'` |
| `default` | `${fieldname}` | `${previous_answer}` |
| `label` | 文字中的 `${fieldname}` | `"Your age is ${age} years"` |
| `choice_filter` | 欄名（無 `${}`） | `district = ${district}` |

{{% alert icon=" " context="warning" %}}
在 `choice_filter` 欄中，直接參考**選項欄名**（無 `${}`），並使用 `${}` 參考**表單字段**。混淆這兩者是常見的錯誤來源。
{{% /alert %}}

---

## 在重複群組中參考值

在重複中，`${fieldname}` 指的是**同一重複實例**中的字段：

```
relevant: ${member_age} < 18
```

這使用當前重複實例的 `member_age` 值，而不是所有實例。

要從重複外部參考**特定**重複實例中的字段，請使用 `indexed-repeat()`：

```
indexed-repeat(${member_name}, ${household_members}, 1)
```

請參閱[函數——重複字段函數](functions#repeated-field-functions)以取得完整詳細資訊。

---

## 空值檢查

測試字段是否已回答：

```
${fieldname} != ''       (字段不為空)
${fieldname} = ''        (字段為空)
```

對於數字，還需要檢查：
```
${age} > 0               (年齡具有正值——在數字上下文中隱式非空)
```

---

## 參考中的類型強制轉換

當您在數字上下文中使用 `${fieldname}`（例如 `${age} + 1`）時，rtSurvey 會自動將字符串值強制轉換為數字。空字段根據操作強制轉換為 `0` 或 `NaN`——使用 `coalesce(${field}, 0)` 安全地將空數字字段預設為零。
