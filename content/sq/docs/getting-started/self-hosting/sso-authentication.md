---
weight: 4
title: "Autentifikimi SSO"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Konfiguroni Hyrjen e Vetme për rtCloud vetjak duke përdorur Keycloak të integruar, një ofrues të jashtëm OIDC ose Azure Active Directory."
---

rtCloud mbështet tre qasje për Hyrjen e Vetme (SSO):

| Opsioni | Më i Mirë Për |
|--------|----------|
| [Keycloak i Integruar](#embedded-keycloak) | Organizatat që dëshirojnë një server SSO plotësisht të vetë-mjaftueshëm të bashkuar me rtCloud |
| [Ofruesi i Jashtëm OIDC](#external-oidc-provider) | Organizatat që tashmë ekzekutojnë një ofrues identiteti (Auth0, Authentik, Okta, Supabase, etj.) |
| [Azure Active Directory](#azure-active-directory) | Organizatat që përdorin Microsoft 365 ose Azure AD |

Pa SSO të konfiguruar, përdoruesit hyjnë me llogari lokale rtCloud të menaxhuara nëpërmjet panelit administrativ.

---

## Keycloak i Integruar

Vendosja përfshin një kontejner opsional Keycloak që ekzekutohet krahas rtCloud. Keycloak është i para-konfiguruar me një realm rtSurvey dhe gati për t'u përdorur.

### Kërkesat

- Një emër domeni me HTTPS (Keycloak kërkon HTTPS në prodhim)
- Të paktën 4 GB RAM në server (Keycloak shton ~512 MB përdorim memorieje)

### Konfigurimi

**1. Konfiguroni variablat e mjedisit në `.env`:**

```dotenv
# Aktivizoni kontejnerin e integruar Keycloak
EMBED_KEYCLOAK=true

# URL-të Keycloak — përdorni domenin tuaj aktual
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Cilësimet e realmit dhe klientit (përputhen me JSON-in e importuar të realmit)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=sekret-klienti-juaj-këtu

# Kredencialet administrative Keycloak
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=ndryshoni_fjalëkalimin_admin_keycloak

# Baza e të dhënave Keycloak (krijohet automatikisht)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=ndryshoni_fjalëkalimin_db_keycloak

# Porta Keycloak dëgjon (anën e hostit, i proxueshëm nga Nginx)
KEYCLOAK_PORT=8091
```

**2. Nisni me profilin e integruar Keycloak:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Verifikoni që Keycloak është i shëndetshëm:**

```bash
docker compose -f docker-compose.production.yml ps
```

Kontejneri `rtcloud-keycloak` duhet të tregojë `Up (healthy)` pas 2–3 minutave.

**4. Aksesoni konsolën administrative Keycloak:**

```
https://rtcloud.example.com/auth/admin
```

Hyni me `KEYCLOAK_ADMIN_USER` dhe `KEYCLOAK_ADMIN_PASSWORD`.

### Çfarë është Para-konfiguruar

Keycloak i integruar fillon me një realm `rtsurvey` të para-importuar që përfshin:

- Konfigurimin e klientit për aplikacionin ueb
- Rolet e parazgjedhura të përdoruesit (`admin`, `project_manager`, `enumerator`, `analyst`)
- Cilësimet e sesionit dhe shenjës të optimizuara për rtSurvey

Mund të shtoni përdorues direkt në konsolën administrative Keycloak ose të lidhni Keycloak me një ofrues identiteti primar (LDAP, SAML).

### Rutimi Nginx

Kur përdorni skriptet e vendosjes cloud, Nginx konfigurohet të proxojë të dy shërbimet:

| Rruga | Mbrapa |
|------|---------|
| `/` | Aplikacioni rtCloud te `127.0.0.1:8080` |
| `/auth/` | Keycloak te `127.0.0.1:8090` |

---

## Ofruesi i Jashtëm OIDC

Lidhni rtCloud me çdo ofrues identiteti të përputhshëm me OpenID Connect. Kjo qasje nuk kërkon kontejnerin Keycloak.

### Ofruesit e Mbështetur

Çdo ofrues i përputhshëm me OIDC funksionon, duke përfshirë:
- Authentik
- Auth0
- Okta
- Keycloak (instancë e jashtme)
- Supabase
- Google (për organizatat Google Workspace)
- GitHub (nëpërmjet aplikacioneve OAuth me zgjerimin OIDC)

### Konfigurimi

**1. Regjistroni rtCloud si klient OIDC te ofruesi juaj i identitetit.**

Do t'ju duhet:
- Një **ID klienti** dhe **sekret klienti**
- Të regjistroni **URI-n e ridrejtimit**: `https://rtcloud.example.com/auth/callback`
- Për mbështetjen e aplikacionit celular, gjithashtu regjistroni: `vn.rta.rtsurvey.auth://callback`

**2. Konfiguroni variablat e mjedisit në `.env`:**

```dotenv
# URL-ja e zbulimit OIDC (specifike për ofruesin — kontrolloni dokumentacionin e IdP tuaj)
OIDC_ISSUER_URL=https://ofruesi-juaj-identiteti.com

# Kredencialet e klientit nga ofruesi juaj i identitetit
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=sekret-klienti-juaj-këtu

# Fushat për të kërkuar (openid, profile dhe email janë zakonisht të mjaftueshme)
OIDC_SCOPE=openid profile email

# URI-ja e ridrejtimit e regjistruar te ofruesi juaj i identitetit
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Opsionale: klienti i veçantë i aplikacionit celular
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Caktoni në true për të krijuar automatikisht llogari rtCloud për përdoruesit e rinj OIDC
OPEN_REGISTRATION=false
```

**3. Rinisni kontejnerin e aplikacionit për të aplikuar ndryshimet:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Aprovizionimi Automatik i Përdoruesve

Kur `OPEN_REGISTRATION=true`, rtCloud krijon automatikisht një llogari lokale herën e parë që një përdorues hyn nëpërmjet OIDC. Llogaria plotësohet me emrin dhe emailin e përdoruesit nga shenja ID.

Kur `OPEN_REGISTRATION=false` (parazgjedhja), një administrator rtCloud duhet të krijojë fillimisht llogarinë e përdoruesit, dhe identiteti OIDC lidhet në hyrjen e parë.

### Pikat Fundore të Personalizuara

Nëse ofruesi juaj nuk mbështet zbulimin OIDC (`.well-known/openid-configuration`), mund të caktoni pikat fundore manualisht:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://ofruesi-juaj.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://ofruesi-juaj.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://ofruesi-juaj.com/oauth2/userinfo
```

---

## Azure Active Directory

Integroni rtCloud me qiramarrësin Microsoft Azure AD të organizatës suaj.

### Konfigurimi

**1. Regjistroni një aplikacion të ri në [Portën Azure](https://portal.azure.com):**

   - Shkoni te **Azure Active Directory** → **Regjistrimet e aplikacioneve** → **Regjistrim i ri**
   - Emri: `rtCloud`
   - URI-ja e ridrejtimit: `https://rtcloud.example.com/auth/callback` (tipi Ueb)
   - Pas krijimit, shënoni **ID-n e Aplikacionit (klientit)** dhe **ID-n e Drejtorisë (qiramarrësit)**
   - Nën **Certifikatat dhe sekretet**, krijoni një sekret të ri klienti

**2. Konfiguroni variablat e mjedisit në `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Rinisni kontejnerin e aplikacionit:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Përdoruesit në qiramarrësin tuaj Azure AD tani mund të hyjnë në rtCloud duke përdorur kredencialet e tyre Microsoft.

---

## Çaktivizimi i SSO

Për t'u kthyer në autentifikimin lokal, hiqni ose komentoni të gjitha variablat e lidhura me SSO nga `.env`, pastaj rinisni kontejnerin e aplikacionit:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Nëse po përdornit Keycloak të integruar, ndaleni duke hequr flamurin `--profile embed-keycloak` dhe duke ekzekutuar `docker compose down` të ndjekur nga `up -d` pa profilin.
