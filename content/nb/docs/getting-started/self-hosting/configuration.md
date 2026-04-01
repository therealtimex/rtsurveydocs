---
weight: 2
title: "Konfigurasjonsreferanse"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "Fullstendig referanse for alle miljøvariabler som brukes til å konfigurere en selvdriftet rtCloud-distribusjon."
---

All konfigurasjon gjøres gjennom miljøvariabler i `.env`-filen i roten av distribusjonskatalogen. Docker Compose leser denne filen automatisk — ingen `--env-file`-flagg er nødvendig.

Variabler merket **påkrevd** må angis før containerne startes. Alle andre har standardverdier og er valgfrie.

---

## Prosjekt

Disse variablene definerer identiteten og tilgangspunktet til rtCloud-instansen din.

| Variabel | Standard | Påkrevd | Beskrivelse |
|----------|---------|----------|-------------|
| `PROJECT_ID` | — | **Ja** | Unik identifikator for denne distribusjonen. Ingen mellomrom eller spesialtegn. Brukes som prefiks for intern navngiving. |
| `PROJECT_URL` | — | **Ja** | Domenenavn eller IP-adresse der brukere får tilgang til appen (f.eks. `rtcloud.example.com` eller `192.168.1.100`). |
| `PROJECT_TYPE` | `rtsurvey` | Nei | Plattformvariant som skal aktiveres. Alternativer: `rtwork`, `rtsurvey`, `rthome`. |
| `PROJECT_PORT` | `80` | Nei | Port applikasjonen lytter på inni containeren. Ikke endre med mindre du vet hva du gjør. |
| `HTTP_PROTOCOL` | `https` | Nei | Protokoll som brukes til å konstruere interne URL-er. Sett til `http` hvis du ikke bruker SSL. |

---

## Database

MySQL-tilkoblingslegitimasjon. Databasen administreres automatisk av MySQL-containeren — du trenger bare å angi sterke passord.

| Variabel | Standard | Påkrevd | Beskrivelse |
|----------|---------|----------|-------------|
| `MYSQL_DATABASE` | `smartsurvey` | Nei | Navn på applikasjonsdatabasen. |
| `MYSQL_USER` | `smartsurvey` | Nei | MySQL-bruker for applikasjonen. |
| `MYSQL_PASSWORD` | — | **Ja** | Passord for `MYSQL_USER`. Bruk en sterk, unik verdi. |
| `MYSQL_ROOT_PASSWORD` | — | **Ja** | MySQL root-passord. Påkrevd for databaseinitialisering og adminoperasjoner. |
| `MYSQL_HOST` | `mysql` | Nei | MySQL-vertsnavn. Bruk standard med mindre du kobler til en ekstern database. |
| `MYSQL_PORT` | `3306` | Nei | MySQL-port. |

---

## Adminkonto

Adminkontoen opprettes automatisk ved første oppstart av en fersk database.

| Variabel | Standard | Påkrevd | Beskrivelse |
|----------|---------|----------|-------------|
| `ADMIN_PASSWORD` | `admin` | **Ja** | Passord for den innebygde `admin`-brukeren. Angi dette før første oppstart. Har ingen effekt hvis databasen allerede eksisterer. |

> Etter første innlogging, endre adminpassordet fra **Kontoinnstillinger**-siden i nettgrensesnittet.

---

## Porter

Kontroller hvilke vertsporter applikasjonen binder seg til.

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `APP_PORT` | `8080` | Vertsport for hoved-nettgrensesnittet. Endre dette hvis port 8080 allerede er i bruk på serveren. |
| `SHINY_PORT` | `3838` | Vertsport for Shiny-analyseserveren. |

---

