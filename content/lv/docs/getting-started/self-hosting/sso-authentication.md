---
weight: 4
title: "SSO autentifikācija"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Konfigurējiet vienas pieteikšanās (SSO) pašmitinātajam rtCloud, izmantojot iebūvēto Keycloak, ārējo OIDC nodrošinātāju vai Azure Active Directory."
---

rtCloud atbalsta trīs pieejas vienas pieteikšanās (SSO) iestatīšanai:

| Iespēja | Piemērots |
|--------|----------|
| [Iebūvētais Keycloak](#embedded-keycloak) | Organizācijām, kas vēlas pilnībā pašpietiekamu SSO serveri, kas kopā ar rtCloud |
| [Ārējais OIDC nodrošinātājs](#external-oidc-provider) | Organizācijām, kas jau izmanto identitātes nodrošinātāju (Auth0, Authentik, Okta, Supabase utt.) |
| [Azure Active Directory](#azure-active-directory) | Organizācijām, kas izmanto Microsoft 365 vai Azure AD |

Bez SSO konfigurācijas lietotāji piesakās ar lokālajiem rtCloud kontiem, ko pārvalda administratora panelī.

---

## Iebūvētais Keycloak

Izvietošana ietver neobligātu Keycloak konteineru, kas darbojas blakus rtCloud. Keycloak ir iepriekš konfigurēts ar rtSurvey reālmu un gatavs lietošanai.

### Prasības

- Domēna nosaukums ar HTTPS (Keycloak ražošanā prasa HTTPS)
- Vismaz 4 GB RAM serverī (Keycloak pievieno ~512 MB atmiņas patēriņu)

### Iestatīšana

**1. Konfigurējiet vides mainīgos failā `.env`:**

```dotenv
# Iespējojiet iebūvēto Keycloak konteineru
EMBED_KEYCLOAK=true

# Keycloak URL — izmantojiet savu faktisko domēnu
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Reālms un klienta iestatījumi (atbilstoši importētajam reālma JSON)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Keycloak administratora akreditācijas dati
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Keycloak datu bāze (tiek automātiski izveidota)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Ports, uz kura klausās Keycloak (saimniekdatora pusē, ko Nginx starpniek)
KEYCLOAK_PORT=8091
```

**2. Palaidiet ar iebūvēto Keycloak profilu:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Pārbaudiet, vai Keycloak ir veselīgs:**

```bash
docker compose -f docker-compose.production.yml ps
```

Konteineram `rtcloud-keycloak` pēc 2–3 minūtēm jārāda `Up (healthy)`.

**4. Piekļūstiet Keycloak administratora konsolei:**

```
https://rtcloud.example.com/auth/admin
```

Piesakieties ar `KEYCLOAK_ADMIN_USER` un `KEYCLOAK_ADMIN_PASSWORD`.

### Kas ir iepriekš konfigurēts

Iebūvētais Keycloak sākas ar iepriekš importētu `rtsurvey` reālmu, kas ietver:

- Klienta konfigurāciju tīmekļa lietojumprogrammai
- Noklusējuma lietotāju lomas (`admin`, `project_manager`, `enumerator`, `analyst`)
- Sesijas un žetona iestatījumus, kas optimizēti rtSurvey

Varat pievienot lietotājus tieši Keycloak administratora konsolē vai savienot Keycloak ar augštecīgu identitātes nodrošinātāju (LDAP, SAML).

### Nginx maršrutēšana

Izmantojot mākoņa izvietošanas skriptus, Nginx ir konfigurēts, lai starpniekotu abus pakalpojumus:

| Ceļš | Aizmugure |
|------|---------|
| `/` | rtCloud lietotne uz `127.0.0.1:8080` |
| `/auth/` | Keycloak uz `127.0.0.1:8090` |

---

## Ārējais OIDC nodrošinātājs

Savienojiet rtCloud ar jebkuru OpenID Connect saderīgu identitātes nodrošinātāju. Šī pieeja neprasa Keycloak konteineru.

### Atbalstītie nodrošinātāji

Darbojas jebkurš OIDC saderīgs nodrošinātājs, tostarp:
- Authentik
- Auth0
- Okta
- Keycloak (ārēja instance)
- Supabase
- Google (Google Workspace organizācijām)
- GitHub (caur OAuth lietotnēm ar OIDC paplašinājumu)

### Iestatīšana

**1. Reģistrējiet rtCloud kā OIDC klientu savā identitātes nodrošinātājā.**

Jums būs nepieciešams:
- **Klienta ID** un **klienta noslēpums**
- Reģistrēt **novirzīšanas URI**: `https://rtcloud.example.com/auth/callback`
- Mobilās lietotnes atbalstam arī reģistrējiet: `vn.rta.rtsurvey.auth://callback`

**2. Konfigurējiet vides mainīgos failā `.env`:**

```dotenv
# OIDC atklāšanas URL (specifisks nodrošinātājam — skatiet IdP dokumentāciju)
OIDC_ISSUER_URL=https://your-identity-provider.com

# Klienta akreditācijas dati no jūsu identitātes nodrošinātāja
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# Pieprasāmie tvērumi (openid, profile un email parasti pietiek)
OIDC_SCOPE=openid profile email

# Novirzīšanas URI, reģistrēts jūsu identitātes nodrošinātājā
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Neobligāts: atsevišķs mobilās lietotnes klients
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Iestatiet uz true, lai automātiski izveidotu rtCloud kontus jauniem OIDC lietotājiem
OPEN_REGISTRATION=false
```

**3. Restartējiet lietotnes konteineru, lai piemērotu izmaiņas:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Automātiskā lietotāju nodrošināšana

Kad `OPEN_REGISTRATION=true`, rtCloud automātiski izveido lokālu kontu, kad lietotājs pirmo reizi piesakās, izmantojot OIDC. Konts tiek aizpildīts ar lietotāja vārdu un e-pastu no ID žetona.

Kad `OPEN_REGISTRATION=false` (noklusējums), rtCloud administratoram vispirms jāizveido lietotāja konts, un OIDC identitāte tiek saistīta pirmajā pieteikšanās reizē.

### Pielāgoti galapunkti

Ja jūsu nodrošinātājs neatbalsta OIDC atklāšanu (`.well-known/openid-configuration`), varat manuāli iestatīt galapunktus:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory

Integrējiet rtCloud ar savas organizācijas Microsoft Azure AD nomnieku.

### Iestatīšana

**1. Reģistrējiet jaunu lietotni [Azure portālā](https://portal.azure.com):**

   - Dodieties uz **Azure Active Directory** → **App registrations** → **New registration**
   - Nosaukums: `rtCloud`
   - Novirzīšanas URI: `https://rtcloud.example.com/auth/callback` (Web tips)
   - Pēc izveides ņemiet vērā **Application (client) ID** un **Directory (tenant) ID**
   - Sadaļā **Certificates & secrets** izveidojiet jaunu klienta noslēpumu

**2. Konfigurējiet vides mainīgos failā `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Restartējiet lietotnes konteineru:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Lietotāji jūsu Azure AD nomniekā tagad var pieteikties rtCloud, izmantojot savus Microsoft akreditācijas datus.

---

## SSO atspējošana

Lai atgrieztos pie lokālās autentifikācijas, noņemiet vai komentējiet visus ar SSO saistītos mainīgos no `.env`, pēc tam restartējiet lietotnes konteineru:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Ja izmantojāt iebūvēto Keycloak, apturiet to, izlaižot karodziņu `--profile embed-keycloak` un palaižot `docker compose down`, pēc kam `up -d` bez profila.
