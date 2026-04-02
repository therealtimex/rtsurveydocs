---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Distribuera rtCloud på en DigitalOcean Droplet med hjälp av automatiserade användardataskript."
---

DigitalOcean använder **Användardata**-skript som körs automatiskt vid första uppstart. Du fyller i konfigurationsvariablerna längst upp i skriptet och klistrar sedan in hela skriptet när du skapar en Droplet.

> Till skillnad från Linode StackScripts har DigitalOcean inget gränssnitt – du måste redigera skriptet direkt innan du klistrar in.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Inbäddad nyckelmantel (rekommenderas)

Använd `digitalocean-droplet-keycloak-embed.sh` för den enklaste installationen med inbyggd SSO.

### Steg 1 — Fyll i konfigurationen

Öppna skriptet och redigera "CONFIGURATION"-blocket högst upp:

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

| Fält | Krävs | Beskrivning |
|-------|--------|-------------|
| `PROJECT_ID` | Ja | Används som databasnamn och Keycloak-klient-ID. Små bokstäver, inga mellanslag. |
| `ADMIN_LÖSENORD` | Nej | Lösenord för appadministratörsinloggning och Keycloak administratörskonsol. Som standard är "admin" - **ändra efter första inloggning**. |
| `DOMÄN` | Ja | Ditt domännamn. DNS En post måste peka på Droplet IP. |
| `LETSENCRYPT_EMAIL` | Ja | E-postadress för Let's Encrypt certifikataviseringar. |
| `PROJECT_URL` | Nej | Åsidosätt den offentliga webbadressen. Lämna tomt för att använda "DOMAIN". Användbart bakom Cloudflare. |

> **Säkerhet:** Alla lösenord är som standard "admin". Ändra dem direkt efter din första inloggning.

### Steg 2 — Skapa en droppe

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Klicka på **Skapa** → **Droppar**
2. Välj **Ubuntu 22.04 LTS** som bild
3. Välj **Basic, 4 GB RAM / 2 vCPUs** eller större
4. Bläddra till **Avancerade alternativ** → markera **Lägg till initieringsskript**
5. Klistra in hela skriptinnehållet i textområdet
6. Klicka på **Skapa droppe**

### Steg 3 — Lägg till DNS-posten

Medan Droplet startar lägger du till en **A-post** i din DNS-leverantör:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Steg 4 — Övervaka framstegen

SSH in i droppen och titta på loggen:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

The script prints your server IP near the start — add the DNS record as soon as you see it.

### Steg 5 — Öppna appen

När installationen är klar visar loggen en sammanfattning:

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

> **Ändra ditt lösenord** direkt efter inloggning via **Inställningar** i menyn uppe till höger.

---

## Efter distribution

### Ändra ett lösenord

SSH i droppen, redigera `.env` och starta om den berörda behållaren:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Uppdatera domänen

Om du tilldelar en annan domän efter implementering, uppdatera `PROJECT_URL` i `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Visa alla behållare

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
