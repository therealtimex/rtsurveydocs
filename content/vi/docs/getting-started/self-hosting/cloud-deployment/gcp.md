---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: true
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "Triển khai rtCloud trên Google Cloud Compute Engine bằng script khởi động gcp-compute.sh."
---

Use `gcp-compute.sh` as the **Startup script** when creating a Compute Engine VM instance. The script runs automatically on first boot.

**Download script:** [gcp-compute.sh](/scripts/gcp-compute.sh)

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

## Step 2 — Create a VM instance

In the [Google Cloud Console](https://console.cloud.google.com/compute):

1. Click **Create instance**
2. **Machine configuration:**
   - Series: `E2`
   - Machine type: `e2-medium` (4 GB RAM) or larger
3. **Boot disk:**
   - Operating system: Ubuntu
   - Version: Ubuntu 22.04 LTS
   - Size: 40 GB or more
4. **Firewall:** check **Allow HTTP traffic** and **Allow HTTPS traffic**
5. **Advanced options** → **Management** → **Automation** → **Startup script** → paste the full script content
6. Click **Create**

---

## Step 3 — Add the DNS record

While the VM boots, add an **A record** in your DNS provider:

```
Type  : A
Name  : myapp
Value : <vm-external-ip>
TTL   : 300
```

Find the external IP in the VM instances list in the console.

---

## Step 4 — Monitor progress

Using the `gcloud` CLI:

```bash
gcloud compute ssh <instance-name> -- tail -f /var/log/rtcloud-setup.log
```

Or SSH directly:

```bash
ssh <username>@<vm-external-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Step 5 — Access the app

When setup completes, the log shows a summary with your app URL and credentials. Log in with username `admin` and password `admin`, then change your password immediately.

---

## Firewall Rules

GCP's **Allow HTTP/HTTPS** checkboxes open ports 80 and 443. To also allow direct Shiny access on port 3838, add a firewall rule:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

Or add it via the console: **VPC Network** → **Firewall** → **Create rule**.

> Do **not** open port 3306 (MySQL) — it should never be publicly accessible.

---

## Static IP (optional)

By default, GCP assigns an ephemeral external IP that changes on VM restart. To keep a stable IP:

1. Go to **VPC Network** → **IP addresses**
2. Click **Reserve external static address**
3. Assign it to your VM instance

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
