---
weight: 1
title: "Snelstart"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "Laat rtCloud binnen 10 minuten op uw eigen server draaien met Docker Compose."
---

Deze gids leidt u door het implementeren van een zelf gehoste rtCloud-instantie op een Linux-server vanaf nul. Aan het einde heeft u een actieve rtCloud die u in uw browser kunt openen.

## Vereisten

Zorg ervoor dat uw server aan de volgende vereisten voldoet voordat u begint:

### Hardware

| Resource | Minimum | Aanbevolen |
|----------|---------|-------------|
| RAM | 2 GB | 4 GB |
| Schijf | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPU's |

### Software

| Software | Versie |
|----------|---------|
| Besturingssysteem | Ubuntu 20.04 LTS of nieuwer (of elke Linux met Docker-ondersteuning) |
| Docker | 20.10 of nieuwer |
| Docker Compose | v2.x (`docker compose`) of v1.x (`docker-compose`) |

**Docker installeren op Ubuntu:**

```bash
curl -fsSL https://get.docker.com | sh
```

Verifieer de installatie:

```bash
docker --version
docker compose version
```

---

## Stap 1 — Haal de bestanden op

Kloon de implementatierepository naar uw server:

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## Stap 2 — Configureer de omgeving

Kopieer het voorbeeldconfiguratiebestand:

```bash
cp .env.production.sample .env
```

Open `.env` in een teksteditor en vul de vereiste waarden in:

```dotenv
# Unieke identificator voor deze implementatie (geen spaties, geen speciale tekens)
PROJECT_ID=mijnproject

# Domein of IP-adres waar gebruikers toegang krijgen tot de app
# Voorbeeld: rtcloud.example.com  of  192.168.1.100
PROJECT_URL=rtcloud.example.com

# Protocol: gebruik "https" als u een domein met SSL heeft, anders "http"
HTTP_PROTOCOL=https

# Sterke, unieke wachtwoorden — verander alle drie voordat u start
MYSQL_PASSWORD=wijzig_mij_sterk_wachtwoord
MYSQL_ROOT_PASSWORD=wijzig_mij_rootwachtwoord
ADMIN_PASSWORD=wijzig_mij_beheerderswachtwoord
```

> **Belangrijk:** Alleen `.env` wordt automatisch gelezen door Docker Compose. Maak geen bestand met de naam `.env.production`, want dat zou verwarring veroorzaken. Het `ADMIN_PASSWORD` wordt alleen toegepast bij de **eerste start** van een verse database.

---

## Stap 3 — Start de containers

Start alle services op de achtergrond:

```bash
docker compose -f docker-compose.production.yml up -d
```

De eerste start duurt **3–5 minuten** terwijl Docker:

1. De rtCloud-applicatie-image ophaalt (~1 GB download)
2. De MySQL-database initialiseert
3. Het basisschema laadt
4. Alle openstaande databasemigraties uitvoert

Monitor de startvoortgang in realtime:

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

Wacht totdat u uitvoer ziet die aangeeft dat de applicatie gereed is. U kunt ook de gezondheidssstatus van de container bekijken:

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## Stap 4 — Toegang tot de applicatie

Zodra beide containers `Up (healthy)` tonen, opent u uw browser:

```
http://<PROJECT_URL>:8080
```

Log in met het beheerdersaccount:

| Veld | Waarde |
|-------|-------|
| Gebruikersnaam | `admin` |
| Wachtwoord | De waarde die u heeft ingesteld voor `ADMIN_PASSWORD` in `.env` |

> Wijzig het beheerderwachtwoord onmiddellijk na uw eerste login via de pagina met accountinstellingen.

---

## Stap 5 — Verifieer alle services

Controleer of alle containers actief en gezond zijn:

```bash
docker compose -f docker-compose.production.yml ps
```

Verwachte uitvoer:

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

Als een container `Up (starting)` of `Up (unhealthy)` toont, wacht dan nog 30–60 seconden en controleer opnieuw. MySQL kan tot een minuut nodig hebben om volledig te initialiseren bij de eerste start.

---

## Poortreferentie

| Poort | Service | Beschrijving |
|------|---------|-------------|
| `8080` | rtCloud App | Hoofd web-UI (configureerbaar via `APP_PORT`) |
| `3838` | Shiny Server | Analyse en op R gebaseerde visualisaties (configureerbaar via `SHINY_PORT`) |

MySQL (poort 3306) en optionele services (Keycloak) zijn alleen intern en worden niet standaard blootgesteld aan de host.

---

## Volgende stappen

Uw rtCloud-instantie is nu actief. Overweeg deze vervolgacties:

- **HTTPS inschakelen** — Wijs een domein aan uw server toe en configureer SSL met Let's Encrypt. Zie [Cloudimplementatie](cloud-deployment) voor geautomatiseerde HTTPS-instelling.
- **Alle instellingen bekijken** — Blader door de [Configuratiereferentie](configuration) om uw implementatie te optimaliseren voor productie.
- **SSO instellen** — Verbind een identiteitsprovider voor gecentraliseerde gebruikersauthenticatie. Zie [SSO-authenticatie](sso-authentication).
- **Plan uw back-ups** — Bekijk de pagina [Onderhoud](maintenance) voor back-up- en upgradeprocedures.
