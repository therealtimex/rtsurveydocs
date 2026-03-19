---
weight: 2
title: "Konfigurationsreferens"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "Fullständig referens för alla miljövariabler som används för att konfigurera en självhostad rtCloud-driftsättning."
---

All konfiguration görs via miljövariabler i filen `.env` i rotkatalogen för din driftsättning. Docker Compose läser denna fil automatiskt — ingen `--env-file`-flagga behövs.

Variabler markerade som **obligatoriska** måste anges innan du startar containrarna. Alla andra har standardvärden och är valfria.

---

## Projekt

Dessa variabler definierar identiteten och åtkomstpunkten för din rtCloud-instans.

| Variabel | Standard | Obligatorisk | Beskrivning |
|----------|---------|----------|-------------|
| `PROJECT_ID` | — | **Ja** | Unik identifierare för denna driftsättning. Inga mellanslag eller specialtecken. Används som prefix för intern namngivning. |
| `PROJECT_URL` | — | **Ja** | Domännamn eller IP-adress där användare kommer åt appen (t.ex. `rtcloud.example.com` eller `192.168.1.100`). |
| `PROJECT_TYPE` | `rtsurvey` | Nej | Plattformsvariant att aktivera. Alternativ: `rtwork`, `rtsurvey`, `rthome`. |
| `PROJECT_PORT` | `80` | Nej | Port som applikationen lyssnar på inuti containern. Ändra inte om du inte vet vad du gör. |
| `HTTP_PROTOCOL` | `https` | Nej | Protokoll som används för att konstruera interna URL:er. Ange `http` om du inte använder SSL. |

---

## Databas

MySQL-anslutningsuppgifter. Databasen hanteras automatiskt av MySQL-containern — du behöver bara ange starka lösenord.

| Variabel | Standard | Obligatorisk | Beskrivning |
|----------|---------|----------|-------------|
| `MYSQL_DATABASE` | `smartsurvey` | Nej | Namn på applikationsdatabasen. |
| `MYSQL_USER` | `smartsurvey` | Nej | MySQL-användare för applikationen. |
| `MYSQL_PASSWORD` | — | **Ja** | Lösenord för `MYSQL_USER`. Använd ett starkt, unikt värde. |
| `MYSQL_ROOT_PASSWORD` | — | **Ja** | MySQL root-lösenord. Krävs för databasinitialisering och adminoperationer. |
| `MYSQL_HOST` | `mysql` | Nej | MySQL-värdnamn. Använd standardvärdet om du inte ansluter till en extern databas. |
| `MYSQL_PORT` | `3306` | Nej | MySQL-port. |

---

## Adminkonto

Adminkontot skapas automatiskt vid första starten av en ny databas.

| Variabel | Standard | Obligatorisk | Beskrivning |
|----------|---------|----------|-------------|
| `ADMIN_PASSWORD` | `admin` | **Ja** | Lösenord för den inbyggda `admin`-användaren. Ange detta innan första starten. Har ingen effekt om databasen redan finns. |

> Efter första inloggningen, ändra adminlösenordet från sidan **Kontoinställningar** i webb-UI:t.

---

## Portar

Kontrollera vilka värdportar applikationen binder till.

| Variabel | Standard | Beskrivning |
|----------|---------|-------------|
| `APP_PORT` | `8080` | Värdport för huvud-webb-UI:t. Ändra detta om port 8080 redan används på din server. |
| `SHINY_PORT` | `3838` | Värdport för Shiny-analysservern. |

---

## Körning

