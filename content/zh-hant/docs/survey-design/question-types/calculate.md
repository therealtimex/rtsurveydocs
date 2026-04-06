---
title: "計算"
description: ""
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 235
---

XLSForms 和 rtSurvey 中的計算問題用於根據表單中的其他字段或值執行計算。這些問題不向使用者顯示，而是在背景執行，儲存其結果以供後續使用或提交。

## 語法

在 XLSForm 中，計算問題定義如下：

| type      | name     | label | calculation |
|-----------|----------|-------|-------------|
| calculate | calc_q1  |       | ${q1} + ${q2} |

- **type**：對於此問題類型始終為「calculate」。
- **name**：計算問題的唯一名稱。
- **label**：通常留空，因為計算問題不向使用者顯示。
- **calculation**：要評估的公式。

## 用途

計算問題通常用於：

1. 執行算術運算
2. 串聯字符串
3. 應用複雜邏輯或函數
4. 儲存中間結果以供後續使用

## 範例

### 基本算術

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | total    | ${price} * ${quantity} |
```

### 字符串串聯

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | full_name| concat(${first_name}, ' ', ${last_name}) |
```

### 使用函數

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | age      | int((today() - ${date_of_birth}) / 365.25) |
```

## rtSurvey 中的進階用法

### pulldata() 函數

rtSurvey 在計算字段中支援 `pulldata()` 函數，允許您從外部 CSV 文件擷取資料：

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | city     | pulldata('cities', 'city_name', 'zip_code', ${zip_input}) |
```

#### 語法

pulldata() 的基本語法為：

```
pulldata('csv_filename', 'column_to_return', 'key_column', ${matching_value})
```

- 'csv_filename'：CSV 文件名稱（不含 .csv 副檔名）
- 'column_to_return'：包含您想要提取的資料的欄名稱
- 'key_column'：要匹配的欄名稱
- ${matching_value}：在鍵欄中查找的值（通常是表單中的變數）

#### 重要注意事項

1. 部署問卷調查時，CSV 文件必須與 XLSForm 一起上傳。
2. 在 CSV 文件中使用逗號作為分隔符，不要使用分號。
3. 避免在 CSV 的資料字段中使用逗號，因為這可能導致解析問題。
4. pulldata() 只支援 1 對 1 的關係。如果找到多個匹配項，它只返回第一個。
5. 可以提取的文字長度可能有限制（約 76 個字符）。
6. 您可以在約束條件中使用 pulldata() 對照 CSV 資料驗證條目。

### 條件計算

您可以使用 if() 語句進行條件計算：

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | discount | if(${total} > 1000, ${total} * 0.1, 0) |
```

## 最佳實踐

1. 使用有意義的計算字段名稱以提高表單可讀性。
2. 避免在單個字段中進行過於複雜的計算；必要時將其分解。
3. 徹底測試您的計算，特別是在使用複雜公式或外部資料時。
4. 請記住，計算字段在每次評估表單時都會執行，這對於非常複雜或大量的計算可能會影響效能。
5. 使用 pulldata() 時，確保您的 CSV 文件格式正確，並使用您的特定資料和表單結構進行徹底測試。

## 限制

- 計算字段不能直接由使用者編輯。
- 計算字段的結果在顯示字段中引用或在表單邏輯中使用之前不會立即可見。
