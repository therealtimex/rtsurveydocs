---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Hurtig start"
icon: "play_circle"
toc: true
description: "Implementér rtCloud på din egen server på få minutter med et automatiseret cloudscript."
---

Denne guide hjælper dig med at få rtCloud kørende på din egen server. De automatiserede scripts tager sig af alt — Docker, SSL, database, firewall — i én kørsel.

## Krav

### Server

| Ressource | Minimum | Anbefalet |
|-----------|---------|----------|
| RAM | 2 GB | 4 GB (kræves ved brug af Keycloak SSO) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domæne

Du skal bruge et domænenavn med en **A-post der peger på serverens IP** inden scriptet køres. Let's Encrypt kræver DNS-opløsning for at udstede SSL-certifikat.

---

## Vælg din cloudleverandør

Vælg din leverandør nedenfor. Hver har et automatiseret script der kører ved første opstart og fuldfører opsætningen på **5–10 minutter**.

| Leverandør | Guide |
|-----------|-------|
| Linode (Akamai) | [Implementér på Linode](../cloud-deployment/linode) — nemmest, formularbaseret opsætning via StackScript |
| DigitalOcean | [Implementér på DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Implementér på AWS](../cloud-deployment/aws) |
| Google Cloud | [Implementér på GCP](../cloud-deployment/gcp) |

> **Anbefalet for de fleste:** Start med Linode — StackScript giver en formularbaseret brugergrænseflade så der ikke er noget at redigere manuelt.
