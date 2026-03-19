---
title: "條碼"
description: "條碼問題允許在問卷調查中掃描和擷取條碼資料。"
icon: "qr_code_scanner"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 231
---

XLSForms 和 rtSurvey 中的 barcode 問題類型使使用者能夠直接在問卷調查中掃描和擷取條碼資料。此功能對於庫存管理、產品追蹤或任何需要快速準確輸入編碼資訊的情境特別有用。

## 基本 XLSForm 規格

| type    | name          | label                   |
|---------|---------------|-------------------------|
| barcode | product_code  | Scan the product barcode|

有關基本 barcode 問題類型的更多詳細資訊，請參閱 [XLSForm 規格](https://xlsform.org/en/#question-types)。

## 用途

條碼問題通常用於：

1. 庫存調查中的產品識別
2. 現場操作中的資產追蹤
3. 活動中的票證或 ID 驗證
4. 編碼資訊的快速資料輸入

## rtSurvey 擴展

雖然 XLSForm 規格中的條碼問題基本規格很簡單，但 rtSurvey 可能提供額外的功能或自訂選項，包括：

1. 支援多種條碼格式（例如 QR 碼、UPC、EAN）
2. 與裝置攝影機整合以進行條碼掃描
3. 當條碼損壞或無法掃描時提供手動輸入選項

## 最佳實踐

1. 確保適當的照明條件以進行準確的條碼掃描。
2. 向使用者提供清晰的裝置定位掃描說明。
3. 包含手動輸入選項作為掃描困難時的備用。
4. 在部署問卷調查前在各種裝置和條碼類型上測試條碼掃描功能。

## 限制

- 條碼掃描準確性可能因裝置攝影機品質和環境條件而異。
- 某些舊款或低端裝置可能不支援條碼掃描。
- 根據實現方式，某些條碼類型可能不受支援。

## 使用範例

以下是如何在庫存調查中使用條碼問題的範例：

| type    | name          | label                   | hint                                      |
|---------|---------------|-------------------------|-------------------------------------------|
| barcode | product_code  | Scan the product barcode| Position the barcode within the frame     |
| integer | quantity      | Enter product quantity  |                                           |
| note    | confirmation  | Product scanned: ${product_code}. Quantity: ${quantity} |           |

在此範例中，問卷調查擷取產品的條碼，詢問數量，然後顯示帶有掃描資訊的確認備注。
