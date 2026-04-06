---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Rýchly štart"
icon: "play_circle"
toc: true
description: "Nasaďte rtCloud na vlastný server za pár minút pomocou automatizovaného cloudového skriptu."
---

Tento sprievodca vám pomôže spustiť rtCloud na vlastnom serveri. Automatizované skripty sa postarajú o všetko — Docker, SSL, databázu, bránu firewall — jedným spustením.

## Požiadavky

### Server

| Zdroj | Minimum | Odporúčané |
|-------|---------|-----------|
| RAM | 2 GB | 4 GB (nutné pri Keycloak SSO) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Doména

Pred spustením skriptu potrebujete doménové meno s **A záznamom smerujúcim na IP servera**. Let's Encrypt vyžaduje DNS rozlíšenie pre vydanie SSL certifikátu.

---

## Vyberte si poskytovateľa cloudu

Vyberte svojho poskytovateľa nižšie. Každý má automatizovaný skript, ktorý sa spustí pri prvom štarte a dokončí nastavenie za **5–10 minút**.

| Poskytovateľ | Sprievodca |
|-------------|----------|
| Linode (Akamai) | [Nasadenie na Linode](../cloud-deployment/linode) — najjednoduchšie, formulárové nastavenie cez StackScript |
| DigitalOcean | [Nasadenie na DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Nasadenie na AWS](../cloud-deployment/aws) |
| Google Cloud | [Nasadenie na GCP](../cloud-deployment/gcp) |

> **Odporúčané pre väčšinu používateľov:** Začnite s Linode — StackScript poskytuje formulárové UI, takže nie je potrebné nič ručne upravovať.