| Variabel | Standard | Beskrivning |
|----------|---------|-------------|
| `RUN_ENV` | `prod` | Körningsmiljö. Använd `prod` för produktionsdriftsättningar, `dev` för lokal utveckling. |
| `RUN_MODE` | `admin` | Containerroll. `admin` kör hela stacken (webb + kö + cron). `worker` kör bara bakgrundsbearbetning (för horisontell skalning). |
| `TZ` | `Asia/Ho_Chi_Minh` | Servertidszon. Påverkar loggtidsstämplar, cron-scheman och datumdisplay. Använd ett [TZ-databasnamn](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (t.ex. `UTC`, `America/New_York`, `Europe/Stockholm`). |
| `LOG_LEVEL` | `info` | Applikationsloggens detaljnivå. Alternativ: `debug`, `info`, `warning`, `error`. |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | Prefix som tillämpas på alla Docker-container- och volymnamn. Ändra detta när du kör flera rtCloud-instanser på samma värd. |
| `RESTART_POLICY` | `unless-stopped` | Docker-containerns omstartsbeteende. Alternativ: `no`, `always`, `on-failure`, `unless-stopped`. |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | Docker-avbild att använda. Ändra taggen för att fästa en specifik version. |
| `REQUIRE_LICENSE` | `false` | Aktivera licensnyckelvalidering vid start. Kontakta RTA för licensinformation. |

---

## Säkerhet

| Variabel | Standard | Beskrivning |
|----------|---------|-------------|
| `CSRF_VALIDATION_ENABLED` | `true` | Aktivera CSRF-tokenvalidering. Håll detta `true` i produktion. Ange `false` endast i lokal utveckling om du stöter på `400 CSRF token could not be verified`-fel. |
| `GII_ENABLED` | `false` | Aktivera Yii-ramverkets kodgeneratorverktyg. **Aktivera aldrig i produktion.** |

---

## SSO — Inbäddad Keycloak

Aktivera den medföljande Keycloak-containern för fullfjädrad SSO i företag. Kräver en domän med HTTPS.

| Variabel | Standard | Beskrivning |
|----------|---------|-------------|
| `EMBED_KEYCLOAK` | `false` | Ange `true` för att starta den inbäddade Keycloak-containern. Aktiverar Docker Compose-profilen `embed-keycloak`. |
| `KEYCLOAK_URL` | — | Fullständig URL för Keycloak-servern (t.ex. `https://rtcloud.example.com/auth`). |
| `KEYCLOAK_REALM` | — | Keycloak realm-namn (t.ex. `rtsurvey`). |
| `KEYCLOAK_CLIENT_ID` | — | Keycloak klient-ID för rtCloud-applikationen. |
| `KEYCLOAK_CLIENT_SECRET` | — | Keycloak klienthemlighet. Generera detta från Keycloak-adminkonsolen. |
| `KEYCLOAK_ADMIN_USER` | `admin` | Keycloak-administratörens användarnamn. |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Keycloak-administratörens lösenord. |
| `KEYCLOAK_DB` | `keycloak` | Databasnamn för Keycloak. Skapas automatiskt vid första starten. |
| `KEYCLOAK_DB_USER` | `keycloak` | Databasanvändare för Keycloak. |
| `KEYCLOAK_DB_PASSWORD` | — | Databaslösenord för Keycloak-användaren. |
| `KC_HOSTNAME` | — | Keycloaks frontend-URL (t.ex. `https://rtcloud.example.com/auth`). |
| `KC_HOSTNAME_STRICT` | `false` | Tillämpa strikt värdnamnsmatchning. Ange `true` i produktion med en fast domän. |

Se [SSO-autentisering](sso-authentication#embedded-keycloak) för den fullständiga installationsguiden.

---

## SSO — Extern OIDC-leverantör

Anslut till en befintlig OIDC-kompatibel identitetsleverantör (Supabase, Auth0, Authentik, Okta, m.fl.).

| Variabel | Standard | Beskrivning |
|----------|---------|-------------|
| `OIDC_ISSUER_URL` | — | OIDC-utfärdarens URL för discovery (t.ex. `https://accounts.google.com`). |
| `OIDC_CLIENT_ID` | — | Klient-ID registrerat hos din identitetsleverantör. |
| `OIDC_CLIENT_SECRET` | — | Klienthemlighet från din identitetsleverantör. |
| `OIDC_SCOPE` | `openid profile email` | Mellanslagsavgränsad lista med OIDC-scope att begära. |
| `OIDC_REDIRECT_URI` | — | Callback-URL för webbappen (t.ex. `https://rtcloud.example.com/auth/callback`). |
| `OIDC_MOBILE_CLIENT_ID` | — | Separat klient-ID för rtSurvey-mobilappen. |
| `OIDC_MOBILE_REDIRECT_URI` | — | Mobilappens callback-URI (t.ex. `vn.rta.rtsurvey.auth://callback`). |
| `OPEN_REGISTRATION` | `false` | Skapa automatiskt rtCloud-konton för användare som autentiserar sig via OIDC för första gången. |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | Åsidosätt auktoriseringsslutpunktens URL (lämna tomt för att använda discovery). |
| `OIDC_TOKEN_ENDPOINT` | — | Åsidosätt tokenslutpunktens URL (lämna tomt för att använda discovery). |
| `OIDC_USERINFO_ENDPOINT` | — | Åsidosätt användarinfo-slutpunktens URL (lämna tomt för att använda discovery). |

---

## SSO — Azure Active Directory

| Variabel | Beskrivning |
|----------|-------------|
| `AZURE_CLIENT_ID` | Azure AD-applikationens (klientens) ID. |
| `AZURE_TENANT_ID` | Azure AD-katalogens (klientorganisationens) ID. |

---

## Valfria integrationer

### Stata

| Variabel | Standard | Beskrivning |
|----------|---------|-------------|
| `STATA_ENABLED` | `false` | Aktivera integration med Stata statistisk programvara för dataanalys. |
| `STATA_BIN_PATH` | `/usr/bin/stata` | Absolut sökväg till Stata-binärfilen inuti containern. |

### Elasticsearch

| Variabel | Beskrivning |
|----------|-------------|
| `ES_HOST` | Elasticsearch-värd (t.ex. `http://elasticsearch:9200`). |
| `ES_PORT` | Elasticsearch-port. |

### Matomo-analys

| Variabel | Beskrivning |
|----------|-------------|
| `PIWIK_URL` | Matomo (Piwik) server-URL. |
| `PIWIK_ID` | Matomo webbplats-ID. |
| `PIWIK_SECRET` | Matomo autentiseringstoken. |

### OpenCPU (R-beräkning)

| Variabel | Beskrivning |
|----------|-------------|
| `OCPU_HOST` | OpenCPU-serverns URL för R-baserad statistisk beräkning. |

### RtBox-integration

| Variabel | Beskrivning |
|----------|-------------|
| `RTBOX_HOST` | RtBox-tjänstens värd-URL. |
| `RTBOX_USER_API` | RtBox användar-API-nyckel. |
| `RTBOX_BASIC_AUTH` | Grundläggande autentiseringsuppgifter för RtBox. |

### Matrix-meddelanden

| Variabel | Beskrivning |
|----------|-------------|
| `MATRIX_HOMESERVER_HOST` | Matrix homeserver-värd. |
| `MATRIX_HOMESERVER_PORT` | Matrix homeserver-port. |

---

## Datavolymer

All applikationsdata lagras i namngivna Docker-volymer. Volymer skapas automatiskt vid första starten och bevaras vid omstarter av containrar och uppdateringar.

| Volym | Monteringspunkt | Innehåll |
|--------|-------------|----------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | MySQL-databasfiler |
| `rtcloud_uploads` | `…/uploads` | Filer uppladdade av undersökningsrespondenter |
| `rtcloud_audios` | `…/audios` | Ljudinspelningar |
| `rtcloud_downloads` | `…/downloads` | Genererade exportfiler |
| `rtcloud_gallery` | `…/gallery` | Galleribilder |
| `rtcloud_voicemail` | `…/voicemail` | Röstmeddelandeinspelningar |
| `rtcloud_analytics` | `…/analytics` | Analysdata |
| `rtcloud_aggregate` | `…/aggregate` | Aggregerade undersökningsresultat |
| `rtcloud_converter` | `…/converter` | Datakonverteringsutdata |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | Shiny-serverns R-skript |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Shiny-serverns loggar |
| `rtcloud_assets` | `…/assets` | Webbtillgångar (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | Applikationens körningscache |
| `rtcloud_cache` | `…/cache` | Applikationscache |
| `rtcloud_tmp` | `…/tmp` | Temporära filer |

Volymnamn är prefixade med värdet av `COMPOSE_PROJECT_NAME` (standard: `rtcloud`).

Lista alla volymer för din driftsättning:

```bash
docker volume ls | grep rtcloud
```
