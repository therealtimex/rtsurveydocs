---
weight: 2
title: "Linode（阿卡邁雲）"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "使用 StackScript 在 Linode 上部署 rtCloud。無需配置 - 只需建立伺服器並遵循部署後步驟即可。"
---

## 步驟 1 — 啟動 StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

這將開啟 Linode Cloud Manager 中的 StackScript 頁面。按一下**部署新的 Linode**。

---

## 第 2 步 — 填寫 Linode 的表格

填寫Linode的標準伺服器建立表單：

|領域 |建議值|
|--------|------------------|
| **圖片** | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS
| **地區** |最貼近您的使用者 |
| **方案** |共享 CPU 4 GB 或更大 |
| **根密碼** |設定強密碼 |
| **時區** *（我們唯一的欄位）* |您的伺服器時區（預設值：`Asia/Ho_Chi_Minh`）|

完成後點選 **建立 Linode**。

---

## 步驟 3 — 等待設定完成

該腳本在首次啟動時自動運行。它會安裝 Docker、拉取 rtSurvey 映像、初始化資料庫並啟動所有服務。這需要 **5-10 分鐘**。

您可以直接在 **Linode Cloud Manager** 中查看進度 - 無需 SSH：

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. 點選您新建立的Linode
3. 點選**啟動 LISH 控制台**（Linode 詳細資料頁面右上角）

將開啟一個瀏覽器終端，顯示即時啟動日誌 - **Weblish** 標籤直接在瀏覽器中執行，無需 SSH 用戶端。

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

等到你看到：

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

該日誌還顯示您的伺服器 IP — 您將在下一步中需要它。

---

## Step 4 — Set up SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

依照 **[設定 SSL 指南 →](../ssl-setup)** 設定 HTTPS。免費的**rtsurvey.com 子網域**是最快的選擇 - 無需 DNS 設定。

---

## 步驟 5 — 首次登入

SSL 啟動後，請依照 **[首次登入指南 →](../first-login)** 存取管理員帳號。

---

## 步驟 6 — 更改預設密碼

所有密碼預設為“admin”。首次登入後立即更改它們：

- **應用程式管理員密碼** — 應用程式內的帳戶設置
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## 防火牆規則（Linode雲端防火牆）

如果您將 Linode 雲端防火牆附加到此伺服器，請使用下列規則：

### 入境

|標籤|行動|協定|港口|來源 |筆記|
|--------|--------|----------|--------|---------|--------|
| `接受入站 ssh` |接受 | TCP | 22 | 22所有 IPv4、所有 IPv6 | SSH 存取 |
| `接受入站http` |接受 | TCP | 80|所有 IPv4、所有 IPv6 | Nginx（HTTP + ACME 挑戰）|
| `接受入站-https` |接受 | TCP | 443 | 443所有 IPv4、所有 IPv6 | Nginx（SSL 設定後的 HTTPS）|
| `接受入站閃亮` |接受 | TCP | 3838|所有 IPv4、所有 IPv6 |閃亮的伺服器（R 分析）|
| `接受入站 icmp` |接受 | ICMP | — |所有 IPv4、所有 IPv6 | Ping / 診斷 |
|預設入站策略 | **掉落** | | | |阻止其他所有內容 |

### 出境

|標籤|行動|筆記|
|--------|--------|--------|
|預設出站策略 | **接受** |允許所有出站（Docker 拉取、certbot、GoDaddy API 等）|

### 外部不需要的連接埠

這些連接埠僅綁定到“127.0.0.1”，並且永遠無法從伺服器外部存取：

|港口|服務 |原因 |
|------|---------|--------|
| 8080|應用容器| Nginx 在內部代理它 |
| 8090|鑰匙斗篷容器| Nginx 在內部代理它 |
| 3306| MySQL |僅限內部 Docker 網路 |

---

## 故障排除

### 檢查設定日誌

```bash
tail -200 /var/log/stackscript.log
```

### 檢查 SSL 日誌

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### 查看容器狀態

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
