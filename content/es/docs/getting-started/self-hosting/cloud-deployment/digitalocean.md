---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Implemente rtCloud en un DigitalOcean Droplet utilizando scripts automatizados de datos de usuario."
---

DigitalOcean utiliza scripts de **Datos de usuario** que se ejecutan automáticamente en el primer arranque. Usted completa las variables de configuración en la parte superior del script y luego pega el script completo al crear un Droplet.

> A diferencia de Linode StackScripts, DigitalOcean no tiene una interfaz de usuario con formulario: debe editar el script directamente antes de pegarlo.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Capa de llaves integrada (recomendada)

Utilice `digitalocean-droplet-keycloak-embed.sh` para realizar la configuración más sencilla con SSO integrado.

### Paso 1: Complete la configuración

Abra el script y edite el bloque `CONFIGURACIÓN` en la parte superior:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"                  # Unique identifier for your project (no spaces)
ADMIN_PASSWORD="admin"                 # Password for app admin and Keycloak — change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Your domain — DNS A record must point here
PROJECT_URL=""                         # Leave blank unless behind Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email for Let's Encrypt notifications

# --- Optional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Campo | Requerido | Descripción |
|-------|----------|-------------|
| `ID_PROYECTO` | Sí | Se utiliza como nombre de la base de datos e ID del cliente Keycloak. Minúsculas, sin espacios. |
| `CONTRASEÑA_ADMIN` | No | Contraseña para iniciar sesión como administrador de la aplicación y para la consola de administración de Keycloak. El valor predeterminado es `admin`: **cambia después del primer inicio de sesión**. |
| `DOMINIO` | Sí | Su nombre de dominio. El registro DNS A debe apuntar a la IP del Droplet. |
| `LETSENCRYPT_EMAIL` | Sí | Dirección de correo electrónico para notificaciones de certificados de Let's Encrypt. |
| `PROJECT_URL` | No | Anule la URL pública. Déjelo en blanco para usar `DOMINIO`. Útil detrás de Cloudflare. |

> **Seguridad:** Todas las contraseñas predeterminadas son `admin`. Cámbielos inmediatamente después de su primer inicio de sesión.

### Paso 2: crear una gota

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Haga clic en **Crear** → **Gotas**
2. Elija **Ubuntu 22.04 LTS** como imagen
3. Seleccione **Básico, 4 GB de RAM / 2 vCPU** o más
4. Desplácese hasta **Opciones avanzadas** → marque **Agregar scripts de inicialización**
5. Pegue el contenido completo del script en el área de texto.
6. Haga clic en **Crear gota**

### Paso 3: agregue el registro DNS

Mientras se inicia el Droplet, agregue un **registro A** en su proveedor de DNS:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### Paso 4: Supervisar el progreso

SSH en el Droplet y observe el registro:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

El script imprime la IP de su servidor cerca del inicio; agregue el registro DNS tan pronto como lo vea.

### Paso 5: accede a la aplicación

Cuando se completa la configuración, el registro muestra un resumen:

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

Open `https://myapp.example.com` in your browser and log in with username `admin` and password `admin`.

> **Cambie su contraseña** inmediatamente después de iniciar sesión a través de **Configuración** en el menú superior derecho.

---

## Después de la implementación

### Cambiar una contraseña

SSH en el Droplet, edite `.env` y reinicie el contenedor afectado:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Actualizar el dominio

Si asigna un dominio diferente después de la implementación, actualice `PROJECT_URL` en `.env`:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Ver todos los contenedores

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
