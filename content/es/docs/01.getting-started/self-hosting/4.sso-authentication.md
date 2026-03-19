---
weight: 4
title: "Autenticación SSO"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Configure el inicio de sesión único para rtCloud autoalojado usando Keycloak integrado, un proveedor OIDC externo o Azure Active Directory."
---

rtCloud admite tres enfoques para el Inicio de sesión único (SSO):

| Opción | Mejor para |
|--------|----------|
| [Keycloak integrado](#embedded-keycloak) | Organizaciones que quieren un servidor SSO completamente autocontenido incluido con rtCloud |
| [Proveedor OIDC externo](#external-oidc-provider) | Organizaciones que ya ejecutan un proveedor de identidad (Auth0, Authentik, Okta, Supabase, etc.) |
| [Azure Active Directory](#azure-active-directory) | Organizaciones que usan Microsoft 365 o Azure AD |

Sin SSO configurado, los usuarios inician sesión con cuentas locales de rtCloud gestionadas a través del panel de administración.

---

## Keycloak integrado {#embedded-keycloak}

La implementación incluye un contenedor Keycloak opcional que se ejecuta junto a rtCloud. Keycloak viene preconfigurado con un realm de rtSurvey y listo para usar.

### Requisitos

- Un nombre de dominio con HTTPS (Keycloak requiere HTTPS en producción)
- Al menos 4 GB de RAM en el servidor (Keycloak añade ~512 MB de uso de memoria)

### Configuración

**1. Configure las variables de entorno en `.env`:**

```dotenv
# Habilitar el contenedor Keycloak integrado
EMBED_KEYCLOAK=true

# URLs de Keycloak — use su dominio real
KEYCLOAK_URL=https://rtcloud.example.com/auth
KC_HOSTNAME=https://rtcloud.example.com/auth
KC_HOSTNAME_STRICT=false

# Configuración de realm y cliente (coincide con el JSON del realm importado)
KEYCLOAK_REALM=rtsurvey
KEYCLOAK_CLIENT_ID=rtsurvey-app
KEYCLOAK_CLIENT_SECRET=your-client-secret-here

# Credenciales de administrador de Keycloak
KEYCLOAK_ADMIN_USER=admin
KEYCLOAK_ADMIN_PASSWORD=change_me_keycloak_admin_password

# Base de datos de Keycloak (creada automáticamente)
KEYCLOAK_DB=keycloak
KEYCLOAK_DB_USER=keycloak
KEYCLOAK_DB_PASSWORD=change_me_keycloak_db_password

# Puerto en el que escucha Keycloak (lado del host, proxiado por Nginx)
KEYCLOAK_PORT=8091
```

**2. Inicie con el perfil Keycloak integrado:**

```bash
docker compose -f docker-compose.production.yml --profile embed-keycloak up -d
```

**3. Verifique que Keycloak esté en buen estado:**

```bash
docker compose -f docker-compose.production.yml ps
```

El contenedor `rtcloud-keycloak` debería mostrar `Up (healthy)` después de 2–3 minutos.

**4. Acceda a la consola de administración de Keycloak:**

```
https://rtcloud.example.com/auth/admin
```

Inicie sesión con `KEYCLOAK_ADMIN_USER` y `KEYCLOAK_ADMIN_PASSWORD`.

### Qué viene preconfigurado

El Keycloak integrado inicia con un realm `rtsurvey` preimportado que incluye:

- Configuración del cliente para la aplicación web
- Roles de usuario predeterminados (`admin`, `project_manager`, `enumerator`, `analyst`)
- Configuración de sesión y token optimizada para rtSurvey

Puede agregar usuarios directamente en la consola de administración de Keycloak o conectar Keycloak a un proveedor de identidad ascendente (LDAP, SAML).

### Enrutamiento Nginx

Al usar los scripts de implementación en la nube, Nginx se configura para hacer proxy de ambos servicios:

| Ruta | Backend |
|------|---------|
| `/` | Aplicación rtCloud en `127.0.0.1:8080` |
| `/auth/` | Keycloak en `127.0.0.1:8090` |

---

## Proveedor OIDC externo {#external-oidc-provider}

Conecte rtCloud a cualquier proveedor de identidad compatible con OpenID Connect. Este enfoque no requiere el contenedor Keycloak.

### Proveedores compatibles

Cualquier proveedor compatible con OIDC funciona, incluyendo:
- Authentik
- Auth0
- Okta
- Keycloak (instancia externa)
- Supabase
- Google (para organizaciones de Google Workspace)
- GitHub (a través de aplicaciones OAuth con extensión OIDC)

### Configuración

**1. Registre rtCloud como cliente OIDC en su proveedor de identidad.**

Necesitará:
- Un **ID de cliente** y un **secreto de cliente**
- Registrar el **URI de redireccionamiento**: `https://rtcloud.example.com/auth/callback`
- Para soporte de aplicaciones móviles, también registre: `vn.rta.rtsurvey.auth://callback`

**2. Configure las variables de entorno en `.env`:**

```dotenv
# URL de descubrimiento OIDC (específica del proveedor — consulte la documentación de su IdP)
OIDC_ISSUER_URL=https://your-identity-provider.com

# Credenciales del cliente de su proveedor de identidad
OIDC_CLIENT_ID=rtcloud-app
OIDC_CLIENT_SECRET=your-client-secret-here

# Ámbitos a solicitar (openid, profile y email suelen ser suficientes)
OIDC_SCOPE=openid profile email

# URI de redireccionamiento registrado en su proveedor de identidad
OIDC_REDIRECT_URI=https://rtcloud.example.com/auth/callback

# Opcional: cliente separado para la aplicación móvil
OIDC_MOBILE_CLIENT_ID=rtcloud-mobile
OIDC_MOBILE_REDIRECT_URI=vn.rta.rtsurvey.auth://callback

# Establecer en true para crear automáticamente cuentas de rtCloud para nuevos usuarios OIDC
OPEN_REGISTRATION=false
```

**3. Reinicie el contenedor de la aplicación para aplicar los cambios:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

### Aprovisionamiento automático de usuarios

Cuando `OPEN_REGISTRATION=true`, rtCloud crea automáticamente una cuenta local la primera vez que un usuario inicia sesión a través de OIDC. La cuenta se completa con el nombre y correo electrónico del usuario del token de ID.

Cuando `OPEN_REGISTRATION=false` (predeterminado), un administrador de rtCloud debe crear primero la cuenta de usuario, y la identidad OIDC se vincula en el primer inicio de sesión.

### Puntos de conexión personalizados

Si su proveedor no admite el descubrimiento OIDC (`.well-known/openid-configuration`), puede establecer los puntos de conexión manualmente:

```dotenv
OIDC_AUTHORIZATION_ENDPOINT=https://your-provider.com/oauth2/authorize
OIDC_TOKEN_ENDPOINT=https://your-provider.com/oauth2/token
OIDC_USERINFO_ENDPOINT=https://your-provider.com/oauth2/userinfo
```

---

## Azure Active Directory {#azure-active-directory}

Integre rtCloud con el tenant de Microsoft Azure AD de su organización.

### Configuración

**1. Registre una nueva aplicación en el [Portal de Azure](https://portal.azure.com):**

   - Vaya a **Azure Active Directory** → **Registros de aplicaciones** → **Nuevo registro**
   - Nombre: `rtCloud`
   - URI de redireccionamiento: `https://rtcloud.example.com/auth/callback` (tipo Web)
   - Después de crear, anote el **ID de aplicación (cliente)** y el **ID de directorio (tenant)**
   - En **Certificados y secretos**, cree un nuevo secreto de cliente

**2. Configure las variables de entorno en `.env`:**

```dotenv
AZURE_CLIENT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
AZURE_TENANT_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

**3. Reinicie el contenedor de la aplicación:**

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Los usuarios en su tenant de Azure AD ahora pueden iniciar sesión en rtCloud con sus credenciales de Microsoft.

---

## Desactivar SSO

Para revertir a la autenticación local, elimine o comente todas las variables relacionadas con SSO de `.env`, luego reinicie el contenedor de la aplicación:

```bash
docker compose -f docker-compose.production.yml up -d --force-recreate rtcloud
```

Si estaba usando Keycloak integrado, deténgalo omitiendo el indicador `--profile embed-keycloak` y ejecutando `docker compose down` seguido de `up -d` sin el perfil.
