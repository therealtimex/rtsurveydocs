---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Gyors kezdés"
icon: "play_circle"
toc: true
description: "Telepítse az rtCloud-ot saját szerverére percek alatt automatizált felhő-szkripttel."
---

Ez az útmutató segít az rtCloud saját szerveren való elindításában. Az automatizált szkriptek mindent elvégeznek — Docker, SSL, adatbázis, tűzfal — egyetlen futtatással.

## Követelmények

### Szerver

| Erőforrás | Minimum | Ajánlott |
|-----------|---------|---------|
| RAM | 2 GB | 4 GB (szükséges Keycloak SSO esetén) |
| Lemez | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domain

A szkript futtatása előtt szükség van egy domainnevre, amelynek **A rekordja a szerver IP-jére mutat**. A Let's Encrypt DNS-feloldást igényel az SSL-tanúsítvány kiállításához.

---

## Válasszon felhőszolgáltatót

Válassza ki a szolgáltatóját alább. Mindegyiknek van automatizált szkriptje, amely az első indításkor fut le és **5–10 percen belül** befejezi a beállítást.

| Szolgáltató | Útmutató |
|------------|---------|
| Linode (Akamai) | [Telepítés Linode-ra](../cloud-deployment/linode) — legegyszerűbb, StackScript alapú form-vezérelt beállítás |
| DigitalOcean | [Telepítés DigitalOcean-ra](../cloud-deployment/digitalocean) |
| AWS EC2 | [Telepítés AWS-re](../cloud-deployment/aws) |
| Google Cloud | [Telepítés GCP-re](../cloud-deployment/gcp) |

> **A legtöbb felhasználónak ajánlott:** Kezdje a Linode-dal — a StackScript form alapú felületet biztosít, így semmit sem kell manuálisan szerkeszteni.
