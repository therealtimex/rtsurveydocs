---
weight: 1
title: "快速入門"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "使用 Docker Compose 在 10 分鐘內在您自己的伺服器上啟動 rtCloud。"
---

本指南帶您從零開始在 Linux 伺服器上部署自行託管的 rtCloud 實例。完成後，您將在瀏覽器中擁有一個可執行的 rtCloud。

## 前提條件

開始之前，請確保您的伺服器符合以下要求：

### 硬體

| 資源 | 最低配置 | 建議配置 |
|----------|---------|-------------|
| RAM | 2 GB | 4 GB |
| 磁碟 | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |

### 軟體

| 軟體 | 版本 |
|----------|---------|
| 作業系統 | Ubuntu 20.04 LTS 或更新版本（或任何支援 Docker 的 Linux） |
| Docker | 20.10 或更新版本 |
| Docker Compose | v2.x（`docker compose`）或 v1.x（`docker-compose`） |

**在 Ubuntu 上安裝 Docker：**

```bash
curl -fsSL https://get.docker.com | sh
```

驗證安裝：

```bash
docker --version
docker compose version
```

---

## 步驟 1 — 取得檔案

將部署儲存庫克隆至您的伺服器：

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## 步驟 2 — 設定環境

複製範例設定檔：

```bash
cp .env.production.sample .env
```

在文字編輯器中開啟 `.env` 並填入所需值：

```dotenv
# 此部署的唯一識別碼（無空格，無特殊字符）
PROJECT_ID=myproject

# 使用者存取應用程式的域名或 IP 位址
# 範例：rtcloud.example.com 或 192.168.1.100
PROJECT_URL=rtcloud.example.com

# 協定：如果有域名和 SSL 請使用「https」，否則使用「http」
HTTP_PROTOCOL=https

# 強健、唯一的密碼——啟動前請更改全部三個
MYSQL_PASSWORD=change_me_strong_password
MYSQL_ROOT_PASSWORD=change_me_root_password
ADMIN_PASSWORD=change_me_admin_password
```

> **重要：** Docker Compose 只會自動讀取 `.env`。請勿建立名為 `.env.production` 的檔案，以免造成混淆。`ADMIN_PASSWORD` 僅在全新資料庫的**首次啟動**時套用。

---

## 步驟 3 — 啟動容器

在後台啟動所有服務：

```bash
docker compose -f docker-compose.production.yml up -d
```

首次啟動需要 **3–5 分鐘**，Docker 會：

1. 拉取 rtCloud 應用程式映像（約 1 GB 下載）
2. 初始化 MySQL 資料庫
3. 載入基礎架構
4. 執行所有待定的資料庫遷移

即時監控啟動進度：

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

等到看到表示應用程式已就緒的輸出。您也可以監看容器健康狀態：

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## 步驟 4 — 存取應用程式

兩個容器均顯示 `Up (healthy)` 後，請開啟瀏覽器：

```
http://<PROJECT_URL>:8080
```

使用管理員帳號登入：

| 欄位 | 值 |
|-------|-------|
| 使用者名稱 | `admin` |
| 密碼 | 您在 `.env` 中為 `ADMIN_PASSWORD` 設定的值 |

> 首次登入後，請立即從帳號設定頁面更改管理員密碼。

---

## 步驟 5 — 驗證所有服務

檢查所有容器是否正在執行且健康：

```bash
docker compose -f docker-compose.production.yml ps
```

預期輸出：

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

如果容器顯示 `Up (starting)` 或 `Up (unhealthy)`，請再等待 30–60 秒後再次檢查。MySQL 在首次啟動時可能需要最多一分鐘才能完全初始化。

---

## 連接埠參考

| 連接埠 | 服務 | 說明 |
|------|---------|-------------|
| `8080` | rtCloud 應用程式 | 主要網頁 UI（可透過 `APP_PORT` 設定） |
| `3838` | Shiny 伺服器 | 分析和基於 R 的視覺化（可透過 `SHINY_PORT` 設定） |

MySQL（連接埠 3306）和任何選用服務（Keycloak）預設為內部專用，不暴露給主機。

---

## 後續步驟

您的 rtCloud 實例現在正在執行。請考慮以下後續任務：

- **啟用 HTTPS** — 將域名指向您的伺服器並使用 Let's Encrypt 設定 SSL。請參閱[雲端部署](cloud-deployment)以取得自動化 HTTPS 設定。
- **檢視所有設定** — 瀏覽[設定參考](configuration)以針對生產環境調整您的部署。
- **設定 SSO** — 連接身份提供者以進行集中式使用者驗證。請參閱 [SSO 驗證](sso-authentication)。
- **規劃備份** — 查看[維護](maintenance)頁面以了解備份和升級程序。
