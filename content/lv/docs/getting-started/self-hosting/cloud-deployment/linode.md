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

## 1. darbība — palaidiet StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Tādējādi tiek atvērta StackScript lapa Linode mākoņu pārvaldniekā. Noklikšķiniet uz **Izvietot jaunu Linode**.

---

## 2. darbība — aizpildiet Linode veidlapu

Aizpildiet Linode standarta servera izveides veidlapu:

| Lauks | Ieteicamā vērtība |
|-------|-------------------|
| **Attēls** | Ubuntu 22.04 LTS |
| **Reģions** | Vistuvāk jūsu lietotājiem |
| **Plāns** | Koplietots CPU 4 GB vai lielāks |
| **Saknes parole** | Iestatiet spēcīgu paroli |
| **Ugunsmūris** | Nav ugunsmūra *(ieteicams)* |
| **Laika josla** *(mūsu vienīgais lauks)* | Jūsu servera laika josla (noklusējums: Asia/Ho_Chi_Minh) |

> **Kāpēc nav ugunsmūra?** Iestatīšanas skriptam ir nepieciešama piekļuve internetam (Docker pulls, Let's Encrypt). Portu bloķēšana pirmās sāknēšanas laikā var izraisīt izvietošanas neizdošanos. Pēc iestatīšanas varat pievienot ugunsmūri — pareizos noteikumus skatiet tālāk [Ugunsmūra noteikumi] (#firewall-rules-linode-cloud-firewall).

Kad esat pabeidzis, noklikšķiniet uz **Izveidot Linode**.

---

## 3. darbība. Pagaidiet, līdz iestatīšana ir pabeigta

Skripts tiek palaists automātiski pirmajā sāknēšanas reizē. Tas instalē Docker, izvelk rtSurvey attēlu, inicializē datu bāzi un startē visus pakalpojumus. Tas aizņem **5–10 minūtes**.

Varat vērot progresu tieši programmā **Linode Cloud Manager** — nav nepieciešams SSH:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Noklikšķiniet uz jaunizveidotā Linode
3. Noklikšķiniet uz **Launch LISH Console** (Linode detalizētās informācijas lapas augšējā labajā stūrī).

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

## 5. darbība — mainiet noklusējuma paroli

Visām parolēm pēc noklusējuma ir “admin”. Mainiet tos uzreiz pēc pirmās pieteikšanās:

- **Lietotnes administratora parole** — konta iestatījumi lietotnē
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Ugunsmūra noteikumi (Linode mākoņa ugunsmūris)

Ja šim serverim pievienojat Linode mākoņa ugunsmūri, izmantojiet šādus noteikumus:

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
| Noklusējuma izejošā politika | **Pieņemt** | Atļaut visus izejošos (Docker pull, certbot, GoDaddy API utt.) |

### Porti NAV nepieciešami ārēji

Šie porti ir saistīti tikai ar '127.0.0.1' un nekad nav sasniedzami no ārpuses servera:

| Osta | Pakalpojums | Iemesls |
|------|---------|--------|
| 8080 | Lietotņu konteiners | Nginx starpniekserveri tam iekšēji |
| 8090 | Keycloak konteiners | Nginx starpniekserveri tam iekšēji |
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
