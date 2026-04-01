---
title: "文字"
description: "rtSurvey 中的自由文字回應問題類型"
icon: "text_fields"
date: "2024-07-01T12:00:00+01:00"
lastmod: "2024-07-01T12:00:00+01:00"
draft: false
toc: true
weight: 221
---

`text` 問題類型收集自由文字回應——任何字符字串。它是最靈活的輸入類型，用於姓名、地址、描述、代碼以及任何不適合更具體類型的內容。

rtSurvey 還使用**時間輸入小工具**擴展了 `text`，允許使用時鐘選擇器進行精確的時間輸入。

## 基本 XLSForm 規格

| type | name | label |
|------|------|-------|
| text | respondent_name | 受訪者全名 |
| text | address | 住家地址 |

有關標準 XLSForm text 類型的更多詳細資訊，請參閱 [XLSForm 規格](https://xlsform.org/en/#question-types)。

## 用途

文字問題用於：

1. 姓名、地址、自由描述
2. 開放式評論或回饋
3. 不適合 integer/decimal 的代碼、ID 或參考號碼
4. 使用 rtSurvey 的時間輸入擴展收集時間值
5. 自動完成文字字段（透過 `search-autocomplete-noedit-v2()`）

## 標準外觀選項

| 外觀 | 說明 |
|------------|-------------|
| *(無)* | 單行文字輸入 |
| `multiline` | 多行文字區域——最適合網頁上的較長自由文字 |

## rtSurvey 時間輸入擴展

rtSurvey 使用**時鐘選擇器小工具**擴展了 `text`，用於收集時間值。這些外觀選項顯示一個時鐘圖示，調查員可以點擊以選擇小時、分鐘、秒或毫秒。

### 外觀變體

| 外觀 | 說明 |
|------------|-------------|
| `inline` | 時鐘圖示顯示在字段旁邊 |
| `inline colors("RRGGBB")` | 帶自訂十六進位顏色的時鐘圖示 |
| `inline-1line` | 時鐘以緊湊單行格式顯示 |
| `inline-1line-RRGGBB` | 帶自訂圖示顏色的單行（十六進位，無 `#`） |
| `inline-1line colors("RRGGBB","RRGGBB")` | 帶兩種顏色的單行 |
| `inline-onlyresult` | 選擇後時鐘圖示消失；只顯示值 |
| `inline-onlyresult colors("RRGGBB")` | 同上，帶自訂圖示顏色 |

### 時間格式符號

在括號中附加格式字串以控制顯示哪些時間組成部分：

| 格式字串 | 顯示 |
|---------------|----------|
| `inline-[%H:%M]` | 小時和分鐘（24 小時制） |
| `inline-[%h:%M]` | 小時和分鐘（12 小時制） |
| `inline-[%H:%M:%S]` | 小時、分鐘、秒（24 小時制） |
| `inline-[%h:%M:%S]` | 小時、分鐘、秒（12 小時制） |
| `inline-[%H:%M:%3]` | 小時、分鐘、毫秒 |
| `inline-[%M:%S]` | 僅分鐘和秒 |
| `inline-[%M:%3]` | 僅分鐘和毫秒 |
| `inline-[%S]` | 僅秒 |
| `inline-[%3]` | 僅毫秒 |
| `inline-[%H]` | 僅小時（24 小時制） |
| `inline-[%h]` | 僅小時（12 小時制） |

### 範例：以分鐘和秒記錄任務持續時間

| type | name | label | appearance |
|------|------|-------|------------|
| text | task_duration | 完成任務所花費的時間 | `inline-[%M:%S]` |

### 範例：以 24 小時制和自訂顏色記錄事件時間

| type | name | label | appearance |
|------|------|-------|------------|
| text | event_time | 事件時間 | `inline-1line colors("0099FF")` |

## 資料格式

文字資料以純字串形式儲存和匯出。對於使用內聯時鐘小工具的時間輸入，值以符合所選格式字串的格式儲存（例如，`%H:%M` 對應 `14:32`）。

## 約束和驗證

應用約束以強制執行格式、長度或模式：

| type | name | label | constraint | constraint_message |
|------|------|-------|------------|-------------------|
| text | name | 全名 | `string-length(.) >= 2` | 姓名必須至少 2 個字符 |
| text | code | 參考代碼 | `regex(., '^[A-Z]{2}[0-9]{4}$')` | 請輸入 2 個大寫字母後跟 4 個數字 |
| text | phone | 電話號碼 | `regex(., '^[0-9]{9,15}$')` | 請輸入有效的電話號碼 |

## 最佳實踐

1. 盡可能使用更具體的類型（`integer`、`decimal`、`date`）——這可以防止無效輸入並簡化分析。
2. 使用 `constraint` 與 `string-length()` 或 `regex()` 來驗證代碼或 ID。
3. 對於受訪者可能需要寫幾句話的開放式問題，使用 `multiline` 外觀。
4. 對於時間收集，選擇符合您分析所需精度的時間格式符號——當您只需要分鐘時收集毫秒會浪費調查員的精力。

## 平台支援

text 問題類型和所有時間輸入外觀在 iOS、Android 和網頁平台上均受支援。

## 限制

- 文字回應是自由格式的——除 regex 模式外，沒有內建的拼寫檢查或詞彙約束。
- 內聯時間小工具是 rtSurvey 擴展，不是標準 XLSForm 規格的一部分。
