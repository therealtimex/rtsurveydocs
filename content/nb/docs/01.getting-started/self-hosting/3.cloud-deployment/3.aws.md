---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "Distribuer rtCloud på en AWS EC2-instans med aws-ec2.sh User Data-skriptet."
---

Bruk `aws-ec2.sh` som **User Data**-skript når du starter en EC2-instans. Skriptet kjøres automatisk ved første oppstart.

**Last ned skript:** [aws-ec2.sh](/scripts/aws-ec2.sh)

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

## Trinn 2 — Start en EC2-instans

I [AWS EC2-konsollen](https://console.aws.amazon.com/ec2):

1. Klikk **Start instans**
2. **AMI:** Ubuntu Server 22.04 LTS (64-bit x86)
3. **Instanstype:** `t3.medium` (4 GB RAM) eller større
4. **Nøkkelpar:** Velg eller opprett ett for SSH-tilgang
5. **Nettverksinnstillinger:** Opprett eller velg en sikkerhetsgruppe (se nedenfor)
6. **Avanserte detaljer** → **User data** → lim inn hele skriptinnholdet
7. Klikk **Start instans**

---

## Trinn 3 — Konfigurer sikkerhetsgruppen

Åpne disse portene i instansens sikkerhetsgruppe:

| Port | Protokoll | Kilde | Formål |
|------|----------|--------|---------|
| 22 | TCP | Din IP | SSH-tilgang |
| 80 | TCP | 0.0.0.0/0 | HTTP (omdirigert til HTTPS av Nginx) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Shiny direkte tilgang |

> **Ikke** åpne port 3306 (MySQL) — den bør aldri være offentlig tilgjengelig.

---

## Trinn 4 — Legg til DNS-posten

Mens instansen starter opp, legg til en **A-post** hos DNS-leverandøren din:

```
Type  : A
Navn  : myapp
Verdi : <instans-offentlig-ip>
TTL   : 300
```

---

## Trinn 5 — Overvåk fremdriften

```bash
ssh ubuntu@<instans-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Trinn 6 — Åpne appen

Når oppsettet er ferdig, viser loggen et sammendrag med app-URL og legitimasjonsopplysninger. Logg inn med brukernavn `admin` og passord `admin`, og endre passordet umiddelbart.

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

### Tildel en Elastic IP (valgfritt)

Hvis du stopper og starter instansen, endres den offentlige IP-en. For å beholde en stabil IP, tildel en **Elastic IP** og knytt den til instansen i EC2-konsollen.
