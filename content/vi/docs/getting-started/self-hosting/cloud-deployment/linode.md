---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Triển khai rtCloud trên Linode bằng StackScript. Không cần cấu hình — chỉ cần tạo máy chủ và làm theo các bước sau khi triển khai."
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

## Quy tắc tường lửa (Linode Cloud Firewall)

Nếu bạn gắn Linode Cloud Firewall vào máy chủ này, hãy sử dụng các quy tắc sau:

### Inbound (Lưu lượng vào)

| Nhãn | Hành động | Giao thức | Cổng | Nguồn | Ghi chú |
|------|----------|----------|------|-------|---------|
| `accept-inbound-ssh` | Chấp nhận | TCP | 22 | All IPv4, All IPv6 | Truy cập SSH |
| `accept-inbound-http` | Chấp nhận | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + ACME challenge) |
| `accept-inbound-https` | Chấp nhận | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS sau khi cài SSL) |
| `accept-inbound-shiny` | Chấp nhận | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | Chấp nhận | ICMP | — | All IPv4, All IPv6 | Ping / chẩn đoán |
| Chính sách inbound mặc định | **Chặn** | | | | Chặn tất cả còn lại |

### Outbound (Lưu lượng ra)

| Nhãn | Hành động | Ghi chú |
|------|----------|---------|
| Chính sách outbound mặc định | **Chấp nhận** | Cho phép tất cả lưu lượng ra (Docker, certbot, GoDaddy API, v.v.) |

### Các cổng KHÔNG cần mở ra ngoài

Các cổng này chỉ được gắn với `127.0.0.1` và không thể truy cập từ bên ngoài:

| Cổng | Dịch vụ | Lý do |
|------|---------|-------|
| 8080 | App container | Nginx proxy nội bộ |
| 8090 | Keycloak container | Nginx proxy nội bộ |
| 3306 | MySQL | Chỉ trong mạng Docker nội bộ |

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
