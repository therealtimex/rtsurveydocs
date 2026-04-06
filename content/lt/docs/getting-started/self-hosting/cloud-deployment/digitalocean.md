---
weight: 1
title: "DigitalOcean"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "water_drop"
toc: true
description: "Įdiekite „rtCloud“ „DigitalOcean Droplet“ naudodami automatinius vartotojo duomenų scenarijus."
---

„DigitalOcean“ naudoja **Vartotojo duomenų** scenarijus, kurie automatiškai paleidžiami pirmą kartą paleidžiant. Jūs užpildote konfigūracijos kintamuosius scenarijaus viršuje, tada įklijuojate visą scenarijų kurdami lašelį.

> Skirtingai nuo Linode StackScripts, DigitalOcean neturi formos vartotojo sąsajos – prieš įklijuodami scenarijų turite redaguoti tiesiogiai.

**Download script:** [digitalocean-droplet-keycloak-embed.sh](/scripts/digitalocean-droplet-keycloak-embed.sh)

---

## Įterpta raktų skraistė (rekomenduojama)

Naudokite „digitalocean-droplet-keycloak-embed.sh“, kad atliktumėte paprasčiausią sąranką su integruotu SSO.

### 1 veiksmas – užpildykite konfigūraciją

Atidarykite scenarijų ir redaguokite bloką „CONFIGURATION“ viršuje:

```bash
# --- Required ---
PROJECT_ID="rtsurvey"                  # Unique identifier for your project (no spaces)
ADMIN_PASSWORD="admin"                 # Password for app admin and Keycloak — change after first login

# --- Domain + SSL ---
DOMAIN="myapp.example.com"            # Your domain — DNS A record must point here
PROJECT_URL=""                         # Leave blank unless behind Cloudflare/proxy
LETSENCRYPT_EMAIL="admin@example.com" # Email for Let's Encrypt notifications

# --- Optional ---
STATA_ENABLED="false"
TZ="Asia/Ho_Chi_Minh"
```

| Laukas | Reikalingas | Aprašymas |
|-------|-----------|--------------|
| „PROJECT_ID“ | Taip | Naudojamas kaip duomenų bazės pavadinimas ir „Keycloak“ kliento ID. Mažosios raidės, be tarpų. |
| „ADMIN_PASSWORD“ | Ne | Programos administratoriaus prisijungimo ir „Keycloak“ administratoriaus pulto slaptažodis. Numatytoji reikšmė yra „admin“ – **pakeisti po pirmojo prisijungimo**. |
| "DOMENAS" | Taip | Jūsų domeno vardas. DNS Įrašas turi nurodyti Droplet IP. |
| `LETSENCRYPT_EMAIL` | Taip | El. pašto adresas pranešimams apie Užšifruokime sertifikatą. |
| „PROJECT_URL“ | Ne | Nepaisyti viešo URL. Jei norite naudoti „DOMAIN“, palikite tuščią. Naudinga už Cloudflare. |

> **Sauga:** pagal numatytuosius nustatymus visi slaptažodžiai yra „admin“. Pakeiskite juos iškart po pirmojo prisijungimo.

### 2 veiksmas – sukurkite lašelį

In the [DigitalOcean control panel](https://cloud.digitalocean.com):

1. Spustelėkite **Sukurti** → **Lašeliai**
2. Pasirinkite **Ubuntu 22.04 LTS** kaip vaizdą
3. Pasirinkite **Pagrindinis, 4 GB RAM / 2 vCPU** arba daugiau
4. Slinkite iki **Išplėstinės parinktys** → pažymėkite **Pridėti inicijavimo scenarijus**
5. Įklijuokite visą scenarijaus turinį į teksto sritį
6. Spustelėkite **Sukurti lašelį**

### 3 veiksmas – pridėkite DNS įrašą

Kol „Droplet“ paleidžiama, pridėkite **A įrašą** prie savo DNS teikėjo:

```
Type  : A
Name  : myapp          (or @ for root domain)
Value : <droplet-ip>
TTL   : 300
```

### 4 veiksmas. Stebėkite pažangą

SSH į „Droplet“ ir žiūrėkite žurnalą:

```bash
ssh root@<droplet-ip>
tail -f /var/log/rtcloud-setup.log
```

Scenarijus išspausdina jūsų serverio IP netoli pradžios – pridėkite DNS įrašą, kai tik jį pamatysite.

### 5 veiksmas – pasiekite programą

Kai sąranka baigta, žurnale rodoma suvestinė:

```
============================================================
 rtCloud deployment complete! (Embedded Keycloak)
============================================================
 App URL   : https://myapp.example.com
 Admin     : admin / admin
 Keycloak  : https://myapp.example.com/auth/admin

 !! SECURITY: All passwords default to 'admin'.
    Change them immediately after first login.
============================================================
```

Open `https://myapp.example.com` in your browser and log in with username `admin` and password `admin`.

> **Pakeiskite slaptažodį** iškart po prisijungimo naudodami viršutiniame dešiniajame meniu esantį **Nustatymai**.

---

## Po įdiegimo

### Pakeiskite slaptažodį

SSH į „Droplet“, redaguokite „.env“ ir iš naujo paleiskite paveiktą sudėtinį rodinį:

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Atnaujinkite domeną

Jei po įdiegimo priskirsite kitą domeną, atnaujinkite „PROJECT_URL“ .env:

```bash
nano /opt/rtcloud/.env   # update PROJECT_URL=
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Peržiūrėti visus konteinerius

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
