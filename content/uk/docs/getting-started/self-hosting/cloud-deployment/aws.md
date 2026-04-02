---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: true
author: "rtSurvey"
icon: "cloud"
toc: true
description: "Розгорніть rtCloud на екземплярі AWS EC2 за допомогою сценарію даних користувача aws-ec2.sh."
---

Use `aws-ec2.sh` as the **User Data** script when launching an EC2 instance. The script runs automatically on first boot.

**Download script:** [aws-ec2.sh](/scripts/aws-ec2.sh)

---

## Step 1 — Fill in the configuration

Open the script and edit the `CONFIGURATION` block at the top:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Embedded Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Defaults to ADMIN_PASSWORD
```

| Field | Required | Description |
|-------|----------|-------------|
| `PROJECT_ID` | Yes | Used as database name and Keycloak client ID. Lowercase, no spaces. |
| `ADMIN_PASSWORD` | No | App admin password and Keycloak admin password. Defaults to `admin` — **change after first login**. |
| `DOMAIN` | No | Your domain for HTTPS. Leave blank for HTTP-only mode. |
| `LETSENCRYPT_EMAIL` | Yes (if DOMAIN set) | Email for Let's Encrypt notifications. |
| `EMBED_KEYCLOAK` | No | `true` to deploy embedded Keycloak (requires 4 GB RAM). |

> **Security:** All passwords default to `admin`. Change them immediately after your first login.

---

## Step 2 — Launch an EC2 instance

In the [AWS EC2 console](https://console.aws.amazon.com/ec2):

1. Click **Launch instance**
2. **AMI:** Ubuntu Server 22.04 LTS (64-bit x86)
3. **Instance type:** `t3.medium` (4 GB RAM) or larger
4. **Key pair:** Select or create one for SSH access
5. **Network settings:** Create or select a Security Group (see below)
6. **Advanced details** → **User data** → paste the full script content
7. Click **Launch instance**

---

## Step 3 — Configure the Security Group

Open these ports in the instance's Security Group:

| Port | Protocol | Source | Purpose |
|------|----------|--------|---------|
| 22 | TCP | Your IP | SSH access |
| 80 | TCP | 0.0.0.0/0 | HTTP (redirected to HTTPS by Nginx) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Shiny direct access |

> Do **not** open port 3306 (MySQL) — it should never be publicly accessible.

---

## Step 4 — Add the DNS record

While the instance boots, add an **A record** in your DNS provider:

```
Type  : A
Name  : myapp
Value : <instance-public-ip>
TTL   : 300
```

---

## Step 5 — Monitor progress

```bash
ssh ubuntu@<instance-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Step 6 — Access the app

When setup completes, the log shows a summary with your app URL and credentials. Log in with username `admin` and password `admin`, then change your password immediately.

---

## After Deployment

### Change a password

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### View all containers

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Assign an Elastic IP (optional)

If you stop and start the instance, the public IP changes. To keep a stable IP, allocate an **Elastic IP** and associate it with the instance in the EC2 console.
