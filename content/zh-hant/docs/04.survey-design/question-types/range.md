---
title: "範圍"
description: "範圍問題讓受訪者透過在定義的最小值和最大值之間拖動滑塊來選擇數字。"
icon: "sliders"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 238
---

`range` 問題類型顯示一個**滑塊**（或等效輸入），讓受訪者在定義的最小值和最大值範圍內選擇數字。它非常適合收集評分、滿意度分數，或任何您希望透過視覺方式約束範圍而非依賴帶約束的文字輸入的數值。

## 基本 XLSForm 規格

| type | name | label | parameters |
|------|------|-------|------------|
| range | satisfaction | 您對服務的滿意度如何？ | start=1 end=5 step=1 |

`parameters` 欄定義滑塊邊界和步進大小：

| 參數 | 說明 | 預設值 |
|-----------|-------------|---------|
| `start` | 最小值（含） | 0 |
| `end` | 最大值（含） | 10 |
| `step` | 有效值之間的增量 | 1 |

有關標準 range 問題類型的更多詳細資訊，請參閱 [XLSForm 規格](https://xlsform.org/en/#question-types)。

## 用途

範圍問題通常用於：

1. 滿意度或評分量表（例如 1–5 或 0–10）
2. Likert 式數字量表
3. 收集只有離散值有效的測量值
4. 年齡範圍或分數範圍，其中滑塊比文字字段更易使用

## 使用範例

### 基本評分量表

| type | name | label | parameters |
|------|------|-------|------------|
| range | overall_rating | 總體評分（0–10） | start=0 end=10 step=1 |

### 小數步進

| type | name | label | parameters |
|------|------|-------|------------|
| range | weight_kg | 體重（公斤） | start=0 end=200 step=0.5 |

### 在計算中使用值

| type | name | label | parameters | calculation |
|------|------|-------|------------|-------------|
| range | score | 測試分數（0–100） | start=0 end=100 step=5 | |
| calculate | grade | | | if(${score} >= 90, 'A', if(${score} >= 80, 'B', if(${score} >= 70, 'C', 'F'))) |
| note | grade_note | 您的成績是：${grade} | | |

## 外觀

`range` 類型預設顯示為滑塊。基本用法不需要額外的外觀值。您可以與 `horizontal` 結合使用，在網頁表單中實現更寬的佈局：

| type | name | label | parameters | appearance |
|------|------|-------|------------|------------|
| range | nps | 您向他人推薦我們的可能性有多高？（0–10） | start=0 end=10 step=1 | horizontal |

## 最佳實踐

1. 始終設定有意義的 `start`、`end` 和 `step` 值——不要依賴預設值。
2. 在 `hint` 欄中標記量表的兩端（例如 `hint: 0 = 非常不滿意，10 = 非常滿意`）以為受訪者提供上下文。
3. 對於 5 點 Likert 量表，使用 `start=1 end=5 step=1` 而非 0–4，因為受訪者期望「1」表示最低。
4. 當輸入的有界性質是問題設計的一部分時（滑塊以視覺方式傳達量表），使用 `range` 而非帶約束的 `integer`。

## 限制

- 對於非常大的範圍（例如 0–10000），滑塊小工具可能不理想——在這些情況下，帶約束的文字 `integer` 更易於使用。
- 在行動裝置上，精細步進值（例如 `step=0.1`）可能難以透過觸控滑塊精確控制。
