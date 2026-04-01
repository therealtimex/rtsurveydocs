---
weight: 5
title: "維護"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "build"
toc: true
description: "自行託管 rtCloud 實例的日常維護：升級、備份、還原和常見問題疑難排解。"
---

## 常用指令

定期使用這些指令管理您的 rtCloud 容器。在包含 `docker-compose.production.yml` 的目錄中執行它們。

```bash
# Check status and health of all containers
docker compose -f docker-compose.production.yml ps

# View live logs (all services)
docker compose -f docker-compose.production.yml logs -f

# View logs for the app only
docker compose -f docker-compose.production.yml logs -f rtcloud

# Restart a single container
docker compose -f docker-compose.production.yml restart rtcloud

# Stop all services
docker compose -f docker-compose.production.yml down

# Start all services
docker compose -f docker-compose.production.yml up -d

# Open a shell inside the app container
docker compose -f docker-compose.production.yml exec rtcloud bash
```

---

## 升級

rtCloud 更新以新的 Docker 映像標籤形式發布。升級會拉取最新映像並重新建立應用程式容器。資料庫遷移在啟動時自動執行。

**1. 拉取最新映像：**

```bash
docker compose -f docker-compose.production.yml pull
```

**2. 重新建立應用程式容器：**

```bash
docker compose -f docker-compose.production.yml up -d
```

Docker 只替換映像已更改的容器。MySQL 容器和所有命名磁碟區不受影響。

### 固定版本

若要升級到特定版本而不是 `latest`，請更新 `.env` 中的 `RTCLOUD_IMAGE`：

```dotenv
RTCLOUD_IMAGE=rtawebteam/rta-smartsurvey:1.2.3
```

然後如上所述執行 `docker compose pull` 和 `up -d`。

### 降級

通常不建議降級，因為資料庫遷移無法還原。如果必須降級，請從升級前的資料庫備份還原。

---

## 備份與還原

### 備份資料庫

執行以下指令將應用程式資料庫匯出至 SQL 檔案：

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > backup-$(date +%Y%m%d-%H%M%S).sql
```

備份檔案寫入主機上您的當前目錄。

### 還原資料庫

```bash
docker compose -f docker-compose.production.yml exec -T mysql \
  mysql -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  < backup-20240101-120000.sql
```

### 備份上傳的檔案

問卷調查提交通常包含上傳的檔案（照片、音頻、文件），儲存在命名的 Docker 磁碟區中。請與資料庫分開備份：

```bash
# Backup uploads
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/uploads-$(date +%Y%m%d).tar.gz -C /data .

# Backup audio recordings
docker run --rm \
  -v rtcloud_audios:/data \
  -v "$(pwd):/backup" \
  alpine tar czf /backup/audios-$(date +%Y%m%d).tar.gz -C /data .
```

如果您更改了預設值，請將 `rtcloud_uploads` 和 `rtcloud_audios` 替換為您的實際磁碟區名稱（以 `COMPOSE_PROJECT_NAME` 為前綴）。

### 還原上傳的檔案

```bash
docker run --rm \
  -v rtcloud_uploads:/data \
  -v "$(pwd):/backup" \
  alpine tar xzf /backup/uploads-20240101.tar.gz -C /data
```

### 自動每日備份

在主機上新增 cron 任務以自動執行備份。使用 `crontab -e` 編輯 root 的 crontab：

```cron
# Daily database backup at 2:00 AM, keep 30 days of history
0 2 * * * cd /opt/rtcloud && docker compose -f docker-compose.production.yml exec -T mysql \
  mysqldump -u root -p"$(grep MYSQL_ROOT_PASSWORD .env | cut -d= -f2)" smartsurvey \
  > /backups/db-$(date +\%Y\%m\%d).sql && \
  find /backups -name "db-*.sql" -mtime +30 -delete
```

---

## 疑難排解

### 應用程式容器無法啟動

檢查容器日誌以查看錯誤訊息：

```bash
docker compose -f docker-compose.production.yml logs rtcloud
```

常見原因：
- `.env` 中缺少或無效的環境變數
- MySQL 尚未就緒（等待 60 秒後再次檢查）
- 連接埠衝突——另一個程序已在使用 `APP_PORT`

### MySQL 不健康

```bash
docker compose -f docker-compose.production.yml logs mysql
```

常見原因：
- `.env` 中未設定 `MYSQL_ROOT_PASSWORD`
- 損壞的資料磁碟區（罕見——使用 `df -h` 檢查磁碟空間）

MySQL 在首次啟動時可能需要 30–60 秒才能初始化。在判斷失敗之前，請等待後再次檢查。

### 連接埠已在使用中

在 `.env` 中將 `APP_PORT` 或 `SHINY_PORT` 更改為可用連接埠，然後重新建立容器：

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate
```

若要查看主機上正在使用某個連接埠的程序：

```bash
lsof -i :8080
```

### 400 CSRF 令牌無法驗證

此錯誤出現在本地或反向代理環境中，請求來源與預期主機不匹配。僅在本地開發環境中停用 CSRF 驗證：

```dotenv
CSRF_VALIDATION_ENABLED=false
```

然後重啟應用程式：

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

> 請勿在生產環境中停用 CSRF 驗證。如果在生產環境中出現此錯誤，請確保您的反向代理正在轉發正確的 `Host` 和 `X-Forwarded-For` 標頭。

### 忘記管理員密碼

直接在資料庫中重設管理員密碼。連接至 MySQL 容器並更新密碼雜湊：

**步驟 1** — 生成新密碼雜湊。將 `newpassword` 替換為您想要的密碼：

```bash
docker compose -f docker-compose.production.yml exec rtcloud php -r "
  \$salt = trim(shell_exec(\"mysql -h mysql -u root -p\\\"\${MYSQL_ROOT_PASSWORD}\\\" \${MYSQL_DATABASE} -se \\\"SELECT salt FROM ss_user WHERE username='admin';\\\"\"));
  echo md5(\$salt . 'newpassword') . PHP_EOL;
"
```

**步驟 2** — 在資料庫中更新雜湊：

```bash
docker compose -f docker-compose.production.yml exec mysql \
  mysql -u root -p"${MYSQL_ROOT_PASSWORD}" smartsurvey \
  -e "UPDATE ss_user SET password='<hash_from_step_1>' WHERE username='admin';"
```

### 容器持續重啟

檢查健康檢查是否失敗：

```bash
docker compose -f docker-compose.production.yml ps
docker inspect rtcloud-app --format '{{json .State.Health}}'
```

應用程式健康檢查呼叫 `/health` 端點。如果持續失敗，請檢查應用程式日誌以查找啟動錯誤。

### 磁碟空間已滿

確認佔用空間的原因：

```bash
# Check host disk usage
df -h

# Check Docker disk usage (images, containers, volumes)
docker system df

# Remove unused images and stopped containers (safe to run)
docker system prune
```

請勿使用 `docker system prune --volumes`，因為這將刪除應用程式資料。

---

## 健康檢查

每個服務都有自動健康檢查。容器狀態反映結果：

| 容器 | 檢查方法 | 啟動期間 | 間隔 |
|-----------|-------------|-------------|----------|
| `rtcloud-app` | HTTP GET `/health` | 90 秒 | 30 秒 |
| `rtcloud-mysql` | `mysqladmin ping` | 30 秒 | 10 秒 |
| `rtcloud-keycloak` | HTTP GET `:9000/health/live` | 120 秒 | 30 秒 |

健康檢查失敗的容器會根據 `RESTART_POLICY` 設定（預設：`unless-stopped`）自動重啟。
