---
title: "隱藏字段"
description: "隱藏字段儲存永遠不會顯示給受訪者的值——用於傳遞上下文、預填資料或儲存中間結果。"
icon: "eye-slash"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 239
---

`hidden` 字段儲存**永遠不向受訪者顯示**的值。與 `calculate`（計算值）不同，`hidden` 用於攜帶**外部提供的值**——例如，任務 ID、從另一個系統傳入的家庭 ID，或在表單啟動時注入的調查員代碼。

## 基本 XLSForm 規格

| type | name | label |
|------|------|-------|
| hidden | household_id | |

隱藏字段不需要標籤，因為螢幕上不顯示任何內容。

## 用途

隱藏字段通常用於：

1. 從問卷調查管理系統傳入預先分配的 ID（例如家庭 ID、案例編號、任務代碼）
2. 儲存表單版本或部署元資料
3. 在表單啟動時注入調查員特定的配置
4. 在連結工作流程中將資料從父表單攜帶到子表單
5. 當表單透過網頁連結打開時，儲存來自 URL 參數的值

## 設定預設值

最常見的模式是將 `hidden` 與 `default` 表達式一起使用，以便在表單打開時設定值：

| type | name | default |
|------|------|---------|
| hidden | deployment_code | 'ZONE_A_2024' |
| hidden | form_version | '3.1' |

## 在計算中引用隱藏字段

隱藏值可以像任何其他字段一樣使用 `${fieldname}` 引用：

| type | name | label | calculation |
|------|------|-------|-------------|
| hidden | zone_code | | |
| calculate | label_prefix | | concat('[', ${zone_code}, '] ') |
| note | intro | ${label_prefix} 歡迎參加家庭問卷調查 | |

## 使用 hidden 與預填 / URL 參數

透過 URL 啟動網頁表單時，您可以傳遞填充隱藏字段的參數。這允許您預先載入家庭 ID 或任務代碼，而無需調查員手動輸入：

```
https://your-server.com/form/FORMID?household_id=H00123&zone_code=NORTH
```

名為 `household_id` 的字段將自動填充為 `H00123`。

## 最佳實踐

1. 當值**從外部注入**且不應重新計算時，使用 `hidden`（而非 `calculate`）。
2. 當值**從表單中的其他字段衍生**時，使用 `calculate`。
3. 如果隱藏字段必須有值，始終設定 `default`——沒有預設值的隱藏字段將為空。
4. 清晰命名隱藏字段以區分它們（例如，使用 `_hidden_` 前綴或一致的命名慣例）。

## 限制

- 隱藏字段像任何其他字段一樣包含在匯出的資料中。
- 它們不能有條件地顯示——它們始終存在（但不可見）。
- 如果您需要動態計算的字段，請改用 `calculate`。
