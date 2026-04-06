---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "使用自动化用户数据脚本在 DigitalOcean Droplet 上部署 rtCloud。"
---

DigitalOcean 使用在首次启动时自动运行的 **用户数据** 脚本。您在脚本顶部填写配置变量，然后在创建 Droplet 时粘贴整个脚本。

> 与 Linode StackScripts 不同，DigitalOcean 没有表单 UI — 您必须在粘贴之前直接编辑脚本。

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## 嵌入式钥匙斗篷（推荐）

使用“digitalocean-droplet-keycloak-embed.sh”通过内置 SSO 进行最简单的设置。

### 第 1 步 — 填写配置

打开脚本并编辑顶部的“CONFIGURATION”块：

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

|领域 |必填|描述 |
|--------|----------|-------------|
| `项目_ID` |是的 |用作数据库名称和 Keycloak 客户端 ID。小写，无空格。 |
| `管理员密码` |没有 |应用程序管理员登录和 Keycloak 管理控制台的密码。默认为“admin”——**首次登录后更改**。 |
| `域` |是的 |您的域名。 DNS A 记录必须指向 Droplet IP。 |
| `LETSENCRYPT_EMAIL` |是的 | Let's Encrypt 证书通知的电子邮件地址。 |
| `PROJECT_URL` |没有 |覆盖公共 URL。留空以使用“DOMAIN”。在 Cloudflare 背后很有用。 |

> **安全性：** 所有密码默认为“admin”。首次登录后立即更改它们。

### 步骤 2 — 创建 Droplet

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. 单击 **创建** → **Droplets**
2.选择**Ubuntu 22.04 LTS**作为镜像
3. 选择 **基本、4 GB RAM / 2 vCPU** 或更大
4. 滚动到 **高级选项** → 选中 **添加初始化脚本**
5. 将完整的脚本内容粘贴到文本区域
6. 单击“**创建 Droplet**”

### 步骤 3 — 添加 DNS 记录

当 Droplet 启动时，在您的 DNS 提供商中添加 **A 记录**：

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### 第 4 步 — 监控进度

通过 SSH 进入 Droplet 并观察日志：

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

该脚本在开头附近打印您的服务器 IP — 一旦您看到它就添加 DNS 记录。

### 第 5 步 — 访问应用程序

设置完成后，日志会显示摘要：

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

Open `https://myapp.example.com` in your browser and log in with username `admin` and password `admin`.

> 通过右上角菜单中的**设置**登录后立即**更改您的密码**。

---

## 部署后

### 更改密码

通过 SSH 连接到 Droplet，编辑 `.env`，然后重新启动受影响的容器：

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### 更新域名

如果您在部署后分配不同的域，请更新“.env”中的“PROJECT_URL”：

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### 查看所有容器

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
