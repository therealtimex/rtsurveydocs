---
weight: 115
title: "Autoalojamiento"
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-03-12T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Implemente y gestione su propia instancia de rtCloud usando Docker. Control total sobre sus datos, infraestructura y configuración."
---

Ejecute rtCloud en su propia infraestructura usando Docker Compose. El autoalojamiento le brinda propiedad completa de sus datos, red y entorno de implementación — ideal para organizaciones con requisitos de residencia de datos, redes aisladas o necesidades de infraestructura personalizada.

## ¿Qué es el autoalojamiento de rtCloud?

El autoalojamiento de rtCloud es una imagen oficial de Docker que empaqueta toda la plataforma rtCloud en una pila de contenedores portátil que puede ejecutar en cualquier servidor Linux. La pila incluye:

| Servicio | Descripción |
|---------|-------------|
| **Aplicación rtCloud** | Aplicación web Apache 2.4 + PHP 7.4 con cola en segundo plano integrada (Beanstalkd), servidor de análisis (Shiny) y tareas programadas |
| **MySQL 8.0** | Base de datos relacional para todos los datos de la aplicación y de las encuestas |
| **Keycloak** *(opcional)* | Servidor de Inicio de sesión único integrado para la gestión de identidades empresariales |

## Cuándo autoalojar

El autoalojamiento es la opción correcta cuando usted:

- Requiere **soberanía de datos** — todos los datos permanecen dentro de su propia infraestructura
- Opera en una **red aislada o restringida** sin acceso a la nube externa
- Tiene **requisitos de cumplimiento** (GDPR, HIPAA, políticas de datos gubernamentales) que exigen almacenamiento en las instalaciones
- Necesita integrarse con un **proveedor de identidad interno** (Active Directory, LDAP, SAML)
- Quiere **personalizar los recursos** — asignación de CPU, RAM y almacenamiento según sus condiciones

## En esta sección

| Página | Descripción |
|------|-------------|
| [Inicio rápido](quick-start) | Ponga en marcha rtCloud en un servidor en menos de 10 minutos |
| [Referencia de configuración](configuration) | Lista completa de todas las variables de entorno y sus valores predeterminados |
| [Implementación en la nube](cloud-deployment) | Scripts automatizados con un clic para DigitalOcean, AWS, GCP y Linode |
| [Autenticación SSO](sso-authentication) | Configure Keycloak, OIDC externo o Azure AD |
| [Mantenimiento](maintenance) | Actualice, haga copias de seguridad, restaure y solucione problemas de su instancia |

## Descripción general de la arquitectura

La implementación se ejecuta como un conjunto de contenedores Docker conectados en una red interna:

```
┌────────────────────────────────────────┐
│            rtcloud-app                 │
│  Apache 2.4 (port 80)                  │
│  PHP 7.4 application                   │
│  Beanstalkd queue (internal)           │
│  Shiny Server (port 3838)              │
│  Cron scheduler                        │
└─────────────────┬──────────────────────┘
                  │ rtcloud-net (bridge)
┌─────────────────▼──────────────────────┐
│            rtcloud-mysql               │
│  MySQL 8.0 (port 3306, internal only)  │
└────────────────────────────────────────┘
```

Cuando SSO está habilitado, un tercer contenedor se ejecuta junto:

```
┌─────────────────────────────────────────┐
│            rtcloud-keycloak             │
│  Keycloak (port 8080, internal only)    │
│  Admin UI (port 9000, internal only)    │
└─────────────────────────────────────────┘
```

Todos los contenedores se comunican a través de una red de puente Docker aislada. Solo el puerto de la aplicación web y (opcionalmente) el puerto de análisis Shiny quedan expuestos al host.
