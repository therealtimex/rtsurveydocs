---
title: "Select_multiple"
description: "Select_multiple 問題讓受訪者從預定義列表中選擇一個或多個選項。"
icon: "check_box"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 225
---

`select_multiple` 問題類型顯示一個列表，受訪者可以選擇**一個或多個選項**。預設情況下，選項以核取方塊呈現。儲存值是所有已選擇選項值的**以空格分隔的列表**。

## 基本 XLSForm 規格

**survey 工作表：**

| type | name | label |
|------|------|-------|
| select_multiple crops | crops_grown | 家庭種植哪些作物？ |

**choices 工作表：**

| list_name | name | label |
|-----------|------|-------|
| crops | maize | 玉米 |
| crops | beans | 豆類 |
| crops | rice | 稻米 |
| crops | vegetables | 蔬菜 |
| crops | other | 其他 |

有關更多詳細資訊，請參閱 [XLSForm 規格](https://xlsform.org/en/#question-types)。

## 儲存資料格式

匯出的欄包含以空格分隔的已選值列表：

```
maize beans vegetables
```

在表達式中測試 select_multiple 值時，使用 `selected()` 函數——而非 `=`（見下文）。

## 用途

Select_multiple 問題用於：

1. 收集多個適用的答案（例如收入來源、種植作物、症狀）
2. 核取方塊式同意項目（例如「選擇所有適用項目」）
3. 語言或技能清單
4. 任何多個答案同時有效的問題

## 外觀選項

{{< table >}}
| 外觀 | 說明 |
|------------|-------------|
| *(無)* | 預設核取方塊，每行一個 |
| `minimal` | 下拉多選小工具 |
| `compact` | 緊湊網格，欄數根據螢幕寬度調整 |
| `compact-N` | 緊湊網格強制為 N 欄 |
| `horizontal` | 選項水平排列在一行中（網頁） |
| `horizontal-compact` | 水平，緊湊間距（網頁） |
| `label` | 只顯示標籤，無核取方塊（與 `list-nolabel` 一起使用） |
| `list-nolabel` | 只顯示核取方塊，無標籤（與 `label` 一起使用） |
| `columns(N)` | 以 N 欄顯示（rtSurvey 擴展） |
| `tagging` | 選項呈現為藥丸狀標籤片 |
| `boxtag` | 選項呈現為矩形樣式方塊 |
| `boxtag -search` | 方塊上方帶有搜尋/篩選輸入框的 Boxtag 版面 |
| `duolingo-style1` | 大型卡片版面——最適合短選項清單 |
| `rating_box` | 網格式評分方塊 |
| `choices-noshow` | 初始顯示前 10 個選項；其餘按需顯示 |
| `checkall` | 在清單頂部新增「全選」選項 |
| `max-items(N)` | 將可見選項數量限制為 N |
{{< /table >}}

### 範例：3 欄緊湊佈局

| type | name | label | appearance |
|------|------|-------|------------|
| select_multiple symptoms | symptoms | 選擇所有觀察到的症狀 | compact-3 |

## 在表達式中使用 `selected()`

由於儲存值是以空格分隔的字串，您**必須**使用 `selected()` 來測試是否選擇了特定選項。使用 `=` 將無法正確工作。

### 在 `relevant` 中

只有在選擇了「其他」時才顯示後續問題：

| type | name | label | relevant |
|------|------|-------|----------|
| select_multiple crops | crops_grown | 種植哪些作物？ | |
| text | crops_other | 請說明其他作物 | `selected(${crops_grown}, 'other')` |

### 在 `constraint` 中

要求至少選擇 2 個選項：

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple issues | issues | `count-selected(.) >= 2` | 請至少選擇 2 個問題 |

限制最多 3 個：

| type | name | constraint | constraint_message |
|------|------|------------|-------------------|
| select_multiple priorities | priorities | `count-selected(.) <= 3` | 請選擇不超過 3 個優先項目 |

### 在 `calculate` 中——合併已選標籤

結合 `selected-at()`、`count-selected()` 和 `choice-label()` 構建可讀摘要：

| type | name | calculation |
|------|------|-------------|
| calculate | crops_summary | join(', ', ${crops_grown}) |

## 「以上皆無」/互斥選項

一個常見的模式是使一個選項與所有其他選項互斥。使用 `constraint` 強制執行：

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| select_multiple issues | issues | 選擇所有存在的問題 | `not(selected(., 'none') and count-selected(.) > 1)` | 「無」不能與其他選項一起選擇 |

**choices：**

| list_name | name | label |
|-----------|------|-------|
| issues | water | 缺水 |
| issues | roads | 道路狀況差 |
| issues | health | 缺乏醫療服務 |
| issues | none | 以上皆無 |

## 計算和匯總選擇

| 函數 | 範例 | 結果 |
|----------|---------|--------|
| `count-selected(field)` | `count-selected(${crops_grown})` | 已選擇的選項數量 |
| `selected(field, value)` | `selected(${crops_grown}, 'maize')` | true/false |
| `selected-at(field, index)` | `selected-at(${crops_grown}, 0)` | 第一個已選值 |
| `choice-label(field, value)` | `choice-label(${crops_grown}, 'maize')` | 某值的標籤 |

## 最佳實踐

1. 始終在 `relevant`、`constraint` 和 `calculate` 中使用 `selected()`——絕不使用 `=` 或 `!=`。
2. 如果問題設計需要，添加約束以限制最大選擇數量。
3. 當零個選擇是有效答案時，包含「無」或「不適用」選項。
4. 對於長列表（15 個以上選項），使用 `minimal`（多選下拉）以避免過多滾動。
5. 匯出資料並在分析工具中使用字串分割——以空格分隔的格式在透視前需要分割。

## 限制

- Select_multiple 值不能直接與 `=` 比較。始終使用 `selected()`。
- 緊湊外觀對於非常長的選項標籤可能顯示效果不佳。
- 使用 `choice_filter` 篩選選項時，篩選適用於所有顯示的選項，與 `select_one` 相同。
