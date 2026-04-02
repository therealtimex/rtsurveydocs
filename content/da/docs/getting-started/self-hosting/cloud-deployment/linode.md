---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Implementer rtCloud på Linode ved hjælp af et StackScript. Ingen konfiguration nødvendig - bare opret serveren og følg trinene efter implementeringen."
---

## Trin 1 — Start StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Dette åbner StackScript-siden i Linode Cloud Manager. Klik på **Deploy New Linode**.

---

## Trin 2 — Udfyld Linodes formular

Udfyld Linodes standardserveroprettelsesformular:

| Felt | Anbefalet værdi |
|-------|------------------------|
| **Billede** | Ubuntu 22.04 LTS |
| **Region** | Tættest på dine brugere |
| **Plan** | Delt CPU 4 GB eller større |
| **Root-adgangskode** | Indstil en stærk adgangskode |
| **Tidszone** *(vores eneste felt)* | Din servertidszone (standard: `Asia/Ho_Chi_Minh`) |

Klik på **Opret Linode**, når du er færdig.

---

## Trin 3 — Vent til opsætningen er fuldført

Scriptet kører automatisk ved første opstart. Den installerer Docker, trækker rtSurvey-billedet, initialiserer databasen og starter alle tjenester. Dette tager **5-10 minutter**.

Du kan se fremskridt direkte i **Linode Cloud Manager** - ingen SSH påkrævet:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Klik på din nyoprettede Linode
3. Klik på **Start LISH Console** (øverst til højre på Linode-detaljesiden)

En browserterminal åbnes og viser live boot-loggen - fanen **Weblish** fungerer direkte i din browser, ingen SSH-klient nødvendig.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Vent til du ser:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Loggen viser også din server-IP - du skal bruge den til næste trin.

---

## Trin 4 — Konfigurer SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Følg **[Set Up SSL guide →](../ssl-setup)** for at konfigurere HTTPS. Det gratis **rtsurvey.com-underdomæne** er den hurtigste mulighed – ingen DNS-opsætning nødvendig.

---

## Trin 5 — Første login

Når SSL er aktivt, skal du følge **[First Login Guide →](../first-login)** for at få adgang til admin-kontoen.

---

## Trin 6 — Skift standardadgangskoden

Alle adgangskoder er som standard "admin". Skift dem umiddelbart efter dit første login:

- **App-administratoradgangskode** — kontoindstillinger i appen
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Firewall-regler (Linode Cloud Firewall)

Hvis du tilslutter en Linode Cloud Firewall til denne server, skal du bruge følgende regler:

### Indgående

| Etiket | Handling | Protokol | Havn | Kilder | Noter |
|-------|--------|--------|------|--------|-------|
| `accept-inbound-ssh` | Accepter | TCP | 22 | Alle IPv4, Alle IPv6 | SSH-adgang |
| `accepter-indgående-http` | Accepter | TCP | 80 | Alle IPv4, Alle IPv6 | Nginx (HTTP + ACME udfordring) |
| `accepter-indgående-https` | Accepter | TCP | 443 | Alle IPv4, Alle IPv6 | Nginx (HTTPS efter SSL-opsætning) |
| `accepter-indgående-skinnende` | Accepter | TCP | 3838 | Alle IPv4, Alle IPv6 | Shiny Server (R-analyse) |
| `accept-inbound-icmp` | Accepter | ICMP | — | Alle IPv4, Alle IPv6 | Ping / diagnostik |
| Standard indgående politik | **Drop** | | | | Bloker alt andet |

### Udgående

| Etiket | Handling | Noter |
|-------|--------|-------|
| Standard udgående politik | **Accepter** | Tillad alle udgående (Docker pulls, certbot, GoDaddy API osv.) |

### Porte er IKKE nødvendige eksternt

Disse porte er kun bundet til `127.0.0.1` og kan aldrig nås uden for serveren:

| Havn | Service | Årsag |
|------|--------|--------|
| 8080 | App container | Nginx proxyer til det internt |
| 8090 | Nøglekappe container | Nginx proxyer til det internt |
| 3306 | MySQL | Kun internt Docker-netværk |

---

## Fejlfinding

### Tjek opsætningsloggen

```bash
tail -200 /var/log/stackscript.log
```

### Tjek SSL-loggen

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Se containerstatus

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
