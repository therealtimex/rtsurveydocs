---
weight: 1
title: "Fillimi i Shpejtë"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "Ekzekutoni rtCloud në serverin tuaj në pak se 10 minuta duke përdorur Docker Compose."
---

Ky udhëzues ju drejton nëpërmjet vendosjes së një instance rtCloud vetjake në një server Linux nga e para. Në fund, do të keni rtCloud të funksionojë dhe të aksesueshëm në shfletuesin tuaj.

## Parakushtet

Sigurohuni që serveri juaj plotëson kërkesat e mëposhtme para fillimit:

### Hardueri

| Burimi | Minimumi | I Rekomanduar |
|----------|---------|-------------|
| RAM | 2 GB | 4 GB |
| Disku | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPU |

### Softueri

| Softueri | Versioni |
|----------|---------|
| OS | Ubuntu 20.04 LTS ose më i ri (ose çdo Linux me mbështetje Docker) |
| Docker | 20.10 ose më i ri |
| Docker Compose | v2.x (`docker compose`) ose v1.x (`docker-compose`) |

**Instaloni Docker në Ubuntu:**

```bash
curl -fsSL https://get.docker.com | sh
```

Verifikoni instalimin:

```bash
docker --version
docker compose version
```

---

## Hapi 1 — Merrni Skedarët

Klononi depozitën e vendosjes në serverin tuaj:

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## Hapi 2 — Konfiguroni Mjedisin

Kopjoni skedarin e mostrës së konfigurimit:

```bash
cp .env.production.sample .env
```

Hapni `.env` në një redaktues teksti dhe plotësoni vlerat e kërkuara:

```dotenv
# Identifikues unik për këtë vendosje (pa hapësira, pa karaktere speciale)
PROJECT_ID=myprojekti

# Domeni ose adresa IP ku përdoruesit do të aksesojnë aplikacionin
# Shembull: rtcloud.example.com  ose  192.168.1.100
PROJECT_URL=rtcloud.example.com

# Protokolli: përdorni "https" nëse keni një domen me SSL, "http" ndryshe
HTTP_PROTOCOL=https

# Fjalëkalime të forta dhe unike — ndryshoni të tria para fillimit
MYSQL_PASSWORD=fjalëkalim_i_fortë_ndryshomëni
MYSQL_ROOT_PASSWORD=fjalëkalim_root_ndryshomëni
ADMIN_PASSWORD=fjalëkalim_admin_ndryshomëni
```

> **E rëndësishme:** Vetëm `.env` lexohet automatikisht nga Docker Compose. Mos krijoni një skedar të quajtur `.env.production`, pasi do të shkaktojë konfuzion. `ADMIN_PASSWORD` aplikohet vetëm në **nisjen e parë** të një baze të dhënash të re.

---

## Hapi 3 — Nisni Kontejnerët

Hapni të gjitha shërbimet në sfond:

```bash
docker compose -f docker-compose.production.yml up -d
```

Nisja e parë merr **3–5 minuta** ndërkohë që Docker:

1. Tërheq imazhin e aplikacionit rtCloud (~1 GB shkarkesë)
2. Inicializon bazën e të dhënave MySQL
3. Ngarkon skemën bazë
4. Ekzekuton të gjitha migrimet e bazës së të dhënave në pritje

Monitoroni progresin e nisjes në kohë reale:

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

Prisni derisa të shihni dalje që tregon se aplikacioni është gati. Gjithashtu mund të shikoni statusin e shëndetit të kontejnerit:

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## Hapi 4 — Aksesoni Aplikacionin

Pasi të dy kontejnerët të tregojnë `Up (healthy)`, hapni shfletuesin tuaj:

```
http://<PROJECT_URL>:8080
```

Hyni duke përdorur llogarinë e administratorit:

| Fusha | Vlera |
|-------|-------|
| Emri i përdoruesit | `admin` |
| Fjalëkalimi | Vlera që keni vendosur për `ADMIN_PASSWORD` në `.env` |

> Ndryshoni fjalëkalimin e administratorit menjëherë pas hyrjes suaj të parë nga faqja e cilësimeve të llogarisë.

---

## Hapi 5 — Verifikoni të Gjitha Shërbimet

Kontrolloni që të gjithë kontejnerët po ekzekutohen dhe janë të shëndetshëm:

```bash
docker compose -f docker-compose.production.yml ps
```

Dalja e pritur:

```
EMRI                    IMAZHI                                   STATUSI
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

Nëse një kontejner tregon `Up (starting)` ose `Up (unhealthy)`, prisni 30–60 sekonda më shumë dhe kontrolloni sërish. MySQL mund të marrë deri në një minutë për t'u inicializuar plotësisht gjatë nisjes së parë.

---

## Referenca e Portave

| Porta | Shërbimi | Përshkrimi |
|------|---------|-------------|
| `8080` | Aplikacioni rtCloud | UI-ja kryesore ueb (konfigurueshëm nëpërmjet `APP_PORT`) |
| `3838` | Serveri Shiny | Analitika dhe vizualizimet e bazuara në R (konfigurueshëm nëpërmjet `SHINY_PORT`) |

MySQL (porta 3306) dhe çdo shërbim opsional (Keycloak) janë vetëm të brendshme dhe nuk ekspozohen ndaj hostit si parazgjedhje.

---

## Hapat e Mëtejshëm

Instanca juaj rtCloud tani po ekzekutohet. Konsideroni këto detyra pasardhëse:

- **Aktivizoni HTTPS** — Drejtoni një domen në serverin tuaj dhe konfiguroni SSL me Let's Encrypt. Shikoni [Vendosja në Cloud](cloud-deployment) për konfigurimin automatik të HTTPS.
- **Rishikoni të gjitha cilësimet** — Shfletoni [Referenca e Konfigurimit](configuration) për të rregulluar vendosjen tuaj për prodhim.
- **Konfiguroni SSO** — Lidhni një ofrues identiteti për autentifikim të centralizuar të përdoruesve. Shikoni [Autentifikimi SSO](sso-authentication).
- **Planifikoni rezervimet** — Rishikoni faqen [Mirëmbajtja](maintenance) për procedurat e rezervimit dhe përditësimit.
