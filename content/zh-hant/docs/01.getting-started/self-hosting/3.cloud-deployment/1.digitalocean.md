---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "使用自動化使用者資料腳本在 DigitalOcean Droplet 上部署 rtCloud。"
---

DigitalOcean 使用**使用者資料**腳本，在首次啟動時自動執行。您在腳本頂部填寫設定變數，然後在建立 Droplet 時貼上整個腳本。

> 與 Linode StackScripts 不同，DigitalOcean 沒有表單 UI——您必須在貼上之前直接編輯腳本。

**下載腳本：** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## 嵌入式 Keycloak（推薦）

使用 `digitalocean-droplet-keycloak-embed.sh` 進行內建 SSO 的最簡單設定。

### 步驟 1 — 填寫設定

開啟腳本並編輯頂部的 `CONFIGURATION` 區塊：

```bash
# --- Required ---
PROJECT_ID="rtsurvey"                  # Unique identifier for your project (no spaces)
ADMIN_PASSWORD="admin"                 # Password for app admin and Keycloak — change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Your domain — DNS A record must point here
PROJECT_URL=""                         # Leave blank unless behind Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email for Let's Encrypt notifications

# --- Optional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| 欄位 | 必填 | 說明 |
|-------|----------|-------------|
| `PROJECT_ID` | 是 | 用作資料庫名稱和 Keycloak 客戶端 ID。小寫，無空格。 |
| `ADMIN_PASSWORD` | 否 | 應用程式管理員登入和 Keycloak 管理控制台的密碼。預設為 `admin`——**首次登入後請更改**。 |
| `DOMAIN` | 是 | 您的域名。DNS A 記錄必須指向 Droplet IP。 |
| `LETSENCRYPT_EMAIL` | 是 | Let's Encrypt 憑證通知的電子郵件地址。 |
| `PROJECT_URL` | 否 | 覆寫公開 URL。留空以使用 `DOMAIN`。在 Cloudflare 後面時有用。 |

> **安全性：** 所有密碼預設為 `admin`。首次登入後請立即更改。

### 步驟 2 — 建立 Droplet

在 [DigitalOcean 控制面板](https://cloud.digitalocean.com)：

1. 點選**建立** → **Droplets**
2. 選擇 **Ubuntu 22.04 LTS** 作為映像
3. 選取 **Basic，4 GB RAM / 2 vCPUs** 或更大
4. 捲動至**進階選項** → 勾選**新增初始化腳本**
5. 將完整腳本內容貼入文字區域
6. 點選**建立 Droplet**

### 步驟 3 — 新增 DNS 記錄

Droplet 啟動時，在您的 DNS 提供商中新增一個 **A 記錄**：

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### 步驟 4 — 監控進度

SSH 進入 Droplet 並查看日誌：

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

腳本在開始時打印您的伺服器 IP——看到後立即新增 DNS 記錄。

### 步驟 5 — 存取應用程式

設定完成後，日誌顯示摘要：

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

在瀏覽器中開啟 `https://myapp.example.com`，使用使用者名稱 `admin` 和密碼 `admin` 登入。

> 登入後立即透過右上角選單中的**設定**更改您的密碼。

---

## 部署後

### 更改密碼

SSH 進入 Droplet，編輯 `.env`，並重啟受影響的容器：

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### 更新域名

如果在部署後指定不同的域名，請更新 `.env` 中的 `PROJECT_URL`：

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### 查看所有容器

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
