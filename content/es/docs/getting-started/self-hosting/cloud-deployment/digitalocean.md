---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Implemente rtCloud en un Droplet de DigitalOcean usando scripts de datos de usuario automatizados."
---

DigitalOcean usa scripts de **Datos de usuario** que se ejecutan automáticamente en el primer arranque. Complete las variables de configuración en la parte superior del script y luego pegue el script completo al crear un Droplet.

> A diferencia de los StackScripts de Linode, DigitalOcean no tiene una interfaz de formulario — debe editar el script directamente antes de pegarlo.

**Descargar script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Keycloak integrado (Recomendado)

Use `digitalocean-droplet-keycloak-embed.sh` para la configuración más simple con SSO integrado.

### Paso 1 — Complete la configuración

Abra el script y edite el bloque `CONFIGURATION` en la parte superior:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"                  # Identificador único para su proyecto (sin espacios)
ADMIN_PASSWORD="admin"                 # Contraseña para el administrador de la aplicación y Keycloak — cámbiela después del primer inicio de sesión

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Su dominio — el registro A de DNS debe apuntar aquí
PROJECT_URL=""                         # Deje en blanco a menos que esté detrás de Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Correo electrónico para notificaciones de Let's Encrypt

# --- Optional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Campo | Requerido | Descripción |
|-------|----------|-------------|
| `PROJECT_ID` | Sí | Se usa como nombre de base de datos e ID de cliente de Keycloak. Minúsculas, sin espacios. |
| `ADMIN_PASSWORD` | No | Contraseña para el inicio de sesión del administrador de la aplicación y la consola de administración de Keycloak. Predeterminado en `admin` — **cámbiela después del primer inicio de sesión**. |
| `DOMAIN` | Sí | Su nombre de dominio. El registro A de DNS debe apuntar a la IP del Droplet. |
| `LETSENCRYPT_EMAIL` | Sí | Dirección de correo electrónico para notificaciones de certificados de Let's Encrypt. |
| `PROJECT_URL` | No | Anule la URL pública. Deje en blanco para usar `DOMAIN`. Útil detrás de Cloudflare. |

> **Seguridad:** Todas las contraseñas tienen `admin` como valor predeterminado. Cámbielas inmediatamente después de su primer inicio de sesión.

### Paso 2 — Cree un Droplet

En el [panel de control de DigitalOcean](https://cloud.digitalocean.com):

1. Haga clic en **Crear** → **Droplets**
2. Elija **Ubuntu 22.04 LTS** como imagen
3. Seleccione **Basic, 4 GB RAM / 2 vCPUs** o superior
4. Desplácese hasta **Opciones avanzadas** → marque **Agregar scripts de inicialización**
5. Pegue el contenido completo del script en el área de texto
6. Haga clic en **Crear Droplet**

### Paso 3 — Agregue el registro DNS

Mientras el Droplet se inicia, agregue un **registro A** en su proveedor de DNS:

```
Type  : A
Name  : myapp          (o @ para dominio raíz)
Value : <droplet-ip>
TTL   : 300
```

### Paso 4 — Monitoree el progreso

Conéctese por SSH al Droplet y observe el registro:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

El script imprime la IP de su servidor cerca del inicio — agregue el registro DNS tan pronto como lo vea.

### Paso 5 — Acceda a la aplicación

Cuando se complete la configuración, el registro muestra un resumen:

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

Abra `https://myapp.example.com` en su navegador e inicie sesión con el usuario `admin` y contraseña `admin`.

> **Cambie su contraseña** inmediatamente después del inicio de sesión a través de **Configuración** en el menú superior derecho.

---

## Después de la implementación

### Cambiar una contraseña

Conéctese por SSH al Droplet, edite `.env` y reinicie el contenedor afectado:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Actualizar el dominio

Si asigna un dominio diferente después de la implementación, actualice `PROJECT_URL` en `.env`:

```bash
nano /opt/rtcloud/.env   # actualice PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Ver todos los contenedores

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
