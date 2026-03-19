---
weight: 1
title: "Rychlý start"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "Spuštění rtCloud na vlastním serveru za méně než 10 minut pomocí Docker Compose."
---

Tento průvodce vás provede nasazením vlastní instance rtCloud na serveru Linux od začátku. Na konci budete mít spuštěný rtCloud přístupný v prohlížeči.

## Předpoklady

Před zahájením se ujistěte, že váš server splňuje následující požadavky:

### Hardware

| Zdroj | Minimum | Doporučeno |
|----------|---------|-------------|
| RAM | 2 GB | 4 GB |
| Disk | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPU |

### Software

| Software | Verze |
|----------|---------|
| OS | Ubuntu 20.04 LTS nebo novější (nebo jakýkoliv Linux s podporou Dockeru) |
| Docker | 20.10 nebo novější |
| Docker Compose | v2.x (`docker compose`) nebo v1.x (`docker-compose`) |

**Instalace Dockeru na Ubuntu:**

```bash
curl -fsSL https://get.docker.com | sh
```

Ověření instalace:

```bash
docker --version
docker compose version
```

---

## Krok 1 — Získejte soubory

Naklonujte repozitář nasazení na váš server:

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## Krok 2 — Nakonfigurujte prostředí

Zkopírujte ukázkový konfigurační soubor:

```bash
cp .env.production.sample .env
```

Otevřete `.env` v textovém editoru a vyplňte požadované hodnoty:

```dotenv
# Jedinečný identifikátor tohoto nasazení (bez mezer, bez speciálních znaků)
PROJECT_ID=myproject

# Doméno nebo IP adresa, kde uživatelé přistoupí k aplikaci
# Příklad: rtcloud.example.com  nebo  192.168.1.100
PROJECT_URL=rtcloud.example.com

# Protokol: použijte "https" pokud máte doménu s SSL, jinak "http"
HTTP_PROTOCOL=https

# Silná, jedinečná hesla — před spuštěním změňte všechna tři
MYSQL_PASSWORD=change_me_strong_password
MYSQL_ROOT_PASSWORD=change_me_root_password
ADMIN_PASSWORD=change_me_admin_password
```

> **Důležité:** Docker Compose automaticky načítá pouze `.env`. Nevytvářejte soubor s názvem `.env.production`, protože by způsobil zmatek. `ADMIN_PASSWORD` se použije pouze při **prvním spuštění** s čerstvou databází.

---

## Krok 3 — Spusťte kontejnery

Spusťte všechny služby na pozadí:

```bash
docker compose -f docker-compose.production.yml up -d
```

První spuštění trvá **3–5 minut** během kdy Docker:

1. Stáhne obraz aplikace rtCloud (~1 GB stahování)
2. Inicializuje databázi MySQL
3. Načte základní schéma
4. Spustí všechny čekající databázové migrace

Sledujte průběh spouštění v reálném čase:

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

Počkejte, dokud neuvidíte výstup indikující, že aplikace je připravena. Můžete také sledovat stav zdraví kontejneru:

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## Krok 4 — Přístup k aplikaci

Jakmile oba kontejnery zobrazují `Up (healthy)`, otevřete prohlížeč:

```
http://<PROJECT_URL>:8080
```

Přihlaste se pomocí účtu administrátora:

| Pole | Hodnota |
|-------|-------|
| Uživatelské jméno | `admin` |
| Heslo | Hodnota, kterou jste nastavili pro `ADMIN_PASSWORD` v `.env` |

> Změňte heslo administrátora ihned po prvním přihlášení na stránce nastavení účtu.

---

## Krok 5 — Ověřte všechny služby

Zkontrolujte, zda všechny kontejnery běží a jsou zdravé:

```bash
docker compose -f docker-compose.production.yml ps
```

Očekávaný výstup:

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

Pokud kontejner zobrazuje `Up (starting)` nebo `Up (unhealthy)`, počkejte 30–60 sekund a zkontrolujte znovu. MySQL může trvat až minutu, než se plně inicializuje při prvním spuštění.

---

## Reference portů

| Port | Služba | Popis |
|------|---------|-------------|
| `8080` | Aplikace rtCloud | Hlavní webové UI (konfigurovatelné přes `APP_PORT`) |
| `3838` | Shiny Server | Analytika a R-based vizualizace (konfigurovatelné přes `SHINY_PORT`) |

MySQL (port 3306) a jakékoliv volitelné služby (Keycloak) jsou pouze interní a ve výchozím nastavení nejsou vystaveny hostiteli.

---

## Další kroky

Vaše instance rtCloud nyní běží. Zvažte tyto následné úkoly:

- **Povolte HTTPS** — Nasměrujte doménu na váš server a nakonfigurujte SSL s Let's Encrypt. Viz [Cloudové nasazení](cloud-deployment) pro automatizované nastavení HTTPS.
- **Zkontrolujte všechna nastavení** — Prohlédněte si [Referenční příručku konfigurace](configuration) pro ladění nasazení pro produkci.
- **Nastavte SSO** — Připojte poskytovatele identit pro centralizovanou autentizaci uživatelů. Viz [SSO autentizace](sso-authentication).
- **Plánujte zálohy** — Prohlédněte si stránku [Údržba](maintenance) pro postupy zálohování a upgradu.
