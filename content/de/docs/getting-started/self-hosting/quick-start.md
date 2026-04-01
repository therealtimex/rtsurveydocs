---
weight: 1
date: "2026-03-12T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
title: "Schnellstart"
icon: "play_circle"
toc: true
description: "Stellen Sie rtCloud in Minuten auf Ihrem eigenen Server mit einem automatisierten Cloud-Skript bereit."
---

Diese Anleitung hilft Ihnen, rtCloud auf Ihrem eigenen Server zum Laufen zu bringen. Die automatisierten Skripte erledigen alles — Docker, SSL, Datenbank, Firewall — in einem einzigen Durchlauf.

## Anforderungen

### Server

| Ressource | Minimum | Empfohlen |
|-----------|---------|----------|
| RAM | 2 GB | 4 GB (erforderlich bei Keycloak SSO) |
| Festplatte | 25 GB | 40 GB |
| CPU | 1 vCPU | 2 vCPUs |
| Betriebssystem | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |

### Domain

Sie benötigen einen Domainnamen mit einem **A-Eintrag, der auf die IP-Adresse des Servers zeigt**, bevor Sie das Skript ausführen. Let's Encrypt erfordert DNS-Auflösung für die SSL-Zertifikatsausstellung.

---

## Wählen Sie Ihren Cloud-Anbieter

Wählen Sie Ihren Anbieter unten. Jeder hat ein automatisiertes Skript, das beim ersten Start ausgeführt wird und die Einrichtung in **5–10 Minuten** abschließt.

| Anbieter | Anleitung |
|----------|----------|
| Linode (Akamai) | [Bereitstellen auf Linode](../cloud-deployment/linode) — am einfachsten, formularbasierte Einrichtung via StackScript |
| DigitalOcean | [Bereitstellen auf DigitalOcean](../cloud-deployment/digitalocean) |
| AWS EC2 | [Bereitstellen auf AWS](../cloud-deployment/aws) |
| Google Cloud | [Bereitstellen auf GCP](../cloud-deployment/gcp) |

> **Empfohlen für die meisten Nutzer:** Beginnen Sie mit Linode — der StackScript bietet eine formularbasierte Benutzeroberfläche, sodass nichts manuell bearbeitet werden muss.
