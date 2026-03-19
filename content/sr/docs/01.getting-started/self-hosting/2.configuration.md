---
weight: 2
title: "Referenca konfiguracije"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "Kompletna referenca svih promenljivih okruženja koji se koriste za konfigurisanje sopstveno hostovane rtCloud primene."
---

Sva konfiguracija se vrši putem promenljivih okruženja u `.env` datoteci u korenom direktorijumu vaše primene. Docker Compose čita ovu datoteku automatski — nije potrebna oznaka `--env-file`.

Promenljive označene kao **obavezne** moraju biti postavljene pre pokretanja kontejnera. Sve ostale imaju podrazumevane vrednosti i opcione su.

---

## Projekat

Ove promenljive definišu identitet i pristupnu tačku vaše rtCloud instance.

| Promenljiva | Podrazumevano | Obavezno | Opis |
|-------------|---------------|----------|------|
| `PROJECT_ID` | — | **Da** | Jedinstveni identifikator za ovu primenu. Bez razmaka ili specijalnih znakova. Koristi se kao prefiks za interno imenovanje. |
| `PROJECT_URL` | — | **Da** | Naziv domena ili IP adresa gde korisnici pristupaju aplikaciji (npr. `rtcloud.example.com` ili `192.168.1.100`). |
| `PROJECT_TYPE` | `rtsurvey` | Ne | Varijanta platforme koja se aktivira. Opcije: `rtwork`, `rtsurvey`, `rthome`. |
| `PROJECT_PORT` | `80` | Ne | Port na kome aplikacija sluša unutar kontejnera. Ne menjajte ako ne znate šta radite. |
| `HTTP_PROTOCOL` | `https` | Ne | Protokol koji se koristi za konstruisanje internih URL-ova. Postavite na `http` ako ne koristite SSL. |

---

## Baza podataka

MySQL akreditivi za vezu. Bazom podataka automatski upravlja MySQL kontejner — potrebno je samo da postavite snažne lozinke.

| Promenljiva | Podrazumevano | Obavezno | Opis |
|-------------|---------------|----------|------|
| `MYSQL_DATABASE` | `smartsurvey` | Ne | Naziv baze podataka aplikacije. |
| `MYSQL_USER` | `smartsurvey` | Ne | MySQL korisnik za aplikaciju. |
| `MYSQL_PASSWORD` | — | **Da** | Lozinka za `MYSQL_USER`. Koristite snažnu, jedinstvenu vrednost. |
| `MYSQL_ROOT_PASSWORD` | — | **Da** | MySQL root lozinka. Potrebna za inicijalizaciju baze podataka i administratorske operacije. |
| `MYSQL_HOST` | `mysql` | Ne | MySQL hostname. Koristite podrazumevano osim ako se povezujete na spoljnu bazu podataka. |
| `MYSQL_PORT` | `3306` | Ne | MySQL port. |

---

## Administratorski nalog

Administratorski nalog se automatski kreira pri prvom pokretanju nove baze podataka.

| Promenljiva | Podrazumevano | Obavezno | Opis |
|-------------|---------------|----------|------|
| `ADMIN_PASSWORD` | `admin` | **Da** | Lozinka za ugrađenog korisnika `admin`. Postavite ovo pre prvog pokretanja. Nema efekta ako baza podataka već postoji. |

> Nakon prve prijave, promenite administratorsku lozinku sa stranice **Podešavanja naloga** u veb UI-u.

---

## Portovi

Kontrolišite koje host portove aplikacija koristi.

| Promenljiva | Podrazumevano | Opis |
|-------------|---------------|------|
| `APP_PORT` | `8080` | Host port za glavni veb UI. Promenite ovo ako je port 8080 već u upotrebi na vašem serveru. |
| `SHINY_PORT` | `3838` | Host port za Shiny analitički server. |

---

## Radno okruženje

