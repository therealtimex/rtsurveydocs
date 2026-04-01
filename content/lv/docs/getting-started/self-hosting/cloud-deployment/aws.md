---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "Izvietojiet rtCloud uz AWS EC2 instances, izmantojot aws-ec2.sh user data skriptu."
---

Izmantojiet `aws-ec2.sh` kā **User Data** skriptu, palaižot EC2 instanci. Skripts automātiski darbojas pirmajā palaišanā.

**Lejupielādēt skriptu:** [aws-ec2.sh](/scripts/aws-ec2.sh)

---

## 1. solis — Aizpildiet konfigurāciju

Atveriet skriptu un rediģējiet `CONFIGURATION` bloku augšpusē:

```bash
# --- Obligāts ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Mainiet pēc pirmās pieteikšanās

# --- Domēns + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Iebūvētais Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Noklusējums ir ADMIN_PASSWORD
```

| Lauks | Obligāts | Apraksts |
|-------|----------|-------------|
| `PROJECT_ID` | Jā | Izmanto kā datu bāzes nosaukumu un Keycloak klienta ID. Maziem burtiem, bez atstarpēm. |
| `ADMIN_PASSWORD` | Nē | Lietotnes administratora parole un Keycloak administratora parole. Noklusējums ir `admin` — **mainiet pēc pirmās pieteikšanās**. |
| `DOMAIN` | Nē | Jūsu domēns HTTPS. Atstājiet tukšu tikai HTTP režīmam. |
| `LETSENCRYPT_EMAIL` | Jā (ja DOMAIN iestatīts) | E-pasts Let's Encrypt paziņojumiem. |
| `EMBED_KEYCLOAK` | Nē | `true`, lai izvietotu iebūvēto Keycloak (nepieciešami 4 GB RAM). |

> **Drošība:** Visas paroles pēc noklusējuma ir `admin`. Mainiet tās nekavējoties pēc pirmās pieteikšanās.

---

## 2. solis — Palaidiet EC2 instanci

[AWS EC2 konsolē](https://console.aws.amazon.com/ec2):

1. Noklikšķiniet uz **Launch instance**
2. **AMI:** Ubuntu Server 22.04 LTS (64-bit x86)
3. **Instances tips:** `t3.medium` (4 GB RAM) vai lielāks
4. **Atslēgu pāris:** Atlasiet vai izveidojiet SSH piekļuvei
5. **Tīkla iestatījumi:** Izveidojiet vai atlasiet drošības grupu (skatiet zemāk)
6. **Advanced details** → **User data** → ielīmējiet pilno skripta saturu
7. Noklikšķiniet uz **Launch instance**

---

## 3. solis — Konfigurējiet drošības grupu

Atveriet šos portus instances drošības grupā:

| Ports | Protokols | Avots | Mērķis |
|------|----------|--------|---------|
| 22 | TCP | Jūsu IP | SSH piekļuve |
| 80 | TCP | 0.0.0.0/0 | HTTP (Nginx novirza uz HTTPS) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Tieša Shiny piekļuve |

> **Neatveriet** portu 3306 (MySQL) — tam nekad nevajadzētu būt publiski pieejamam.

---

## 4. solis — Pievienojiet DNS ierakstu

Kamēr instance sāknējas, pievienojiet **A ierakstu** sava DNS nodrošinātāja panelī:

```
Tips  : A
Nosaukums  : myapp
Vērtība : <instance-public-ip>
TTL   : 300
```

---

## 5. solis — Uzraugiet progresu

```bash
ssh ubuntu@<instance-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## 6. solis — Piekļūstiet lietotnei

Kad iestatīšana ir pabeigta, žurnāls rāda kopsavilkumu ar jūsu lietotnes URL un akreditācijas datiem. Piesakieties ar lietotājvārdu `admin` un paroli `admin`, pēc tam nekavējoties mainiet savu paroli.

---

## Pēc izvietošanas

### Paroles maiņa

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Visu konteineru skatīšana

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Elastīgā IP piešķiršana (neobligāts)

Ja apturēsiet un palaidīsiet instanci, publiskā IP mainīsies. Lai saglabātu stabilu IP, piešķiriet **Elastic IP** un saistiet to ar instanci EC2 konsolē.
