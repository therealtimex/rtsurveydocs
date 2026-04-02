---
weight: 4
title: "设置 SSL"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "为您的 rtSurvey 服务器配置 HTTPS。需要先登录才能登录。"
---

登录之前必须配置 SSL。首次打开应用程序时，您将自动重定向到 SSL 设置屏幕。

---

## SSL 设置选项

![SSL 设置选项](/img/ssl-setup/ssl-setup-options.png)

选择以下三个选项之一：

| 选项 | 何时使用 |
|--------|-------------|
| **免费 rtsurvey.com 子域** *(受到推崇的)* | 无需 DNS 设置。我们为您创造记录。 2-5 分钟内准备就绪。 |
| **我自己的域名** | 您已经有一个域，并且它的 DNS 指向该服务器。 |
| **手动安装证书** | 企业或自定义 CA。需要 SSH 访问。 |

---

## 选项 1 — 免费 rtsurvey.com 子域（推荐）

这是最快的选择。无需域名注册或 DNS 更改。

1. 单击免费 rtsurvey.com 子域以展开该部分
2. 在输入字段中输入您想要的子域名

   > 使用小写字母、数字和连字符。 3–30 个字符。
   > 例子： `myproject` → `myproject.rtsurvey.com`

3. 单击创建 **https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. 颁发证书时等待 2-5 分钟

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. 证书准备就绪后，您将自动重定向到新的 HTTPS URL

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## 选项 2 — 我自己的域

如果您有现有域且其 DNS A 记录已指向该服务器的 IP，请使用此选项。

1. 单击我自己的域以展开该部分
2. 输入您的完整域名 (e.g. `survey.myorganization.org`)
3. 单击创建证书

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt 将验证您的域并颁发证书。这需要首先正确指向 DNS，否则请求将失败。

---

## 选项 3 — 手动安装证书

适用于使用自定义或内部 CA 的企业环境。您将通过 SSH 将证书文件放置在服务器上，然后在应用程序中输入您的域名。

### 先决条件

- 通过 SSH 访问服务器
- 您的域的有效证书和私钥（PEM 格式）

### 第 1 步 — 通过 SSH 连接到服务器

```bash
ssh root@<server-ip>
```

### 第 2 步 — 放置您的证书文件

创建目录并复制文件：

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

使用以下确切名称将文件复制到该目录中：

| 文件 | 描述 |
|------|-------------|
| `fullchain.pem` | 您的证书 + 任何中间 CA 证书（串联） |
| `privkey.pem` | 你的私钥 |

例子：

```bash
# 从本地计算机复制（在本地运行，而不是在服务器上运行）
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

设置正确的权限：

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### 第 3 步 — 在应用程序中输入您的域名

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. 在 SSL 设置屏幕中，单击手动安装证书
2. 输入您的域名（必须与证书的公用名或 SAN 匹配）
3. 单击“应用”

服务器将使用您的证书配置 Nginx 并自动重新加载。

---

## 下一步

SSL 激活后，继续首次登录。 [first-login](first-login).
