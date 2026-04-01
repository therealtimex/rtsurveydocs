---
weight: 4
title: "SSO-godkendelse"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Konfigurer Single Sign-On til selvhostet rtCloud ved hjælp af indlejret Keycloak, en ekstern OIDC-udbyder eller Azure Active Directory."
---

rtCloud understøtter tre tilgange til Single Sign-On (SSO):

| Valgmulighed | Bedst til |
|--------|----------|
| [Indlejret Keycloak](#embedded-keycloak) | Organisationer, der ønsker en fuldt selvstændig SSO-server bundlet med rtCloud |
| [Ekstern OIDC-udbyder](#external-oidc-provider) | Organisationer, der allerede kører en identitetsudbyder (Auth0, Authentik, Okta, Supabase osv.) |
| [Azure Active Directory](#azure-active-directory) | Organisationer, der bruger Microsoft 365 eller Azure AD |

Uden SSO konfigureret logger brugere ind med lokale rtCloud-konti administreret via adminpanelet.

---

## Indlejret Keycloak

Implementeringen inkluderer en valgfri Keycloak-container, der kører sideløbende med rtCloud. Keycloak er forudkonfigureret med et rtSurvey-realm og klar til brug.

### Krav

- Et domænenavn med HTTPS (Keycloak kræver HTTPS i produktion)
- Mindst 4 GB RAM på serveren (Keycloak tilføjer ~512 MB hukommelsesforbrug)

### Opsætning

**1. Konfigurer miljøvariabler i `.env`:**

```dotenv
# Aktivér den indlejrede Keycloak-container
EMBED_KEYCLOAK=true

# Keycloak-URL'er – brug dit faktiske domæne
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Realm- og klientindstillinger (match det importerede realm-JSON)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=din-klienthemmelighed-her

# Keycloak-administratoroplysninger
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=skift_mig_keycloak_admin_adgangskode

# Keycloak-database (oprettes automatisk)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=skift_mig_keycloak_db_adgangskode

# Port Keycloak lytter på (host-side, proxyet af Nginx)
KEYCLOAK_PORT=8091
```

**2. Start med den indlejrede Keycloak-profil:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Bekræft, at Keycloak er sund:**

```bash
docker compose -f docker-compose.production.yml ps
```

Containeren `rtcloud-keycloak` bør vise `Up (healthy)` efter 2–3 minutter.

**4. Tilgå Keycloak-administratorkonsollen:**

```
https://rtcloud.example.com/auth/admin
```

Log ind med `KEYCLOAK_ADMIN_USER` og `KEYCLOAK_ADMIN_PASSWORD`.

### Hvad er forudkonfigureret

Den indlejrede Keycloak starter med et forudimporteret `rtsurvey`-realm, der inkluderer:

- Klientkonfiguration til webapplikationen
- Standardbrugerroller (`admin`, `project_manager`, `enumerator`, `analyst`)
- Sessions- og tokenindstillinger optimeret til rtSurvey

Du kan tilføje brugere direkte i Keycloak-administratorkonsollen eller forbinde Keycloak til en upstream-identitetsudbyder (LDAP, SAML).

### Nginx-routing

Når cloud-implementeringsscripts bruges, konfigureres Nginx til at proxye begge tjenester:

| Sti | Backend |
|------|---------|
| `/` | rtCloud-appen på `127.0.0.1:8080` |
| `/auth/` | Keycloak på `127.0.0.1:8090` |

---

## Ekstern OIDC-udbyder

Forbind rtCloud til enhver OpenID Connect-kompatibel identitetsudbyder. Denne tilgang kræver ikke Keycloak-containeren.

### Understøttede udbydere

Enhver OIDC-kompatibel udbyder fungerer, herunder:
- Authentik
- Auth0
- Okta
- Keycloak (ekstern instans)
- Supabase
- Google (til Google Workspace-organisationer)
- GitHub (via OAuth-apps med OIDC-udvidelse)

### Opsætning

**1. Registrér rtCloud som en OIDC-klient hos din identitetsudbyder.**

Du skal bruge:
- Et **klient-ID** og en **klienthemmelighed**
- At registrere **omdirigerings-URI'en**: `https://rtcloud.example.com/auth/callback`
- Til mobilappsupport, registrér også: `vn.rta.rtsurvey.auth://callback`

**2. Konfigurer miljøvariabler i `.env`:**

```dotenv
# OIDC-opdagelses-URL (udbyderspecifik – tjek din IdP-dokumentation)
OIDC_ISSUER_URL=https://din-identitetsudbyder.com

# Klientoplysninger fra din identitetsudbyder
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=din-klienthemmelighed-her

# Scopes der anmodes om (openid, profile og email er typisk tilstrækkeligt)
OIDC_SCOPE=openid profile email

# Omdirigerings-URI registreret hos din identitetsudbyder
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Valgfrit: separat mobilappklient
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Sæt til true for automatisk at oprette rtCloud-konti til nye OIDC-brugere
OPEN_REGISTRATION=false
```

**3. Genstart app-containeren for at anvende ændringerne:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Automatisk oprettelse af brugere

Når `OPEN_REGISTRATION=true`, opretter rtCloud automatisk en lokal konto, første gang en bruger logger ind via OIDC. Kontoen udfyldes med brugerens navn og e-mail fra ID-tokenet.

Når `OPEN_REGISTRATION=false` (standard), skal en rtCloud-administrator oprette brugerkontoen først, og OIDC-identiteten knyttes ved første login.

### Brugerdefinerede endepunkter

Hvis din udbyder ikke understøtter OIDC-opdagelse (`.well-known/openid-configuration`), kan du angive endepunkter manuelt:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://din-udbyder.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://din-udbyder.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://din-udbyder.com/oauth2/userinfo
```

---

## Azure Active Directory

Integrer rtCloud med din organisations Microsoft Azure AD-lejer.

### Opsætning

**1. Registrér en ny app i [Azure Portal](https://portal.azure.com):**

   - Gå til **Azure Active Directory** → **Appregistreringer** → **Ny registrering**
   - Navn: `rtCloud`
   - Omdirigerings-URI: `https://rtcloud.example.com/auth/callback` (Web-type)
   - Efter oprettelse skal du notere **Applikations(klient)-ID** og **Mappe(lejer)-ID**
   - Under **Certifikater og hemmeligheder** skal du oprette en ny klienthemmelighed

**2. Konfigurer miljøvariabler i `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Genstart app-containeren:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Brugere i din Azure AD-lejer kan nu logge ind på rtCloud med deres Microsoft-legitimationsoplysninger.

---

## Deaktivering af SSO

For at vende tilbage til lokal godkendelse skal du fjerne eller kommentere ud alle SSO-relaterede variabler i `.env` og derefter genstarte app-containeren:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Hvis du brugte indlejret Keycloak, skal du stoppe det ved at udelade flaget `--profile embed-keycloak` og køre `docker compose down` efterfulgt af `up -d` uden profilen.
