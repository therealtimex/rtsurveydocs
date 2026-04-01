---
weight: 3
title: "雲端部署"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "使用自動化腳本將 rtCloud 部署至主要雲端提供商，包括 DigitalOcean、AWS EC2、Google Cloud 和 Linode。"
---

部署儲存庫包含適用於主要雲端提供商的自動化佈建腳本。每個腳本在全新的 **Ubuntu 22.04 LTS** 伺服器首次啟動時執行，並執行完全無人值守的設定：

- 安裝 Docker 和 Docker Compose
- 為所有內部服務生成安全隨機密碼
- 寫入 `docker-compose.production.yml` 和 `.env`
- 將 Nginx 設定為反向代理
- 從 Let's Encrypt 取得免費 TLS 憑證（自動重試直到 DNS 解析）
- 設定 UFW 防火牆
- 選擇性地部署嵌入式 Keycloak SSO 伺服器
- 輸出包含所有憑證的完整部署摘要

在標準實例上，設定在 **5–10 分鐘**內完成。

---

## 選擇腳本

根據您的雲端提供商和 SSO 設定，有多種腳本變體：

| 腳本 | 提供商 | SSO 模式 | 最適合 |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | 內建 Keycloak | 簡單、自包含的 SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak 或外部 OIDC | 完全控制 |
| `linode-stackscript-keycloak-embed.sh` | Linode | 內建 Keycloak | 基於表單的設定，最簡單 |
| `linode-stackscript-oidc.sh` | Linode | 僅外部 OIDC | 現有身份提供者 |
| `linode-stackscript.sh` | Linode | Keycloak 或外部 OIDC | 完全控制 |
| `aws-ec2.sh` | AWS EC2 | Keycloak 或外部 OIDC | AWS 部署 |
| `gcp-compute.sh` | Google Cloud | Keycloak 或外部 OIDC | GCP 部署 |

> **大多數使用者推薦：** 使用 `keycloak-embed` 變體。它包含內建的 Keycloak 身份伺服器，需要最少的設定欄位。

---

## 伺服器規格指南

| 使用場景 | RAM | 磁碟 | 範例 |
|----------|-----|------|---------|
| 評估/開發 | 2 GB | 25 GB | DO Basic $18/月，t3.small，e2-small |
| 小型團隊（< 50 使用者） | 4 GB | 40 GB | DO Basic $24/月，t3.medium，e2-medium |
| 生產（> 50 使用者） | 8 GB | 80 GB | DO General $48/月，t3.large，n2-standard-2 |

> 嵌入式 Keycloak 至少需要 **4 GB RAM**。僅在不含 Keycloak 的評估情況下使用 2 GB。

---

## DNS 設定

所有腳本都需要在 Let's Encrypt 能夠發行憑證之前，有一個**指向您伺服器 IP 的 A 記錄**的域名。

腳本在設定過程中較早期會列印您的伺服器 IP：

```
============================================================
 Server IP : 139.162.51.85
 Add this DNS A record now if you haven't already:
   myapp.example.com  ->  139.162.51.85
 The script will retry Certbot every 60s until DNS resolves.
============================================================
```

腳本每 60 秒**自動重試** Let's Encrypt，最多 1 小時。只需新增 DNS 記錄然後等待——不需要重啟。

> **速率限制：** Let's Encrypt 每個域名每 7 天最多允許 **5 個憑證**。避免使用相同域名反複部署和銷毀伺服器。如果達到限制，腳本將顯示 `retry after` 時間戳並立即停止。

---

## 部署後檢查清單

- [ ] 應用程式在 `https://your-domain.com` 開啟
- [ ] 使用 `admin` 和您設定的密碼登入
- [ ] 所有容器健康：`docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] Let's Encrypt 續期正常：`certbot renew --dry-run`
- [ ] MySQL 連接埠 3306 **未**暴露：`ufw status`
- [ ] 設定每日資料庫備份（請參閱[維護](../maintenance)）

---

## 疑難排解

### 檢查完整設定日誌

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Let's Encrypt 速率限制

如果日誌中看到 `too many certificates`，您已達到每 7 天 5 個憑證的限制。日誌顯示確切的重試時間：

```
[SSL] ERROR: Let's Encrypt rate limit hit. retry after 2026-03-15 16:22 UTC.
```

等到那個時間後重新部署。

### Keycloak 持續不健康

確保伺服器至少有 4 GB RAM，然後檢查日誌：

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### certbot 後 SSL 設定未套用

如果憑證已發行但 Nginx 仍顯示僅 HTTP，請檢查日誌中的錯誤行並手動重新載入 Nginx：

```bash
nginx -t && systemctl reload nginx
```
