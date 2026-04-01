---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Distribuire rtCloud su Linode utilizzando uno StackScript. Nessuna configurazione necessaria — basta creare il server e seguire i passaggi post-distribuzione."
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

## Regole firewall (Linode Cloud Firewall)

Se si collega un Linode Cloud Firewall a questo server, utilizzare le seguenti regole:

### Traffico in entrata (Inbound)

| Etichetta | Azione | Protocollo | Porta | Sorgenti | Note |
|---------|--------|-----------|------|---------|------|
| `accept-inbound-ssh` | Accetta | TCP | 22 | All IPv4, All IPv6 | Accesso SSH |
| `accept-inbound-http` | Accetta | TCP | 80 | All IPv4, All IPv6 | Nginx (HTTP + challenge ACME) |
| `accept-inbound-https` | Accetta | TCP | 443 | All IPv4, All IPv6 | Nginx (HTTPS dopo la configurazione SSL) |
| `accept-inbound-shiny` | Accetta | TCP | 3838 | All IPv4, All IPv6 | Shiny Server (analisi R) |
| `accept-inbound-icmp` | Accetta | ICMP | — | All IPv4, All IPv6 | Ping / diagnostica |
| Criterio in entrata predefinito | **Rifiuta** | | | | Blocca tutto il resto |

### Traffico in uscita (Outbound)

| Etichetta | Azione | Note |
|---------|--------|------|
| Criterio in uscita predefinito | **Accetta** | Consenti tutto il traffico in uscita (Docker, certbot, API GoDaddy, ecc.) |

### Porte NON necessarie esternamente

Queste porte sono associate solo a `127.0.0.1` e non sono mai raggiungibili dall'esterno:

| Porta | Servizio | Motivo |
|-------|---------|--------|
| 8080 | Container app | Nginx fa il proxy internamente |
| 8090 | Container Keycloak | Nginx fa il proxy internamente |
| 3306 | MySQL | Solo rete Docker interna |

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
