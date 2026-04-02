---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Implementer rtCloud på en DigitalOcean Droplet ved hjælp af automatiserede brugerdatascripts."
---

DigitalOcean bruger **Brugerdata**-scripts, der kører automatisk ved første opstart. Du udfylder konfigurationsvariablerne øverst i scriptet og indsætter derefter hele scriptet, når du opretter en Droplet.

> I modsætning til Linode StackScripts har DigitalOcean ingen formular UI - du skal redigere scriptet direkte før indsættelse.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Embedded Keycloak (anbefalet)

Brug `digitalocean-droplet-keycloak-embed.sh` til den enkleste opsætning med indbygget SSO.

### Trin 1 — Udfyld konfigurationen

Åbn scriptet og rediger 'CONFIGURATION'-blokken øverst:

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

| Felt | Påkrævet | Beskrivelse |
|-------|--------|-------------|
| `PROJECT_ID` | Ja | Bruges som databasenavn og Keycloak klient-id. Små bogstaver, ingen mellemrum. |
| `ADMIN_PASSWORD` | Nej | Adgangskode til app admin login og Keycloak admin konsol. Som standard er "admin" - **ændres efter første login**. |
| `DOMÆNE` | Ja | Dit domænenavn. DNS En post skal pege på Droplet IP. |
| `LETSENCRYPT_EMAIL` | Ja | E-mailadresse til Let's Encrypt-certifikatmeddelelser. |
| `PROJECT_URL` | Nej | Tilsidesæt den offentlige webadresse. Lad stå tomt for at bruge "DOMAIN". Nyttigt bag Cloudflare. |

> **Sikkerhed:** Alle adgangskoder er som standard "admin". Skift dem umiddelbart efter dit første login.

### Trin 2 — Opret en dråbe

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Klik på **Opret** → **Dråber**
2. Vælg **Ubuntu 22.04 LTS** som billede
3. Vælg **Basic, 4 GB RAM / 2 vCPU'er** eller større
4. Rul til **Avancerede indstillinger** → marker **Tilføj initialiseringsscripts**
5. Indsæt hele scriptindholdet i tekstområdet
6. Klik på **Opret dråbe**

### Trin 3 — Tilføj DNS-posten

Mens Droplet starter, skal du tilføje en **A record** i din DNS-udbyder:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Trin 4 — Overvåg fremskridt

SSH ind i dråben og se loggen:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Scriptet udskriver din server-IP nær starten - tilføj DNS-posten, så snart du ser den.

### Trin 5 — Få adgang til appen

Når opsætningen er fuldført, viser loggen en oversigt:

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

> **Skift din adgangskode** umiddelbart efter login via **Indstillinger** i menuen øverst til højre.

---

## Efter implementering

### Skift en adgangskode

SSH ind i dråben, rediger ".env", og genstart den berørte beholder:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Opdater domænet

Hvis du tildeler et andet domæne efter implementeringen, skal du opdatere `PROJECT_URL` i `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Se alle containere

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
