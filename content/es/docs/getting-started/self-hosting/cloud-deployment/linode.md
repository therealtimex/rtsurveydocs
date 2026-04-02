---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Implemente rtCloud en Linode usando un StackScript. No se necesita configuración: simplemente cree el servidor y siga los pasos posteriores a la implementación."
---

## Paso 1: Inicie StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Esto abre la página StackScript en Linode Cloud Manager. Haga clic en **Implementar nuevo Linode**.

---

## Paso 2: Complete el formulario de Linode

Complete el formulario de creación de servidor estándar de Linode:

| Campo | Valor recomendado |
|-------|------------------|
| **Imagen** | Ubuntu 22.04LTS |
| **Región** | Más cerca de tus usuarios |
| **Planificar** | CPU compartida de 4 GB o más |
| **Contraseña raíz** | Establecer una contraseña segura |
| **Cortafuegos** | Sin firewall *(recomendado)* |
| **Zona horaria** *(nuestro único campo)* | La zona horaria de su servidor (predeterminada: `Asia/Ho_Chi_Minh`) |

> **¿Por qué no hay firewall?** El script de configuración necesita acceso saliente a Internet (Docker extrae, Let's Encrypt). El bloqueo de puertos durante el primer arranque puede provocar que falle la implementación. Puede conectar un firewall una vez completada la configuración; consulte [Reglas de firewall](#firewall-rules-linode-cloud-firewall) a continuación para conocer las reglas correctas.

Haga clic en **Crear Linode** cuando haya terminado.

---

## Paso 3: Espere a que se complete la configuración

El script se ejecuta automáticamente en el primer arranque. Instala Docker, extrae la imagen rtSurvey, inicializa la base de datos e inicia todos los servicios. Esto lleva **entre 5 y 10 minutos**.

Puede ver el progreso directamente en **Linode Cloud Manager**; no se requiere SSH:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Haga clic en su Linode recién creado
3. Haga clic en **Iniciar consola LISH** (arriba a la derecha de la página de detalles de Linode)

Se abre una terminal del navegador que muestra el registro de inicio en vivo: la pestaña **Weblish** funciona directamente en su navegador, no se necesita un cliente SSH.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Espere hasta que vea:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

El registro también muestra la IP de su servidor; la necesitará para el siguiente paso.

---

## Paso 4: configurar SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Siga la **[Guía de configuración de SSL →](../ssl-setup)** para configurar HTTPS. El subdominio gratuito **rtsurvey.com** es la opción más rápida: no es necesario configurar DNS.

---

## Paso 5: cambiar la contraseña predeterminada

Todas las contraseñas predeterminadas son "admin". Cámbielos inmediatamente después de su primer inicio de sesión:

- **Contraseña de administrador de la aplicación**: configuración de la cuenta dentro de la aplicación
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Reglas de firewall (Linode Cloud Firewall)

Si adjunta un Linode Cloud Firewall a este servidor, utilice las siguientes reglas:

### Entrante

| Etiqueta | Acción | Protocolo | Puerto | Fuentes | Notas |
|-------|--------|----------|------|---------|-------|
| `aceptar-ssh-entrante` | Aceptar | TCP | 22 | Todo IPv4, Todo IPv6 | Acceso SSH |
| `aceptar-http-entrante` | Aceptar | TCP | 80 | Todo IPv4, Todo IPv6 | Nginx (desafío HTTP + ACME) |
| `aceptar-entrante-https` | Aceptar | TCP | 443 | Todo IPv4, Todo IPv6 | Nginx (HTTPS después de la configuración SSL) |
| `aceptar-entrante-brillante` | Aceptar | TCP | 3838 | Todo IPv4, Todo IPv6 | Servidor Shiny (análisis R) |
| `aceptar-icmp-entrante` | Aceptar | ICMP | — | Todo IPv4, Todo IPv6 | Ping / diagnóstico |
| Política de entrada predeterminada | **Soltar** | | | | Bloquear todo lo demás |

### Saliente

| Etiqueta | Acción | Notas |
|-------|--------|-------|
| Política de salida predeterminada | **Aceptar** | Permitir todas las salidas (extracciones de Docker, certbot, API de GoDaddy, etc.) |

### Puertos NO necesarios externamente

Estos puertos están vinculados únicamente a `127.0.0.1` y nunca se puede acceder a ellos desde fuera del servidor:

| Puerto | Servicio | Razón |
|------|---------|--------|
| 8080 | Contenedor de aplicaciones | Nginx lo proxy internamente |
| 8090 | Contenedor Keycloak | Nginx lo proxy internamente |
| 3306 | MySQL | Sólo red interna Docker |

---

## Solución de problemas

### Verifique el registro de configuración

```bash
tail -200 /var/log/stackscript.log
```

### Verifique el registro SSL

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Ver el estado del contenedor

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
