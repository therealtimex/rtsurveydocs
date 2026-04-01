---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Deploy rtCloud on Linode using a StackScript. No configuration needed — just create the server and follow the post-deployment steps."
---

The rtSurvey StackScript provisions a fresh Ubuntu 22.04 server with everything pre-installed: Docker, Nginx, Keycloak SSO, and the rtSurvey application. You do not need to edit any files or run any commands manually.

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

**You must configure SSL before you can log in.** If you try to access the app without SSL, you will see a warning and cannot proceed.

Open your browser at:

```
http://<server-ip>
```

The app will redirect you to the SSL setup screen.

![SSL setup options screen](/img/ssl-setup/ssl-setup-options.png)

Choose one of three options:

| Option | When to use |
|--------|-------------|
| **Free rtsurvey.com subdomain** *(Recommended)* | Fastest — no DNS setup needed. We create the record for you. Ready in 2–5 minutes. |
| **My own domain** | You have a domain and its DNS already points to this server. |
| **Install certificate manually** | Enterprise or custom CA. Requires SSH access. |

### Using the free rtsurvey.com subdomain

1. Enter your desired subdomain name (e.g. `myproject` → `myproject.rtsurvey.com`)
2. Click **Create https://[subdomain].rtsurvey.com**
3. Wait 2–5 minutes for the certificate to be issued

This is the quickest option — no domain registration or DNS changes required.

---

## Step 5 — First login

Once SSL is active, open your browser at your new URL (e.g. `https://myproject.rtsurvey.com`).

To log in with the default admin account, **long-press the "Log In or Register" button** for 1–2 seconds to reveal the username and password fields.

| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `admin` |

See [First Login](../../first-login) for a detailed walkthrough with screenshots.

---

## Step 6 — Change the default password

All passwords default to `admin`. Change them immediately after your first login:

- **App admin password** — account settings inside the app
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

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
