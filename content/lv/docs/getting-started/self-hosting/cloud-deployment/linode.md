---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Izvietojiet rtCloud uz Linode, izmantojot StackScript. Nav nepieciešama konfigurācija — vienkārši izveidojiet serveri un veiciet darbības pēc izvietošanas."
---

## 1. darbība — palaidiet StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Tādējādi Linode Cloud Manager tiek atvērta StackScript lapa. Noklikšķiniet uz **Izvietot jaunu Linode**.

---

## 2. solis — aizpildiet Linodes veidlapu

Aizpildiet Linodes standarta servera izveides veidlapu:

| Lauks | Ieteicamā vērtība |
|-------|-------------------|
| **Attēls** | Ubuntu 22.04 LTS |
| **Reģions** | Vistuvāk jūsu lietotājiem |
| **Plāns** | Koplietots CPU 4 GB vai lielāks |
| **Saknes parole** | Iestatiet spēcīgu paroli |
| **Laika josla** *(mūsu vienīgais lauks)* | Jūsu servera laika josla (noklusējums: Asia/Ho_Chi_Minh) |

Kad esat pabeidzis, noklikšķiniet uz **Izveidot Linode**.

---

## 3. darbība. Pagaidiet, līdz iestatīšana ir pabeigta

Skripts tiek palaists automātiski pirmajā sāknēšanas reizē. Tas instalē Docker, izvelk rtSurvey attēlu, inicializē datu bāzi un startē visus pakalpojumus. Tas aizņem **5–10 minūtes**.

Jūs varat vērot progresu tieši programmā **Linode Cloud Manager** — nav nepieciešams SSH:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Noklikšķiniet uz jaunizveidotās Linodes
3. Noklikšķiniet uz **Palaist LISH konsoli** (Linode detalizētās informācijas lapas augšējā labajā stūrī).

Tiek atvērts pārlūkprogrammas terminālis, kurā tiek rādīts tiešraides sāknēšanas žurnāls — cilne **Weblish** darbojas tieši jūsu pārlūkprogrammā, nav nepieciešams SSH klients.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Pagaidiet, līdz redzat:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Žurnālā ir redzams arī jūsu servera IP — tas būs nepieciešams nākamajai darbībai.

---

## 4. darbība — iestatiet SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Lai konfigurētu HTTPS, izpildiet **[SSL iestatīšanas rokasgrāmatu →](../ssl-setup)**. Bezmaksas **rsurvey.com apakšdomēns** ir ātrākā iespēja — nav nepieciešama DNS iestatīšana.

---

## 5. darbība — pirmā pieteikšanās

Kad SSL ir aktīvs, izpildiet **[Pirmās pieteikšanās rokasgrāmatu →](../first-login)**, lai piekļūtu administratora kontam.

---

## 6. darbība — mainiet noklusējuma paroli

Visām parolēm pēc noklusējuma ir “admin”. Mainiet tos uzreiz pēc pirmās pieteikšanās:

- **Lietotnes administratora parole** — konta iestatījumi lietotnē
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Ugunsmūra noteikumi (Linode Cloud Firewall)

Ja šim serverim pievienojat Linode Cloud Firewall, izmantojiet šādus noteikumus:

### Ienākošais

| Etiķete | Darbība | Protokols | Osta | Avoti | Piezīmes |
|-------|--------|----------|------|----------|-------|
| `accept-inbound-ssh` | Pieņemt | TCP | 22 | Visi IPv4, visi IPv6 | SSH piekļuve |
| `accept-inbound-http` | Pieņemt | TCP | 80 | Visi IPv4, visi IPv6 | Nginx (HTTP + ACME izaicinājums) |
| `accept-inbound-https` | Pieņemt | TCP | 443 | Visi IPv4, visi IPv6 | Nginx (HTTPS pēc SSL iestatīšanas) |
| `pieņemt-ienākošos-spīdīgo` | Pieņemt | TCP | 3838 | Visi IPv4, visi IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | Pieņemt | ICMP | — | Visi IPv4, visi IPv6 | Ping / diagnostika |
| Noklusējuma ienākošā politika | **Piliens** | | | | Bloķēt visu pārējo |

### Izejošais

| Etiķete | Darbība | Piezīmes |
|-------|---------|-------|
| Noklusējuma izejošā politika | **Pieņemt** | Atļaut visu izejošo (Docker pulls, certbot, GoDaddy API utt.) |

### Porti NAV nepieciešami ārēji

Šie porti ir saistīti tikai ar '127.0.0.1' un nekad nav sasniedzami no ārpuses servera:

| Osta | Pakalpojums | Iemesls |
|------|---------|--------|
| 8080 | Lietotņu konteiners | Nginx starpniekserveri tam iekšēji |
| 8090 | Atslēgvārpa konteiners | Nginx starpniekserveri tam iekšēji |
| 3306 | MySQL | Tikai iekšējais Docker tīkls |

---

## Traucējummeklēšana

### Pārbaudiet iestatīšanas žurnālu

```bash
tail -200 /var/log/stackscript.log
```

### Pārbaudiet SSL žurnālu

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Skatīt konteinera statusu

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
