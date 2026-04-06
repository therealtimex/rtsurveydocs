---
title: "問題類型"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey 支援所有標準 XLSForm 問題類型，以及幾個擴展類型。每種問題類型控制收集何種資料以及輸入小工具在裝置上的呈現方式。

要設定問題類型，請在 XLSForm 的**問卷**工作表的 `type` 欄中輸入類型名稱。

## 文字輸入

| 類型 | 說明 |
|------|-------------|
| [text](text) | 自由文字回應——允許任何字符 |
| [integer](integer) | 整數（無小數點） |
| [decimal](decimal) | 帶小數點的數字 |
| [range](range) | 從定義最小/最大範圍的滑塊中選擇的數字 |

## 選擇

| 類型 | 說明 |
|------|-------------|
| [select_one listname](select-one) | 從清單中選取正好一個選項 |
| [select_multiple listname](select-multiple) | 從清單中選取一個或多個選項 |
| [select_one_from_file filename](select-one-from-file) | 從外部 CSV 文件載入的選項中選取一個 |
| [rank listname](rank) | 按喜好或優先順序排列選項 |

## 日期和時間

| 類型 | 說明 |
|------|-------------|
| [date](date) | 日曆日期（年、月、日） |
| [time](time) | 一天中的時間（小時、分鐘） |
| [datetime](datetime-date-time) | 組合的日期和時間 |

## 位置

| 類型 | 說明 |
|------|-------------|
| [geopoint](geopoint) | 單個 GPS 座標（緯度、經度、海拔、精度） |
| [geotrace](geotrace) | 路徑——形成線的一系列 GPS 點 |
| [geoshape](geoshape) | 區域——GPS 點的封閉多邊形 |

## 媒體

| 類型 | 說明 |
|------|-------------|
| [image](image) | 照片擷取或圖像上傳 |
| [audio](audio) | 音頻錄音 |
| [video](video) | 視頻錄製 |
| [file](file) | 一般文件上傳（PDF、文件等） |

## 其他

| 類型 | 說明 |
|------|-------------|
| [barcode](barcode) | 掃描條碼或 QR 碼 |
| [note](note) | 唯讀顯示文字——顯示說明或計算摘要 |
| [calculate](calculate) | 儲存計算值的隱藏字段 |
| [hidden](hidden) | 儲存靜態或預填值的隱藏字段 |
| [trigger / acknowledge](trigger) | 調查員必須勾選以確認已閱讀聲明的核取方塊 |
| [meta](meta) | 自動元資料：時間戳、裝置 ID、調查員資訊 |

## 類型和外觀如何協同工作

`type` 決定**收集何種資料**。`appearance` 欄控制**小工具的外觀**。許多類型支援多種外觀——例如 `select_one` 可以顯示為單選按鈕、下拉選單、Likert 量表或緊湊網格。

請參閱[外觀](../appearance)以取得完整的選項清單。