| Promenljiva | Podrazumevano | Opis |
|-------------|---------------|------|
| `RUN_ENV` | `prod` | Radno okruženje. Koristite `prod` za produkcione primene, `dev` za lokalni razvoj. |
| `RUN_MODE` | `admin` | Uloga kontejnera. `admin` pokreće celi stek (veb + red + cron). `worker` pokreće samo pozadinsku obradu (za horizontalno skaliranje). |
| `TZ` | `Asia/Ho_Chi_Minh` | Vremenska zona servera. Utiče na vremenske oznake u evidencijama, cron rasporede i prikaz datuma. Koristite [TZ ime baze podataka](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (npr. `UTC`, `America/New_York`, `Europe/London`). |
| `LOG_LEVEL` | `info` | Detaljnost aplikativnog evidenciranja. Opcije: `debug`, `info`, `warning`, `error`. |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | Prefiks primenjen na sva Docker imena kontejnera i volumena. Promenite ovo kada pokrećete više rtCloud instanci na istom hostu. |
| `RESTART_POLICY` | `unless-stopped` | Ponašanje Docker kontejnera pri ponovnom pokretanju. Opcije: `no`, `always`, `on-failure`, `unless-stopped`. |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | Docker slika koja se koristi. Promenite oznaku da zakačite određenu verziju. |
| `REQUIRE_LICENSE` | `false` | Aktivirajte validaciju licencnog ključa pri pokretanju. Kontaktirajte RTA za informacije o licenci. |

---

## Bezbednost

| Promenljiva | Podrazumevano | Opis |
|-------------|---------------|------|
| `CSRF_VALIDATION_ENABLED` | `true` | Aktivirajte validaciju CSRF tokena. Zadržite ovo na `true` u produkciji. Postavite na `false` samo u lokalnom razvoju ako naiđete na greške `400 CSRF token could not be verified`. |
| `GII_ENABLED` | `false` | Aktivirajte Yii framework alat za generisanje koda. **Nikada ne aktivirajte u produkciji.** |

---

## SSO — Ugrađeni Keycloak

Aktivirajte priloženi Keycloak kontejner za SSO sa punim funkcionalnostima na nivou preduzeća. Zahteva domen sa HTTPS-om.

| Promenljiva | Podrazumevano | Opis |
|-------------|---------------|------|
| `EMBED_KEYCLOAK` | `false` | Postavite na `true` da pokrenete ugrađeni Keycloak kontejner. Aktivira `embed-keycloak` Docker Compose profil. |
| `KEYCLOAK_URL` | — | Puni URL Keycloak servera (npr. `https://rtcloud.example.com/auth`). |
| `KEYCLOAK_REALM` | — | Naziv Keycloak realma (npr. `rtsurvey`). |
| `KEYCLOAK_CLIENT_ID` | — | Keycloak ID klijenta za rtCloud aplikaciju. |
| `KEYCLOAK_CLIENT_SECRET` | — | Keycloak tajna klijenta. Generišite ovo iz Keycloak administratorske konzole. |
| `KEYCLOAK_ADMIN_USER` | `admin` | Keycloak administratorsko korisničko ime. |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Keycloak administratorska lozinka. |
| `KEYCLOAK_DB` | `keycloak` | Naziv baze podataka za Keycloak. Automatski se kreira pri prvom pokretanju. |
| `KEYCLOAK_DB_USER` | `keycloak` | Korisnik baze podataka za Keycloak. |
| `KEYCLOAK_DB_PASSWORD` | — | Lozinka baze podataka za Keycloak korisnika. |
| `KC_HOSTNAME` | — | Keycloak frontend URL (npr. `https://rtcloud.example.com/auth`). |
| `KC_HOSTNAME_STRICT` | `false` | Primenite striktno podudaranje hostname-a. Postavite na `true` u produkciji sa fiksnim domenom. |

Pogledajte [SSO autentifikaciju](sso-authentication#embedded-keycloak) za kompletan vodič za podešavanje.

---

## SSO — Spoljni OIDC pružalac

Povežite se na postojećeg OIDC-kompatibilnog pružaoca identiteta (Supabase, Auth0, Authentik, Okta, itd.).

| Promenljiva | Podrazumevano | Opis |
|-------------|---------------|------|
| `OIDC_ISSUER_URL` | — | OIDC URL za otkrivanje izdavaoca (npr. `https://accounts.google.com`). |
| `OIDC_CLIENT_ID` | — | ID klijenta registrovanog kod vašeg pružaoca identiteta. |
| `OIDC_CLIENT_SECRET` | — | Tajna klijenta od vašeg pružaoca identiteta. |
| `OIDC_SCOPE` | `openid profile email` | Lista OIDC opsega za zahtevanje razdvojena razmacima. |
| `OIDC_REDIRECT_URI` | — | URL za povratni poziv za veb aplikaciju (npr. `https://rtcloud.example.com/auth/callback`). |
| `OIDC_MOBILE_CLIENT_ID` | — | Poseban ID klijenta za rtSurvey mobilnu aplikaciju. |
| `OIDC_MOBILE_REDIRECT_URI` | — | URI mobilne aplikacije za povratni poziv (npr. `vn.rta.rtsurvey.auth://callback`). |
| `OPEN_REGISTRATION` | `false` | Automatski kreirajte rtCloud naloge za korisnike koji se prvi put autentifikuju putem OIDC-a. |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | Zamenite URL krajnje tačke za autorizaciju (ostavite prazno da koristite otkrivanje). |
| `OIDC_TOKEN_ENDPOINT` | — | Zamenite URL krajnje tačke za token (ostavite prazno da koristite otkrivanje). |
| `OIDC_USERINFO_ENDPOINT` | — | Zamenite URL krajnje tačke za informacije o korisniku (ostavite prazno da koristite otkrivanje). |

---

## SSO — Azure Active Directory

| Promenljiva | Opis |
|-------------|------|
| `AZURE_CLIENT_ID` | Azure AD ID aplikacije (klijenta). |
| `AZURE_TENANT_ID` | Azure AD ID direktorijuma (zakupca). |

---

## Opcione integracije

### Stata

| Promenljiva | Podrazumevano | Opis |
|-------------|---------------|------|
| `STATA_ENABLED` | `false` | Aktivirajte integraciju Stata statističkog softvera za analizu podataka. |
| `STATA_BIN_PATH` | `/usr/bin/stata` | Apsolutna putanja do Stata binarne datoteke unutar kontejnera. |

### Elasticsearch

| Promenljiva | Opis |
|-------------|------|
| `ES_HOST` | Elasticsearch host (npr. `http://elasticsearch:9200`). |
| `ES_PORT` | Elasticsearch port. |

### Matomo analitika

| Promenljiva | Opis |
|-------------|------|
| `PIWIK_URL` | URL Matomo (Piwik) servera. |
| `PIWIK_ID` | Matomo ID sajta. |
| `PIWIK_SECRET` | Matomo autentifikacioni token. |

### OpenCPU (R izračunavanje)

| Promenljiva | Opis |
|-------------|------|
| `OCPU_HOST` | URL OpenCPU servera za statističko izračunavanje zasnovano na R-u. |

### RtBox integracija

| Promenljiva | Opis |
|-------------|------|
| `RTBOX_HOST` | URL hosta RtBox servisa. |
| `RTBOX_USER_API` | API ključ korisnika RtBox-a. |
| `RTBOX_BASIC_AUTH` | Akreditivi za osnovna autentifikaciju za RtBox. |

### Matrix poruke

| Promenljiva | Opis |
|-------------|------|
| `MATRIX_HOMESERVER_HOST` | Matrix homeserver host. |
| `MATRIX_HOMESERVER_PORT` | Matrix homeserver port. |

---

## Volumeni podataka

Svi aplikativni podaci su smešteni u imenovanim Docker volumenima. Volumeni se automatski kreiraju pri prvom pokretanju i opstaju kroz restartovanje i ažuriranja kontejnera.

| Volumen | Tačka montiranja | Sadržaj |
|---------|-----------------|---------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | MySQL datoteke baze podataka |
| `rtcloud_uploads` | `…/uploads` | Datoteke koje su ispitanici ankete otpremili |
| `rtcloud_audios` | `…/audios` | Audio snimci |
| `rtcloud_downloads` | `…/downloads` | Generisane izvozne datoteke |
| `rtcloud_gallery` | `…/gallery` | Slike galerije |
| `rtcloud_voicemail` | `…/voicemail` | Snimci govorne pošte |
| `rtcloud_analytics` | `…/analytics` | Analitički podaci |
| `rtcloud_aggregate` | `…/aggregate` | Agregirani rezultati ankete |
| `rtcloud_converter` | `…/converter` | Izlazi konverzije podataka |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | Shiny server R skripte |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Evidencije Shiny servera |
| `rtcloud_assets` | `…/assets` | Veb resursi (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | Keš aplikativnog radnog okruženja |
| `rtcloud_cache` | `…/cache` | Keš aplikacije |
| `rtcloud_tmp` | `…/tmp` | Privremene datoteke |

Nazivi volumena su prefiksovani vrednošću `COMPOSE_PROJECT_NAME` (podrazumevano: `rtcloud`).

Navedite sve volumene za vašu primenu:

```bash
docker volume ls | grep rtcloud
```
