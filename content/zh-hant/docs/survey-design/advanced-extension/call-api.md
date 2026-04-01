---
title: "呼叫 API"
description: "呼叫 API 讓您的問卷調查從外部網路服務獲取資料，並使用回應填充字段或驗證答案。"
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 294
---

**呼叫 API** 功能讓問卷調查字段向外部服務發出 HTTP 請求，並使用回應填充計算值或驗證使用者輸入。這使得在資料收集過程中可以進行即時查詢、ID 驗證、條碼查詢以及任何其他伺服器端檢查。

有兩個函數：

- `callapi()` — 從 API 獲取值並將其儲存在 `calculate` 或 `text` 字段中
- `callapi-verify()` — 呼叫 API，如果回應與預期值不符則阻止進度（在 `constraint` 中使用）

---

## `callapi()` — 獲取並儲存 API 回應

### 語法

將 `callapi()` 放在 `calculate` 或 `text` 字段的 **`calculation`** 欄中：

```
callapi(method, url, allowed_auto, max_retry, no_overwrite, extract_expr, timeout, lifetime, response_q, call_type, post_body)
```

### 參數

| # | 參數 | 說明 |
|---|-----------|-------------|
| 1 | `method` | HTTP 方法：`'GET'` 或 `'POST'` |
| 2 | `url` | API 端點 URL |
| 3 | `allowed_auto` | `1` 為到達字段時自動呼叫；`0` 為需要手動觸發按鈕 |
| 4 | `max_retry` | 失敗時的最大重試次數 |
| 5 | `no_overwrite` | `1` 為字段已有值時保留現有值；`0` 為始終覆蓋 |
| 6 | `extract_expr` | 從回應中提取所需值的 JSONPath 表達式（例如 `$.data.name`） |
| 7 | `timeout` | 請求超時（毫秒） |
| 8 | `lifetime` | 快取回應在重新獲取前保持有效的時間（毫秒） |
| 9 | `response_q` | 用於儲存原始 HTTP 回應代碼的字段名稱（例如 `${response_status}`） |
| 10 | `call_type` | *(可選)* 特殊呼叫模式：`'lazy-upload'` 或 `'lazy-upload-multiple'` |
| 11 | `post_body` | *(可選)* POST 主體字串。使用 `##fieldname##` 引用表單字段 |

### 範例：GET 請求按 ID 查詢家庭

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| text | household_id | 家庭 ID | | |
| calculate | hh_name | | callapi | `callapi('GET', concat('https://api.example.com/households/', ${household_id}), 1, 3, 0, '$.name', 10000, 0, '')` |
| note | hh_display | 家庭：${hh_name} | | |

### 範例：帶 JSON 主體的 POST 請求

```
callapi('POST', 'https://api.example.com/lookup', 1, 2, 0, '$.result.value', 15000, 0, '', '', '{"id": "##household_id##"}')
```

在 `post_body` 中，使用 `##fieldname##` 注入任何表單字段的當前值。

### 外觀：`callapi`

在字段的 `appearance` 欄中添加 `callapi` 以啟用 API 呼叫整合：

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | api_result | | callapi | `callapi('GET', ...)` |

當 `allowed_auto` 為 `0` 時，rtSurvey 顯示一個**「獲取」按鈕**，調查員手動點擊。

---

## `callapi-verify()` — 根據 API 驗證值

`callapi-verify()` 在 API 確認輸入值有效之前阻止字段的提交。在 **`constraint`** 欄中使用。

### 語法

```
callapi-verify(method, url, extract_expr, match_expr, timeout, constraint_mode, post_body, message)
```

### 參數

| # | 參數 | 說明 |
|---|-----------|-------------|
| 1 | `method` | HTTP 方法：`'GET'` 或 `'POST'` |
| 2 | `url` | 驗證 API 端點 |
| 3 | `extract_expr` | 從回應中提取預期值的 JSONPath |
| 4 | `match_expr` | 將提取的值與字段值比較的表達式（例如 `$.status = 'valid'`） |
| 5 | `timeout` | 請求超時（毫秒） |
| 6 | `constraint_mode` | `'soft'` 僅警告；`'hard'` 阻止繼續 |
| 7 | `post_body` | *(可選)* 帶 `##fieldname##` 替換的 POST 主體 |
| 8 | `message` | *(可選)* 錯誤訊息。支援多語言：`<en>Invalid!</en><vi>Không hợp lệ!</vi>` |

### 範例：根據資產登記冊驗證條碼

| type | name | label | appearance | constraint | constraint_message |
|------|------|-------|------------|------------|-------------------|
| barcode | asset_code | 掃描資產條碼 | callapi-verify | `callapi-verify('POST', 'https://api.example.com/assets/verify', '$.valid', ". = 'true'", 10000, 'hard', '{"code": "##asset_code##"}')` | 登記冊中找不到資產 |

### 外觀：`callapi-verify(...)`

在 constraint 中含有 `callapi-verify()` 的字段的 `appearance` 欄應包含 `callapi-verify(params)` 或 `callapi-verify(dynamicParams)`，以通知 rtSurvey 此字段使用 API 驗證。

---

## 將 App API 資料與 callapi 結合使用

將 `callapi()` 與 `pulldata('app-api', 'user.token')` 結合，將已驗證使用者的令牌注入 API 請求：

```
callapi('POST', 'https://api.example.com/data', 1, 2, 0, '$.value', 10000, 0, '', '',
  concat('{"token":"', pulldata('app-api','user.token'), '","id":"##item_id##"}'))
```

## 最佳實踐

1. 始終設定合理的 `timeout`（5000–15000 毫秒）——不要使用 0 或非常大的值。
2. 對於調查員應有意識地觸發的驗證（例如 ID 檢查），設定 `allowed_auto=0`。
3. 當字段稍後可能被編輯且您不希望重新獲取覆蓋手動更正時，設定 `no_overwrite=1`。
4. 使用帶有特定 JSONPath 的 `extract_expr`，而不是依賴原始回應文字。
5. 在離線模式下測試 API 呼叫——callapi 會優雅地失敗並顯示錯誤，但表單對於非關鍵字段應仍然可以完成。

## 限制

- 需要在呼叫時有網路連線——裝置離線時呼叫將失敗。
- API 回應必須是 JSON——XML 或純文字回應需要額外解析。
- 高呼叫頻率（例如每個重複實例一次 API 呼叫）可能會減慢表單導航速度。
