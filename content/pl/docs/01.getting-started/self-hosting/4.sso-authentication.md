---
weight: 4
title: "Uwierzytelnianie SSO"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Konfiguracja Single Sign-On dla samodzielnie hostowanego rtCloud przy użyciu wbudowanego Keycloak, zewnętrznego dostawcy OIDC lub Azure Active Directory."
---

rtCloud obsługuje trzy podejścia do Single Sign-On (SSO):

| Opcja | Najlepsza dla |
|--------|----------|
| [Wbudowany Keycloak](#embedded-keycloak) | Organizacje chcące w pełni samodzielnego serwera SSO dołączonego do rtCloud |
| [Zewnętrzny dostawca OIDC](#external-oidc-provider) | Organizacje już korzystające z dostawcy tożsamości (Auth0, Authentik, Okta, Supabase itp.) |
| [Azure Active Directory](#azure-active-directory) | Organizacje korzystające z Microsoft 365 lub Azure AD |

Bez skonfigurowanego SSO użytkownicy logują się przy użyciu lokalnych kont rtCloud zarządzanych przez panel administratora.

---

## Wbudowany Keycloak {#embedded-keycloak}

Wdrożenie zawiera opcjonalny kontener Keycloak działający obok rtCloud. Keycloak jest wstępnie skonfigurowany z realmem rtSurvey i gotowy do użycia.

### Wymagania

- Nazwa domeny z HTTPS (Keycloak wymaga HTTPS w środowisku produkcyjnym)
- Co najmniej 4 GB RAM na serwerze (Keycloak dodaje ~512 MB użycia pamięci)

### Konfiguracja

**1. Skonfiguruj zmienne środowiskowe w `.env`:**

```dotenv
# Włącz wbudowany kontener Keycloak
EMBED_KEYCLOAK=true

# URL Keycloak — użyj swojej rzeczywistej domeny
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Ustawienia realmu i klienta (zgodne z importowanym realm JSON)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Dane uwierzytelniające administratora Keycloak
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Baza danych Keycloak (tworzona automatycznie)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Port, na którym nasłuchuje Keycloak (po stronie hosta, proxy przez Nginx)
KEYCLOAK_PORT=8091
```

**2. Uruchom z wbudowanym profilem Keycloak:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Sprawdź, czy Keycloak jest zdrowy:**

```bash
docker compose -f docker-compose.production.yml ps
```

Kontener `rtcloud-keycloak` powinien pokazywać `Up (healthy)` po 2–3 minutach.

**4. Dostęp do konsoli administratora Keycloak:**

```
https://rtcloud.example.com/auth/admin
```

Zaloguj się używając `KEYCLOAK_ADMIN_USER` i `KEYCLOAK_ADMIN_PASSWORD`.

### Co jest wstępnie skonfigurowane

Wbudowany Keycloak startuje z wstępnie zaimportowanym realmem `rtsurvey` zawierającym:

- Konfigurację klienta dla aplikacji webowej
- Domyślne role użytkowników (`admin`, `project_manager`, `enumerator`, `analyst`)
- Ustawienia sesji i tokenów zoptymalizowane dla rtSurvey

Możesz dodawać użytkowników bezpośrednio w konsoli administratora Keycloak lub połączyć Keycloak z dostawcą tożsamości wyższego szczebla (LDAP, SAML).

### Routing Nginx

Przy korzystaniu ze skryptów wdrożenia chmury Nginx jest skonfigurowany do proxy obu usług:

| Ścieżka | Backend |
|------|---------|
| `/` | Aplikacja rtCloud na `127.0.0.1:8080` |
| `/auth/` | Keycloak na `127.0.0.1:8090` |

---

## Zewnętrzny dostawca OIDC {#external-oidc-provider}

Połącz rtCloud z dowolnym dostawcą tożsamości kompatybilnym z OpenID Connect. To podejście nie wymaga kontenera Keycloak.

### Obsługiwani dostawcy

Działa każdy dostawca zgodny z OIDC, w tym:
- Authentik
- Auth0
- Okta
- Keycloak (zewnętrzna instancja)
- Supabase
- Google (dla organizacji korzystających z Google Workspace)
- GitHub (przez aplikacje OAuth z rozszerzeniem OIDC)

### Konfiguracja

**1. Zarejestruj rtCloud jako klienta OIDC u dostawcy tożsamości.**

Będziesz potrzebować:
- **ID klienta** i **sekretu klienta**
- Zarejestrowania **redirect URI**: `https://rtcloud.example.com/auth/callback`
- Dla obsługi aplikacji mobilnej zarejestruj też: `vn.rta.rtsurvey.auth://callback`

**2. Skonfiguruj zmienne środowiskowe w `.env`:**

```dotenv
# URL odkrycia OIDC (specyficzny dla dostawcy — sprawdź dokumentację IdP)
OIDC_ISSUER_URL=https://your-identity-provider.com

# Dane uwierzytelniające klienta od dostawcy tożsamości
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# Zakresy do żądania (openid, profile i email są zazwyczaj wystarczające)
OIDC_SCOPE=openid profile email

# Redirect URI zarejestrowany u dostawcy tożsamości
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Opcjonalnie: oddzielny klient aplikacji mobilnej
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Ustaw na true, aby automatycznie tworzyć konta rtCloud dla nowych użytkowników OIDC
OPEN_REGISTRATION=false
```

**3. Uruchom ponownie kontener aplikacji, aby zastosować zmiany:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Automatyczne tworzenie użytkowników

Gdy `OPEN_REGISTRATION=true`, rtCloud automatycznie tworzy lokalne konto za pierwszym razem, gdy użytkownik loguje się przez OIDC. Konto jest uzupełniane imieniem i adresem email użytkownika z tokenu ID.

Gdy `OPEN_REGISTRATION=false` (domyślnie), administrator rtCloud musi najpierw utworzyć konto użytkownika, a tożsamość OIDC jest łączona przy pierwszym logowaniu.

### Niestandardowe punkty końcowe

Jeśli Twój dostawca nie obsługuje odkrycia OIDC (`.well-known/openid-configuration`), możesz ustawić punkty końcowe ręcznie:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory {#azure-active-directory}

Zintegruj rtCloud z dzierżawcą Microsoft Azure AD swojej organizacji.

### Konfiguracja

**1. Zarejestruj nową aplikację w [Azure Portal](https://portal.azure.com):**

   - Przejdź do **Azure Active Directory** → **App registrations** → **New registration**
   - Nazwa: `rtCloud`
   - Redirect URI: `https://rtcloud.example.com/auth/callback` (typ Web)
   - Po utworzeniu zanotuj **Application (client) ID** i **Directory (tenant) ID**
   - W **Certificates & secrets** utwórz nowy sekret klienta

**2. Skonfiguruj zmienne środowiskowe w `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Uruchom ponownie kontener aplikacji:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Użytkownicy w Twojej dzierżawie Azure AD mogą teraz logować się do rtCloud używając swoich danych uwierzytelniających Microsoft.

---

## Wyłączanie SSO

Aby przywrócić lokalne uwierzytelnianie, usuń lub zakomentuj wszystkie zmienne związane z SSO z `.env`, a następnie uruchom ponownie kontener aplikacji:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Jeśli korzystałeś z wbudowanego Keycloak, zatrzymaj go pomijając flagę `--profile embed-keycloak` i uruchamiając `docker compose down`, a następnie `up -d` bez profilu.