## Kjøretid

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `RUN_ENV` | `prod` | Kjøretidsmiljø. Bruk `prod` for produksjonsdistribusjoner, `dev` for lokal utvikling. |
| `RUN_MODE` | `admin` | Containerrolle. `admin` kjører hele stabelen (nett + kø + cron). `worker` kjører kun bakgrunnsbehandling (for horisontal skalering). |
| `TZ` | `Asia/Ho_Chi_Minh` | Servertidssone. Påvirker logg-tidsstempler, cron-planer og datovisning. Bruk et [TZ-databasenavn](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (f.eks. `UTC`, `Europe/Oslo`). |
| `LOG_LEVEL` | `info` | Utførlighet for applikasjonslogger. Alternativer: `debug`, `info`, `warning`, `error`. |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | Prefiks brukt på alle Docker-container- og volumnavn. Endre dette ved kjøring av flere rtCloud-instanser på samme vert. |
| `RESTART_POLICY` | `unless-stopped` | Docker-containers omstartsatferd. Alternativer: `no`, `always`, `on-failure`, `unless-stopped`. |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | Docker-bilde som skal brukes. Endre taggen for å feste en bestemt versjon. |
| `REQUIRE_LICENSE` | `false` | Aktiver validering av lisensnøkkel ved oppstart. Kontakt RTA for lisensinformasjon. |

---

## Sikkerhet

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `CSRF_VALIDATION_ENABLED` | `true` | Aktiver CSRF-tokenvalidering. Hold denne på `true` i produksjon. Sett til `false` kun i lokal utvikling hvis du møter `400 CSRF token could not be verified`-feil. |
| `GII_ENABLED` | `false` | Aktiver Yii-rammeverkets kodegeneratorverktøy. **Aldri aktiver i produksjon.** |

---

## SSO — Innebygd Keycloak

Aktiver den medfølgende Keycloak-containeren for full-funksjon bedrifts-SSO. Krever et domene med HTTPS.

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `EMBED_KEYCLOAK` | `false` | Sett til `true` for å starte den innebygde Keycloak-containeren. Aktiverer `embed-keycloak` Docker Compose-profilen. |
| `KEYCLOAK_URL` | — | Full URL til Keycloak-serveren (f.eks. `https://rtcloud.example.com/auth`). |
| `KEYCLOAK_REALM` | — | Keycloak realm-navn (f.eks. `rtsurvey`). |
| `KEYCLOAK_CLIENT_ID` | — | Keycloak klient-ID for rtCloud-applikasjonen. |
| `KEYCLOAK_CLIENT_SECRET` | — | Keycloak klienthemmelighet. Generer denne fra Keycloak admin-konsollen. |
| `KEYCLOAK_ADMIN_USER` | `admin` | Keycloak-administratorbrukernavn. |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Keycloak-administratorpassord. |
| `KEYCLOAK_DB` | `keycloak` | Databasenavn for Keycloak. Opprettes automatisk ved første oppstart. |
| `KEYCLOAK_DB_USER` | `keycloak` | Databasebruker for Keycloak. |
| `KEYCLOAK_DB_PASSWORD` | — | Databasepassord for Keycloak-brukeren. |
| `KC_HOSTNAME` | — | Keycloak frontend-URL (f.eks. `https://rtcloud.example.com/auth`). |
| `KC_HOSTNAME_STRICT` | `false` | Håndhev strengt vertsnavn-samsvar. Sett til `true` i produksjon med et fast domene. |

Se [SSO-autentisering](sso-authentication#embedded-keycloak) for den fullstendige oppsettsveiledningen.

---

## SSO — Ekstern OIDC-leverandør

Koble til en eksisterende OIDC-kompatibel identitetsleverandør (Supabase, Auth0, Authentik, Okta, osv.).

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `OIDC_ISSUER_URL` | — | OIDC-utstedersoppdagings-URL (f.eks. `https://accounts.google.com`). |
| `OIDC_CLIENT_ID` | — | Klient-ID registrert hos identitetsleverandøren. |
| `OIDC_CLIENT_SECRET` | — | Klienthemmelighet fra identitetsleverandøren. |
| `OIDC_SCOPE` | `openid profile email` | Mellomrom-separert liste over OIDC-omfang som skal be om. |
| `OIDC_REDIRECT_URI` | — | Tilbakekallingsadresse for nettappen (f.eks. `https://rtcloud.example.com/auth/callback`). |
| `OIDC_MOBILE_CLIENT_ID` | — | Separat klient-ID for rtSurvey-mobilappen. |
| `OIDC_MOBILE_REDIRECT_URI` | — | Mobilappens tilbakekallingsadresse (f.eks. `vn.rta.rtsurvey.auth://callback`). |
| `OPEN_REGISTRATION` | `false` | Opprett automatisk rtCloud-kontoer for brukere som autentiserer via OIDC for første gang. |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | Overstyr autorisasjonsendepunkt-URL (la stå tomt for å bruke oppdagelse). |
| `OIDC_TOKEN_ENDPOINT` | — | Overstyr token-endepunkt-URL (la stå tomt for å bruke oppdagelse). |
| `OIDC_USERINFO_ENDPOINT` | — | Overstyr brukerinformasjons-endepunkt-URL (la stå tomt for å bruke oppdagelse). |

---

## SSO — Azure Active Directory

| Variabel | Beskrivelse |
|----------|-------------|
| `AZURE_CLIENT_ID` | Azure AD-applikasjons-(klient-)ID. |
| `AZURE_TENANT_ID` | Azure AD-katalog-(leietaker-)ID. |

---

## Valgfrie integrasjoner

### Stata

| Variabel | Standard | Beskrivelse |
|----------|---------|-------------|
| `STATA_ENABLED` | `false` | Aktiver Stata-statistikkprogramvareintegrasjon for dataanalyse. |
| `STATA_BIN_PATH` | `/usr/bin/stata` | Absolutt sti til Stata-binæren inni containeren. |

### Elasticsearch

| Variabel | Beskrivelse |
|----------|-------------|
| `ES_HOST` | Elasticsearch-vert (f.eks. `http://elasticsearch:9200`). |
| `ES_PORT` | Elasticsearch-port. |

### Matomo Analytics

| Variabel | Beskrivelse |
|----------|-------------|
| `PIWIK_URL` | Matomo (Piwik) server-URL. |
| `PIWIK_ID` | Matomo nettsted-ID. |
| `PIWIK_SECRET` | Matomo autentiseringstoken. |

### OpenCPU (R-beregning)

| Variabel | Beskrivelse |
|----------|-------------|
| `OCPU_HOST` | OpenCPU server-URL for R-basert statistisk beregning. |

### RtBox-integrasjon

| Variabel | Beskrivelse |
|----------|-------------|
| `RTBOX_HOST` | RtBox tjeneste-vert-URL. |
| `RTBOX_USER_API` | RtBox bruker-API-nøkkel. |
| `RTBOX_BASIC_AUTH` | Grunnleggende autentiseringslegitimasjon for RtBox. |

### Matrix-meldinger

| Variabel | Beskrivelse |
|----------|-------------|
| `MATRIX_HOMESERVER_HOST` | Matrix hjemserver-vert. |
| `MATRIX_HOMESERVER_PORT` | Matrix hjemserver-port. |

---

## Datavolumer

Alle applikasjonsdata lagres i navngitte Docker-volumer. Volumer opprettes automatisk ved første oppstart og vedvarer på tvers av containeromstarter og oppdateringer.

| Volum | Monteringspunkt | Innhold |
|--------|-------------|----------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | MySQL-databasefiler |
| `rtcloud_uploads` | `…/uploads` | Filer lastet opp av undersøkelsesrespondenter |
| `rtcloud_audios` | `…/audios` | Lydopptak |
| `rtcloud_downloads` | `…/downloads` | Genererte eksportfiler |
| `rtcloud_gallery` | `…/gallery` | Galleribilder |
| `rtcloud_voicemail` | `…/voicemail` | Talepostopptak |
| `rtcloud_analytics` | `…/analytics` | Analysedata |
| `rtcloud_aggregate` | `…/aggregate` | Aggregerte undersøkelsesresultater |
| `rtcloud_converter` | `…/converter` | Datakonverteringsutdata |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | Shiny server R-skript |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Shiny server-logger |
| `rtcloud_assets` | `…/assets` | Nettressurser (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | Applikasjonens kjøretidsbuffer |
| `rtcloud_cache` | `…/cache` | Applikasjonsbuffer |
| `rtcloud_tmp` | `…/tmp` | Midlertidige filer |

Volumnavn har prefikset fra verdien av `COMPOSE_PROJECT_NAME` (standard: `rtcloud`).

List alle volumer for distribusjonen din:

```bash
docker volume ls | grep rtcloud
```
