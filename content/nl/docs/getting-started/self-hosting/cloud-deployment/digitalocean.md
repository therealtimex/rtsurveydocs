---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Implementeer rtCloud op een DigitalOcean Droplet met behulp van geautomatiseerde user-data scripts."
---

DigitalOcean gebruikt **User Data**-scripts die automatisch worden uitgevoerd bij de eerste start. U vult de configuratievariabelen bovenaan het script in en plakt vervolgens het volledige script wanneer u een Droplet aanmaakt.

> In tegenstelling tot Linode StackScripts heeft DigitalOcean geen formulier-UI — u moet het script rechtstreeks bewerken voordat u het plakt.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Ingebedde Keycloak (Aanbevolen)

Gebruik `digitalocean-droplet-keycloak-embed.sh` voor de eenvoudigste installatie met ingebouwde SSO.

### Stap 1 — Vul de configuratie in

Open het script en bewerk het `CONFIGURATIE`-blok bovenaan:

```bash
# --- Vereist ---
PROJECT_ID="rtsurvey"                  # Unieke identificator voor uw project (geen spaties)
ADMIN_PASSWORD="admin"                 # Wachtwoord voor app-beheerder en Keycloak — wijzig na eerste login

# --- Domein + SSL ---
DOMAIN="mijnapp.example.com"           # Uw domein — DNS A-record moet hier naar verwijzen
PROJECT_URL=""                         # Leeg laten tenzij achter Cloudflare/proxy
LETSENCRYPT_EMAIL="beheerder@example.com" # E-mail voor Let's Encrypt-meldingen

# --- Optioneel ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Veld | Vereist | Beschrijving |
|-------|----------|-------------|
| `PROJECT_ID` | Ja | Gebruikt als databasenaam en Keycloak-client-ID. Kleine letters, geen spaties. |
| `ADMIN_PASSWORD` | Nee | Wachtwoord voor app-beheerderlogin en Keycloak-beheerconsole. Standaard `admin` — **wijzigen na eerste login**. |
| `DOMAIN` | Ja | Uw domeinnaam. DNS A-record moet naar het Droplet-IP verwijzen. |
| `LETSENCRYPT_EMAIL` | Ja | E-mailadres voor Let's Encrypt-certificaatmeldingen. |
| `PROJECT_URL` | Nee | De openbare URL overschrijven. Leeg laten om `DOMAIN` te gebruiken. Nuttig achter Cloudflare. |

> **Beveiliging:** Alle wachtwoorden zijn standaard `admin`. Wijzig ze onmiddellijk na uw eerste login.

### Stap 2 — Maak een Droplet aan

In het [DigitalOcean-configuratiescherm](https://cloud.digitalocean.com):

1. Klik op **Aanmaken** → **Droplets**
2. Kies **Ubuntu 22.04 LTS** als de image
3. Selecteer **Basic, 4 GB RAM / 2 vCPU's** of groter
4. Scroll naar **Geavanceerde opties** → vink **Initialisatiescripts toevoegen** aan
5. Plak de volledige scriptinhoud in het tekstgebied
6. Klik op **Droplet aanmaken**

### Stap 3 — Voeg het DNS-record toe

Terwijl de Droplet opstart, voegt u een **A-record** toe bij uw DNS-provider:

```
Type  : A
Naam  : mijnapp          (of @ voor rootdomein)
Waarde: <droplet-ip>
TTL   : 300
```

### Stap 4 — Monitor de voortgang

SSH in de Droplet en bekijk het logboek:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Het script drukt uw server-IP vroeg af — voeg het DNS-record toe zodra u het ziet.

### Stap 5 — Toegang tot de app

Wanneer de installatie is voltooid, toont het logboek een samenvatting:

```
============================================================
 rtCloud implementatie voltooid! (Ingebedde Keycloak)
============================================================
 App URL   : https://mijnapp.example.com
 Beheerder : admin / admin
 Keycloak  : https://mijnapp.example.com/auth/admin

 !! BEVEILIGING: Alle wachtwoorden zijn standaard 'admin'.
    Wijzig ze onmiddellijk na de eerste login.
============================================================
```

Open `https://mijnapp.example.com` in uw browser en log in met gebruikersnaam `admin` en wachtwoord `admin`.

> **Wijzig uw wachtwoord** onmiddellijk na de login via **Instellingen** in het menu rechtsboven.

---

## Na implementatie

### Een wachtwoord wijzigen

SSH in de Droplet, bewerk `.env` en herstart de betreffende container:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Het domein bijwerken

Als u na de implementatie een ander domein toewijst, werkt u `PROJECT_URL` bij in `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Alle containers weergeven

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
