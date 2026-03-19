---
weight: 2
title: "Konfigurointiviite"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "Täydellinen viite kaikille ympäristömuuttujille, joita käytetään itse isännöidyn rtCloud-käyttöönoton konfigurointiin."
---

Kaikki konfigurointi tehdään ympäristömuuttujien kautta käyttöönottohakemistosi juuressa olevassa `.env`-tiedostossa. Docker Compose lukee tämän tiedoston automaattisesti — `--env-file`-lippua ei tarvita.

**Pakollisiksi** merkityt muuttujat on asetettava ennen konttien käynnistämistä. Kaikki muut ovat valinnaisia oletusarvoillaan.

---

## Projekti

Nämä muuttujat määrittävät rtCloud-instanssisi identiteetin ja pääsypisteen.

| Muuttuja | Oletus | Pakollinen | Kuvaus |
|----------|---------|----------|-------------|
| `PROJECT_ID` | — | **Kyllä** | Tämän käyttöönoton yksilöllinen tunniste. Ei välilyöntejä tai erikoismerkkejä. Käytetään sisäisen nimeämisen etuliitteenä. |
| `PROJECT_URL` | — | **Kyllä** | Verkkotunnus tai IP-osoite, josta käyttäjät pääsevät sovellukseen (esim. `rtcloud.example.com` tai `192.168.1.100`). |
| `PROJECT_TYPE` | `rtsurvey` | Ei | Aktivoitava alustavariantti. Vaihtoehdot: `rtwork`, `rtsurvey`, `rthome`. |
| `PROJECT_PORT` | `80` | Ei | Portti, jota sovellus kuuntelee kontin sisällä. Älä muuta, ellet tiedä mitä teet. |
| `HTTP_PROTOCOL` | `https` | Ei | Sisäisten URL-osoitteiden rakentamiseen käytetty protokolla. Aseta `http`, jos et käytä SSL:ää. |

---

## Tietokanta

MySQL-yhteyden tunnistetiedot. Tietokantaa hallitsee automaattisesti MySQL-kontti — sinun tarvitsee vain asettaa vahvat salasanat.

| Muuttuja | Oletus | Pakollinen | Kuvaus |
|----------|---------|----------|-------------|
| `MYSQL_DATABASE` | `smartsurvey` | Ei | Sovellustietokannan nimi. |
| `MYSQL_USER` | `smartsurvey` | Ei | MySQL-käyttäjä sovellukselle. |
| `MYSQL_PASSWORD` | — | **Kyllä** | `MYSQL_USER`-käyttäjän salasana. Käytä vahvaa, yksilöllistä arvoa. |
| `MYSQL_ROOT_PASSWORD` | — | **Kyllä** | MySQL:n root-salasana. Vaaditaan tietokannan alustukseen ja ylläpito-operaatioihin. |
| `MYSQL_HOST` | `mysql` | Ei | MySQL-isäntänimi. Käytä oletusarvoa, ellet yhdistä ulkoiseen tietokantaan. |
| `MYSQL_PORT` | `3306` | Ei | MySQL-portti. |

---

## Järjestelmänvalvojatili

Järjestelmänvalvojatili luodaan automaattisesti uuden tietokannan ensimmäisellä käynnistyksellä.

| Muuttuja | Oletus | Pakollinen | Kuvaus |
|----------|---------|----------|-------------|
| `ADMIN_PASSWORD` | `admin` | **Kyllä** | Sisäänrakennetun `admin`-käyttäjän salasana. Aseta tämä ennen ensimmäistä käynnistystä. Ei vaikuta, jos tietokanta on jo olemassa. |

> Ensimmäisen kirjautumisen jälkeen vaihda järjestelmänvalvojan salasana verkkokäyttöliittymän **Tiliasetukset**-sivulta.

---

## Portit

Hallitse, mihin isäntäportteihin sovellus sitoutuu.

| Muuttuja | Oletus | Kuvaus |
|----------|---------|-------------|
| `APP_PORT` | `8080` | Isäntäportti pääverkkokäyttöliittymälle. Muuta, jos portti 8080 on jo käytössä palvelimellasi. |
| `SHINY_PORT` | `3838` | Isäntäportti Shiny-analytiikkapalvelimelle. |

---

## Suoritusympäristö

