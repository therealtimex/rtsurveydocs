---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "Vendosni rtCloud në një instancë AWS EC2 duke përdorur skriptin user data aws-ec2.sh."
---

Përdorni `aws-ec2.sh` si skriptin **User Data** kur hapni një instancë EC2. Skripti ekzekutohet automatikisht në nisjen e parë.

**Shkarkoni skriptin:** [aws-ec2.sh](/scripts/aws-ec2.sh)

---

## Hapi 1 — Plotësoni konfigurimin

Hapni skriptin dhe editoni bllokun `CONFIGURATION` në krye:

```bash
# --- E detyrueshme ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Ndryshojeni pas hyrjes së parë

# --- Domeni + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Keycloak i Integruar ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Parazgjedhja ADMIN_PASSWORD
```

| Fusha | E detyrueshme | Përshkrimi |
|-------|----------|-------------|
| `PROJECT_ID` | Po | Përdoret si emri i bazës së të dhënave dhe ID klientit Keycloak. Me shkronja të vogla, pa hapësira. |
| `ADMIN_PASSWORD` | Jo | Fjalëkalimi i adminit të aplikacionit dhe fjalëkalimi admin Keycloak. Parazgjedhja `admin` — **ndryshojeni pas hyrjes së parë**. |
| `DOMAIN` | Jo | Domeni juaj për HTTPS. Lini bosh për mënyrën vetëm HTTP. |
| `LETSENCRYPT_EMAIL` | Po (nëse DOMAIN është caktuar) | Email për njoftimet Let's Encrypt. |
| `EMBED_KEYCLOAK` | Jo | `true` për të vendosur Keycloak të integruar (kërkon 4 GB RAM). |

> **Siguria:** Të gjitha fjalëkalimet parazgjidhen me `admin`. Ndryshojini menjëherë pas hyrjes suaj të parë.

---

## Hapi 2 — Hapni një instancë EC2

Në [konsolën AWS EC2](https://console.aws.amazon.com/ec2):

1. Klikoni **Hap instancë**
2. **AMI:** Ubuntu Server 22.04 LTS (64-bit x86)
3. **Tipi i instancës:** `t3.medium` (4 GB RAM) ose më i madh
4. **Çifti i çelësave:** Zgjidhni ose krijoni një për akses SSH
5. **Cilësimet e rrjetit:** Krijoni ose zgjidhni një Grup Sigurie (shikoni më poshtë)
6. **Detajet e avancuara** → **Të dhënat e përdoruesit** → ngjitni të gjithë përmbajtjen e skriptit
7. Klikoni **Hap instancë**

---

## Hapi 3 — Konfiguroni Grupin e Sigurisë

Hapni këto porta në Grupin e Sigurisë të instancës:

| Porta | Protokolli | Burimi | Qëllimi |
|------|----------|--------|---------|
| 22 | TCP | IP-ja juaj | Aksesi SSH |
| 80 | TCP | 0.0.0.0/0 | HTTP (ridrejtuar në HTTPS nga Nginx) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Aksesi direkt Shiny |

> **Mos** hapni portën 3306 (MySQL) — nuk duhet të jetë kurrë publikisht e aksesueshme.

---

## Hapi 4 — Shtoni rekordin DNS

Ndërkohë që instanca po niset, shtoni një **rekord A** te ofruesi juaj DNS:

```
Tipi  : A
Emri  : myapp
Vlera : <ip-publike-e-instancës>
TTL   : 300
```

---

## Hapi 5 — Monitoroni progresin

```bash
ssh ubuntu@<instance-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Hapi 6 — Aksesoni aplikacionin

Kur konfigurimi përfundon, regjistri tregon një përmbledhje me URL-n e aplikacionit dhe kredencialet. Hyni me emrin e përdoruesit `admin` dhe fjalëkalimin `admin`, pastaj ndryshoni fjalëkalimin menjëherë.

---

## Pas Vendosjes

### Ndryshoni një fjalëkalim

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Shikoni të gjithë kontejnerët

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Caktoni një IP Elastic (opsionale)

Nëse ndaloni dhe nisni instancën, IP-ja publike ndryshon. Për të mbajtur një IP të qëndrueshme, alokoni një **IP Elastic** dhe asociojeni me instancën në konsolën EC2.
