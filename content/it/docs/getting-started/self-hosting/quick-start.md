---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Avvio rapido"
icon: "play_circle"
toc: true
description: "Distribuisci rtCloud sul tuo server in pochi minuti con uno script cloud automatizzato."
---

Questa guida ti aiuta a mettere in funzione rtCloud sul tuo server. Gli script automatizzati gestiscono tutto — Docker, SSL, database, firewall — in una singola esecuzione.

## Requisiti

### Server

| Risorsa | Minimo | Consigliato |
|---------|--------|------------|
| RAM | 2 GB | 4 GB (necessario con Keycloak SSO) |
| Disco | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Dominio

È necessario un nome di dominio con un **record A che punta all'IP del server** prima di eseguire lo script. Let's Encrypt richiede la risoluzione DNS per il rilascio del certificato SSL.

---

## Scegli il tuo provider cloud

Seleziona il tuo provider qui sotto. Ognuno ha uno script automatizzato che viene eseguito al primo avvio e completa la configurazione in **5–10 minuti**.

| Provider | Guida |
|---------|-------|
| Linode (Akamai) | [Distribuisci su Linode](../cloud-deployment/linode) — più semplice, configurazione basata su modulo via StackScript |
| DigitalOcean | [Distribuisci su DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Distribuisci su AWS](../cloud-deployment/aws) |
| Google Cloud | [Distribuisci su GCP](../cloud-deployment/gcp) |

> **Consigliato per la maggior parte degli utenti:** Inizia con Linode — lo StackScript fornisce un'interfaccia basata su modulo, quindi non c'è nulla da modificare manualmente.
