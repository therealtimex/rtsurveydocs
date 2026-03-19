---
weight: 2
title: "Konfigurationsreference"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "Komplet reference til alle miljøvariabler, der bruges til at konfigurere en selvhostet rtCloud-implementering."
---

Al konfiguration udføres via miljøvariabler i `.env`-filen i roden af dit implementeringsbibliotek. Docker Compose læser denne fil automatisk – der er ikke behov for et `--env-file`-flag.

Variabler markeret som **påkrævet** skal angives, inden containerne startes. Alle andre har standardværdier og er valgfrie.

---

## Projekt

Disse variabler definerer identiteten og adgangspunktet for din rtCloud-instans.

| Variabel | Standard | Påkrævet | Beskrivelse |
|----------|---------|----------|-------------|
| `PROJECT_ID` | — | **Ja** | Unik identifikator for denne implementering. Ingen mellemrum eller specialtegn. Bruges som præfiks til intern navngivning. |
| `PROJECT_URL` | — | **Ja** | Domænenavn eller IP-adresse, hvor brugere tilgår appen (f.eks. `rtcloud.example.com` eller `192.168.1.100`). |
| `PROJECT_TYPE` | `rtsurvey` | Nej | Platformsvariant der aktiveres. Valgmuligheder: `rtwork`, `rtsurvey`, `rthome`. |
| `PROJECT_PORT` | `80` | Nej | Port, som applikationen lytter på inde i containeren. Skift ikke, medmindre du ved, hvad du gør. |
| `HTTP_PROTOCOL` | `https` | Nej | Protokol, der bruges til at konstruere interne URL'er. Sæt til `http`, hvis du ikke bruger SSL. |

---

## Database

MySQL-forbindelsesoplysninger. Databasen administreres automatisk af MySQL-containeren – du behøver kun at angive stærke adgangskoder.

| Variabel | Standard | Påkrævet | Beskrivelse |
|----------|---------|----------|-------------|
| `MYSQL_DATABASE` | `smartsurvey` | Nej | Navn på applikationsdatabasen. |
| `MYSQL_USER` | `smartsurvey` | Nej | MySQL-bruger til applikationen. |
| `MYSQL_PASSWORD` | — | **Ja** | Adgangskode til `MYSQL_USER`. Brug en stærk, unik værdi. |
| `MYSQL_ROOT_PASSWORD` | — | **Ja** | MySQL root-adgangskode. Påkrævet til databaseinitialisering og administratorhandlinger. |
| `MYSQL_HOST` | `mysql` | Nej | MySQL-værtsnavn. Brug standarden, medmindre du forbinder til en ekstern database. |
| `MYSQL_PORT` | `3306` | Nej | MySQL-port. |

---

## Adminkonto

Adminkontoen oprettes automatisk ved første opstart af en ny database.

| Variabel | Standard | Påkrævet | Beskrivelse |
|----------|---------|----------|-------------|
| `ADMIN_PASSWORD` | `admin` | **Ja** | Adgangskode til den indbyggede `admin`-bruger. Angiv dette inden første opstart. Har ingen effekt, hvis databasen allerede eksisterer. |

> Efter første login skal du ændre admin-adgangskoden fra siden **Kontoindstillinger** i webgrænsefladen.

---

## Porte

Kontroller, hvilke hostporte applikationen binder til.

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `APP_PORT` | `8080` | Hostport til hoved-webgrænsefladen. Skift dette, hvis port 8080 allerede er i brug på din server. |
| `SHINY_PORT` | `3838` | Hostport til Shiny-analyseserveren. |

---

