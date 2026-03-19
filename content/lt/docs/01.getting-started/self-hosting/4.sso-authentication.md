---
weight: 4
title: "SSO autentifikavimas"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Konfigūruokite vieningo prisijungimo (SSO) funkciją savarankiškai valdomam rtCloud naudodami integruotą Keycloak, išorinį OIDC teikėją arba Azure Active Directory."
---

rtCloud palaiko tris vieningo prisijungimo (SSO) metodus:

| Parinktis | Geriausiai tinka |
|--------|----------|
| [Integruotas Keycloak](#embedded-keycloak) | Organizacijoms, norinčioms visiškai savarankiško SSO serverio, susieto su rtCloud |
| [Išorinis OIDC teikėjas](#external-oidc-provider) | Organizacijoms, jau naudojančioms tapatybės teikėją (Auth0, Authentik, Okta, Supabase ir kt.) |
| [Azure Active Directory](#azure-active-directory) | Organizacijoms, naudojančioms Microsoft 365 arba Azure AD |

Nekonfigūravus SSO, naudotojai prisijungia su vietinėmis rtCloud paskyromis, valdomis per administravimo skydelį.

---

## Integruotas Keycloak

Diegimas apima neprivalomą Keycloak konteinerį, veikiantį kartu su rtCloud. Keycloak iš anksto sukonfigūruotas su rtSurvey sritimi ir paruoštas naudoti.

### Reikalavimai

- Domeno vardas su HTTPS (gamyboje Keycloak reikalauja HTTPS)
- Mažiausiai 4 GB RAM serveryje (Keycloak naudoja ~512 MB atminties)

### Sąranka

**1. Konfigūruokite aplinkos kintamuosius `.env` faile:**

```dotenv
# Įjunkite integruotą Keycloak konteinerį
EMBED_KEYCLOAK=true

# Keycloak URL – naudokite savo tikrąjį domeną
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Srities ir kliento nustatymai (atitinka importuotą srities JSON)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Keycloak administratoriaus prisijungimo duomenys
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Keycloak duomenų bazė (sukuriama automatiškai)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Prievadas, kuriame Keycloak klauso (pagrindinio kompiuterio pusė, tarpininkaujama Nginx)
KEYCLOAK_PORT=8091
```

**2. Paleiskite su integruotu Keycloak profiliu:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Patikrinkite, ar Keycloak sveikas:**

```bash
docker compose -f docker-compose.production.yml ps
```

Po 2–3 minučių `rtcloud-keycloak` konteineris turėtų rodyti `Up (healthy)`.

**4. Pasiekite Keycloak administravimo konsolę:**

```
https://rtcloud.example.com/auth/admin
```

Prisijunkite naudodami `KEYCLOAK_ADMIN_USER` ir `KEYCLOAK_ADMIN_PASSWORD`.

### Kas iš anksto sukonfigūruota

Integruotas Keycloak paleidžiamas su iš anksto importuota `rtsurvey` sritimi, kurioje yra:

- Kliento konfigūracija žiniatinklio programai
- Numatytieji naudotojų vaidmenys (`admin`, `project_manager`, `enumerator`, `analyst`)
- Seanso ir žetono nustatymai, optimizuoti rtSurvey

Galite pridėti naudotojus tiesiogiai Keycloak administravimo konsolėje arba prijungti Keycloak prie aukštesnio lygio tapatybės teikėjo (LDAP, SAML).

### Nginx maršrutizavimas

Naudojant debesies diegimo scenarijus, Nginx sukonfigūruotas tarpininkauti abiem paslaugoms:

| Kelias | Galinė paslauga |
|------|---------|
| `/` | rtCloud programa `127.0.0.1:8080` |
| `/auth/` | Keycloak `127.0.0.1:8090` |

---

## Išorinis OIDC teikėjas

Prijunkite rtCloud prie bet kurio OpenID Connect suderinamojo tapatybės teikėjo. Šiam metodui Keycloak konteinerio nereikia.

### Palaikomi teikėjai

Veikia bet kuris OIDC suderinamasis teikėjas, įskaitant:
- Authentik
- Auth0
- Okta
- Keycloak (išorinė instancija)
- Supabase
- Google (Google Workspace organizacijoms)
- GitHub (per OAuth programas su OIDC plėtiniu)

### Sąranka

**1. Registruokite rtCloud kaip OIDC klientą savo tapatybės teikėjuje.**

Jums reikės:
- **Kliento ID** ir **kliento paslapties**
- Registruoti **nukreipimo URI**: `https://rtcloud.example.com/auth/callback`
- Mobilios programos palaikymui taip pat registruoti: `vn.rta.rtsurvey.auth://callback`

**2. Konfigūruokite aplinkos kintamuosius `.env` faile:**

```dotenv
# OIDC atradimo URL (priklauso nuo teikėjo – tikrinkite savo IdP dokumentaciją)
OIDC_ISSUER_URL=https://your-identity-provider.com

# Kliento prisijungimo duomenys iš jūsų tapatybės teikėjo
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# Prašomos sritys (openid, profile ir email paprastai pakanka)
OIDC_SCOPE=openid profile email

# Nukreipimo URI, registruotas jūsų tapatybės teikėjuje
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Neprivaloma: atskiras mobilios programos klientas
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Nustatykite į true, kad automatiškai kurtumėte rtCloud paskyras naujiems OIDC naudotojams
OPEN_REGISTRATION=false
```

**3. Iš naujo paleiskite programos konteinerį, kad pritaikytumėte pakeitimus:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Automatinis naudotojų parengimas

Kai `OPEN_REGISTRATION=true`, rtCloud automatiškai sukuria vietinę paskyrą pirmą kartą naudotojui prisijungus per OIDC. Paskyra užpildoma naudotojo vardu ir el. paštu iš ID žetono.

Kai `OPEN_REGISTRATION=false` (numatytasis), rtCloud administratorius pirmiausia turi sukurti naudotojo paskyrą, o OIDC tapatybė susieta pirmojo prisijungimo metu.

### Pasirinktiniai galiniai taškai

Jei jūsų teikėjas nepalaiko OIDC atradimo (`.well-known/openid-configuration`), galite nustatyti galinių taškų adresus neautomatiniu būdu:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory

Integruokite rtCloud su savo organizacijos Microsoft Azure AD nuomotoju.

### Sąranka

**1. Registruokite naują programą [Azure portale](https://portal.azure.com):**

   - Eikite į **Azure Active Directory** → **Programų registracijos** → **Nauja registracija**
   - Pavadinimas: `rtCloud`
   - Nukreipimo URI: `https://rtcloud.example.com/auth/callback` (žiniatinklio tipas)
   - Sukūrus, užsirašykite **Programos (kliento) ID** ir **Katalogo (nuomotojo) ID**
   - Skiltyje **Sertifikatai ir paslaptys** sukurkite naują kliento paslaptį

**2. Konfigūruokite aplinkos kintamuosius `.env` faile:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Iš naujo paleiskite programos konteinerį:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Jūsų Azure AD nuomotojo naudotojai dabar gali prisijungti prie rtCloud naudodami savo Microsoft prisijungimo duomenis.

---

## SSO išjungimas

Norėdami grįžti prie vietinės autentifikacijos, pašalinkite arba pakomentuokite visus SSO susijusius kintamuosius iš `.env`, tada iš naujo paleiskite programos konteinerį:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Jei naudojote integruotą Keycloak, sustabdykite jį praleisdami `--profile embed-keycloak` žymą ir paleisdami `docker compose down`, po to `up -d` be profilio.
