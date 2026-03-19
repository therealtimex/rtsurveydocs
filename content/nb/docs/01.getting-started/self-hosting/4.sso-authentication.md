---
weight: 4
title: "SSO-autentisering"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Konfigurer Single Sign-On for selvdriftet rtCloud med innebygd Keycloak, en ekstern OIDC-leverandør eller Azure Active Directory."
---

rtCloud støtter tre tilnærminger for Single Sign-On (SSO):

| Alternativ | Best for |
|--------|----------|
| [Innebygd Keycloak](#embedded-keycloak) | Organisasjoner som ønsker en fullstendig selvstendig SSO-server medfølgende rtCloud |
| [Ekstern OIDC-leverandør](#external-oidc-provider) | Organisasjoner som allerede kjører en identitetsleverandør (Auth0, Authentik, Okta, Supabase, osv.) |
| [Azure Active Directory](#azure-active-directory) | Organisasjoner som bruker Microsoft 365 eller Azure AD |

Uten SSO konfigurert logger brukere inn med lokale rtCloud-kontoer administrert via adminpanelet.

---

## Innebygd Keycloak {#embedded-keycloak}

Distribusjonen inkluderer en valgfri Keycloak-container som kjører ved siden av rtCloud. Keycloak er forhåndskonfigurert med et rtSurvey realm og klar til bruk.

### Krav

- Et domenenavn med HTTPS (Keycloak krever HTTPS i produksjon)
- Minst 4 GB RAM på serveren (Keycloak legger til ~512 MB minnebruk)

### Oppsett

**1. Konfigurer miljøvariabler i `.env`:**

```dotenv
# Aktiver den innebygde Keycloak-containeren
EMBED_KEYCLOAK=true

# Keycloak URL-er — bruk ditt faktiske domene
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Realm- og klientinnstillinger (samsvar med importert realm JSON)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Keycloak-adminlegitimasjon
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Keycloak-database (opprettes automatisk)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Port Keycloak lytter på (vertssiden, proxyet av Nginx)
KEYCLOAK_PORT=8091
```

**2. Start med den innebygde Keycloak-profilen:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Kontroller at Keycloak er sunn:**

```bash
docker compose -f docker-compose.production.yml ps
```

`rtcloud-keycloak`-containeren bør vise `Up (healthy)` etter 2–3 minutter.

**4. Åpne Keycloak admin-konsollen:**

```
https://rtcloud.example.com/auth/admin
```

Logg inn med `KEYCLOAK_ADMIN_USER` og `KEYCLOAK_ADMIN_PASSWORD`.

### Hva er forhåndskonfigurert

Den innebygde Keycloak starter med et forhåndsimportert `rtsurvey`-realm som inkluderer:

- Klientkonfigurasjon for nettapplikasjonen
- Standardbrukerroller (`admin`, `project_manager`, `enumerator`, `analyst`)
- Økt- og tokeninnstillinger optimalisert for rtSurvey

Du kan legge til brukere direkte i Keycloak admin-konsollen eller koble Keycloak til en oppstrøms identitetsleverandør (LDAP, SAML).

### Nginx-ruting

Når du bruker skydistribusjonsskriptene, er Nginx konfigurert til å proxy begge tjenester:

| Sti | Bakstjeneste |
|------|---------|
| `/` | rtCloud-app på `127.0.0.1:8080` |
| `/auth/` | Keycloak på `127.0.0.1:8090` |

---

## Ekstern OIDC-leverandør {#external-oidc-provider}

Koble rtCloud til en hvilken som helst OpenID Connect-kompatibel identitetsleverandør. Denne tilnærmingen krever ikke Keycloak-containeren.

### Støttede leverandører

Enhver OIDC-kompatibel leverandør fungerer, inkludert:
- Authentik
- Auth0
- Okta
- Keycloak (ekstern instans)
- Supabase
- Google (for Google Workspace-organisasjoner)
- GitHub (via OAuth-apper med OIDC-utvidelse)

### Oppsett

**1. Registrer rtCloud som en OIDC-klient hos identitetsleverandøren.**

Du trenger:
- En **klient-ID** og **klienthemmelighet**
- Å registrere **redirect URI**: `https://rtcloud.example.com/auth/callback`
- For mobilappstøtte, registrer også: `vn.rta.rtsurvey.auth://callback`

**2. Konfigurer miljøvariabler i `.env`:**

```dotenv
# OIDC-oppdagelsesadresse (leverandørspesifikk — sjekk IdP-dokumentasjonen)
OIDC_ISSUER_URL=https://your-identity-provider.com

# Klientlegitimasjon fra identitetsleverandøren
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# Omfang som skal be om (openid, profile og email er vanligvis tilstrekkelig)
OIDC_SCOPE=openid profile email

# Redirect URI registrert hos identitetsleverandøren
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Valgfritt: separat mobilappklient
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Sett til true for automatisk å opprette rtCloud-kontoer for nye OIDC-brukere
OPEN_REGISTRATION=false
```

**3. Start app-containeren på nytt for å bruke endringene:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Automatisk klargjøring av brukere

Når `OPEN_REGISTRATION=true`, oppretter rtCloud automatisk en lokal konto første gang en bruker logger inn via OIDC. Kontoen fylles med brukerens navn og e-post fra ID-tokenet.

Når `OPEN_REGISTRATION=false` (standard), må en rtCloud-administrator opprette brukerkontoen først, og OIDC-identiteten kobles ved første innlogging.

### Egendefinerte endepunkter

Hvis leverandøren ikke støtter OIDC-oppdagelse (`.well-known/openid-configuration`), kan du angi endepunkter manuelt:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory {#azure-active-directory}

Integrer rtCloud med organisasjonens Microsoft Azure AD-leietaker.

### Oppsett

**1. Registrer en ny app i [Azure Portal](https://portal.azure.com):**

   - Gå til **Azure Active Directory** → **App-registreringer** → **Ny registrering**
   - Navn: `rtCloud`
   - Redirect URI: `https://rtcloud.example.com/auth/callback` (Netttype)
   - Etter opprettelse, noter **Applikasjons-(klient-)ID** og **Katalog-(leietaker-)ID**
   - Under **Sertifikater og hemmeligheter**, opprett en ny klienthemmelighet

**2. Konfigurer miljøvariabler i `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Start app-containeren på nytt:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Brukere i Azure AD-leietakeren kan nå logge inn på rtCloud med Microsoft-legitimasjonen sin.

---

## Deaktivere SSO

For å gå tilbake til lokal autentisering, fjern eller kommenter ut alle SSO-relaterte variabler fra `.env`, og start deretter app-containeren på nytt:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Hvis du brukte innebygd Keycloak, stopp den ved å utelate `--profile embed-keycloak`-flagget og kjøre `docker compose down` etterfulgt av `up -d` uten profilen.
