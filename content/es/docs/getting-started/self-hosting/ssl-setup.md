---
weight: 4
title: "Configurar SSL"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Configure HTTPS para su servidor rtSurvey. Requerido antes de iniciar sesión."
---

SSL debe configurarse antes de que pueda iniciar sesión. Cuando abra la aplicación por primera vez, será redirigido automáticamente a la pantalla de configuración de SSL.

---

## Opciones de configuración SSL

![Opciones de configuración SSL](/img/ssl-setup/ssl-setup-options.png)

Elija una de tres opciones:

| Opción | Cuándo usar |
|--------|-------------|
| **Subdominio gratuito rtsurvey.com** *(Recomendado)* | No se necesita configuración DNS. Creamos el registro por usted. Listo en 2–5 minutos. |
| **Mi propio dominio** | Ya tiene un dominio y su DNS apunta a este servidor. |
| **Instalar certificado manualmente** | Empresa o CA personalizado. Requiere acceso SSH. |

---

## Opción 1 — Subdominio gratuito rtsurvey.com *(Recomendado)*

Esta es la opción más rápida. No se requiere registro de dominio ni cambios DNS.

1. Haga clic en **Subdominio gratuito rtsurvey.com** para expandir la sección
2. Escriba el nombre de subdominio deseado en el campo de entrada

   > Use letras minúsculas, números y guiones. 3–30 caracteres.
   > Ejemplo: `myproject` → `myproject.rtsurvey.com`

3. Haga clic en **Crear https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Espere 2–5 minutos mientras se emite el certificado

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Una vez listo el certificado, será redirigido automáticamente a su nueva URL HTTPS

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Opción 2 — Mi propio dominio

Use esto si tiene un dominio existente y su registro DNS `A` ya apunta a la IP de este servidor.

1. Haga clic en **Mi propio dominio** para expandir la sección
2. Ingrese su nombre de dominio completo (p.ej. `survey.myorganization.org`)
3. Haga clic en **Crear certificado**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt verificará su dominio y emitirá un certificado. Requiere que el DNS esté correctamente apuntado primero — la solicitud fallará de lo contrario.

---

## Opción 3 — Instalar certificado manualmente

Para entornos empresariales con CA personalizado o interno. Colocará sus archivos de certificado en el servidor mediante SSH y luego ingresará su dominio en la aplicación.

### Requisitos previos

- Acceso SSH al servidor
- Certificado válido y clave privada para su dominio (formato PEM)

### Paso 1 — SSH al servidor

```bash
ssh root@<server-ip>
```

### Paso 2 — Coloque sus archivos de certificado

Cree el directorio y copie sus archivos:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Copie sus archivos con estos nombres exactos:

| Archivo | Descripción |
|---------|-------------|
| `fullchain.pem` | Su certificado + certificados CA intermedios (concatenados) |
| `privkey.pem` | Su clave privada |

Ejemplo:

```bash
# Copiar desde su máquina local (ejecutar localmente, no en el servidor)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Establecer permisos correctos:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Paso 3 — Ingrese su dominio en la aplicación

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. En la pantalla de configuración SSL, haga clic en **Instalar certificado manualmente**
2. Ingrese su nombre de dominio (debe coincidir con el Common Name o SAN del certificado)
3. Haga clic en **Aplicar**

El servidor configurará Nginx con su certificado y recargará automáticamente.

---

## Siguiente paso

Una vez que SSL esté activo, proceda al [Primer inicio de sesión](first-login).
