---
weight: 1
title: "Brzi start"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "play_circle"
toc: true
description: "Pokrenite rtCloud na sopstvenom serveru za manje od 10 minuta koristeći Docker Compose."
---

Ovaj vodič vas provodi kroz primenu sopstveno hostovane rtCloud instance na Linux serveru od nule. Na kraju ćete imati pokrenuti rtCloud dostupan u pregledaču.

## Preduslovi

Proverite da vaš server ispunjava sledeće zahteve pre početka:

### Hardver

| Resurs | Minimum | Preporučeno |
|--------|---------|-------------|
| RAM | 2 GB | 4 GB |
| Disk | 10 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPU |

### Softver

| Softver | Verzija |
|---------|---------|
| OS | Ubuntu 20.04 LTS ili noviji (ili bilo koji Linux sa Docker podrškom) |
| Docker | 20.10 ili noviji |
| Docker Compose | v2.x (`docker compose`) ili v1.x (`docker-compose`) |

**Instalirajte Docker na Ubuntu:**

```bash
curl -fsSL https://get.docker.com | sh
```

Proverite instalaciju:

```bash
docker --version
docker compose version
```

---

## Korak 1 — Preuzmite datoteke

Klonirajte repozitorijum za primenu na server:

```bash
git clone ssh://git@rtgit.rta.vn:2224/rtlab/rtwebteam/rta-smart-survey-docker.git rtcloud
cd rtcloud
```

---

## Korak 2 — Podesite okruženje

Kopirajte primer konfiguracione datoteke:

```bash
cp .env.production.sample .env
```

Otvorite `.env` u uređivaču teksta i popunite potrebne vrednosti:

```dotenv
# Jedinstveni identifikator za ovu primenu (bez razmaka, bez specijalnih znakova)
PROJECT_ID=myproject

# Domen ili IP adresa gde će korisnici pristupati aplikaciji
# Primer: rtcloud.example.com  ili  192.168.1.100
PROJECT_URL=rtcloud.example.com

# Protokol: koristite "https" ako imate domen sa SSL-om, inače "http"
HTTP_PROTOCOL=https

# Snažne, jedinstvene lozinke — promenite sve tri pre pokretanja
MYSQL_PASSWORD=change_me_strong_password
MYSQL_ROOT_PASSWORD=change_me_root_password
ADMIN_PASSWORD=change_me_admin_password
```

> **Važno:** Samo `.env` čita Docker Compose automatski. Ne kreirajte datoteku pod imenom `.env.production`, jer bi to izazvalo zabunu. `ADMIN_PASSWORD` se primenjuje samo pri **prvom pokretanju** nove baze podataka.

---

## Korak 3 — Pokrenite kontejnere

Pokrenite sve servise u pozadini:

```bash
docker compose -f docker-compose.production.yml up -d
```

Prvo pokretanje traje **3–5 minuta** dok Docker:

1. Preuzima sliku rtCloud aplikacije (~1 GB preuzimanja)
2. Inicijalizuje MySQL bazu podataka
3. Učitava osnovnu šemu
4. Izvršava sve čekajuće migracije baze podataka

Pratite napredak pokretanja u realnom vremenu:

```bash
docker compose -f docker-compose.production.yml logs -f rtcloud
```

Sačekajte dok ne vidite izlaz koji ukazuje da je aplikacija spremna. Takođe možete pratiti status zdravlja kontejnera:

```bash
watch docker compose -f docker-compose.production.yml ps
```

---

## Korak 4 — Pristupite aplikaciji

Kada oba kontejnera pokažu `Up (healthy)`, otvorite pregledač:

```
http://<PROJECT_URL>:8080
```

Prijavite se koristeći administratorski nalog:

| Polje | Vrednost |
|-------|---------|
| Korisničko ime | `admin` |
| Lozinka | Vrednost koju ste postavili za `ADMIN_PASSWORD` u `.env` |

> Promenite administratorsku lozinku odmah nakon prve prijave sa stranice za podešavanja naloga.

---

## Korak 5 — Proverite sve servise

Proverite da svi kontejneri rade i da su zdravi:

```bash
docker compose -f docker-compose.production.yml ps
```

Očekivani izlaz:

```
NAME                    IMAGE                                   STATUS
rtcloud-app             rtawebteam/rta-smartsurvey:...          Up (healthy)
rtcloud-mysql           mysql:8.0                               Up (healthy)
```

Ako kontejner pokazuje `Up (starting)` ili `Up (unhealthy)`, sačekajte još 30–60 sekundi i proverite ponovo. MySQL može da treba i do minut da se potpuno inicijalizuje pri prvom pokretanju.

---

## Referenca portova

| Port | Servis | Opis |
|------|--------|------|
| `8080` | rtCloud aplikacija | Glavni veb UI (podesivo putem `APP_PORT`) |
| `3838` | Shiny Server | Analitika i vizualizacije zasnovane na R-u (podesivo putem `SHINY_PORT`) |

MySQL (port 3306) i svi opcioni servisi (Keycloak) su samo interni i podrazumevano nisu izloženi hostu.

---

## Sledeći koraci

Vaša rtCloud instanca sada radi. Razmotrite ove naknadne zadatke:

- **Aktivirajte HTTPS** — Usmerite domen na vaš server i konfigurišite SSL sa Let's Encrypt. Pogledajte [Primenu u oblaku](cloud-deployment) za automatizovano HTTPS podešavanje.
- **Pregledajte sva podešavanja** — Pregledajte [Referencu konfiguracije](configuration) da prilagodite vašu primenu za produkciju.
- **Podesite SSO** — Povežite pružaoca identiteta za centralizovanu autentifikaciju korisnika. Pogledajte [SSO autentifikaciju](sso-authentication).
- **Planirajte rezervne kopije** — Pregledajte stranicu [Održavanje](maintenance) za procedure pravljenja rezervnih kopija i nadogradnje.
