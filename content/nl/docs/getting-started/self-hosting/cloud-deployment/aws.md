---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "Implementeer rtCloud op een AWS EC2-instantie met het aws-ec2.sh user data script."
---

Gebruik `aws-ec2.sh` als het **User Data**-script bij het starten van een EC2-instantie. Het script wordt automatisch uitgevoerd bij de eerste start.

**Download script:** [aws-ec2.sh](/scripts/aws-ec2.sh)

---

## Stap 1 — Vul de configuratie in

Open het script en bewerk het `CONFIGURATIE`-blok bovenaan:

```bash
# --- Vereist ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Wijzigen na eerste login

# --- Domein + SSL ---
DOMAIN="mijnapp.example.com"
LETSENCRYPT_EMAIL="beheerder@example.com"

# --- Ingebedde Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Standaard ADMIN_PASSWORD
```

| Veld | Vereist | Beschrijving |
|-------|----------|-------------|
| `PROJECT_ID` | Ja | Gebruikt als databasenaam en Keycloak-client-ID. Kleine letters, geen spaties. |
| `ADMIN_PASSWORD` | Nee | App-beheerderswachtwoord en Keycloak-beheerderswachtwoord. Standaard `admin` — **wijzigen na eerste login**. |
| `DOMAIN` | Nee | Uw domein voor HTTPS. Leeg laten voor alleen HTTP-modus. |
| `LETSENCRYPT_EMAIL` | Ja (als DOMAIN ingesteld) | E-mail voor Let's Encrypt-meldingen. |
| `EMBED_KEYCLOAK` | Nee | `true` om ingebedde Keycloak te implementeren (vereist 4 GB RAM). |

> **Beveiliging:** Alle wachtwoorden zijn standaard `admin`. Wijzig ze onmiddellijk na uw eerste login.

---

## Stap 2 — Start een EC2-instantie

In de [AWS EC2-console](https://console.aws.amazon.com/ec2):

1. Klik op **Instantie starten**
2. **AMI:** Ubuntu Server 22.04 LTS (64-bit x86)
3. **Instantietype:** `t3.medium` (4 GB RAM) of groter
4. **Sleutelpaar:** Selecteer of maak er een aan voor SSH-toegang
5. **Netwerkinstellingen:** Maak of selecteer een Beveiligingsgroep (zie hieronder)
6. **Geavanceerde details** → **User data** → plak de volledige scriptinhoud
7. Klik op **Instantie starten**

---

## Stap 3 — Configureer de Beveiligingsgroep

Open deze poorten in de Beveiligingsgroep van de instantie:

| Poort | Protocol | Bron | Doel |
|------|----------|--------|---------|
| 22 | TCP | Uw IP | SSH-toegang |
| 80 | TCP | 0.0.0.0/0 | HTTP (doorgestuurd naar HTTPS door Nginx) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Directe Shiny-toegang |

> Open **niet** poort 3306 (MySQL) — die mag nooit publiek toegankelijk zijn.

---

## Stap 4 — Voeg het DNS-record toe

Terwijl de instantie opstart, voegt u een **A-record** toe bij uw DNS-provider:

```
Type  : A
Naam  : mijnapp
Waarde: <instantie-openbaar-ip>
TTL   : 300
```

---

## Stap 5 — Monitor de voortgang

```bash
ssh ubuntu@<instantie-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Stap 6 — Toegang tot de app

Wanneer de installatie is voltooid, toont het logboek een samenvatting met uw app-URL en gegevens. Log in met gebruikersnaam `admin` en wachtwoord `admin`, en wijzig uw wachtwoord onmiddellijk.

---

## Na implementatie

### Een wachtwoord wijzigen

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Alle containers weergeven

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Een Elastic IP toewijzen (optioneel)

Als u de instantie stopt en start, verandert het openbare IP. Om een stabiel IP te behouden, wijst u een **Elastic IP** toe en koppelt u dit aan de instantie in de EC2-console.
