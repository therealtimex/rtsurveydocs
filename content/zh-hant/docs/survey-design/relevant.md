---
title: "跳過問題"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 280
---

跳題邏輯，也稱為分支或條件邏輯，允許您建立根據受訪者答案調整的動態問卷調查。在 rtSurvey 中，跳題邏輯使用 XLSForm 中的 `relevant` 欄來實現。

## 基本跳題邏輯

要實現基本跳題邏輯，請使用 `relevant` 欄指定條件：

```
| type           | name          | label                       | relevant            |
|----------------|---------------|-----------------------------|--------------------|
| select_one y_n | likes_pizza   | Do you like pizza?          |                    |
| select_multiple pizza_toppings | favorite_topping | Favorite toppings | ${likes_pizza} = 'yes' |
```

在此範例中，「最喜歡的配料」問題只有在受訪者回答「是」喜歡披薩時才會出現。

## 相關表達式的語法

- 使用 `${ }` 參考其他問題變數。
- 對於 `select_one` 問題，直接比較：`${question_name} = 'answer'`
- 對於 `select_multiple` 問題，使用 `selected()` 函數。

## 進階跳題邏輯

### 多個條件

您可以使用 `and`、`or` 和括號組合多個條件：

```
| type    | name  | label                   | relevant                                  |
|---------|-------|-------------------------|-------------------------------------------|
| integer | age   | What is your age?       |                                           |
| text    | school| What school do you attend? | ${age} < 18 and (${location} = 'urban' or ${location} = 'suburban') |
```

### 使用 select_multiple 問題

對於 `select_multiple` 問題，使用 `selected()` 函數：

```
| type           | name          | label                       | relevant                               |
|----------------|---------------|-----------------------------|-----------------------------------------|
| select_multiple pizza_toppings | favorite_topping | Favorite toppings |                                         |
| text           | cheese_type   | Favorite type of cheese     | selected(${favorite_topping}, 'cheese') |
```

### 多選中的「其他」選項

使用 `relevant` 實現自由文字「其他」選項：

```
| type           | name                  | label                               | relevant                               |
|----------------|----------------------|-------------------------------------|---------------------------------------|
| select_multiple pizza_toppings | favorite_toppings | What are your favorite pizza toppings? |                                       |
| text           | favorite_toppings_other | What other toppings do you like?   | selected(${favorite_toppings}, 'other') |
```

請記得在您的選項工作表中包含「other」作為選項。

## rtSurvey 特定功能

### 動態相關性

rtSurvey 允許基於計算字段的動態相關性：

```
| type      | name       | label              | calculation                   |
|-----------|------------|--------------------|-----------------------------|
| calculate | total_score| Total Score        | ${score1} + ${score2} + ${score3} |
| text      | feedback   | Feedback           | ${total_score} > 75             |
```

### 重複中的相關性

rtSurvey 支援重複群組中的相關性：

```
| type         | name         | label            | relevant               |
|--------------|--------------|------------------|------------------------|
| begin repeat | child_info   | Child Information|                        |
| integer      | child_age    | Child's Age      |                        |
| text         | school_name  | School Name      | ${child_age} >= 5      |
| end repeat   |              |                  |                        |
```

### 級聯相關性

rtSurvey 高效處理級聯相關性，其中一個問題的相關性取決於另一個問題，而後者又取決於第三個問題：

```
| type           | name        | label                  | relevant               |
|----------------|-------------|------------------------|------------------------|
| select_one y_n | has_car     | Do you own a car?      |                        |
| select_one car_type | car_type | What type of car?    | ${has_car} = 'yes'     |
| text           | model       | Specific model         | ${car_type} = 'sedan'  |
```

## rtSurvey 跳題邏輯的最佳實踐

1. **保持簡單**：盡可能避免過於複雜的相關性條件。
2. **徹底測試**：使用 rtSurvey 的預覽功能測試問卷調查的所有可能路徑。
3. **考慮效能**：非常複雜的跳題邏輯可能會影響問卷調查效能，特別是在行動裝置上。
4. **使用清晰的變數名稱**：這使您的相關性表達式更易於閱讀和維護。
5. **記錄您的邏輯**：添加備注解釋複雜的跳題模式，特別是對於團隊協作。
6. **注意資料分析**：被跳過的問題將導致缺失資料。相應地規劃您的分析。

## 跳題邏輯疑難排解

- **語法錯誤**：確保所有 `${ }` 正確關閉且拼寫正確。
- **循環參考**：避免建立問題相互依賴的迴圈。
- **大小寫敏感性**：請記住，答案選項在相關性表達式中是大小寫敏感的。
- **數字比較**：對數字比較使用適當的運算符（`<`、`>`、`=`）。

## 結論

有效使用跳題邏輯可以顯著改善 rtSurvey 專案中的受訪者體驗和資料品質。透過利用 rtSurvey 的進階功能並遵循最佳實踐，您可以建立動態、高效的問卷調查，適應每個受訪者的獨特情況。
