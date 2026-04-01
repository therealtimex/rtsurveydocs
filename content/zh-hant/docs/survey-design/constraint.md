---
title: "驗證回應"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 270
---

確保資料品質的一種方式是為表單中的資料字段添加約束條件。約束條件幫助防止使用者輸入無效或不可能的答案。例如，在詢問一個人的收入時，您希望避免不切實際的值，例如負數或極高的值。在表單中添加資料約束條件很容易。只需按照以下步驟操作：

1. 在您的表單中添加名為「constraint」的新欄位。
2. 在「constraint」欄中，輸入指定答案限制的公式。

### 範例

讓我們考慮一個例子，我們想為一個人的收入添加約束條件。約束條件要求收入在 $0 到 $1,000,000 之間。以下是您設定約束條件的方式：

{{< table >}}
| `name`      | `constraint`                  |
|---------------|-----------------------------|
| Income        | . >= 0 & . <= 1000000      |
{{< /table >}}

在上面的例子中，公式中的「.」指的是問題變數，代表使用者為「Income」問題輸入的值。約束條件「. >= 0 && . <= 1000000」確保輸入的收入大於或等於 0 且小於或等於 1,000,000。


### 硬性約束

**硬性約束**如果輸入值不滿足表達式，則完全阻止表單提交。調查員在輸入有效值之前無法繼續進行。

要添加硬性約束，請在 `constraint` 欄中輸入您的表達式。可選地在 `constraint_message` 中添加人類可讀的訊息：

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | age | Age of respondent | `. > 0 and . <= 120` | Age must be between 1 and 120 |
| decimal | temperature | Body temperature (°C) | `. >= 35 and . <= 42` | Temperature must be between 35°C and 42°C |
| text | phone | Phone number | `regex(., '^[0-9]{10}$')` | Enter a 10-digit phone number |
{{< /table >}}

#### 多個條件

使用 `and` / `or` 組合條件：

```
. >= 0 and . <= 100
```

```
. = 'yes' or . = 'no'
```

#### 使用 `regex()` 進行模式驗證

`regex(value, pattern)` 函數對值進行正則表達式測試：

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| text | email | Email address | `regex(., '^[^@]+@[^@]+\.[^@]+$')` | Enter a valid email address |
| text | zip_code | ZIP code | `regex(., '^[0-9]{5}$')` | Enter a 5-digit ZIP code |
{{< /table >}}

#### 在約束條件中參考其他字段

使用 `${fieldname}` 參考其他問題的值：

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | end_year | End year | `. >= ${start_year}` | End year must be after start year |
| decimal | loan_repaid | Amount repaid | `. <= ${loan_amount}` | Cannot repay more than the loan amount |
{{< /table >}}

### 軟性警告

**軟性警告**（也稱為軟性約束或警告）警告調查員某個值看起來不尋常，但仍允許他們繼續進行。當某個值技術上有效但統計上不太可能時，這很有用。

rtSurvey 支援使用帶有特殊 `constraint_type` 方法的 `constraint` 欄，或透過與備注字段結合的外觀 `soft` 進行軟性警告。

最常見的模式是使用一個帶有 `relevant` 表達式的**備注**來標記可疑值，配合一個**確認**問題：

{{< table >}}
| `type` | `name` | `label` | `relevant` |
|--------|--------|---------|------------|
| integer | children | Number of children | |
| note | children_warning | Warning: You entered ${children} children. Please confirm this is correct. | `. > 15` |
| trigger | children_confirm | Confirm the number of children is correct | `${children} > 15` |
{{< /table >}}

#### 僅使用 constraint_message 的軟性警告

對於更簡單的軟性警告，您可以將約束條件設置為對極端值發出警告，但仍允許較大範圍：

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | children | Number of children | `. >= 0 and . <= 30` | This value seems very high. Please verify. |
{{< /table >}}

{{% alert icon=" " context="warning" %}}
硬性約束和軟性約束之間的區別對資料品質很重要。對邏輯上不可能的值（負年齡、超過 100°C 的溫度）使用**硬性約束**。對統計上不太可能但並非不可能的值使用**軟性警告**——您不希望阻止合理的邊緣案例。
{{% /alert %}}
