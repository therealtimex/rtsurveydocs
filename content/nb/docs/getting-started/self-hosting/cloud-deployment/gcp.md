---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "Distribuer rtCloud på Google Cloud Compute Engine med gcp-compute.sh-oppstartsskriptet."
---

Bruk `gcp-compute.sh` som **oppstartsskript** når du oppretter en Compute Engine VM-instans. Skriptet kjøres automatisk ved første oppstart.

**Last ned skript:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## Trinn 1 — Fyll inn konfigurasjonen

Åpne skriptet og rediger `CONFIGURATION`-blokken øverst:

```bash
# --- Påkrevd ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Endre etter første innlogging

# --- Domene + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Innebygd Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Standard er ADMIN_PASSWORD
```

| Felt | Påkrevd | Beskrivelse |
|-------|----------|-------------|
| `PROJECT_ID` | Ja | Brukes som databasenavn og Keycloak klient-ID. Kun små bokstaver, ingen mellomrom. |
| `ADMIN_PASSWORD` | Nei | App-adminpassord og Keycloak-adminpassord. Standard er `admin` — **endre etter første innlogging**. |
| `DOMAIN` | Nei | Domenet ditt for HTTPS. La stå tomt for kun HTTP-modus. |
| `LETSENCRYPT_EMAIL` | Ja (hvis DOMAIN er satt) | E-post for Let's Encrypt-varsler. |
| `EMBED_KEYCLOAK` | Nei | `true` for å distribuere innebygd Keycloak (krever 4 GB RAM). |

> **Sikkerhet:** Alle passord er standard `admin`. Endre dem umiddelbart etter første innlogging.

---

## Trinn 2 — Opprett en VM-instans

I [Google Cloud Console](https://console.cloud.google.com/compute):

1. Klikk **Opprett instans**
2. **Maskinkonfigurasjon:**
   - Serie: `E2`
   - Maskintype: `e2-medium` (4 GB RAM) eller større
3. **Oppstartsdisk:**
   - Operativsystem: Ubuntu
   - Versjon: Ubuntu 22.04 LTS
   - Størrelse: 40 GB eller mer
4. **Brannmur:** merk av for **Tillat HTTP-trafikk** og **Tillat HTTPS-trafikk**
5. **Avanserte alternativer** → **Administrasjon** → **Automatisering** → **Oppstartsskript** → lim inn hele skriptinnholdet
6. Klikk **Opprett**

---

## Trinn 3 — Legg til DNS-posten

Mens VM-en starter opp, legg til en **A-post** hos DNS-leverandøren din:

```
Type  : A
Navn  : myapp
Verdi : <vm-ekstern-ip>
TTL   : 300
```

Finn den eksterne IP-en i VM-instanslisten i konsollen.

---

## Trinn 4 — Overvåk fremdriften

Med `gcloud` CLI:

```bash
gcloud compute ssh <instansnavn> -- tail -f /var/log/rtcloud-setup.log
```

Eller SSH direkte:

```bash
ssh <brukernavn>@<vm-ekstern-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Trinn 5 — Åpne appen

Når oppsettet er ferdig, viser loggen et sammendrag med app-URL og legitimasjonsopplysninger. Logg inn med brukernavn `admin` og passord `admin`, og endre passordet umiddelbart.

---

## Brannmurregler

GCPs **Tillat HTTP/HTTPS**-avmerkingsbokser åpner portene 80 og 443. For også å tillate direkte Shiny-tilgang på port 3838, legg til en brannmurregel:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

Eller legg den til via konsollen: **VPC-nettverk** → **Brannmur** → **Opprett regel**.

> **Ikke** åpne port 3306 (MySQL) — den bør aldri være offentlig tilgjengelig.

---

## Statisk IP (valgfritt)

Som standard tildeler GCP en flyktig ekstern IP som endres ved VM-omstart. For å beholde en stabil IP:

1. Gå til **VPC-nettverk** → **IP-adresser**
2. Klikk **Reserver ekstern statisk adresse**
3. Knytt den til VM-instansen din

---

## Etter distribusjon

### Endre et passord

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Se alle containere

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
