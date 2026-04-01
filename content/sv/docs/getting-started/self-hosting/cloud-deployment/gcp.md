---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "Driftsätt rtCloud på Google Cloud Compute Engine med startskriptet gcp-compute.sh."
---

Använd `gcp-compute.sh` som **Startskript** när du skapar en Compute Engine VM-instans. Skriptet körs automatiskt vid första starten.

**Ladda ned skript:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## Steg 1 — Fyll i konfigurationen

Öppna skriptet och redigera `CONFIGURATION`-blocket överst:

```bash
# --- Obligatoriskt ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Ändra efter första inloggningen

# --- Domän + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Inbäddad Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Standardvärdet är ADMIN_PASSWORD
```

| Fält | Obligatoriskt | Beskrivning |
|-------|----------|-------------|
| `PROJECT_ID` | Ja | Används som databasnamn och Keycloak-klient-ID. Gemener, inga mellanslag. |
| `ADMIN_PASSWORD` | Nej | Appens adminlösenord och Keycloak-adminlösenord. Standardvärde är `admin` — **ändra efter första inloggningen**. |
| `DOMAIN` | Nej | Din domän för HTTPS. Lämna tomt för HTTP-only-läge. |
| `LETSENCRYPT_EMAIL` | Ja (om DOMAIN anges) | E-post för Let's Encrypt-aviseringar. |
| `EMBED_KEYCLOAK` | Nej | `true` för att driftsätta inbäddad Keycloak (kräver 4 GB RAM). |

> **Säkerhet:** Alla lösenord har standardvärdet `admin`. Ändra dem omedelbart efter din första inloggning.

---

## Steg 2 — Skapa en VM-instans

I [Google Cloud Console](https://console.cloud.google.com/compute):

1. Klicka på **Skapa instans**
2. **Maskinkonfiguration:**
   - Serie: `E2`
   - Maskintyp: `e2-medium` (4 GB RAM) eller större
3. **Startdisk:**
   - Operativsystem: Ubuntu
   - Version: Ubuntu 22.04 LTS
   - Storlek: 40 GB eller mer
4. **Brandvägg:** markera **Tillåt HTTP-trafik** och **Tillåt HTTPS-trafik**
5. **Avancerade alternativ** → **Hantering** → **Automatisering** → **Startskript** → klistra in hela skriptinnehållet
6. Klicka på **Skapa**

---

## Steg 3 — Lägg till DNS-posten

Medan VM:n startar, lägg till en **A-post** hos din DNS-leverantör:

```
Typ  : A
Namn : myapp
Värde: <vm-extern-ip>
TTL  : 300
```

Hitta den externa IP:n i listan över VM-instanser i konsolen.

---

## Steg 4 — Övervaka förloppet

Med `gcloud` CLI:

```bash
gcloud compute ssh <instansnamn> -- tail -f /var/log/rtcloud-setup.log
```

Eller SSH direkt:

```bash
ssh <användarnamn>@<vm-extern-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Steg 5 — Öppna appen

När konfigurationen är klar visar loggen en sammanfattning med din app-URL och inloggningsuppgifter. Logga in med användarnamnet `admin` och lösenordet `admin`, och ändra sedan ditt lösenord omedelbart.

---

## Brandväggsregler

GCPs **Tillåt HTTP/HTTPS**-kryssrutor öppnar portarna 80 och 443. För att även tillåta direkt Shiny-åtkomst på port 3838, lägg till en brandväggsregel:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

Eller lägg till den via konsolen: **VPC-nätverk** → **Brandvägg** → **Skapa regel**.

> Öppna **inte** port 3306 (MySQL) — den ska aldrig vara offentligt tillgänglig.

---

## Statisk IP (valfritt)

Som standard tilldelar GCP en tillfällig extern IP som ändras vid VM-omstart. För att behålla en stabil IP:

1. Gå till **VPC-nätverk** → **IP-adresser**
2. Klicka på **Reservera extern statisk adress**
3. Tilldela den till din VM-instans

---

## Efter driftsättning

### Ändra ett lösenord

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Visa alla containrar

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
