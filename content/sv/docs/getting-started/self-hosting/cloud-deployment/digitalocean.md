---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Driftsätt rtCloud på en DigitalOcean Droplet med automatiserade user-data-skript."
---

DigitalOcean använder **User Data**-skript som körs automatiskt vid första starten. Du fyller i konfigurationsvariablerna överst i skriptet och klistrar sedan in hela skriptet när du skapar en Droplet.

> Till skillnad från Linode StackScripts har DigitalOcean inget formulär-UI — du måste redigera skriptet direkt innan du klistrar in det.

**Ladda ned skript:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Inbäddad Keycloak (rekommenderat)

Använd `digitalocean-droplet-keycloak-embed.sh` för den enklaste konfigurationen med inbyggd SSO.

### Steg 1 — Fyll i konfigurationen

Öppna skriptet och redigera `CONFIGURATION`-blocket överst:

```bash
# --- Obligatoriskt ---
PROJECT_ID="rtsurvey"                  # Unik identifierare för ditt projekt (inga mellanslag)
ADMIN_PASSWORD="admin"                 # Lösenord för appens admin och Keycloak — ändra efter första inloggningen

# --- Domän + SSL ---
DOMAIN="myapp.example.com"            # Din domän — DNS A-post måste peka hit
PROJECT_URL=""                         # Lämna tomt om du inte använder Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # E-post för Let's Encrypt-aviseringar

# --- Valfritt ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Fält | Obligatoriskt | Beskrivning |
|-------|----------|-------------|
| `PROJECT_ID` | Ja | Används som databasnamn och Keycloak-klient-ID. Gemener, inga mellanslag. |
| `ADMIN_PASSWORD` | Nej | Lösenord för appens adminlogin och Keycloak-adminkonsolen. Standardvärde är `admin` — **ändra efter första inloggningen**. |
| `DOMAIN` | Ja | Ditt domännamn. DNS A-post måste peka på Dropletens IP. |
| `LETSENCRYPT_EMAIL` | Ja | E-postadress för Let's Encrypt-certifikataviseringar. |
| `PROJECT_URL` | Nej | Åsidosätt den publika URL:en. Lämna tomt för att använda `DOMAIN`. Användbart bakom Cloudflare. |

> **Säkerhet:** Alla lösenord har standardvärdet `admin`. Ändra dem omedelbart efter din första inloggning.

### Steg 2 — Skapa en Droplet

I [DigitalOcean-kontrollpanelen](https://cloud.digitalocean.com):

1. Klicka på **Skapa** → **Droplets**
2. Välj **Ubuntu 22.04 LTS** som avbild
3. Välj **Basic, 4 GB RAM / 2 vCPUs** eller större
4. Scrolla till **Avancerade alternativ** → markera **Lägg till initialiseringsskript**
5. Klistra in hela skriptinnehållet i textfältet
6. Klicka på **Skapa Droplet**

### Steg 3 — Lägg till DNS-posten

Medan Dropleten startar, lägg till en **A-post** hos din DNS-leverantör:

```
Typ  : A
Namn : myapp          (eller @ för rotdomänen)
Värde: <droplet-ip>
TTL  : 300
```

### Steg 4 — Övervaka förloppet

SSH:a in i Dropleten och se loggen:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Skriptet skriver ut din server-IP tidigt — lägg till DNS-posten så snart du ser den.

### Steg 5 — Öppna appen

När konfigurationen är klar visar loggen en sammanfattning:

```
============================================================
 rtCloud-driftsättning klar! (Inbäddad Keycloak)
============================================================
 App-URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SÄKERHET: Alla lösenord har standardvärdet 'admin'.
    Ändra dem omedelbart efter första inloggningen.
============================================================
```

Öppna `https://myapp.example.com` i din webbläsare och logga in med användarnamnet `admin` och lösenordet `admin`.

> **Ändra ditt lösenord** omedelbart efter inloggningen via **Inställningar** i menyn uppe till höger.

---

## Efter driftsättning

### Ändra ett lösenord

SSH:a in i Dropleten, redigera `.env` och starta om den berörda containern:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Uppdatera domänen

Om du tilldelar en annan domän efter driftsättning, uppdatera `PROJECT_URL` i `.env`:

```bash
nano /opt/rtcloud/.env   # uppdatera PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Visa alla containrar

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
