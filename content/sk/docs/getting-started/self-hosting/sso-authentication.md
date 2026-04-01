---
weight: 4
title: "SSO autentifikácia"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Konfigurácia Single Sign-On pre vlastný hosting rtCloud pomocou vstavaného Keycloak, externého poskytovateľa OIDC alebo Azure Active Directory."
---

rtCloud podporuje tri prístupy pre Single Sign-On (SSO):

| Možnosť | Najvhodnejšie pre |
|--------|----------|
| [Vstavaný Keycloak](#embedded-keycloak) | Organizácie, ktoré chcú plne samostatný server SSO bundlovaný s rtCloud |
| [Externý poskytovateľ OIDC](#external-oidc-provider) | Organizácie, ktoré už prevádzkujú poskytovateľa identity (Auth0, Authentik, Okta, Supabase atď.) |
| [Azure Active Directory](#azure-active-directory) | Organizácie používajúce Microsoft 365 alebo Azure AD |

Bez nakonfigurovaného SSO sa používatelia prihlasujú pomocou lokálnych účtov rtCloud spravovaných cez administrátorský panel.

---

## Vstavaný Keycloak

Nasadenie obsahuje voliteľný kontajner Keycloak, ktorý beží vedľa rtCloud. Keycloak je vopred nakonfigurovaný s realmom rtSurvey a pripravený na použitie.

### Požiadavky

- Doménové meno s HTTPS (Keycloak vyžaduje HTTPS v produkcii)
- Aspoň 4 GB RAM na serveri (Keycloak pridáva ~512 MB využitia pamäte)

### Nastavenie

**1. Nakonfigurujte premenné prostredia v `.env`:**

```dotenv
# Aktivovanie vstavaného kontajnera Keycloak
EMBED_KEYCLOAK=true

# URL Keycloak — použite vašu skutočnú doménu
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Nastavenia realmu a klienta (zodpovedajú importovanému JSON realmu)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Prihlasovacie údaje správcu Keycloak
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Databáza Keycloak (vytvorí sa automaticky)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Port, na ktorom počúva Keycloak (na strane hostiteľa, proxované Nginx)
KEYCLOAK_PORT=8091
```

**2. Spustite s profilom vstavaného Keycloak:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Overte, že Keycloak je zdravý:**

```bash
docker compose -f docker-compose.production.yml ps
```

Kontajner `rtcloud-keycloak` by mal po 2–3 minútach zobrazovať `Up (healthy)`.

**4. Prístup k administrátorskej konzole Keycloak:**

```
https://rtcloud.example.com/auth/admin
```

Prihláste sa s `KEYCLOAK_ADMIN_USER` a `KEYCLOAK_ADMIN_PASSWORD`.

### Čo je vopred nakonfigurované

Vstavaný Keycloak sa spúšťa s vopred importovaným realmom `rtsurvey`, ktorý zahŕňa:

- Konfiguráciu klienta pre webovú aplikáciu
- Predvolené role používateľov (`admin`, `project_manager`, `enumerator`, `analyst`)
- Nastavenia relácie a tokenu optimalizované pre rtSurvey

Používateľov môžete pridávať priamo v administrátorskej konzole Keycloak alebo pripojiť Keycloak k upstream poskytovateľovi identity (LDAP, SAML).

### Smerovanie Nginx

Pri použití skriptov cloudového nasadenia je Nginx nakonfigurovaný na proxy oboch služieb:

| Cesta | Backend |
|------|---------|
| `/` | Aplikácia rtCloud na `127.0.0.1:8080` |
| `/auth/` | Keycloak na `127.0.0.1:8090` |

---

## Externý poskytovateľ OIDC

Prepojte rtCloud s akýmkoľvek poskytovateľom identity kompatibilným s OpenID Connect. Tento prístup nevyžaduje kontajner Keycloak.

### Podporovaní poskytovatelia

Funguje akýkoľvek poskytovateľ kompatibilný s OIDC, vrátane:
- Authentik
- Auth0
- Okta
- Keycloak (externá inštancia)
- Supabase
- Google (pre organizácie Google Workspace)
- GitHub (cez OAuth aplikácie s rozšírením OIDC)

### Nastavenie

**1. Zaregistrujte rtCloud ako klienta OIDC u vášho poskytovateľa identity.**

Budete potrebovať:
- **ID klienta** a **tajomstvo klienta**
- Registráciu **URI presmerovania**: `https://rtcloud.example.com/auth/callback`
- Pre podporu mobilnej aplikácie tiež zaregistrujte: `vn.rta.rtsurvey.auth://callback`

**2. Nakonfigurujte premenné prostredia v `.env`:**

```dotenv
# URL na objavenie OIDC (špecifické pre poskytovateľa — skontrolujte dokumentáciu vášho IdP)
OIDC_ISSUER_URL=https://your-identity-provider.com

# Prihlasovacie údaje klienta od vášho poskytovateľa identity
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# Rozsahy na žiadosť (openid, profile a email sú zvyčajne dostatočné)
OIDC_SCOPE=openid profile email

# URI presmerovania zaregistrované u vášho poskytovateľa identity
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Voliteľné: samostatný klient pre mobilnú aplikáciu
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Nastavte na true na automatické vytváranie účtov rtCloud pre nových používateľov OIDC
OPEN_REGISTRATION=false
```

**3. Reštartujte kontajner aplikácie na aplikovanie zmien:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Automatické zriaďovanie používateľov

Keď je `OPEN_REGISTRATION=true`, rtCloud automaticky vytvorí lokálny účet pri prvom prihlásení používateľa cez OIDC. Účet sa naplní menom a emailom používateľa z ID tokenu.

Keď je `OPEN_REGISTRATION=false` (predvolené), správca rtCloud musí najprv vytvoriť používateľský účet a identita OIDC sa prepojí pri prvom prihlásení.

### Vlastné koncové body

Ak váš poskytovateľ nepodporuje objavenie OIDC (`.well-known/openid-configuration`), môžete nastaviť koncové body manuálne:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory

Integrujte rtCloud s tenantom Microsoft Azure AD vašej organizácie.

### Nastavenie

**1. Zaregistrujte novú aplikáciu na [Azure Portal](https://portal.azure.com):**

   - Prejdite na **Azure Active Directory** → **App registrations** → **New registration**
   - Názov: `rtCloud`
   - URI presmerovania: `https://rtcloud.example.com/auth/callback` (typ Web)
   - Po vytvorení poznamenajte **Application (client) ID** a **Directory (tenant) ID**
   - Pod **Certificates & secrets** vytvorte nové tajomstvo klienta

**2. Nakonfigurujte premenné prostredia v `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Reštartujte kontajner aplikácie:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Používatelia vo vašom tenante Azure AD sa teraz môžu prihlásiť do rtCloud pomocou svojich Microsoft prihlasovacích údajov.

---

## Deaktivácia SSO

Na vrátenie k lokálnej autentifikácii odstráňte alebo zakomentujte všetky premenné súvisiace s SSO v `.env`, potom reštartujte kontajner aplikácie:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Ak ste používali vstavaný Keycloak, zastavte ho vynechaním príznaku `--profile embed-keycloak` a spustením `docker compose down` nasledovaného `up -d` bez profilu.
