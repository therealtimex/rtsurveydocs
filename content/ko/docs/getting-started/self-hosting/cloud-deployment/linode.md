---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "StackScript를 사용하여 Linode에 rtCloud를 배포합니다. 구성 불필요 — 서버를 만들고 배포 후 단계를 따르세요."
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

## 방화벽 규칙 (Linode Cloud Firewall)

이 서버에 Linode Cloud Firewall을 연결하는 경우 다음 규칙을 사용하세요:

### 인바운드 (수신)

| 레이블 | 작업 | 프로토콜 | 포트 | 소스 | 비고 |
|-------|------|---------|------|------|------|
| `accept-inbound-ssh` | 허용 | TCP | 22 | All IPv4, All IPv6 | SSH 접근 |
| `accept-inbound-http` | 허용 | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME 챌린지) |
| `accept-inbound-https` | 허용 | TCP | 443 | All IPv4, All IPv6 | Nginx (SSL 설정 후 HTTPS) |
| `accept-inbound-shiny` | 허용 | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R 분석) |
| `accept-inbound-icmp` | 허용 | ICMP | — | All IPv4, All IPv6 | Ping / 진단 |
| 기본 인바운드 정책 | **차단** | | | | 나머지 모두 차단 |

### 아웃바운드 (송신)

| 레이블 | 작업 | 비고 |
|-------|------|------|
| 기본 아웃바운드 정책 | **허용** | 모든 아웃바운드 트래픽 허용 (Docker, certbot, GoDaddy API 등) |

### 외부에 불필요한 포트

이 포트들은 `127.0.0.1`에만 바인딩되어 외부에서 접근할 수 없습니다:

| 포트 | 서비스 | 이유 |
|------|--------|------|
| 8080 | 앱 컨테이너 | Nginx가 내부에서 프록시 |
| 8090 | Keycloak 컨테이너 | Nginx가 내부에서 프록시 |
| 3306 | MySQL | Docker 내부 네트워크 전용 |

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
