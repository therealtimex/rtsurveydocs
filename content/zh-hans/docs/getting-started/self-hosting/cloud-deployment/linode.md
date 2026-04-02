---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "使用 StackScript 在 Linode 上部署 rtCloud。无需配置 - 只需创建服务器并遵循部署后步骤即可。"
---

## 步骤 1 — 启动 StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

这将打开 Linode Cloud Manager 中的 StackScript 页面。单击**部署新的 Linode**。

---

## 第 2 步 — 填写 Linode 的表格

填写Linode的标准服务器创建表单：

|领域 |推荐值|
|--------|------------------|
| **图片** | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS
| **地区** |最贴近您的用户 |
| **计划** |共享 CPU 4 GB 或更大 |
| **根密码** |设置强密码 |
| **时区** *（我们唯一的字段）* |您的服务器时区（默认值：`Asia/Ho_Chi_Minh`）|

完成后点击 **创建 Linode**。

---

## 步骤 3 — 等待设置完成

该脚本在首次启动时自动运行。它会安装 Docker、拉取 rtSurvey 映像、初始化数据库并启动所有服务。这需要 **5-10 分钟**。

您可以直接在 **Linode Cloud Manager** 中查看进度 - 无需 SSH：

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. 点击您新创建的Linode
3. 单击**启动 LISH 控制台**（Linode 详细信息页面右上角）

将打开一个浏览器终端，显示实时启动日志 - **Weblish** 选项卡直接在浏览器中运行，无需 SSH 客户端。

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

该日志还显示您的服务器 IP — 您将在下一步中需要它。

---

## 步骤 4 — 设置 SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

按照 **[设置 SSL 指南 →](../ssl-setup)** 配置 HTTPS。免费的**rtsurvey.com 子域**是最快的选择 - 无需 DNS 设置。

---

## 步骤 5 — 首次登录

SSL 激活后，请按照 **[首次登录指南 →](../first-login)** 访问管理员帐户。

---

## 步骤 6 — 更改默认密码

所有密码默认为“admin”。首次登录后立即更改它们：

- **应用程序管理员密码** — 应用程序内的帐户设置
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## 防火墙规则（Linode云防火墙）

如果您将 Linode 云防火墙附加到此服务器，请使用以下规则：

### 入境

|标签|行动|协议|港口|来源 |笔记|
|--------|--------|----------|--------|---------|--------|
| `接受入站 ssh` |接受 | TCP | 22 | 22所有 IPv4、所有 IPv6 | SSH 访问 |
| `接受入站http` |接受 | TCP | 80|所有 IPv4、所有 IPv6 | Nginx（HTTP + ACME 挑战）|
| `接受入站-https` |接受 | TCP | 443 | 443所有 IPv4、所有 IPv6 | Nginx（SSL 设置后的 HTTPS）|
| `接受入站闪亮` |接受 | TCP | 3838|所有 IPv4、所有 IPv6 |闪亮的服务器（R 分析）|
| `接受入站 icmp` |接受 | ICMP | — |所有 IPv4、所有 IPv6 | Ping / 诊断 |
|默认入站策略 | **掉落** | | | |阻止其他所有内容 |

### 出境

|标签|行动|笔记|
|--------|--------|--------|
|默认出站策略 | **接受** |允许所有出站（Docker 拉取、certbot、GoDaddy API 等）|

### 外部不需要的端口

这些端口仅绑定到“127.0.0.1”，并且永远无法从服务器外部访问：

|港口|服务 |原因 |
|------|---------|--------|
| 8080|应用容器 | Nginx 在内部代理它 |
| 8090|钥匙斗篷容器| Nginx 在内部代理它 |
| 3306| MySQL |仅限内部 Docker 网络 |

---

## 故障排除

### 检查设置日志

```bash
tail -200 /var/log/stackscript.log
```

### 检查 SSL 日志

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### 查看容器状态

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
