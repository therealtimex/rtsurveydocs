---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "Diekite rtCloud Google Cloud Compute Engine naudodami gcp-compute.sh paleisties scenarijų."
---

Naudokite `gcp-compute.sh` kaip **Paleisties scenarijų** kuriant Compute Engine VM instanciją. Scenarijus automatiškai paleidžiamas pirmąjį kartą.

**Atsisiųsti scenarijų:** [gcp-compute.sh](/scripts/gcp-compute.sh)

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

## 2 žingsnis — Sukurkite VM instanciją

[Google Cloud konsolėje](https://console.cloud.google.com/compute):

1. Spustelėkite **Kurti instanciją**
2. **Mašinos konfigūracija:**
   - Serija: `E2`
   - Mašinos tipas: `e2-medium` (4 GB RAM) arba didesnis
3. **Paleisties diskas:**
   - Operacinė sistema: Ubuntu
   - Versija: Ubuntu 22.04 LTS
   - Dydis: 40 GB arba daugiau
4. **Ugniasienė:** pažymėkite **Leisti HTTP srautą** ir **Leisti HTTPS srautą**
5. **Išplėstinės parinktys** → **Valdymas** → **Automatizavimas** → **Paleisties scenarijus** → įklijuokite visą scenarijaus turinį
6. Spustelėkite **Kurti**

---

## 3 žingsnis — Pridėkite DNS įrašą

Kol VM paleidžiamas, pridėkite **A įrašą** savo DNS teikėjuje:

```
Tipas  : A
Vardas : myapp
Reikšmė: <vm-external-ip>
TTL    : 300
```

Išorinį IP rasite konsolėje VM instancijų sąraše.

---

## 4 žingsnis — Stebėkite eigą

Naudodami `gcloud` CLI:

```bash
gcloud compute ssh <instance-name> -- tail -f /var/log/rtcloud-setup.log
```

Arba prisijunkite tiesiogiai per SSH:

```bash
ssh <username>@<vm-external-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## 5 žingsnis — Pasiekite programą

Kai sąranka baigiama, žurnale rodoma santrauka su jūsų programos URL ir prisijungimo duomenimis. Prisijunkite naudodami naudotojo vardą `admin` ir slaptažodį `admin`, tada iš karto pakeiskite slaptažodį.

---

## Ugniasienės taisyklės

GCP **Leisti HTTP/HTTPS** žymimieji langeliai atidaro prievadus 80 ir 443. Norėdami leisti tiesioginę Shiny prieigą per prievadą 3838, pridėkite ugniasienės taisyklę:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

Arba pridėkite per konsolę: **VPC tinklas** → **Ugniasienė** → **Kurti taisyklę**.

> **Neatidarykite** prievado 3306 (MySQL) – jis niekada neturėtų būti viešai prieinamas.

---

## Statinis IP (neprivaloma)

Pagal numatytuosius nustatymus GCP priskiria laikiną išorinį IP, kuris pasikeičia iš naujo paleidžiant VM. Norėdami išlaikyti stabilų IP:

1. Eikite į **VPC tinklas** → **IP adresai**
2. Spustelėkite **Rezervuoti išorinį statinį adresą**
3. Priskirkite jį savo VM instancijai

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