## Kørselsindstillinger

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `RUN_ENV` | `prod` | Kørselsindstillinger. Brug `prod` til produktionsimplementeringer, `dev` til lokal udvikling. |
| `RUN_MODE` | `admin` | Containerrolle. `admin` kører den fulde stak (web + kø + cron). `worker` kører kun baggrundsbehandling (til horisontal skalering). |
| `TZ` | `Asia/Ho_Chi_Minh` | Serverens tidszone. Påvirker logstemplar, cron-skemaer og datovisning. Brug et [TZ-databasenavn](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (f.eks. `UTC`, `America/New_York`, `Europe/London`). |
| `LOG_LEVEL` | `info` | Applikationslogomfang. Valgmuligheder: `debug`, `info`, `warning`, `error`. |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | Præfiks anvendt på alle Docker-container- og volumeNavne. Skift dette, når du kører flere rtCloud-instanser på samme host. |
| `RESTART_POLICY` | `unless-stopped` | Docker-containerens genstartsadfærd. Valgmuligheder: `no`, `always`, `on-failure`, `unless-stopped`. |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | Docker-image der bruges. Skift tagget for at fastlåse en specifik version. |
| `REQUIRE_LICENSE` | `false` | Aktivér licensnøglevalidering ved opstart. Kontakt RTA for licensoplysninger. |

---

## Sikkerhed

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `CSRF_VALIDATION_ENABLED` | `true` | Aktivér CSRF-tokenvalidering. Hold dette `true` i produktion. Sæt til `false` kun i lokal udvikling, hvis du oplever `400 CSRF-token kunne ikke bekræftes`-fejl. |
| `GII_ENABLED` | `false` | Aktivér Yii-frameworkets kodegeneratorværktøj. **Aktivér aldrig i produktion.** |

---

## SSO — Indlejret Keycloak

Aktivér den medfølgende Keycloak-container til fuldt udstyret virksomheds-SSO. Kræver et domæne med HTTPS.

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `EMBED_KEYCLOAK` | `false` | Sæt til `true` for at starte den indlejrede Keycloak-container. Aktiverer Docker Compose-profilen `embed-keycloak`. |
| `KEYCLOAK_URL` | — | Fuld URL til Keycloak-serveren (f.eks. `https://rtcloud.example.com/auth`). |
| `KEYCLOAK_REALM` | — | Keycloak realm-navn (f.eks. `rtsurvey`). |
| `KEYCLOAK_CLIENT_ID` | — | Keycloak-klient-ID for rtCloud-applikationen. |
| `KEYCLOAK_CLIENT_SECRET` | — | Keycloak-klienthemmelighed. Generér dette fra Keycloak-administratorkonsollen. |
| `KEYCLOAK_ADMIN_USER` | `admin` | Keycloak-administratorbrugernavn. |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Keycloak-administratoradgangskode. |
| `KEYCLOAK_DB` | `keycloak` | Databasenavn til Keycloak. Oprettes automatisk ved første opstart. |
| `KEYCLOAK_DB_USER` | `keycloak` | Databasebruger til Keycloak. |
| `KEYCLOAK_DB_PASSWORD` | — | Databaseadgangskode til Keycloak-brugeren. |
| `KC_HOSTNAME` | — | Keycloak frontend-URL (f.eks. `https://rtcloud.example.com/auth`). |
| `KC_HOSTNAME_STRICT` | `false` | Håndhæv strengt værtsnavn-matching. Sæt til `true` i produktion med et fast domæne. |

Se [SSO-godkendelse](sso-authentication#embedded-keycloak) for den komplette opsætningsvejledning.

---

## SSO — Ekstern OIDC-udbyder

Forbind til en eksisterende OIDC-kompatibel identitetsudbyder (Supabase, Auth0, Authentik, Okta osv.).

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `OIDC_ISSUER_URL` | — | OIDC-udsteder-opdagelses-URL (f.eks. `https://accounts.google.com`). |
| `OIDC_CLIENT_ID` | — | Klient-ID registreret hos din identitetsudbyder. |
| `OIDC_CLIENT_SECRET` | — | Klienthemmelighed fra din identitetsudbyder. |
| `OIDC_SCOPE` | `openid profile email` | Mellemrumsadskilt liste over OIDC-scopes der anmodes om. |
| `OIDC_REDIRECT_URI` | — | Callback-URL til webappen (f.eks. `https://rtcloud.example.com/auth/callback`). |
| `OIDC_MOBILE_CLIENT_ID` | — | Separat klient-ID til rtSurvey-mobilappen. |
| `OIDC_MOBILE_REDIRECT_URI` | — | Mobilappens callback-URI (f.eks. `vn.rta.rtsurvey.auth://callback`). |
| `OPEN_REGISTRATION` | `false` | Opret automatisk rtCloud-konti til brugere, der første gang godkendes via OIDC. |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | Tilsidesæt godkendelsesendpunkt-URL (lad stå tom for at bruge opdagelse). |
| `OIDC_TOKEN_ENDPOINT` | — | Tilsidesæt token-endpunkt-URL (lad stå tom for at bruge opdagelse). |
| `OIDC_USERINFO_ENDPOINT` | — | Tilsidesæt brugerinfo-endpunkt-URL (lad stå tom for at bruge opdagelse). |

---

## SSO — Azure Active Directory

| Variabel | Beskrivelse |
|----------|-------------|
| `AZURE_CLIENT_ID` | Azure AD-applikations(klient)-ID. |
| `AZURE_TENANT_ID` | Azure AD-mappe(lejer)-ID. |

---

## Valgfrie integrationer

### Stata

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `STATA_ENABLED` | `false` | Aktivér Stata statistisk software-integration til dataanalyse. |
| `STATA_BIN_PATH` | `/usr/bin/stata` | Absolut sti til Stata-binærfilen inde i containeren. |

### Elasticsearch

| Variabel | Beskrivelse |
|----------|-------------|
| `ES_HOST` | Elasticsearch-vært (f.eks. `http://elasticsearch:9200`). |
| `ES_PORT` | Elasticsearch-port. |

### Matomo Analytics

| Variabel | Beskrivelse |
|----------|-------------|
| `PIWIK_URL` | Matomo (Piwik) server-URL. |
| `PIWIK_ID` | Matomo websteds-ID. |
| `PIWIK_SECRET` | Matomo godkendelsestoken. |

### OpenCPU (R-beregning)

| Variabel | Beskrivelse |
|----------|-------------|
| `OCPU_HOST` | OpenCPU server-URL til R-baseret statistisk beregning. |

### RtBox-integration

| Variabel | Beskrivelse |
|----------|-------------|
| `RTBOX_HOST` | RtBox-tjenestevært-URL. |
| `RTBOX_USER_API` | RtBox bruger-API-nøgle. |
| `RTBOX_BASIC_AUTH` | Grundlæggende godkendelsesoplysninger til RtBox. |

### Matrix-beskedtjeneste

| Variabel | Beskrivelse |
|----------|-------------|
| `MATRIX_HOMESERVER_HOST` | Matrix-hjemmeservervært. |
| `MATRIX_HOMESERVER_PORT` | Matrix-hjemmeserverport. |

---

## Datavolumener

Alle applikationsdata er lagret i navngivne Docker-volumener. Volumener oprettes automatisk ved første opstart og bevares på tværs af containergenstart og -opdateringer.

| Volumen | Monteringspunkt | Indhold |
|--------|-------------|----------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | MySQL-databasefiler |
| `rtcloud_uploads` | `…/uploads` | Filer uploadet af undersøgelsesrespondenter |
| `rtcloud_audios` | `…/audios` | Lydoptagelser |
| `rtcloud_downloads` | `…/downloads` | Genererede eksportfiler |
| `rtcloud_gallery` | `…/gallery` | Galleribilleder |
| `rtcloud_voicemail` | `…/voicemail` | Voicemail-optagelser |
| `rtcloud_analytics` | `…/analytics` | Analysedata |
| `rtcloud_aggregate` | `…/aggregate` | Aggregerede undersøgelsesresultater |
| `rtcloud_converter` | `…/converter` | Datakonverteringsoutput |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | Shiny Server R-scripts |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Shiny Server-logs |
| `rtcloud_assets` | `…/assets` | Webaktiver (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | Applikationens runtime-cache |
| `rtcloud_cache` | `…/cache` | Applikationscache |
| `rtcloud_tmp` | `…/tmp` | Midlertidige filer |

Volumennavne er præfikset af værdien af `COMPOSE_PROJECT_NAME` (standard: `rtcloud`).

Vis alle volumener for din implementering:

```bash
docker volume ls | grep rtcloud
```