| Muuttuja | Oletus | Kuvaus |
|----------|---------|-------------|
| `RUN_ENV` | `prod` | Suoritusympäristö. Käytä `prod` tuotantokäyttöönotoissa, `dev` paikallisessa kehityksessä. |
| `RUN_MODE` | `admin` | Konttirooli. `admin` ajaa koko pinon (verkko + jono + cron). `worker` ajaa vain taustatyöskentelyn (horisontaaliseen skaalaukseen). |
| `TZ` | `Asia/Ho_Chi_Minh` | Palvelinaikavyöhyke. Vaikuttaa lokien aikaleimioihin, cron-aikatauluihin ja päivämäärän näyttöön. Käytä [TZ-tietokannan nimeä](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (esim. `UTC`, `America/New_York`, `Europe/London`). |
| `LOG_LEVEL` | `info` | Sovelluksen lokin yksityiskohtaisuus. Vaihtoehdot: `debug`, `info`, `warning`, `error`. |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | Kaikkiin Docker-konttien ja -taltioiden nimiin lisätty etuliite. Muuta tätä, kun ajat useita rtCloud-instansseja samalla isännällä. |
| `RESTART_POLICY` | `unless-stopped` | Docker-konttien uudelleenkäynnistyksen toiminta. Vaihtoehdot: `no`, `always`, `on-failure`, `unless-stopped`. |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | Käytettävä Docker-kuva. Muuta tunnistetta kiinnittääksesi tiettyyn versioon. |
| `REQUIRE_LICENSE` | `false` | Ota lisenssitunnuksen vahvistus käyttöön käynnistyksen yhteydessä. Ota yhteyttä RTA:han lisenssitietoja varten. |

---

## Turvallisuus

| Muuttuja | Oletus | Kuvaus |
|----------|---------|-------------|
| `CSRF_VALIDATION_ENABLED` | `true` | Ota CSRF-tunnuksen vahvistus käyttöön. Pidä tämä `true` tuotannossa. Aseta `false` vain paikallisessa kehityksessä, jos kohtaat `400 CSRF-tunnusta ei voitu vahvistaa` -virheitä. |
| `GII_ENABLED` | `false` | Ota Yii-kehyksen koodigeneroinnin työkalu käyttöön. **Älä koskaan ota käyttöön tuotannossa.** |

---

## SSO — Upotettu Keycloak

Ota käyttöön pakattu Keycloak-kontti täysin toimivaa yritysten SSO:ta varten. Vaatii verkkotunnuksen HTTPS:llä.

| Muuttuja | Oletus | Kuvaus |
|----------|---------|-------------|
| `EMBED_KEYCLOAK` | `false` | Aseta `true` käynnistääksesi upotetun Keycloak-kontin. Aktivoi `embed-keycloak` Docker Compose -profiilin. |
| `KEYCLOAK_URL` | — | Keycloak-palvelimen täydellinen URL (esim. `https://rtcloud.example.com/auth`). |
| `KEYCLOAK_REALM` | — | Keycloak-realm-nimi (esim. `rtsurvey`). |
| `KEYCLOAK_CLIENT_ID` | — | Keycloak-asiakastunnus rtCloud-sovellukselle. |
| `KEYCLOAK_CLIENT_SECRET` | — | Keycloak-asiakassalaisuus. Luo tämä Keycloak-hallintakonsolista. |
| `KEYCLOAK_ADMIN_USER` | `admin` | Keycloak-järjestelmänvalvojan käyttäjätunnus. |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Keycloak-järjestelmänvalvojan salasana. |
| `KEYCLOAK_DB` | `keycloak` | Keycloakin tietokannan nimi. Luodaan automaattisesti ensimmäisellä käynnistyksellä. |
| `KEYCLOAK_DB_USER` | `keycloak` | Tietokannan käyttäjä Keycloakille. |
| `KEYCLOAK_DB_PASSWORD` | — | Tietokannan salasana Keycloak-käyttäjälle. |
| `KC_HOSTNAME` | — | Keycloakin käyttöliittymän URL (esim. `https://rtcloud.example.com/auth`). |
| `KC_HOSTNAME_STRICT` | `false` | Pakota tiukka isäntänimen tarkistus. Aseta `true` tuotannossa kiinteällä verkkotunnuksella. |

Katso täydellinen asennusopas kohdasta [SSO-todennus](sso-authentication#embedded-keycloak).

---

## SSO — Ulkoinen OIDC-tarjoaja

Yhdistä olemassa olevaan OIDC-yhteensopivaan identiteetintarjoajaan (Supabase, Auth0, Authentik, Okta jne.).

| Muuttuja | Oletus | Kuvaus |
|----------|---------|-------------|
| `OIDC_ISSUER_URL` | — | OIDC-myöntäjän löytö-URL (esim. `https://accounts.google.com`). |
| `OIDC_CLIENT_ID` | — | Identiteetintarjoajaan rekisteröity asiakastunnus. |
| `OIDC_CLIENT_SECRET` | — | Asiakassalaisuus identiteetintarjoajaltasi. |
| `OIDC_SCOPE` | `openid profile email` | Välilyönnillä erotettu luettelo pyydettävistä OIDC-laajuuksista. |
| `OIDC_REDIRECT_URI` | — | Verkkosovelluksen takaisinsoitto-URL (esim. `https://rtcloud.example.com/auth/callback`). |
| `OIDC_MOBILE_CLIENT_ID` | — | Erillinen asiakastunnus rtSurvey-mobiilisovellukselle. |
| `OIDC_MOBILE_REDIRECT_URI` | — | Mobiilisovelluksen takaisinsoitto-URI (esim. `vn.rta.rtsurvey.auth://callback`). |
| `OPEN_REGISTRATION` | `false` | Luo automaattisesti rtCloud-tilit käyttäjille, jotka todentautuvat OIDC:n kautta ensimmäistä kertaa. |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | Ohita valtuutuspisteen URL (jätä tyhjäksi käyttääksesi löytöä). |
| `OIDC_TOKEN_ENDPOINT` | — | Ohita tunnistepisteen URL (jätä tyhjäksi käyttääksesi löytöä). |
| `OIDC_USERINFO_ENDPOINT` | — | Ohita käyttäjätietopisteen URL (jätä tyhjäksi käyttääksesi löytöä). |

---

## SSO — Azure Active Directory

| Muuttuja | Kuvaus |
|----------|-------------|
| `AZURE_CLIENT_ID` | Azure AD -sovelluksen (asiakas) tunnus. |
| `AZURE_TENANT_ID` | Azure AD -hakemiston (vuokralainen) tunnus. |

---

## Valinnaiset integraatiot

### Stata

| Muuttuja | Oletus | Kuvaus |
|----------|---------|-------------|
| `STATA_ENABLED` | `false` | Ota Stata-tilastoohjelmiston integraatio käyttöön data-analyysia varten. |
| `STATA_BIN_PATH` | `/usr/bin/stata` | Absoluuttinen polku Stata-binääriin kontin sisällä. |

### Elasticsearch

| Muuttuja | Kuvaus |
|----------|-------------|
| `ES_HOST` | Elasticsearch-isäntä (esim. `http://elasticsearch:9200`). |
| `ES_PORT` | Elasticsearch-portti. |

### Matomo Analytics

| Muuttuja | Kuvaus |
|----------|-------------|
| `PIWIK_URL` | Matomo (Piwik) -palvelimen URL. |
| `PIWIK_ID` | Matomo-sivuston tunnus. |
| `PIWIK_SECRET` | Matomo-todennustunnus. |

### OpenCPU (R-laskenta)

| Muuttuja | Kuvaus |
|----------|-------------|
| `OCPU_HOST` | OpenCPU-palvelimen URL R-pohjaiseen tilastolliseen laskentaan. |

### RtBox-integraatio

| Muuttuja | Kuvaus |
|----------|-------------|
| `RTBOX_HOST` | RtBox-palvelun isäntä-URL. |
| `RTBOX_USER_API` | RtBox-käyttäjän API-avain. |
| `RTBOX_BASIC_AUTH` | Perustodennus-tunnistetiedot RtBoxille. |

### Matrix-viestintä

| Muuttuja | Kuvaus |
|----------|-------------|
| `MATRIX_HOMESERVER_HOST` | Matrix-kotipalvelimen isäntä. |
| `MATRIX_HOMESERVER_PORT` | Matrix-kotipalvelimen portti. |

---

## Datataltiot

Kaikki sovellusdata tallennetaan nimettyihin Docker-taltioihin. Taltiot luodaan automaattisesti ensimmäisellä käynnistyksellä ja säilyvät konttien uudelleenkäynnistyksissä ja päivityksissä.

| Taltio | Liitospiste | Sisältö |
|--------|-------------|----------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | MySQL-tietokantatiedostot |
| `rtcloud_uploads` | `…/uploads` | Kyselyn vastaajien lataamat tiedostot |
| `rtcloud_audios` | `…/audios` | Ääninauhotteet |
| `rtcloud_downloads` | `…/downloads` | Generoidut vientitiedostot |
| `rtcloud_gallery` | `…/gallery` | Gallerian kuvat |
| `rtcloud_voicemail` | `…/voicemail` | Puhepostinauhotteet |
| `rtcloud_analytics` | `…/analytics` | Analytiikkadata |
| `rtcloud_aggregate` | `…/aggregate` | Kootut kyselytulokset |
| `rtcloud_converter` | `…/converter` | Datamuunnostuotokset |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | Shiny-palvelimen R-skriptit |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Shiny-palvelimen lokit |
| `rtcloud_assets` | `…/assets` | Verkkoresurssit (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | Sovelluksen suoritusaikainen välimuisti |
| `rtcloud_cache` | `…/cache` | Sovelluksen välimuisti |
| `rtcloud_tmp` | `…/tmp` | Väliaikaiset tiedostot |

Taltioiden nimien etuliite on `COMPOSE_PROJECT_NAME`-muuttujan arvo (oletus: `rtcloud`).

Listaa kaikki käyttöönottosi taltiot:

```bash
docker volume ls | grep rtcloud
```
