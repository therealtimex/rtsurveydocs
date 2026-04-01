---
weight: 2
title: "Referenční příručka konfigurace"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "Kompletní reference pro všechny proměnné prostředí používané ke konfiguraci vlastního nasazení rtCloud."
---

Veškerá konfigurace se provádí prostřednictvím proměnných prostředí v souboru `.env` v kořeni adresáře nasazení. Docker Compose tento soubor načítá automaticky — žádný příznak `--env-file` není potřeba.

Proměnné označené jako **povinné** musí být nastaveny před spuštěním kontejnerů. Všechny ostatní mají výchozí hodnoty a jsou volitelné.

---

## Projekt

Tyto proměnné definují identitu a přístupový bod vaší instance rtCloud.

| Proměnná | Výchozí | Povinné | Popis |
|----------|---------|----------|-------------|
| `PROJECT_ID` | — | **Ano** | Jedinečný identifikátor tohoto nasazení. Bez mezer nebo speciálních znaků. Používá se jako předpona pro interní pojmenování. |
| `PROJECT_URL` | — | **Ano** | Název domény nebo IP adresa, kde uživatelé přistupují k aplikaci (např. `rtcloud.example.com` nebo `192.168.1.100`). |
| `PROJECT_TYPE` | `rtsurvey` | Ne | Varianta platformy k aktivaci. Možnosti: `rtwork`, `rtsurvey`, `rthome`. |
| `PROJECT_PORT` | `80` | Ne | Port, na kterém aplikace naslouchá uvnitř kontejneru. Neměňte, pokud nevíte, co děláte. |
| `HTTP_PROTOCOL` | `https` | Ne | Protokol používaný k sestavení interních URL adres. Nastavte na `http`, pokud nepoužíváte SSL. |

---

## Databáze

Přihlašovací údaje pro připojení MySQL. Databáze je automaticky spravována kontejnerem MySQL — stačí nastavit silná hesla.

| Proměnná | Výchozí | Povinné | Popis |
|----------|---------|----------|-------------|
| `MYSQL_DATABASE` | `smartsurvey` | Ne | Název databáze aplikace. |
| `MYSQL_USER` | `smartsurvey` | Ne | Uživatel MySQL pro aplikaci. |
| `MYSQL_PASSWORD` | — | **Ano** | Heslo pro `MYSQL_USER`. Použijte silnou, jedinečnou hodnotu. |
| `MYSQL_ROOT_PASSWORD` | — | **Ano** | Heslo root pro MySQL. Vyžadováno pro inicializaci databáze a operace správce. |
| `MYSQL_HOST` | `mysql` | Ne | Název hostitele MySQL. Použijte výchozí, pokud se nepřipojujete k externí databázi. |
| `MYSQL_PORT` | `3306` | Ne | Port MySQL. |

---

## Účet administrátora

Účet administrátora je automaticky vytvořen při prvním spuštění s čerstvou databází.

| Proměnná | Výchozí | Povinné | Popis |
|----------|---------|----------|-------------|
| `ADMIN_PASSWORD` | `admin` | **Ano** | Heslo pro vestavěného uživatele `admin`. Nastavte před prvním spuštěním. Nemá žádný vliv, pokud databáze již existuje. |

> Po prvním přihlášení změňte heslo administrátora na stránce **Nastavení účtu** ve webovém UI.

---

## Porty

Kontrola, na které hostitelské porty se aplikace váže.

| Proměnná | Výchozí | Popis |
|----------|---------|-------------|
| `APP_PORT` | `8080` | Hostitelský port pro hlavní webové UI. Změňte, pokud je port 8080 již na vašem serveru obsazen. |
| `SHINY_PORT` | `3838` | Hostitelský port pro analytický server Shiny. |

---

## Runtime

