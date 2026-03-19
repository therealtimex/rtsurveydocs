---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "Driftsätt rtCloud på en AWS EC2-instans med user data-skriptet aws-ec2.sh."
---

Använd `aws-ec2.sh` som **User Data**-skript när du startar en EC2-instans. Skriptet körs automatiskt vid första starten.

**Ladda ned skript:** [aws-ec2.sh](/scripts/aws-ec2.sh)

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

## Steg 2 — Starta en EC2-instans

I [AWS EC2-konsolen](https://console.aws.amazon.com/ec2):

1. Klicka på **Starta instans**
2. **AMI:** Ubuntu Server 22.04 LTS (64-bit x86)
3. **Instanstyp:** `t3.medium` (4 GB RAM) eller större
4. **Nyckelpar:** Välj eller skapa ett för SSH-åtkomst
5. **Nätverksinställningar:** Skapa eller välj en säkerhetsgrupp (se nedan)
6. **Avancerade detaljer** → **Användardata** → klistra in hela skriptinnehållet
7. Klicka på **Starta instans**

---

## Steg 3 — Konfigurera säkerhetsgruppen

Öppna dessa portar i instansens säkerhetsgrupp:

| Port | Protokoll | Källa | Syfte |
|------|----------|--------|---------|
| 22 | TCP | Din IP | SSH-åtkomst |
| 80 | TCP | 0.0.0.0/0 | HTTP (omdirigeras till HTTPS av Nginx) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Direkt Shiny-åtkomst |

> Öppna **inte** port 3306 (MySQL) — den ska aldrig vara offentligt tillgänglig.

---

## Steg 4 — Lägg till DNS-posten

Medan instansen startar, lägg till en **A-post** hos din DNS-leverantör:

```
Typ  : A
Namn : myapp
Värde: <instansens publika IP>
TTL  : 300
```

---

## Steg 5 — Övervaka förloppet

```bash
ssh ubuntu@<instans-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Steg 6 — Öppna appen

När konfigurationen är klar visar loggen en sammanfattning med din app-URL och inloggningsuppgifter. Logga in med användarnamnet `admin` och lösenordet `admin`, och ändra sedan ditt lösenord omedelbart.

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

### Tilldela en Elastic IP (valfritt)

Om du stoppar och startar instansen ändras den publika IP-adressen. För att behålla en stabil IP, allokera en **Elastic IP** och associera den med instansen i EC2-konsolen.
