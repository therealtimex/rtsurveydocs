---
weight: 2
title: "Konfigurációs referencia"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "settings"
toc: true
description: "Az összes környezeti változó teljes referenciája, amelyek a saját üzemeltetésű rtCloud-telepítés konfigurálásához használhatók."
---

Minden konfiguráció a telepítési könyvtár gyökerében lévő `.env` fájlban lévő környezeti változókon keresztül történik. A Docker Compose automatikusan olvassa be ezt a fájlt — nincs szükség `--env-file` jelzőre.

A **kötelező** jelöléssel ellátott változókat a konténerek indítása előtt be kell állítani. A többinek alapértékei vannak, és opcionálisak.

---

## Projekt

Ezek a változók az rtCloud-példány identitását és hozzáférési pontját határozzák meg.

| Változó | Alapérték | Kötelező | Leírás |
|----------|---------|----------|-------------|
| `PROJECT_ID` | — | **Igen** | A telepítés egyedi azonosítója. Szóközök és különleges karakterek nélkül. Belső elnevezési előtagként használatos. |
| `PROJECT_URL` | — | **Igen** | Domainné vagy IP-cím, ahol a felhasználók elérik az alkalmazást (pl. `rtcloud.example.com` vagy `192.168.1.100`). |
| `PROJECT_TYPE` | `rtsurvey` | Nem | Aktiválandó platformváltozat. Lehetőségek: `rtwork`, `rtsurvey`, `rthome`. |
| `PROJECT_PORT` | `80` | Nem | A konténeren belül az alkalmazás által figyelt port. Ne változtassa meg, hacsak nem tudja, mit csinál. |
| `HTTP_PROTOCOL` | `https` | Nem | A belső URL-ek felépítéséhez használt protokoll. Állítsa `http`-re, ha nem használ SSL-t. |

---

## Adatbázis

MySQL-kapcsolati hitelesítő adatok. Az adatbázist automatikusan kezeli a MySQL-konténer — csak erős jelszavakat kell beállítania.

| Változó | Alapérték | Kötelező | Leírás |
|----------|---------|----------|-------------|
| `MYSQL_DATABASE` | `smartsurvey` | Nem | Az alkalmazás adatbázisának neve. |
| `MYSQL_USER` | `smartsurvey` | Nem | MySQL-felhasználó az alkalmazáshoz. |
| `MYSQL_PASSWORD` | — | **Igen** | A `MYSQL_USER` jelszava. Használjon erős, egyedi értéket. |
| `MYSQL_ROOT_PASSWORD` | — | **Igen** | MySQL root jelszó. Szükséges az adatbázis inicializálásához és a rendszergazdai műveletekhez. |
| `MYSQL_HOST` | `mysql` | Nem | MySQL-állomásnév. Használja az alapértéket, hacsak nem csatlakozik külső adatbázishoz. |
| `MYSQL_PORT` | `3306` | Nem | MySQL-port. |

---

## Rendszergazdai fiók

A rendszergazdai fiók automatikusan jön létre a friss adatbázis első indításakor.

| Változó | Alapérték | Kötelező | Leírás |
|----------|---------|----------|-------------|
| `ADMIN_PASSWORD` | `admin` | **Igen** | A beépített `admin` felhasználó jelszava. Az első indítás előtt állítsa be. Nincs hatása, ha az adatbázis már létezik. |

> Az első bejelentkezés után változtassa meg a rendszergazdai jelszót a webes felület **Fiókbeállítások** oldalán.

---

## Portok

Szabályozza, hogy az alkalmazás mely gazdaportokhoz kötődik.

| Változó | Alapérték | Leírás |
|----------|---------|-------------|
| `APP_PORT` | `8080` | Gazdaport a fő webes felülethez. Változtassa meg, ha a 8080-as port már használatban van a kiszolgálón. |
| `SHINY_PORT` | `3838` | Gazdaport a Shiny elemzési szerverhez. |

---

## Futtatókörnyezet

