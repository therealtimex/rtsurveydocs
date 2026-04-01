---
weight: 4
title: "SSO-autentisering"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Konfigurera Single Sign-On för självhostad rtCloud med inbäddad Keycloak, en extern OIDC-leverantör eller Azure Active Directory."
---

rtCloud stöder tre tillvägagångssätt för Single Sign-On (SSO):

| Alternativ | Bäst för |
|--------|----------|
| [Inbäddad Keycloak](#embedded-keycloak) | Organisationer som vill ha en helt självständig SSO-server paketerad med rtCloud |
| [Extern OIDC-leverantör](#external-oidc-provider) | Organisationer som redan kör en identitetsleverantör (Auth0, Authentik, Okta, Supabase, m.fl.) |
| [Azure Active Directory](#azure-active-directory) | Organisationer som använder Microsoft 365 eller Azure AD |

Utan SSO konfigurerat loggar användare in med lokala rtCloud-konton hanterade via adminpanelen.

---

## Inbäddad Keycloak {#embedded-keycloak}

Driftsättningen inkluderar en valfri Keycloak-container som körs parallellt med rtCloud. Keycloak är förkonfigurerad med ett rtSurvey-realm och redo att använda.

### Krav

- Ett domännamn med HTTPS (Keycloak kräver HTTPS i produktion)
- Minst 4 GB RAM på servern (Keycloak lägger till ~512 MB minnesanvändning)

### Konfiguration

**1. Konfigurera miljövariabler i `.env`:**

```dotenv
# Aktivera den inbäddade Keycloak-containern
EMBED_KEYCLOAK=true

# Keycloak URL:er — använd din faktiska domän
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Realm- och klientinställningar (matchar det importerade realm-JSON)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=din-klienthemlighet-här

# Keycloak-adminuppgifter
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Keycloak-databas (skapas automatiskt)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Port som Keycloak lyssnar på (värd-sidan, proxieras av Nginx)
KEYCLOAK_PORT=8091
```

**2. Starta med den inbäddade Keycloak-profilen:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Verifiera att Keycloak är frisk:**

```bash
docker compose -f docker-compose.production.yml ps
```

Containern `rtcloud-keycloak` bör visa `Up (healthy)` efter 2–3 minuter.

**4. Öppna Keycloak-adminkonsolen:**

```
https://rtcloud.example.com/auth/admin
```

Logga in med `KEYCLOAK_ADMIN_USER` och `KEYCLOAK_ADMIN_PASSWORD`.

### Vad är förkonfigurerat

Den inbäddade Keycloak startar med ett förimporterat `rtsurvey`-realm som inkluderar:

- Klientkonfiguration för webbapplikationen
- Standardanvändarroller (`admin`, `project_manager`, `enumerator`, `analyst`)
- Sessions- och tokeninställningar optimerade för rtSurvey

Du kan lägga till användare direkt i Keycloak-adminkonsolen eller ansluta Keycloak till en uppströms identitetsleverantör (LDAP, SAML).

### Nginx-routing

När du använder molndriftsättningsskripten är Nginx konfigurerad att proxia båda tjänsterna:

| Sökväg | Backend |
|------|---------|
| `/` | rtCloud-app på `127.0.0.1:8080` |
| `/auth/` | Keycloak på `127.0.0.1:8090` |

---

## Extern OIDC-leverantör {#external-oidc-provider}

Anslut rtCloud till vilken OpenID Connect-kompatibel identitetsleverantör som helst. Detta tillvägagångssätt kräver inte Keycloak-containern.

### Stödda leverantörer

Alla OIDC-kompatibla leverantörer fungerar, inklusive:
- Authentik
- Auth0
- Okta
- Keycloak (extern instans)
- Supabase
- Google (för Google Workspace-organisationer)
- GitHub (via OAuth-appar med OIDC-tillägg)

### Konfiguration

**1. Registrera rtCloud som en OIDC-klient hos din identitetsleverantör.**

Du behöver:
- Ett **klient-ID** och en **klienthemlighet**
- Att registrera **omdirigerings-URI:n**: `https://rtcloud.example.com/auth/callback`
- För mobilappsstöd, registrera också: `vn.rta.rtsurvey.auth://callback`

**2. Konfigurera miljövariabler i `.env`:**

```dotenv
# OIDC-discovery-URL (leverantörsspecifik — kontrollera din IdP:s dokumentation)
OIDC_ISSUER_URL=https://din-identitetsleverantör.com

# Klientuppgifter från din identitetsleverantör
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=din-klienthemlighet-här

# Scope att begära (openid, profile och email är vanligtvis tillräckligt)
OIDC_SCOPE=openid profile email

# Omdirigerings-URI registrerad hos din identitetsleverantör
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Valfritt: separat mobilappsklient
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Ange true för att automatiskt skapa rtCloud-konton för nya OIDC-användare
OPEN_REGISTRATION=false
```

**3. Starta om appcontainern för att tillämpa ändringarna:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Automatisk provisionering av användare

När `OPEN_REGISTRATION=true` skapar rtCloud automatiskt ett lokalt konto första gången en användare loggar in via OIDC. Kontot fylls i med användarens namn och e-post från ID-token.

När `OPEN_REGISTRATION=false` (standard) måste en rtCloud-administratör skapa användarkontot först, och OIDC-identiteten kopplas vid första inloggningen.

### Anpassade slutpunkter

Om din leverantör inte stöder OIDC-discovery (`.well-known/openid-configuration`) kan du ange slutpunkter manuellt:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://din-leverantör.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://din-leverantör.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://din-leverantör.com/oauth2/userinfo
```

---

## Azure Active Directory {#azure-active-directory}

Integrera rtCloud med din organisations Microsoft Azure AD-klientorganisation.

### Konfiguration

**1. Registrera en ny app i [Azure Portal](https://portal.azure.com):**

   - Gå till **Azure Active Directory** → **Appregistreringar** → **Ny registrering**
   - Namn: `rtCloud`
   - Omdirigerings-URI: `https://rtcloud.example.com/auth/callback` (Webbtyp)
   - Efter skapande, notera **Program (klient)-ID** och **Katalog (klientorganisation)-ID**
   - Under **Certifikat och hemligheter**, skapa en ny klienthemlighet

**2. Konfigurera miljövariabler i `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Starta om appcontainern:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Användare i din Azure AD-klientorganisation kan nu logga in på rtCloud med sina Microsoft-uppgifter.

---

## Inaktivera SSO

För att återgå till lokal autentisering, ta bort eller kommentera bort alla SSO-relaterade variabler från `.env` och starta sedan om appcontainern:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Om du använde inbäddad Keycloak, stoppa den genom att utelämna flaggan `--profile embed-keycloak` och köra `docker compose down` följt av `up -d` utan profilen.
