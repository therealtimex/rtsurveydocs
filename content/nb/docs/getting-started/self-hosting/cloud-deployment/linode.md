---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Distribuer rtCloud på Linode ved hjelp av et StackScript. Ingen konfigurasjon nødvendig – bare opprett serveren og følg trinnene etter distribusjon."
---

## Trinn 1 — Start StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Dette åpner StackScript-siden i Linode Cloud Manager. Klikk på **Deploy New Linode**.

---

## Trinn 2 — Fyll ut Linodes skjema

Fyll ut Linodes standard serveropprettingsskjema:

| Felt | Anbefalt verdi |
|-------|------------------------|
| **Bilde** | Ubuntu 22.04 LTS |
| **Region** | Nærmest brukerne dine |
| **Plan** | Delt CPU 4 GB eller større |
| **Root-passord** | Angi et sterkt passord |
| **Tidssone** *(vårt eneste felt)* | Serverens tidssone (standard: `Asia/Ho_Chi_Minh`) |

Klikk på **Create Linode** når du er ferdig.

---

## Trinn 3 — Vent til oppsettet er fullført

Skriptet kjører automatisk ved første oppstart. Den installerer Docker, henter rtSurvey-bildet, initialiserer databasen og starter alle tjenester. Dette tar **5–10 minutter**.

Du kan se fremdriften direkte i **Linode Cloud Manager** – ingen SSH kreves:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Klikk på din nyopprettede Linode
3. Klikk på **Start LISH Console** (øverst til høyre på Linode-detaljsiden)

En nettleserterminal åpnes og viser live oppstartsloggen - fanen **Weblish** fungerer direkte i nettleseren din, ingen SSH-klient er nødvendig.

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

Loggen viser også serverens IP - du trenger den for neste trinn.

---

## Trinn 4 — Sett opp SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Følg **[Sett opp SSL-veiledningen →](../ssl-setup)** for å konfigurere HTTPS. Det gratis **rtsurvey.com-underdomenet** er det raskeste alternativet – ingen DNS-oppsett nødvendig.

---

## Trinn 5 — Første pålogging

Når SSL er aktiv, følger du **[First Login Guide →](../first-login)** for å få tilgang til admin-kontoen.

---

## Trinn 6 — Endre standardpassordet

Alle passord er som standard "admin". Endre dem umiddelbart etter din første pålogging:

- **App-administratorpassord** — kontoinnstillinger inne i appen
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Brannmurregler (Linode Cloud Firewall)

Hvis du kobler en Linode Cloud Firewall til denne serveren, bruk følgende regler:

### Inngående

| Etikett | Handling | Protokoll | Port | Kilder | Merknader |
|-------|--------|--------|------|--------|-------|
| `accept-inbound-ssh` | Godta | TCP | 22 | Alle IPv4, Alle IPv6 | SSH-tilgang |
| `accept-inbound-http` | Godta | TCP | 80 | Alle IPv4, Alle IPv6 | Nginx (HTTP + ACME utfordring) |
| `accept-inbound-https` | Godta | TCP | 443 | Alle IPv4, Alle IPv6 | Nginx (HTTPS etter SSL-oppsett) |
| `accept-inbound-shiny` | Godta | TCP | 3838 | Alle IPv4, Alle IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | Godta | ICMP | — | Alle IPv4, Alle IPv6 | Ping / diagnostikk |
| Standard inngående policy | **Slipp** | | | | Blokker alt annet |

### Utgående

| Etikett | Handling | Merknader |
|-------|--------|-------|
| Standard utgående policy | **Godta** | Tillat alle utgående (Docker pulls, certbot, GoDaddy API, etc.) |

### Porter er IKKE nødvendig eksternt

Disse portene er bare bundet til «127.0.0.1» og kan aldri nås fra utenfor serveren:

| Port | Service | Grunn |
|------|--------|--------|
| 8080 | Appbeholder | Nginx proxyer til det internt |
| 8090 | Keycloak container | Nginx proxyer til det internt |
| 3306 | MySQL | Kun internt Docker-nettverk |

---

## Feilsøking

### Sjekk oppsettloggen

```bash
tail -200 /var/log/stackscript.log
```

### Sjekk SSL-loggen

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Se beholderstatus

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
