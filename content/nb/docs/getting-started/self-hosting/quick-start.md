---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Hurtigstart"
icon: "play_circle"
toc: true
description: "Distribuer rtCloud på din egen server på få minutter med et automatisert skyskript."
---

Denne veiledningen hjelper deg med å kjøre rtCloud på din egen server. De automatiserte skriptene tar seg av alt — Docker, SSL, database, brannmur — i én enkelt kjøring.

## Krav

### Server

| Ressurs | Minimum | Anbefalt |
|---------|---------|---------|
| RAM | 2 GB | 4 GB (påkrevd med Keycloak SSO) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domene

Du trenger et domenenavn med en **A-post som peker til serverens IP** før du kjører skriptet. Let's Encrypt krever DNS-oppløsning for å utstede SSL-sertifikat.

---

## Velg din skyleverandør

Velg din leverandør nedenfor. Hver har et automatisert skript som kjører ved første oppstart og fullfører oppsett på **5–10 minutter**.

| Leverandør | Veiledning |
|-----------|-----------|
| Linode (Akamai) | [Distribuer på Linode](../cloud-deployment/linode) — enklest, skjemabasert oppsett via StackScript |
| DigitalOcean | [Distribuer på DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Distribuer på AWS](../cloud-deployment/aws) |
| Google Cloud | [Distribuer på GCP](../cloud-deployment/gcp) |

> **Anbefalt for de fleste:** Start med Linode — StackScript gir et skjemabasert grensesnitt slik at det ikke er noe å redigere manuelt.
