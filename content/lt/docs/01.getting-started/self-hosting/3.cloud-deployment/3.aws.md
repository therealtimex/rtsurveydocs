---
weight: 3
title: "AWS EC2"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud"
toc: true
description: "Diekite rtCloud AWS EC2 instancijoje naudodami aws-ec2.sh naudotojo duomenų scenarijų."
---

Naudokite `aws-ec2.sh` kaip **Naudotojo duomenų** scenarijų paleidžiant EC2 instanciją. Scenarijus automatiškai paleidžiamas pirmąjį kartą.

**Atsisiųsti scenarijų:** [aws-ec2.sh](/scripts/aws-ec2.sh)

---

## 1 žingsnis — Užpildykite konfigūraciją

Atidarykite scenarijų ir redaguokite `CONFIGURATION` bloką viršuje:

```bash
# --- Privaloma ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Pakeiskite po pirmojo prisijungimo

# --- Domenas + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Integruotas Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Numatytasis – ADMIN_PASSWORD
```

| Laukas | Privalomas | Aprašymas |
|-------|----------|-------------|
| `PROJECT_ID` | Taip | Naudojamas kaip duomenų bazės pavadinimas ir Keycloak kliento ID. Mažosios raidės, be tarpų. |
| `ADMIN_PASSWORD` | Ne | Programos admin slaptažodis ir Keycloak admin slaptažodis. Numatytasis – `admin` – **pakeiskite po pirmojo prisijungimo**. |
| `DOMAIN` | Ne | Jūsų domenas HTTPS. Palikite tuščią tik HTTP režimui. |
| `LETSENCRYPT_EMAIL` | Taip (jei nustatytas DOMAIN) | El. paštas „Let's Encrypt" pranešimams. |
| `EMBED_KEYCLOAK` | Ne | `true`, kad diegtumėte integruotą Keycloak (reikia 4 GB RAM). |

> **Saugumas:** visi slaptažodžiai pagal numatytuosius nustatymus yra `admin`. Pakeiskite juos iš karto po pirmojo prisijungimo.

---

## 2 žingsnis — Paleiskite EC2 instanciją

[AWS EC2 konsolėje](https://console.aws.amazon.com/ec2):

1. Spustelėkite **Paleisti instanciją**
2. **AMI:** Ubuntu Server 22.04 LTS (64 bitų x86)
3. **Instancijos tipas:** `t3.medium` (4 GB RAM) arba didesnis
4. **Raktų pora:** pasirinkite arba sukurkite SSH prieigai
5. **Tinklo nustatymai:** sukurkite arba pasirinkite saugos grupę (žr. toliau)
6. **Išplėstinė informacija** → **Naudotojo duomenys** → įklijuokite visą scenarijaus turinį
7. Spustelėkite **Paleisti instanciją**

---

## 3 žingsnis — Konfigūruokite saugos grupę

Atidarykite šiuos prievadus instancijos saugos grupėje:

| Prievadas | Protokolas | Šaltinis | Paskirtis |
|------|----------|--------|---------|
| 22 | TCP | Jūsų IP | SSH prieiga |
| 80 | TCP | 0.0.0.0/0 | HTTP (Nginx nukreipia į HTTPS) |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 3838 | TCP | 0.0.0.0/0 | Tiesioginė Shiny prieiga |

> **Neatidarykite** prievado 3306 (MySQL) – jis niekada neturėtų būti viešai prieinamas.

---

## 4 žingsnis — Pridėkite DNS įrašą

Kol instancija paleidžiama, pridėkite **A įrašą** savo DNS teikėjuje:

```
Tipas  : A
Vardas : myapp
Reikšmė: <instance-public-ip>
TTL    : 300
```

---

## 5 žingsnis — Stebėkite eigą

```bash
ssh ubuntu@<instance-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## 6 žingsnis — Pasiekite programą

Kai sąranka baigiama, žurnale rodoma santrauka su jūsų programos URL ir prisijungimo duomenimis. Prisijunkite naudodami naudotojo vardą `admin` ir slaptažodį `admin`, tada iš karto pakeiskite slaptažodį.

---

## Po diegimo

### Slaptažodžio keitimas

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Visų konteinerių peržiūra

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Elastic IP priskyrimas (neprivaloma)

Jei sustabdote ir paleidžiate instanciją, viešasis IP pasikeičia. Norėdami išlaikyti stabilų IP, paskirstykite **Elastic IP** ir susiekite jį su instancija EC2 konsolėje.
