---
weight: 4
title: "SSL 설정"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "rtSurvey 서버에 HTTPS를 구성합니다. 로그인 전에 필요합니다."
---

SSL은 로그인하기 전에 구성해야 합니다. 앱을 처음 열면 SSL 설정 화면으로 자동 리다이렉션됩니다.

---

## SSL 설정 옵션

![SSL 설정 옵션](/img/ssl-setup/ssl-setup-options.png)

| Option | When to use |
|--------|-------------|
| **무료 rtsurvey.com 서브도메인 *(권장)*** | No DNS setup needed. We create the record for you. Ready in 2–5 minutes. |
| **내 도메인** | You already have a domain and its DNS points to this server. |
| **인증서 수동 설치** | Enterprise or custom CA. Requires SSH access. |

---

## Option 1 — 무료 rtsurvey.com 서브도메인 *(권장)*

This is the fastest option. No domain registration or DNS changes required.

1. Click **무료 rtsurvey.com 서브도메인 *(권장)*** to expand the section
2. Type your desired subdomain name in the input field

   > Use lowercase letters, numbers, and hyphens. 3–30 characters.
   > Example: `myproject` → `myproject.rtsurvey.com`

3. Click **Create https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Wait 2–5 minutes while the certificate is issued

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Once the certificate is ready, you will be redirected to your new HTTPS URL automatically

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Option 2 — 내 도메인

Use this if you have an existing domain and its DNS `A` record already points to this server's IP.

1. Click **내 도메인** to expand the section
2. Enter your full domain name (e.g. `survey.myorganization.org`)
3. Click **Create certificate**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt will verify your domain and issue a certificate. This requires DNS to be correctly pointed first — the request will fail otherwise.

---

## Option 3 — 인증서 수동 설치

For enterprise environments using a custom or internal CA. You will place your certificate files on the server via SSH, then enter your domain in the app.

### Prerequisites

- SSH access to the server
- A valid certificate and private key for your domain (PEM format)

### Step 1 — SSH into the server

```bash
ssh root@<server-ip>
```

### Step 2 — Place your certificate files

Create the directory and copy your files:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Copy your files into that directory with these exact names:

| File | Description |
|------|-------------|
| `fullchain.pem` | Your certificate + any intermediate CA certificates (concatenated) |
| `privkey.pem` | Your private key |

Example:

```bash
# Copy from your local machine (run this locally, not on the server)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Set correct permissions:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Step 3 — Enter your domain in the app

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. In the SSL setup screen, click **인증서 수동 설치**
2. Enter your domain name (must match the certificate's Common Name or SAN)
3. Click **Apply**

The server will configure Nginx with your certificate and reload automatically.

---

## 다음 단계

SSL이 활성화되면 [첫 번째 로그인](first-login)으로 이동하세요.