| Változó | Alapérték | Leírás |
|----------|---------|-------------|
| `RUN_ENV` | `prod` | Futtatókörnyezet. Éles telepítésekhez használja a `prod`-ot, helyi fejlesztéshez a `dev`-et. |
| `RUN_MODE` | `admin` | Konténer szerepkör. Az `admin` az összes összetevőt futtatja (web + sor + cron). A `worker` csak háttérfeldolgozást futtat (vízszintes skálázáshoz). |
| `TZ` | `Asia/Ho_Chi_Minh` | Kiszolgáló időzónája. Befolyásolja a napló időbélyegeit, a cron-ütemezéseket és a dátummegjelenítést. Használjon [TZ adatbázis nevet](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (pl. `UTC`, `America/New_York`, `Europe/London`). |
| `LOG_LEVEL` | `info` | Az alkalmazásnapló részletessége. Lehetőségek: `debug`, `info`, `warning`, `error`. |
| `COMPOSE_PROJECT_NAME` | `rtcloud` | Az összes Docker-konténer és kötet nevére alkalmazott előtag. Változtassa meg, ha ugyanazon a gazdagépen több rtCloud-példányt futtat. |
| `RESTART_POLICY` | `unless-stopped` | Docker-konténer újraindítási viselkedése. Lehetőségek: `no`, `always`, `on-failure`, `unless-stopped`. |
| `RTCLOUD_IMAGE` | `rtawebteam/rta-smartsurvey:survey-dockerize` | Használandó Docker-képfájl. Változtassa meg a címkét egy adott verzió rögzítéséhez. |
| `REQUIRE_LICENSE` | `false` | Licenckulcs-ellenőrzés engedélyezése az indításkor. A licencinformációkért forduljon az RTA-hoz. |

---

## Biztonság

| Változó | Alapérték | Leírás |
|----------|---------|-------------|
| `CSRF_VALIDATION_ENABLED` | `true` | CSRF-token ellenőrzés engedélyezése. Éles környezetben tartsa `true` értéken. Csak helyi fejlesztésnél állítsa `false`-ra, ha `400 CSRF token could not be verified` hibával találkozik. |
| `GII_ENABLED` | `false` | A Yii keretrendszer kódgenerátor eszközének engedélyezése. **Soha ne engedélyezze éles környezetben.** |

---

## SSO — Beágyazott Keycloak

Engedélyezze a csomagolt Keycloak-konténert a teljes funkcionalitású vállalati SSO-hoz. HTTPS-sel rendelkező domaint igényel.

| Változó | Alapérték | Leírás |
|----------|---------|-------------|
| `EMBED_KEYCLOAK` | `false` | A beágyazott Keycloak-konténer elindításához állítsa `true`-ra. Aktiválja az `embed-keycloak` Docker Compose profilt. |
| `KEYCLOAK_URL` | — | A Keycloak-szerver teljes URL-je (pl. `https://rtcloud.example.com/auth`). |
| `KEYCLOAK_REALM` | — | Keycloak realm neve (pl. `rtsurvey`). |
| `KEYCLOAK_CLIENT_ID` | — | Keycloak kliens azonosítója az rtCloud alkalmazáshoz. |
| `KEYCLOAK_CLIENT_SECRET` | — | Keycloak kliens titka. Generálja a Keycloak adminisztrátori konzolból. |
| `KEYCLOAK_ADMIN_USER` | `admin` | Keycloak adminisztrátori felhasználónév. |
| `KEYCLOAK_ADMIN_PASSWORD` | — | Keycloak adminisztrátori jelszó. |
| `KEYCLOAK_DB` | `keycloak` | A Keycloak adatbázisának neve. Az első indításkor automatikusan létrejön. |
| `KEYCLOAK_DB_USER` | `keycloak` | A Keycloak adatbázis-felhasználója. |
| `KEYCLOAK_DB_PASSWORD` | — | A Keycloak-felhasználó adatbázis-jelszava. |
| `KC_HOSTNAME` | — | Keycloak frontend URL (pl. `https://rtcloud.example.com/auth`). |
| `KC_HOSTNAME_STRICT` | `false` | Szigorú állomásnév-egyeztetés kényszerítése. Éles környezetben rögzített domainnel állítsa `true`-ra. |

A teljes beállítási útmutatóért tekintse meg az [SSO-hitelesítés](sso-authentication#embedded-keycloak) oldalt.

---

## SSO — Külső OIDC-szolgáltató

Csatlakoztasson egy meglévő OIDC-kompatibilis identitásszolgáltatóhoz (Supabase, Auth0, Authentik, Okta stb.).

| Változó | Alapérték | Leírás |
|----------|---------|-------------|
| `OIDC_ISSUER_URL` | — | OIDC kibocsátó felderítési URL-je (pl. `https://accounts.google.com`). |
| `OIDC_CLIENT_ID` | — | Az identitásszolgáltatónál regisztrált kliens azonosítója. |
| `OIDC_CLIENT_SECRET` | — | Az identitásszolgáltatótól kapott kliens titka. |
| `OIDC_SCOPE` | `openid profile email` | Szóközzel elválasztott OIDC hatókörök listája. |
| `OIDC_REDIRECT_URI` | — | A webalkalmazás visszahívási URL-je (pl. `https://rtcloud.example.com/auth/callback`). |
| `OIDC_MOBILE_CLIENT_ID` | — | Külön kliens azonosítója az rtSurvey mobilalkalmazáshoz. |
| `OIDC_MOBILE_REDIRECT_URI` | — | Mobilalkalmazás visszahívási URI-ja (pl. `vn.rta.rtsurvey.auth://callback`). |
| `OPEN_REGISTRATION` | `false` | rtCloud-fiókok automatikus létrehozása az OIDC-n keresztül először bejelentkező felhasználóknak. |
| `OIDC_AUTHORIZATION_ENDPOINT` | — | Az engedélyezési végpont URL-jének felülírása (hagyja üresen a felderítés használatához). |
| `OIDC_TOKEN_ENDPOINT` | — | A token-végpont URL-jének felülírása (hagyja üresen a felderítés használatához). |
| `OIDC_USERINFO_ENDPOINT` | — | A felhasználóinformáció-végpont URL-jének felülírása (hagyja üresen a felderítés használatához). |

---

## SSO — Azure Active Directory

| Változó | Leírás |
|----------|-------------|
| `AZURE_CLIENT_ID` | Azure AD alkalmazás (kliens) azonosítója. |
| `AZURE_TENANT_ID` | Azure AD könyvtár (bérlő) azonosítója. |

---

## Opcionális integrációk

### Stata

| Változó | Alapérték | Leírás |
|----------|---------|-------------|
| `STATA_ENABLED` | `false` | Stata statisztikai szoftver integrációjának engedélyezése az adatelemzéshez. |
| `STATA_BIN_PATH` | `/usr/bin/stata` | A Stata bináris fájl abszolút elérési útja a konténeren belül. |

### Elasticsearch

| Változó | Leírás |
|----------|-------------|
| `ES_HOST` | Elasticsearch-gazdagép (pl. `http://elasticsearch:9200`). |
| `ES_PORT` | Elasticsearch-port. |

### Matomo elemzés

| Változó | Leírás |
|----------|-------------|
| `PIWIK_URL` | Matomo (Piwik) szerver URL-je. |
| `PIWIK_ID` | Matomo webhely azonosítója. |
| `PIWIK_SECRET` | Matomo hitelesítési token. |

### OpenCPU (R számítás)

| Változó | Leírás |
|----------|-------------|
| `OCPU_HOST` | OpenCPU szerver URL-je R-alapú statisztikai számításokhoz. |

### RtBox integráció

| Változó | Leírás |
|----------|-------------|
| `RTBOX_HOST` | RtBox szolgáltatás gazdagép URL-je. |
| `RTBOX_USER_API` | RtBox felhasználói API-kulcs. |
| `RTBOX_BASIC_AUTH` | Alapszintű hitelesítési hitelesítő adatok az RtBox-hoz. |

### Matrix üzenetküldés

| Változó | Leírás |
|----------|-------------|
| `MATRIX_HOMESERVER_HOST` | Matrix homeserver gazdagép. |
| `MATRIX_HOMESERVER_PORT` | Matrix homeserver port. |

---

## Adatkötetek

Az összes alkalmazásadat elnevezett Docker-kötetekben tárolódik. A kötetek az első indításkor automatikusan létrejönnek, és a konténerek újraindítása és frissítése után is megmaradnak.

| Kötet | Csatlakozási pont | Tartalom |
|--------|-------------|----------|
| `rtcloud_mysql_data` | `/var/lib/mysql` | MySQL adatbázisfájlok |
| `rtcloud_uploads` | `…/uploads` | Felmérési válaszadók által feltöltött fájlok |
| `rtcloud_audios` | `…/audios` | Hangfelvételek |
| `rtcloud_downloads` | `…/downloads` | Generált exportfájlok |
| `rtcloud_gallery` | `…/gallery` | Galéria képei |
| `rtcloud_voicemail` | `…/voicemail` | Hangposta felvételei |
| `rtcloud_analytics` | `…/analytics` | Elemzési adatok |
| `rtcloud_aggregate` | `…/aggregate` | Összesített felmérési eredmények |
| `rtcloud_converter` | `…/converter` | Adatkonverziós kimenetek |
| `rtcloud_shiny_data` | `/srv/shiny-server/smartsurvey` | Shiny szerver R-szkriptjei |
| `rtcloud_shiny_logs` | `/var/log/shiny-server` | Shiny szerver naplói |
| `rtcloud_assets` | `…/assets` | Webes erőforrások (CSS, JS) |
| `rtcloud_runtime` | `…/protected/runtime` | Alkalmazás futásidejű gyorsítótára |
| `rtcloud_cache` | `…/cache` | Alkalmazás gyorsítótára |
| `rtcloud_tmp` | `…/tmp` | Ideiglenes fájlok |

A kötetnevek a `COMPOSE_PROJECT_NAME` értékével vannak előtagolva (alapértelmezett: `rtcloud`).

A telepítéshez tartozó összes kötet listázása:

```bash
docker volume ls | grep rtcloud
```
