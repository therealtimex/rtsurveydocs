---
weight: 4
title: "SSO-hitelesítés"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Egyszeri bejelentkezés (SSO) konfigurálása saját üzemeltetésű rtCloud-hoz beágyazott Keycloak, külső OIDC-szolgáltató vagy Azure Active Directory segítségével."
---

Az rtCloud háromféle megközelítést támogat az egyszeri bejelentkezéshez (SSO):

| Lehetőség | A legjobb |
|--------|----------|
| [Beágyazott Keycloak](#embedded-keycloak) | Szervezetek számára, amelyek teljesen önálló SSO-szervert szeretnének az rtCloud-hoz csatolva |
| [Külső OIDC-szolgáltató](#external-oidc-provider) | Szervezetek számára, amelyek már futtatnak identitásszolgáltatót (Auth0, Authentik, Okta, Supabase stb.) |
| [Azure Active Directory](#azure-active-directory) | Szervezetek számára, amelyek Microsoft 365-öt vagy Azure AD-t használnak |

SSO konfigurálása nélkül a felhasználók helyi rtCloud-fiókokkal jelentkeznek be, amelyeket az adminisztrátori panelen keresztül kezelnek.

---

## Beágyazott Keycloak {#embedded-keycloak}

A telepítés tartalmaz egy opcionális Keycloak-konténert, amely az rtCloud mellett fut. A Keycloak előre konfigurálva van egy rtSurvey realmmal és azonnal használható.

### Követelmények

- Domain neve HTTPS-sel (a Keycloak éles környezetben HTTPS-t igényel)
- Legalább 4 GB RAM a kiszolgálón (a Keycloak körülbelül 512 MB memóriát használ)

### Beállítás

**1. Konfigurálja a környezeti változókat a `.env` fájlban:**

```dotenv
# A beágyazott Keycloak-konténer engedélyezése
EMBED_KEYCLOAK=true

# Keycloak URL-ek — használja a tényleges domaint
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Realm és kliens beállítások (illeszkednek az importált realm JSON-hoz)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Keycloak rendszergazdai hitelesítő adatok
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Keycloak adatbázis (automatikusan létrejön)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Port, amelyen a Keycloak figyel (gazdagép oldalon, az Nginx proxiálja)
KEYCLOAK_PORT=8091
```

**2. Indítsa el a beágyazott Keycloak profillal:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Ellenőrizze, hogy a Keycloak egészséges-e:**

```bash
docker compose -f docker-compose.production.yml ps
```

Az `rtcloud-keycloak` konténernek 2–3 perc után `Up (healthy)` állapotot kell mutatnia.

**4. Érje el a Keycloak adminisztrátori konzolt:**

```
https://rtcloud.example.com/auth/admin
```

Jelentkezzen be a `KEYCLOAK_ADMIN_USER` és `KEYCLOAK_ADMIN_PASSWORD` hitelesítő adatokkal.

### Mi van előre konfigurálva

A beágyazott Keycloak egy előre importált `rtsurvey` realmmal indul, amely tartalmazza:

- Kliens konfigurációt a webalkalmazáshoz
- Alapértelmezett felhasználói szerepköröket (`admin`, `project_manager`, `enumerator`, `analyst`)
- Munkamenet- és tokenbeállításokat, amelyek az rtSurvey-hez vannak optimalizálva

Hozzáadhat felhasználókat közvetlenül a Keycloak adminisztrátori konzolban, vagy csatlakoztathatja a Keycloakot egy upstream identitásszolgáltatóhoz (LDAP, SAML).

### Nginx-útválasztás

A felhőtelepítési szkriptek használatakor az Nginx mindkét szolgáltatás proxyálásához van konfigurálva:

| Útvonal | Háttér |
|------|---------|
| `/` | rtCloud alkalmazás a `127.0.0.1:8080` porton |
| `/auth/` | Keycloak a `127.0.0.1:8090` porton |

---

## Külső OIDC-szolgáltató {#external-oidc-provider}

Csatlakoztassa az rtCloud-ot bármely OpenID Connect-kompatibilis identitásszolgáltatóhoz. Ez a megközelítés nem igényli a Keycloak-konténert.

### Támogatott szolgáltatók

Bármely OIDC-kompatibilis szolgáltató működik, beleértve:
- Authentik
- Auth0
- Okta
- Keycloak (külső példány)
- Supabase
- Google (Google Workspace szervezetek számára)
- GitHub (OIDC-bővítménnyel rendelkező OAuth-alkalmazásokon keresztül)

### Beállítás

**1. Regisztrálja az rtCloud-ot OIDC-kliensként az identitásszolgáltatójánál.**

A következőkre lesz szüksége:
- **Kliens azonosítóra** és **kliens titokra**
- A **redirect URI** regisztrálásához: `https://rtcloud.example.com/auth/callback`
- Mobilalkalmazás-támogatáshoz regisztrálja ezt is: `vn.rta.rtsurvey.auth://callback`

**2. Konfigurálja a környezeti változókat a `.env` fájlban:**

```dotenv
# OIDC felderítési URL (szolgáltatóspecifikus — ellenőrizze az IdP dokumentációját)
OIDC_ISSUER_URL=https://your-identity-provider.com

# Hitelesítő adatok az identitásszolgáltatótól
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# Kérendő hatókörök (az openid, profile és email általában elegendő)
OIDC_SCOPE=openid profile email

# Az identitásszolgáltatónál regisztrált redirect URI
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Opcionális: külön mobilalkalmazás kliens
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Állítsa true-ra az rtCloud-fiókok automatikus létrehozásához az új OIDC-felhasználóknak
OPEN_REGISTRATION=false
```

**3. Indítsa újra az alkalmazáskonténert a változtatások alkalmazásához:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Felhasználók automatikus kiosztása

Ha az `OPEN_REGISTRATION=true`, az rtCloud automatikusan létrehoz egy helyi fiókot, amikor egy felhasználó először jelentkezik be OIDC-n keresztül. A fiók az ID tokenből kerül feltöltésre a felhasználó nevével és e-mail-címével.

Ha az `OPEN_REGISTRATION=false` (alapértelmezett), egy rtCloud rendszergazdának először létre kell hoznia a felhasználói fiókot, és az OIDC-identitás az első bejelentkezéskor lesz összekapcsolva.

### Egyéni végpontok

Ha a szolgáltató nem támogatja az OIDC felderítést (`.well-known/openid-configuration`), manuálisan beállíthatja a végpontokat:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory {#azure-active-directory}

Integrálja az rtCloud-ot a szervezet Microsoft Azure AD bérlőjével.

### Beállítás

**1. Regisztráljon új alkalmazást az [Azure Portalon](https://portal.azure.com):**

   - Lépjen az **Azure Active Directory** → **App registrations** → **New registration** menüpontra
   - Név: `rtCloud`
   - Redirect URI: `https://rtcloud.example.com/auth/callback` (Web típus)
   - A létrehozás után jegyezze fel az **Application (client) ID** és **Directory (tenant) ID** értékeket
   - A **Certificates & secrets** alatt hozzon létre egy új kliens titkot

**2. Konfigurálja a környezeti változókat a `.env` fájlban:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Indítsa újra az alkalmazáskonténert:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Az Azure AD bérlő felhasználói mostantól be tudnak jelentkezni az rtCloud-ba Microsoft hitelesítő adataikkal.

---

## Az SSO letiltása

A helyi hitelesítésre való visszatéréshez távolítsa el vagy kommentálja ki az összes SSO-val kapcsolatos változót a `.env` fájlból, majd indítsa újra az alkalmazáskonténert:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Ha beágyazott Keycloakot használt, állítsa le az `--profile embed-keycloak` jelző elhagyásával, és futtassa a `docker compose down`, majd az `up -d` parancsot a profil nélkül.
