---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Snabbstart"
icon: "play_circle"
toc: true
description: "Driftsätt rtCloud på din egen server på några minuter med ett automatiserat molnskript."
---

Den här guiden hjälper dig att få igång rtCloud på din egen server. De automatiserade skripten tar hand om allt — Docker, SSL, databas, brandvägg — i en enda körning.

## Krav

### Server

| Resurs | Minimum | Rekommenderat |
|--------|---------|--------------|
| RAM | 2 GB | 4 GB (krävs med Keycloak SSO) |
| Disk | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domän

Du behöver ett domännamn med en **A-post som pekar på serverns IP** innan du kör skriptet. Let's Encrypt kräver DNS-upplösning för att utfärda SSL-certifikat.

---

## Välj din molnleverantör

Välj din leverantör nedan. Var och en har ett automatiserat skript som körs vid första uppstarten och slutför inställningen på **5–10 minuter**.

| Leverantör | Guide |
|-----------|-------|
| Linode (Akamai) | [Driftsätt på Linode](../cloud-deployment/linode) — enklast, formulärbaserad inställning via StackScript |
| DigitalOcean | [Driftsätt på DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Driftsätt på AWS](../cloud-deployment/aws) |
| Google Cloud | [Driftsätt på GCP](../cloud-deployment/gcp) |

> **Rekommenderas för de flesta:** Börja med Linode — StackScript ger ett formulärbaserat gränssnitt så det finns inget att redigera manuellt.
