---
weight: 1
title: "Hurtigstart"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "Få rtCloud til at køre på din egen server på under 10 minutter ved hjælp af Docker Compose."
---

Denne guide gennemgår implementering af en selvhostet rtCloud-instans på en Linux-server fra bunden. Når du er færdig, vil du have en kørende rtCloud tilgængelig i din browser.

## Forudsætninger

Sørg for, at din server opfylder følgende krav, inden du begynder:

### Hardware

| Ressource | Minimum | Anbefalet |
|----------|---------|-------------|
| RAM | 2 GB | 4 GB |
| Disk | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPU'er |

### Software

| Software | Version |
|----------|---------|
| OS | Ubuntu 20.04 LTS eller nyere (eller enhver Linux med Docker-understøttelse) |
| Docker | 20.10 eller nyere |
| Docker Compose | v2.x (`docker compose`) eller v1.x (`docker-compose`) |

**Installer Docker på Ubuntu:**

```bash
curl -fsSL https://get.docker.com | sh
```

Bekræft installationen:

```bash
docker --version
docker compose version
```

---

## Trin 1 — Hent filerne

Klon implementeringslageret til din server:

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## Trin 2 — Konfigurer miljøet

Kopiér eksempelkonfigurationsfilen:

```bash
cp .env.production.sample .env
```

Åbn `.env` i en teksteditor og udfyld de påkrævede værdier:

```dotenv
# Unik identifikator for denne implementering (ingen mellemrum, ingen specialtegn)
PROJECT_ID=mitprojekt

# Domæne eller IP-adresse, hvor brugere vil tilgå appen
# Eksempel: rtcloud.example.com  eller  192.168.1.100
PROJECT_URL=rtcloud.example.com

# Protokol: brug "https", hvis du har et domæne med SSL, ellers "http"
HTTP_PROTOCOL=https

# Stærke, unikke adgangskoder – skift alle tre, inden du starter
MYSQL_PASSWORD=skift_mig_stærk_adgangskode
MYSQL_ROOT_PASSWORD=skift_mig_root_adgangskode
ADMIN_PASSWORD=skift_mig_admin_adgangskode
```

> **Vigtigt:** Kun `.env` læses automatisk af Docker Compose. Opret ikke en fil med navnet `.env.production`, da det vil skabe forvirring. `ADMIN_PASSWORD` anvendes kun ved **første opstart** af en ny database.

---

## Trin 3 — Start containerne

Start alle tjenester i baggrunden:

```bash
docker compose -f docker-compose.production.yml up -d
```

Den første opstart tager **3–5 minutter**, mens Docker:

1. Trækker rtCloud-applikationsimaget (~1 GB download)
2. Initialiserer MySQL-databasen
3. Indlæser basisskemaet
4. Kører alle ventende databasemigreringer

Overvåg opstartsforløbet i realtid:

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

Vent, til du ser output, der angiver, at applikationen er klar. Du kan også overvåge containerens sundhedsstatus:

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## Trin 4 — Få adgang til applikationen

Når begge containere viser `Up (healthy)`, åbn din browser:

```
http://<PROJECT_URL>:8080
```

Log ind med administratorkontoen:

| Felt | Værdi |
|-------|-------|
| Brugernavn | `admin` |
| Adgangskode | Den værdi, du angav for `ADMIN_PASSWORD` i `.env` |

> Skift admin-adgangskoden umiddelbart efter din første login fra kontoindstillingssiden.

---

## Trin 5 — Bekræft alle tjenester

Kontrollér, at alle containere kører og er sunde:

```bash
docker compose -f docker-compose.production.yml ps
```

Forventet output:

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

Hvis en container viser `Up (starting)` eller `Up (unhealthy)`, vent 30–60 sekunder mere og kontrollér igen. MySQL kan tage op til et minut at initialisere fuldt ud ved første opstart.

---

## Portreference

| Port | Tjeneste | Beskrivelse |
|------|---------|-------------|
| `8080` | rtCloud App | Hoved-webgrænseflade (kan konfigureres via `APP_PORT`) |
| `3838` | Shiny Server | Analyse og R-baserede visualiseringer (kan konfigureres via `SHINY_PORT`) |

MySQL (port 3306) og eventuelle valgfrie tjenester (Keycloak) er kun interne og eksponeres ikke til hosten som standard.

---

## Næste trin

Din rtCloud-instans kører nu. Overvej disse opfølgende opgaver:

- **Aktiver HTTPS** – Peg et domæne mod din server og konfigurer SSL med Let's Encrypt. Se [Cloud-implementering](cloud-deployment) for automatiseret HTTPS-opsætning.
- **Gennemgå alle indstillinger** – Gennemse [Konfigurationsreferencen](configuration) for at optimere din implementering til produktion.
- **Opsæt SSO** – Forbind en identitetsudbyder til centraliseret brugergodkendelse. Se [SSO-godkendelse](sso-authentication).
- **Planlæg dine sikkerhedskopier** – Gennemse siden [Vedligeholdelse](maintenance) for sikkerhedskopiering og opgraderingsprocedurer.