| Proměnná | Výchozí | Popis |
|----------|---------|-------------|
| `RUN_ENV` | `prod` | Runtime prostředí. Použijte `prod` pro produkční nasazení, `dev` pro lokální vývoj. |
| `RUN_MODE` | `admin` | Role kontejneru. `admin` spouští celý zásobník (web + fronta + cron). `worker` spouští pouze zpracování na pozadí (pro horizontální škálování). |
| `TZ` | `Asia/Ho_Chi_Minh` | Časové pásmo serveru. Ovlivňuje časová razítka protokolů, plány cron a zobrazení dat. Použijte [název databáze TZ](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (např. `UTC`, `America/New_York`, `Europe/London`). |
| `LOG_LEVEL` | `info` | Podrobnost protokolu aplikace. Možnosti: `debug`, `info`, `warning`, `error`. |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | Předpona aplikovaná na všechny názvy kontejnerů a svazků Docker. Změňte při spuštění více instancí rtCloud na stejném hostiteli. |
| `RESTART_POLICY` | `unless-stopped` | Chování restartu kontejneru Docker. Možnosti: `no`, `always`, `on-failure`, `unless-stopped`. |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | Docker obraz k použití. Změňte tag pro připnutí konkrétní verze. |
| `REQUIRE_LICENSE` | `false` | Povolení ověření licenčního klíče při spuštění. Pro informace o licenci kontaktujte RTA. |

---

## Bezpečnost

| Proměnná | Výchozí | Popis |
|----------|---------|-------------|
| `CSRF_VALIDATION_ENABLED` | `true` | Povolení ověření CSRF tokenu. V produkci nechte `true`. Nastavte na `false` pouze při lokálním vývoji, pokud se vyskytují chyby `400 CSRF token could not be verified`. |
| `GII_ENABLED` | `false` | Povolení nástroje generátoru kódu Yii frameworku. **Nikdy nepovolujte v produkci.** |

---

## SSO — Vložený Keycloak

Povolte přibalený kontejner Keycloak pro plnohodnotné podnikové SSO. Vyžaduje doménu s HTTPS.

| Proměnná | Výchozí | Popis |
|----------|---------|-------------|
| `EMBED_KEYCLOAK` | `false` | Nastavte na `true` pro spuštění vloženého kontejneru Keycloak. Aktivuje profil Docker Compose `embed-keycloak`. |
| `KEYCLOAK_URL` | — | Úplná URL Keycloak serveru (např. `https://rtcloud.example.com/auth`). |
| `KEYCLOAK_REALM` | — | Název realm Keycloak (např. `rtsurvey`). |
| `KEYCLOAK_CLIENT_ID` | — | ID klienta Keycloak pro aplikaci rtCloud. |
| `KEYCLOAK_CLIENT_SECRET` | — | Tajný klíč klienta Keycloak. Vygenerujte z administrátorské konzole Keycloak. |
| `KEYCLOAK_ADMIN_USER` | `admin` | Uživatelské jméno administrátora Keycloak. |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Heslo administrátora Keycloak. |
| `KEYCLOAK_DB` | `keycloak` | Název databáze pro Keycloak. Vytvoří se automaticky při prvním spuštění. |
| `KEYCLOAK_DB_USER` | `keycloak` | Uživatel databáze pro Keycloak. |
| `KEYCLOAK_DB_PASSWORD` | — | Heslo databáze pro uživatele Keycloak. |
| `KC_HOSTNAME` | — | Frontend URL Keycloak (např. `https://rtcloud.example.com/auth`). |
| `KC_HOSTNAME_STRICT` | `false` | Vynutí striktní shodu názvu hostitele. V produkci s pevnou doménou nastavte na `true`. |

Viz [SSO autentizace](sso-authentication#embedded-keycloak) pro kompletního průvodce nastavením.

---

## SSO — Externí OIDC poskytovatel

Připojte se k existujícímu poskytovateli identit kompatibilnímu s OIDC (Supabase, Auth0, Authentik, Okta atd.).

| Proměnná | Výchozí | Popis |
|----------|---------|-------------|
| `OIDC_ISSUER_URL` | — | URL pro discovery OIDC issuer (např. `https://accounts.google.com`). |
| `OIDC_CLIENT_ID` | — | ID klienta zaregistrované u vašeho poskytovatele identit. |
| `OIDC_CLIENT_SECRET` | — | Tajný klíč klienta od vašeho poskytovatele identit. |
| `OIDC_SCOPE` | `openid profile email` | Mezerou oddělený seznam OIDC rozsahů k požadování. |
| `OIDC_REDIRECT_URI` | — | Callback URL pro webovou aplikaci (např. `https://rtcloud.example.com/auth/callback`). |
| `OIDC_MOBILE_CLIENT_ID` | — | Samostatné ID klienta pro mobilní aplikaci rtSurvey. |
| `OIDC_MOBILE_REDIRECT_URI` | — | Callback URI mobilní aplikace (např. `vn.rta.rtsurvey.auth://callback`). |
| `OPEN_REGISTRATION` | `false` | Automatické vytvoření rtCloud účtů pro uživatele, kteří se poprvé ověřují přes OIDC. |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | Přepsání URL autorizačního endpointu (ponechte prázdné pro použití discovery). |
| `OIDC_TOKEN_ENDPOINT` | — | Přepsání URL token endpointu (ponechte prázdné pro použití discovery). |
| `OIDC_USERINFO_ENDPOINT` | — | Přepsání URL userinfo endpointu (ponechte prázdné pro použití discovery). |

---

## SSO — Azure Active Directory

| Proměnná | Popis |
|----------|-------------|
| `AZURE_CLIENT_ID` | ID aplikace (klienta) Azure AD. |
| `AZURE_TENANT_ID` | ID adresáře (tenanta) Azure AD. |

---

## Volitelné integrace

### Stata

| Proměnná | Výchozí | Popis |
|----------|---------|-------------|
| `STATA_ENABLED` | `false` | Povolení integrace statistického softwaru Stata pro analýzu dat. |
| `STATA_BIN_PATH` | `/usr/bin/stata` | Absolutní cesta k binárnímu souboru Stata uvnitř kontejneru. |

### Elasticsearch

| Proměnná | Popis |
|----------|-------------|
| `ES_HOST` | Hostitel Elasticsearch (např. `http://elasticsearch:9200`). |
| `ES_PORT` | Port Elasticsearch. |

### Matomo Analytics

| Proměnná | Popis |
|----------|-------------|
| `PIWIK_URL` | URL serveru Matomo (Piwik). |
| `PIWIK_ID` | ID webu Matomo. |
| `PIWIK_SECRET` | Autentizační token Matomo. |

### OpenCPU (výpočty R)

| Proměnná | Popis |
|----------|-------------|
| `OCPU_HOST` | URL serveru OpenCPU pro statistické výpočty v R. |

### Integrace RtBox

| Proměnná | Popis |
|----------|-------------|
| `RTBOX_HOST` | URL hostitele služby RtBox. |
| `RTBOX_USER_API` | API klíč uživatele RtBox. |
| `RTBOX_BASIC_AUTH` | Přihlašovací údaje pro základní autentizaci RtBox. |

### Zasílání zpráv Matrix

| Proměnná | Popis |
|----------|-------------|
| `MATRIX_HOMESERVER_HOST` | Hostitel homeserveru Matrix. |
| `MATRIX_HOMESERVER_PORT` | Port homeserveru Matrix. |

---

## Datové svazky

Veškerá data aplikace jsou uložena v pojmenovaných Docker svazcích. Svazky jsou automaticky vytvořeny při prvním spuštění a přetrvávají po restartování kontejnerů a aktualizacích.

| Svazek | Bod připojení | Obsah |
|--------|-------------|----------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | Soubory databáze MySQL |
| `rtcloud_uploads` | `…/uploads` | Soubory nahrané respondenty průzkumu |
| `rtcloud_audios` | `…/audios` | Zvukové nahrávky |
| `rtcloud_downloads` | `…/downloads` | Generované exportní soubory |
| `rtcloud_gallery` | `…/gallery` | Obrázky galerie |
| `rtcloud_voicemail` | `…/voicemail` | Hlasové zprávy |
| `rtcloud_analytics` | `…/analytics` | Analytická data |
| `rtcloud_aggregate` | `…/aggregate` | Agregované výsledky průzkumu |
| `rtcloud_converter` | `…/converter` | Výstupy konverze dat |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | R skripty Shiny serveru |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Protokoly Shiny serveru |
| `rtcloud_assets` | `…/assets` | Webové prostředky (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | Mezipaměť runtime aplikace |
| `rtcloud_cache` | `…/cache` | Mezipaměť aplikace |
| `rtcloud_tmp` | `…/tmp` | Dočasné soubory |

Názvy svazků jsou předponou hodnotou `COMPOSE_PROJECT_NAME` (výchozí: `rtcloud`).

Výpis všech svazků pro vaše nasazení:

```bash
docker volume ls | grep rtcloud
```
