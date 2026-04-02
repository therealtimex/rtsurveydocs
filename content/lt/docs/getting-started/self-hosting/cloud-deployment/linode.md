---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Įdiekite „rtCloud“ „Linode“ naudodami „StackScript“. Nereikia jokios konfigūracijos – tiesiog sukurkite serverį ir atlikite veiksmus po įdiegimo."
---

## 1 veiksmas – paleiskite „StackScript“.

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Tai atidaro „StackScript“ puslapį „Linode Cloud Manager“. Spustelėkite **Deploy New Linode**.

---

## 2 veiksmas – užpildykite Linode formą

Užpildykite Linode standartinę serverio kūrimo formą:

| Laukas | Rekomenduojama vertė |
|-------|-------------------|
| **Vaizdas** | Ubuntu 22.04 LTS |
| **Regionas** | Arčiausiai jūsų naudotojų |
| **Planas** | Bendras CPU 4 GB ar didesnis |
| **Root slaptažodis** | Nustatykite tvirtą slaptažodį |
| **Laiko juosta** *(mūsų vienintelis laukas)* | Jūsų serverio laiko juosta (numatytasis: „Asia/Ho_Chi_Minh“) |

Baigę spustelėkite **Sukurti linodą**.

---

## 3 veiksmas – palaukite, kol sąranka bus baigta

The script runs automatically on first boot. It installs Docker, pulls the rtSurvey image, initialises the database, and starts all services. This takes **5–10 minutes**.

Pažangą galite stebėti tiesiogiai naudodami **Linode Cloud Manager** – nereikia SSH:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Spustelėkite savo naujai sukurtą Linode
3. Spustelėkite **Paleisti LISH konsolę** (išsamios Linode puslapio viršuje, dešinėje)

Atsidaro naršyklės terminalas, kuriame rodomas tiesioginis įkrovos žurnalas – skirtukas **Weblish** veikia tiesiogiai jūsų naršyklėje, nereikia SSH kliento.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Palaukite, kol pamatysite:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Žurnalas taip pat rodo jūsų serverio IP – jums jo reikės kitam veiksmui.

---

## 4 veiksmas – nustatykite SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Norėdami sukonfigūruoti HTTPS, vadovaukitės **[SSL sąrankos vadovas →](../ssl-setup)**. Nemokamas **rsurvey.com padomenis** yra greičiausia parinktis – nereikia nustatyti DNS.

---

## 5 veiksmas – pirmasis prisijungimas

Kai SSL bus aktyvus, vadovaukitės **[Pirmojo prisijungimo vadovas →](../first-login)**, kad pasiektumėte administratoriaus paskyrą.

---

## 6 veiksmas – pakeiskite numatytąjį slaptažodį

All passwords default to `admin`. Change them immediately after your first login:

- **Programos administratoriaus slaptažodis** – paskyros nustatymai programoje
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Ugniasienės taisyklės (Linode Cloud Firewall)

Jei prie šio serverio prijungiate Linode Cloud Firewall, vadovaukitės šiomis taisyklėmis:

### Atvyksta

| Etiketė | Veiksmas | Protokolas | Uostas | Šaltiniai | Pastabos |
|-------|--------|----------|------|----------|--------|
| `accept-inbound-ssh` | Priimti | TCP | 22 | Visi IPv4, visi IPv6 | SSH prieiga |
| `priimti-įeinantį-http` | Priimti | TCP | 80 | Visi IPv4, visi IPv6 | Nginx (HTTP + ACME iššūkis) |
| `priimti-įeinantį-https` | Priimti | TCP | 443 | Visi IPv4, visi IPv6 | Nginx (HTTPS po SSL sąrankos) |
| `priimti-įeinantis-blizgantis` | Priimti | TCP | 3838 | Visi IPv4, visi IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | Priimti | ICMP | — | Visi IPv4, visi IPv6 | Ping / diagnostika |
| Numatytoji atvykimo politika | **Lašas** | | | | Blokuoti visa kita |

### Išeinantis

| Etiketė | Veiksmas | Pastabos |
|-------|---------|-------|
| Numatytoji siuntimo politika | **Priimti** | Leisti visus išeinančius („Docker“ ištraukimus, „certbot“, „GoDaddy“ API ir kt.) |

### Prievadai NĖRA reikalingi išoriškai

Šie prievadai yra susieti tik su „127.0.0.1“ ir niekada nepasiekiami iš išorės:

| Uostas | Paslauga | Priežastis |
|------|---------|--------|
| 8080 | Programos konteineris | „Nginx“ tarpinis serveris jam naudojamas viduje |
| 8090 | Keycloak konteineris | „Nginx“ tarpinis serveris jam naudojamas viduje |
| 3306 | MySQL | Tik vidinis Docker tinklas |

---

## Trikčių šalinimas

### Patikrinkite sąrankos žurnalą

```bash
tail -200 /var/log/stackscript.log
```

### Patikrinkite SSL žurnalą

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Peržiūrėkite konteinerio būseną

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
