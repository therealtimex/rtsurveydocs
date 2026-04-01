---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "使用 StackScript 在 Linode 上部署 rtCloud。无需配置 — 只需创建服务器并按照部署后步骤操作。"
---

## Step 1 — Launch the StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

This opens the StackScript page in Linode Cloud Manager. Click **Deploy New Linode**.

---

## Step 2 — Fill in Linode's form

Fill in Linode's standard server creation form:

| Field | Recommended value |
|-------|------------------|
| **Image** | Ubuntu 22.04 LTS |
| **Region** | Closest to your users |
| **Plan** | Shared CPU 4 GB or larger |
| **Root Password** | Set a strong password |
| **Timezone** *(our only field)* | Your server timezone (default: `Asia/Ho_Chi_Minh`) |

Click **Create Linode** when done.

---

## Step 3 — Wait for setup to complete

The script runs automatically on first boot. It installs Docker, pulls the rtSurvey image, initialises the database, and starts all services. This takes **5–10 minutes**.

You can watch progress directly in **Linode Cloud Manager** — no SSH required:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Click on your newly created Linode
3. Click **Launch LISH Console** (top right of the Linode detail page)

A browser terminal opens showing the live boot log — the **Weblish** tab works directly in your browser, no SSH client needed.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Wait until you see:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

The log also shows your server IP — you will need it for the next step.

---

## Step 4 — Set up SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Follow the **[Set Up SSL guide →](../ssl-setup)** to configure HTTPS. The free **rtsurvey.com subdomain** is the fastest option — no DNS setup needed.

---

## Step 5 — First login

Once SSL is active, follow the **[First Login guide →](../first-login)** to access the admin account.

---

## Step 6 — Change the default password

All passwords default to `admin`. Change them immediately after your first login:

- **App admin password** — account settings inside the app
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## 防火墙规则（Linode Cloud Firewall）

如果您将 Linode Cloud Firewall 附加到此服务器，请使用以下规则：

### 入站规则（Inbound）

| 标签 | 操作 | 协议 | 端口 | 来源 | 备注 |
|------|------|------|------|------|------|
| `accept-inbound-ssh` | 接受 | TCP | 22 | All IPv4, All IPv6 | SSH 访问 |
| `accept-inbound-http` | 接受 | TCP | 80 | All IPv4, All IPv6 | Nginx（HTTP + ACME 验证） |
| `accept-inbound-https` | 接受 | TCP | 443 | All IPv4, All IPv6 | Nginx（SSL 配置后的 HTTPS） |
| `accept-inbound-shiny` | 接受 | TCP | 3838 | All IPv4, All IPv6 | Shiny Server（R 分析） |
| `accept-inbound-icmp` | 接受 | ICMP | — | All IPv4, All IPv6 | Ping / 诊断 |
| 默认入站策略 | **丢弃** | | | | 阻止其他所有流量 |

### 出站规则（Outbound）

| 标签 | 操作 | 备注 |
|------|------|------|
| 默认出站策略 | **接受** | 允许所有出站流量（Docker、certbot、GoDaddy API 等） |

### 无需对外开放的端口

这些端口仅绑定到 `127.0.0.1`，无法从外部访问：

| 端口 | 服务 | 原因 |
|------|------|------|
| 8080 | 应用容器 | Nginx 在内部代理 |
| 8090 | Keycloak 容器 | Nginx 在内部代理 |
| 3306 | MySQL | 仅限 Docker 内部网络 |

---

## Troubleshooting

### Check the setup log

```bash
tail -200 /var/log/stackscript.log
```

### Check the SSL log

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### View container status

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
