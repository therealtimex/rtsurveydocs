---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Брзи почетак"
icon: "play_circle"
toc: true
description: "Поставите rtCloud на сопственом серверу за неколико минута помоћу аутоматизованог скрипта."
---

Овај водич помаже вам да покренете rtCloud на сопственом серверу. Аутоматизоване скрипте бринуо о свему — Docker, SSL, бази података, заштитном зиду — у jedном покретању.

## Захтеви

### Сервер

| Ресурс | Минимум | Препоручено |
|--------|---------|-----------|
| RAM | 2 GB | 4 GB (потребно са Keycloak SSO) |
| Диск | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Домен

Потребно је доменско ime са **A записом koji упућује на IP сервера** пре покретања скрипте. Let's Encrypt захтева DNS резолуцију за издавање SSL сертификата.

---

## Изаберите провајдера облака

Изаберите свог провајдера испод. Сваки има аутоматизовану скрипту која се покреће при prvом boot-у и завршава подешавање за **5–10 минута**.

| Провајдер | Водич |
|---------|------|
| Linode (Akamai) | [Постављање на Linode](../cloud-deployment/linode) — najlakše, podešavanje zasnovano na formi putem StackScript |
| DigitalOcean | [Постављање на DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Постављање на AWS](../cloud-deployment/aws) |
| Google Cloud | [Постављање на GCP](../cloud-deployment/gcp) |

> **Препоручено за већину корисника:** Почните са Linode — StackScript пружа UI на основу форме, тако да нема ничега за ручно уређивање.
