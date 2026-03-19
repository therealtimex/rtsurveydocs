---
title: "外觀"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

rtSurvey 中的 `appearance` 欄允許您自訂問卷調查中問題的視覺呈現和行為。此功能增強使用者體驗，可以顯著提高資料收集效率。rtSurvey 支援標準 XLSForm 外觀屬性，並使用額外選項進行擴展。

## 標準 XLSForm 外觀屬性

rtSurvey 支援以下標準 XLSForm 外觀屬性：

| 外觀屬性 | 問題類型 | 說明 |
|----------------------|----------------|-------------|
| multiline | text | 建立多行文字方塊（最適合網頁客戶端） |
| minimal | select_one, select_multiple | 在下拉選單中顯示選項 |
| quick | select_one | 選取後自動前進至下一個問題（僅限行動） |
| no-calendar | date | 抑制日曆顯示（僅限行動） |
| month-year | date | 允許僅選取月份和年份 |
| year | date | 允許僅選取年份 |
| horizontal-compact | select_one, select_multiple | 水平顯示選項（僅限網頁） |
| horizontal | select_one, select_multiple | 在欄中水平顯示選項（僅限網頁） |
| likert | select_one | 將選項呈現為 Likert 量表 |
| compact | select_one, select_multiple | 以最小間距並排顯示選項 |
| quickcompact | select_one | 結合緊湊顯示和自動前進（僅限行動） |
| field-list | groups | 在一個螢幕上顯示整個群組（僅限行動） |
| label | select_one, select_multiple | 顯示無輸入的選項標籤 |
| list-nolabel | select_one, select_multiple | 顯示無標籤的輸入（與 `label` 一起使用） |
| table-list | groups | 以表格格式顯示問題 |
| signature | image | 啟用簽名擷取（僅限行動） |
| draw | image | 允許手繪（僅限行動） |
| map, quick map | select_one, select_one_from_file | 啟用從地圖特徵選取 |

## 使用外觀的最佳實踐

1. **一致性**：在整個問卷調查中一致使用外觀屬性，以保持統一的外觀。
2. **行動與網頁**：考慮外觀在不同裝置和平台上的呈現方式。
3. **效能**：謹慎使用可能減慢表單載入速度的外觀屬性（例如大型群組的 `table-list`）。
4. **使用者體驗**：選擇讓資料輸入對受訪者更容易和直覺的外觀。
5. **測試**：始終在目標裝置上測試您的表單，確保外觀如預期運作。

## 進階技術

### 組合外觀

某些外觀屬性可以組合以實現更複雜的佈局：

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Select one: | minimal compact |
```

### 動態外觀

rtSurvey 允許根據表單邏輯動態更改外觀：

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Enter time: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## 行動應用程式注意事項

- 某些外觀（例如 `quick`、`signature`）特定於行動裝置。
- 在 Android 和 iOS 上進行徹底測試，確保一致的行為。

## rtSurvey 擴展外觀屬性

除了標準 XLSForm 外觀外，rtSurvey 還支援以下平台特定選項：

### 資料和顯示控制

| 外觀屬性 | 問題類型 | 說明 |
|----------------------|----------------|-------------|
| `invisible` | 任何 | 從視圖中隱藏字段，同時仍收集或計算其值。與 `hidden` 類型不同——字段仍參與邏輯。 |
| `displaytitle` | 任何 | 強制顯示字段的標籤/標題，即使它本來會被抑制。 |
| `autopull` | select_one, select_multiple | 在表單載入或觸發字段更改時自動擷取外部資料以填充選項。 |
| `floating_hint` | text, integer, decimal | 將提示文字顯示為輸入字段上方的浮動標籤，而不是下方。 |
| `calculate-button` | calculate | 添加可見按鈕，按需觸發字段重新計算，而不是自動計算。 |

### 佈局

| 外觀屬性 | 問題類型 | 說明 |
|----------------------|----------------|-------------|
| `1screen` | group | 強制整個群組在單一螢幕上顯示，無論群組大小如何。 |
| `columns(n)` | select_one, select_multiple | 在 `n` 欄中顯示選項。例如：`columns(3)` 顯示三欄單選按鈕。 |
| `gridformat<row=R col=C colspan=S align=center>` | 任何 | 在 CSS 網格佈局中將字段定位在行 `R`、列 `C`，跨越 `S` 欄。與 `advanced-extension/grid-layout` 一起使用。 |
| `ignore-simplify` | 任何 | 指示表單渲染器跳過此字段佈局的自動簡化或壓縮。 |

### 小工具

| 外觀屬性 | 問題類型 | 說明 |
|----------------------|----------------|-------------|
| `likert` | select_one | 將選項呈現為 Likert 量表行（已在標準表格中；已確認支援）。 |
| `distress` | select_one | 將選項呈現為 Kessler 心理困擾量表（K10）視覺小工具，帶有情感圖示。 |

### API 整合

| 外觀屬性 | 問題類型 | 說明 |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | 啟用此字段的 API 呼叫整合。計算欄應包含 `callapi()` 表達式。請參閱 [Call API](advanced-extension/call-api)。 |
| `callapi-verify(params)` | text, integer, decimal | 使用靜態參數觸發 API 驗證呼叫。表單在 API 確認值之前會阻止進度。 |
| `callapi-verify(dynamicParams)` | text, integer, decimal | 與 `callapi-verify` 相同，但參數在執行時從其他字段值派生。 |

### 內聯日期/時間格式

對於 `date`、`time` 和 `datetime` 字段，您可以使用附加到外觀的格式字符串指定自訂顯示格式：

```
inline-[%d/%m/%Y]
inline-1line-[%d/%m/%Y %H:%M]
```

格式標記與 `format-date()` 和 `format-date-time()` 相同。請參閱[函數——日期和時間函數](operators-and-functions/functions#date-and-time-functions)。

範例：

| type | name | label | appearance |
|------|------|-------|------------|
| datetime | event_time | Event date and time | inline-[%d/%m/%Y %I:%M %p] |
| date | birth_date | Date of birth | inline-[%d/%m/%Y] |

## 已知限制

- 複雜的外觀可能無法在所有平台上完全相同地呈現。
- 某些進階 rtSurvey 外觀可能在離線模式下不受支援。

## 外觀問題疑難排解

1. **外觀未套用**：檢查外觀欄中的拼寫錯誤。
2. **不一致的呈現**：驗證與問題類型和平台的相容性。
3. **效能問題**：考慮簡化複雜的外觀，特別是對於大型問卷調查。
