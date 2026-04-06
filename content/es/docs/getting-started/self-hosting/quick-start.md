---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Inicio rápido"
icon: "play_circle"
toc: true
description: "Despliegue rtCloud en su propio servidor en minutos con un script de nube automatizado."
---

Esta guía le ayuda a poner en marcha rtCloud en su propio servidor. Los scripts automatizados se encargan de todo — Docker, SSL, base de datos, firewall — en una sola ejecución.

## Requisitos

### Servidor

| Recurso | Mínimo | Recomendado |
|---------|--------|------------|
| RAM | 2 GB | 4 GB (necesario con Keycloak SSO) |
| Disco | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| SO | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Dominio

Necesita un nombre de dominio con un **registro A apuntando a la IP del servidor** antes de ejecutar el script. Let's Encrypt requiere resolución DNS para emitir el certificado SSL.

---

## Elija su proveedor de nube

Seleccione su proveedor a continuación. Cada uno tiene un script automatizado que se ejecuta en el primer arranque y completa la configuración en **5–10 minutos**.

| Proveedor | Guía |
|-----------|------|
| Linode (Akamai) | [Desplegar en Linode](../cloud-deployment/linode) — más fácil, configuración basada en formulario via StackScript |
| DigitalOcean | [Desplegar en DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Desplegar en AWS](../cloud-deployment/aws) |
| Google Cloud | [Desplegar en GCP](../cloud-deployment/gcp) |

> **Recomendado para la mayoría:** Comience con Linode — el StackScript proporciona una interfaz basada en formulario para que no haya nada que editar manualmente.
