---
weight: 4
title: "Autenticazione SSO"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Configura il Single Sign-On per rtCloud self-hosted usando Keycloak integrato, un provider OIDC esterno o Azure Active Directory."
---

rtCloud supporta tre approcci per il Single Sign-On (SSO):

| Opzione | Ideale per |
|--------|----------|
| [Keycloak integrato](#embedded-keycloak) | Organizzazioni che vogliono un server SSO completamente autonomo integrato con rtCloud |
| [Provider OIDC esterno](#external-oidc-provider) | Organizzazioni che già gestiscono un provider di identità (Auth0, Authentik, Okta, Supabase, ecc.) |
| [Azure Active Directory](#azure-active-directory) | Organizzazioni che usano Microsoft 365 o Azure AD |

Senza SSO configurato, gli utenti accedono con account rtCloud locali gestiti tramite il pannello di amministrazione.

---

## Keycloak integrato

Il deployment include un container Keycloak opzionale che viene eseguito insieme a rtCloud. Keycloak è pre-configurato con un realm rtSurvey ed è pronto all'uso.

### Requisiti

- Un nome di dominio con HTTPS (Keycloak richiede HTTPS in produzione)
- Almeno 4 GB di RAM sul server (Keycloak aggiunge circa 512 MB di utilizzo della memoria)

### Configurazione

**1. Configura le variabili d'ambiente in `.env`:**

```dotenv
# Abilita il container Keycloak integrato
EMBED_KEYCLOAK=true

# URL di Keycloak — usa il tuo dominio effettivo
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Impostazioni realm e client (corrispondono al realm JSON importato)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Credenziali admin Keycloak
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Database Keycloak (creato automaticamente)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Porta su cui Keycloak è in ascolto (lato host, proxiato da Nginx)
KEYCLOAK_PORT=8091
```

**2. Avvia con il profilo Keycloak integrato:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Verifica che Keycloak sia in salute:**

```bash
docker compose -f docker-compose.production.yml ps
```

Il container `rtcloud-keycloak` dovrebbe mostrare `Up (healthy)` dopo 2–3 minuti.

**4. Accedi alla console di amministrazione Keycloak:**

```
https://rtcloud.example.com/auth/admin
```

Accedi con `KEYCLOAK_ADMIN_USER` e `KEYCLOAK_ADMIN_PASSWORD`.

### Cosa è pre-configurato

Il Keycloak integrato si avvia con un realm `rtsurvey` pre-importato che include:

- Configurazione client per l'applicazione web
- Ruoli utente predefiniti (`admin`, `project_manager`, `enumerator`, `analyst`)
- Impostazioni di sessione e token ottimizzate per rtSurvey

Puoi aggiungere utenti direttamente nella console di amministrazione Keycloak o connettere Keycloak a un provider di identità upstream (LDAP, SAML).

### Routing Nginx

Quando si usano gli script di deployment cloud, Nginx è configurato per fare proxy a entrambi i servizi:

| Percorso | Backend |
|------|---------|
| `/` | App rtCloud su `127.0.0.1:8080` |
| `/auth/` | Keycloak su `127.0.0.1:8090` |

---

## Provider OIDC esterno

Connetti rtCloud a qualsiasi provider di identità compatibile con OpenID Connect. Questo approccio non richiede il container Keycloak.

### Provider supportati

Funziona qualsiasi provider conforme a OIDC, inclusi:
- Authentik
- Auth0
- Okta
- Keycloak (istanza esterna)
- Supabase
- Google (per le organizzazioni Google Workspace)
- GitHub (tramite app OAuth con estensione OIDC)

### Configurazione

**1. Registra rtCloud come client OIDC nel tuo provider di identità.**

Avrai bisogno di:
- Un **ID client** e un **segreto client**
- Registrare l'**URI di reindirizzamento**: `https://rtcloud.example.com/auth/callback`
- Per il supporto dell'app mobile, registra anche: `vn.rta.rtsurvey.auth://callback`

**2. Configura le variabili d'ambiente in `.env`:**

```dotenv
# URL di discovery OIDC (specifico del provider — controlla la documentazione del tuo IdP)
OIDC_ISSUER_URL=https://your-identity-provider.com

# Credenziali client dal tuo provider di identità
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# Scope da richiedere (openid, profile ed email sono generalmente sufficienti)
OIDC_SCOPE=openid profile email

# URI di reindirizzamento registrato nel tuo provider di identità
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Opzionale: client separato per l'app mobile
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Imposta a true per creare automaticamente account rtCloud per nuovi utenti OIDC
OPEN_REGISTRATION=false
```

**3. Riavvia il container dell'app per applicare le modifiche:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Provisioning automatico degli utenti

Quando `OPEN_REGISTRATION=true`, rtCloud crea automaticamente un account locale la prima volta che un utente accede tramite OIDC. L'account viene popolato con il nome e l'email dell'utente dal token ID.

Quando `OPEN_REGISTRATION=false` (predefinito), un amministratore rtCloud deve creare prima l'account utente, e l'identità OIDC viene collegata al primo accesso.

### Endpoint personalizzati

Se il tuo provider non supporta il discovery OIDC (`.well-known/openid-configuration`), puoi impostare gli endpoint manualmente:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory

Integra rtCloud con il tenant Microsoft Azure AD della tua organizzazione.

### Configurazione

**1. Registra una nuova app nel [Portale Azure](https://portal.azure.com):**

   - Vai su **Azure Active Directory** → **Registrazioni app** → **Nuova registrazione**
   - Nome: `rtCloud`
   - URI di reindirizzamento: `https://rtcloud.example.com/auth/callback` (tipo Web)
   - Dopo la creazione, annota l'**ID applicazione (client)** e l'**ID directory (tenant)**
   - Sotto **Certificati e segreti**, crea un nuovo segreto client

**2. Configura le variabili d'ambiente in `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Riavvia il container dell'app:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Gli utenti nel tuo tenant Azure AD possono ora accedere a rtCloud usando le loro credenziali Microsoft.

---

## Disabilitare SSO

Per tornare all'autenticazione locale, rimuovi o commenta tutte le variabili relative a SSO da `.env`, poi riavvia il container dell'app:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Se stavi usando Keycloak integrato, fermalo omettendo il flag `--profile embed-keycloak` ed eseguendo `docker compose down` seguito da `up -d` senza il profilo.
