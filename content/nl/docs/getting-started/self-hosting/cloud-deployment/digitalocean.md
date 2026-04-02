---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Implementeer rtCloud op een DigitalOcean Droplet met behulp van geautomatiseerde scripts voor gebruikersgegevens."
---

DigitalOcean gebruikt **Gebruikersgegevens**-scripts die automatisch worden uitgevoerd bij de eerste keer opstarten. U vult de configuratievariabelen bovenaan het script in en plakt vervolgens het hele script bij het maken van een Droplet.

> In tegenstelling tot Linode StackScripts heeft DigitalOcean geen formulier-UI; u moet het script direct bewerken voordat u het plakt.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Ingebouwde sleutelmantel (aanbevolen)

Gebruik `digitalocean-droplet-keycloak-embed.sh` voor de eenvoudigste installatie met ingebouwde SSO.

### Stap 1 — Vul de configuratie in

Open het script en bewerk het blok `CONFIGURATIE` bovenaan:

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

| Veld | Vereist | Beschrijving |
|-------|----------|------------|
| `PROJECT_ID` | Ja | Gebruikt als databasenaam en Keycloak-client-ID. Kleine letters, geen spaties. |
| `ADMIN_PASSWORD` | Nee | Wachtwoord voor inloggen op de app-beheerder en Keycloak-beheerdersconsole. Standaard ingesteld op `admin` — **wijzigen na eerste aanmelding**. |
| `DOMEIN` | Ja | Uw domeinnaam. DNS Een record moet verwijzen naar het Droplet IP-adres. |
| `LETSENCRYPT_EMAIL` | Ja | E-mailadres voor Let's Encrypt-certificaatmeldingen. |
| `PROJECT_URL` | Nee | Overschrijf de openbare URL. Laat dit leeg om `DOMAIN` te gebruiken. Handig achter Cloudflare. |

> **Beveiliging:** Alle wachtwoorden zijn standaard `admin`. Wijzig ze onmiddellijk na uw eerste login.

### Stap 2 — Maak een druppel

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Klik op **Maken** → **Druppels**
2. Kies **Ubuntu 22.04 LTS** als afbeelding
3. Selecteer **Basis, 4 GB RAM / 2 vCPU's** of groter
4. Scroll naar **Geavanceerde opties** → vink **Initialisatiescripts toevoegen** aan
5. Plak de volledige scriptinhoud in het tekstgebied
6. Klik op **Druppel maken**

### Stap 3 — Voeg de DNS-record toe

Terwijl de Droplet opstart, voegt u een **A-record** toe aan uw DNS-provider:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Stap 4 — Bewaak de voortgang

SSH in de Droplet en bekijk het logboek:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Het script drukt het IP-adres van uw server af aan het begin. Voeg het DNS-record toe zodra u het ziet.

### Stap 5 — Open de app

Wanneer de installatie is voltooid, wordt in het logboek een samenvatting weergegeven:

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

> **Wijzig uw wachtwoord** direct na het inloggen via **Instellingen** in het menu rechtsboven.

---

## Na implementatie

### Wijzig een wachtwoord

SSH in de Droplet, bewerk `.env` en start de betrokken container opnieuw:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Update het domein

Als u na de implementatie een ander domein toewijst, update dan `PROJECT_URL` in `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Bekijk alle containers

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
