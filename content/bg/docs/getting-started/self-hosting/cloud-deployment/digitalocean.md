---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Разгръщане на rtCloud на DigitalOcean Droplet с помощта на автоматизирани скриптове за потребителски данни."
---

DigitalOcean uses **User Data** scripts that run automatically on first boot. You fill in the configuration variables at the top of the script, then paste the entire script when creating a Droplet.

> Unlike Linode StackScripts, DigitalOcean has no form UI — you must edit the script directly before pasting.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Embedded Keycloak (Recommended)

Use `digitalocean-droplet-keycloak-embed.sh` for the simplest setup with built-in SSO.

### Step 1 — Fill in the configuration

Open the script and edit the `CONFIGURATION` block at the top:

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

| Field | Required | Description |
|-------|----------|-------------|
| `PROJECT_ID` | Yes | Used as database name and Keycloak client ID. Lowercase, no spaces. |
| `ADMIN_PASSWORD` | No | Password for app admin login and Keycloak admin console. Defaults to `admin` — **change after first login**. |
| `DOMAIN` | Yes | Your domain name. DNS A record must point to the Droplet IP. |
| `LETSENCRYPT_EMAIL` | Yes | Email address for Let's Encrypt certificate notifications. |
| `PROJECT_URL` | No | Override the public URL. Leave blank to use `DOMAIN`. Useful behind Cloudflare. |

> **Security:** All passwords default to `admin`. Change them immediately after your first login.

### Step 2 — Create a Droplet

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Click **Create** → **Droplets**
2. Choose **Ubuntu 22.04 LTS** as the image
3. Select **Basic, 4 GB RAM / 2 vCPUs** or larger
4. Scroll to **Advanced Options** → check **Add Initialization scripts**
5. Paste the full script content into the text area
6. Click **Create Droplet**

### Step 3 — Add the DNS record

While the Droplet boots, add an **A record** in your DNS provider:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Step 4 — Monitor progress

SSH into the Droplet and watch the log:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

The script prints your server IP near the start — add the DNS record as soon as you see it.

### Step 5 — Access the app

When setup completes, the log shows a summary:

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

> **Change your password** immediately after login via **Settings** in the top-right menu.

---

## After Deployment

### Change a password

SSH into the Droplet, edit `.env`, and restart the affected container:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Update the domain

If you assign a different domain after deployment, update `PROJECT_URL` in `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### View all containers

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
