---
weight: 5
title: "首次登入"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "如何在部署後首次登入您的 rtSurvey 執行個體。"
---

> **登入前必須設定 SSL。** 如果您透過 HTTP 存取應用程式，將看到安全性警告且 SSO 將被封鎖。請先完成 [SSL 設定](ssl-setup)。

SSL 啟用後，在您的 HTTPS 網址開啟瀏覽器：

```
https://your-domain.com
```

---

## 登入畫面

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

登入頁面顯示：

- **使用者名稱**和**密碼**欄位
- **登入**按鈕
- **使用 SSO 登入**按鈕（分隔線下方）— 供擁有 SSO 帳戶的團隊成員使用

---

## 預設管理員憑證

輸入預設憑證並點選**登入**：

| 欄位 | 值 |
|------|----|
| 使用者名稱 | `admin` |
| 密碼 | `admin` |

> **首次登入後立即變更密碼。**

---

## 如果看到安全性警告

如果您透過 HTTP 存取應用程式（SSL 設定前），將看到：

- 登入頁面頂部的黃色警告橫幅
- 點選**登入**時彈出的對話框，警告憑證將以未加密形式傳送

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

點選**設定 SSL** 來設定 HTTPS，或點選**無論如何繼續**以不使用 SSL 登入（不建議）。

HTTP 上的 SSO 登入被完全封鎖——點選**使用 SSO 登入**將顯示通知而非重新導向。

---

## 登入後

登入後，您將進入儀表板。從這裡：

1. **變更管理員密碼** — 帳戶設定 → 變更密碼
2. **建立第一個專案** — 專案 → 新增專案
3. **上傳或建立表單** — 表單 → 上傳 XLSForm 或開啟表單建構器
4. **新增使用者** — 使用者 → 邀請或為您的團隊建立帳戶
