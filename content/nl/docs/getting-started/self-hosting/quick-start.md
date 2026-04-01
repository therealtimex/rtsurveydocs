---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Snel starten"
icon: "play_circle"
toc: true
description: "Implementeer rtCloud op uw eigen server in minuten met een geautomatiseerd cloudscript."
---

Deze gids helpt u rtCloud op uw eigen server te laten draaien. De geautomatiseerde scripts regelen alles — Docker, SSL, database, firewall — in één uitvoering.

## Vereisten

### Server

| Bron | Minimum | Aanbevolen |
|------|---------|-----------|
| RAM | 2 GB | 4 GB (vereist met Keycloak SSO) |
| Schijf | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domein

U hebt een domeinnaam nodig met een **A-record dat naar het IP-adres van de server wijst** voordat u het script uitvoert. Let's Encrypt vereist DNS-omzetting voor het afgeven van het SSL-certificaat.

---

## Kies uw cloudprovider

Selecteer uw provider hieronder. Elk heeft een geautomatiseerd script dat bij de eerste opstart wordt uitgevoerd en de installatie voltooit in **5–10 minuten**.

| Provider | Gids |
|---------|------|
| Linode (Akamai) | [Implementeer op Linode](../cloud-deployment/linode) — eenvoudigst, formuliergebaseerde instelling via StackScript |
| DigitalOcean | [Implementeer op DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Implementeer op AWS](../cloud-deployment/aws) |
| Google Cloud | [Implementeer op GCP](../cloud-deployment/gcp) |

> **Aanbevolen voor de meeste gebruikers:** Begin met Linode — de StackScript biedt een formuliergebaseerde UI, zodat er niets handmatig bewerkt hoeft te worden.
