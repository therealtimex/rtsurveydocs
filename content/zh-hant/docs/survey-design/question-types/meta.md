---
title: "元資料"
description: "元資料問題類型自動捕獲裝置、調查員和時間資訊，無需受訪者輸入。"
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 237
---

元資料問題類型是**自動填寫**的特殊字段——受訪者永遠不會看到它們。它們捕獲有關提交的上下文：收集時間、使用的裝置以及收集者。在 `survey` 工作表中像任何其他問題類型一樣添加它們；它們只是不在螢幕上顯示。

## 基本 XLSForm 規格

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| deviceid | deviceid | |

對於元資料字段，標籤是可選的，因為它們永遠不會顯示。

---

## 時間元資料字段

### `start`

記錄**表單打開的日期和時間**。以 ISO 8601 格式儲存（`YYYY-MM-DDTHH:MM:SS.sss+HH:MM`）。

```
type    | name  | label
start   | start |
```

### `end`

記錄**表單提交的日期和時間**。與 `start` 一起，您可以計算填寫表單所花費的時間：

```
type      | name          | calculation
calculate | duration_min  | (decimal-date-time(${end}) - decimal-date-time(${start})) * 1440
```

### `today`

記錄**當前日期**（無時間組成部分）。以 `YYYY-MM-DD` 格式儲存。當您只需要日期而不需要完整時間戳時很有用。

```
type  | name  | label
today | today |
```

---

## 裝置元資料字段

### `deviceid`

記錄用於資料收集的**裝置的唯一識別碼**。在 Android 上，這通常是 IMEI 或 Android ID。用於追蹤哪台裝置提交了每個表單，以及檢測來自同一裝置的重複提交。

```
type      | name     | label
deviceid  | deviceid |
```

### `devicephonenum`

記錄裝置中 SIM 卡的**電話號碼**（如果可用）。如果裝置沒有 SIM 卡或號碼未儲存在 SIM 卡上，可能為空。

```
type           | name          | label
devicephonenum | devicephonenum |
```

### `simserial`

記錄 **SIM 卡的序列號**（ICCID）。用於識別使用了哪個 SIM/電信業者。

```
type      | name      | label
simserial | simserial |
```

### `subscriberid`

記錄 **IMSI（國際行動用戶識別碼）**——SIM 卡上的唯一用戶識別碼。

```
type         | name        | label
subscriberid | subscriberid |
```

---

## 調查員元資料字段

### `username`

記錄**已登入調查員的用戶名**（rtSurvey 應用程式中使用的帳戶）。這是追蹤誰收集了每個提交記錄最可靠的方式。

```
type     | name     | label
username | username |
```

### `email`

記錄**已登入調查員的電子郵件地址**。

```
type  | name  | label
email | email |
```

### `phonenumber`

記錄與**調查員帳戶關聯的電話號碼**（如已配置）。

```
type        | name       | label
phonenumber | phonenumber |
```

---

## 稽核日誌

### `audit`

`audit` 元資料字段啟用**詳細稽核日誌記錄**——它記錄調查員訪問每個問題的帶時間戳的日誌、在每個問題上花費的時間，以及（可選）每個步驟的 GPS 位置。稽核日誌與每個提交記錄一起作為單獨的 `audit.csv` 文件儲存。

```
type  | name  | parameters
audit | audit | location-priority=balanced location-min-interval=30 location-max-age=60
```

#### 稽核參數

| 參數 | 說明 |
|-----------|-------------|
| `location-priority` | GPS 精度等級：`no-gps`、`low-power`、`balanced`、`high-accuracy` |
| `location-min-interval` | 位置擷取之間的最短秒數 |
| `location-max-age` | 可接受的快取位置的最長存在時間（秒） |

稽核日誌捕獲：
- 問題名稱和事件類型（`question`、`form.start`、`form.exit`、`form.save`、`form.finalize`）
- 每個事件的開始和結束時間戳
- GPS 座標（如果設定了 `location-priority`）

{{% alert icon=" " context="warning" %}}
`audit` 字段為每個提交生成一個單獨的文件。確保您的資料管道同時處理主表單資料和稽核 CSV。
{{% /alert %}}

---

## 完整範例

典型的家庭問卷調查可能包含所有時間和調查員元資料字段：

| type | name | label |
|------|------|-------|
| start | start | |
| end | end | |
| today | today | |
| deviceid | deviceid | |
| username | username | |
| email | email | |
| audit | audit | |
| text | household_id | 家庭 ID |
| ... | ... | ... |

---

## 最佳實踐

1. 始終包含 `start` 和 `end`——它們是免費的、自動的，對品質監控非常有價值。
2. 始終包含 `username` 以追蹤調查員。
3. 當您想要檢測重複提交或追蹤實地裝置時，包含 `deviceid`。
4. 在需要驗證調查員確實訪問了每個問題的高責任性問卷調查中使用 `audit`。
5. SIM 相關字段（`simserial`、`subscriberid`、`devicephonenum`）僅在帶有活躍 SIM 卡的 Android 裝置上可靠——對於僅使用平板電腦的部署，請跳過它們。

---

## 限制

- 所有元資料字段都是**唯讀的**——它們不能被其他計算引用或修改。
- `username` 和 `email` 需要調查員登入；對於匿名提交，它們將為空。
- SIM/電話元資料字段在僅 Wi-Fi 平板電腦和某些 Android 版本上可能返回空值，原因是權限限制。
