---
weight: 2
title: "Linode (Akamai-wolk)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Implementeer rtCloud op Linode met behulp van een StackScript. Geen configuratie nodig: maak gewoon de server aan en volg de stappen na de implementatie."
---

## Stap 1 — Start StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Hiermee wordt de StackScript-pagina in Linode Cloud Manager geopend. Klik op **Nieuwe Linode implementeren**.

---

## Stap 2 — Vul het formulier van Linode in

Vul het standaard servercreatieformulier van Linode in:

| Veld | Aanbevolen waarde |
|-------|------------------|
| **Afbeelding** | Ubuntu 22.04LTS |
| **Regio** | Het dichtst bij uw gebruikers |
| **Plannen** | Gedeelde CPU 4 GB of groter |
| **Rootwachtwoord** | Stel een sterk wachtwoord in |
| **Tijdzone** *(ons enige veld)* | De tijdzone van uw server (standaard: `Azië/Ho_Chi_Minh`) |

Klik op **Linode maken** als u klaar bent.

---

## Stap 3 — Wacht tot de installatie is voltooid

Het script wordt automatisch uitgevoerd bij de eerste keer opstarten. Het installeert Docker, haalt de rtSurvey-image op, initialiseert de database en start alle services. Dit duurt **5–10 minuten**.

Je kunt de voortgang rechtstreeks bekijken in **Linode Cloud Manager** – geen SSH vereist:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Klik op je nieuw gemaakte Linode
3. Klik op **LISH Console starten** (rechtsboven op de Linode-detailpagina)

Er wordt een browserterminal geopend met het live opstartlogboek. Het tabblad **Weblish** werkt rechtstreeks in uw browser, er is geen SSH-client nodig.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Wacht tot je ziet:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Het log toont ook het IP-adres van uw server; u heeft dit nodig voor de volgende stap.

---

## Stap 4 — SSL instellen

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Volg de **[SSL-handleiding instellen →](../ssl-setup)** om HTTPS te configureren. Het gratis **rtsurvey.com-subdomein** is de snelste optie: er is geen DNS-installatie nodig.

---

## Stap 5 — Eerste login

Zodra SSL actief is, volgt u de **[Handleiding voor eerste aanmelding →](../eerste aanmelding)** om toegang te krijgen tot het beheerdersaccount.

---

## Stap 6 — Wijzig het standaardwachtwoord

Alle wachtwoorden zijn standaard 'admin'. Wijzig ze onmiddellijk na uw eerste login:

- **App-beheerderswachtwoord** — accountinstellingen in de app
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Firewallregels (Linode Cloud Firewall)

Als u een Linode Cloud Firewall aan deze server koppelt, hanteer dan de volgende regels:

### Binnenkomend

| Etiket | Actie | Protocol | Haven | Bronnen | Opmerkingen |
|-------|--------|----------|------|---------|-------|
| `accepteer-inkomende-ssh` | Accepteren | TCP | 22 | Alles IPv4, Alles IPv6 | SSH-toegang |
| `accepteren-inkomend-http` | Accepteren | TCP | 80 | Alles IPv4, Alles IPv6 | Nginx (HTTP + ACME-uitdaging) |
| `accepteren-inkomend-https` | Accepteren | TCP | 443 | Alles IPv4, Alles IPv6 | Nginx (HTTPS na SSL-installatie) |
| `accepteren-inkomend-glanzend` | Accepteren | TCP | 3838 | Alles IPv4, Alles IPv6 | Glanzende server (R-analyse) |
| `accepteren-inkomend-icmp` | Accepteren | ICMP | — | Alles IPv4, Alles IPv6 | Ping / diagnostiek |
| Standaardbeleid voor inkomend verkeer | **Laat vallen** | | | | Al het andere blokkeren |

### Uitgaand

| Etiket | Actie | Opmerkingen |
|-------|--------|-------|
| Standaardbeleid voor uitgaand verkeer | **Accepteren** | Alle uitgaande berichten toestaan ​​(Docker-pulls, certbot, GoDaddy API, etc.) |

### Poorten NIET extern nodig

Deze poorten zijn alleen gebonden aan `127.0.0.1` en zijn nooit bereikbaar van buiten de server:

| Haven | Dienst | Reden |
|------|---------|--------|
| 8080 | App-container | Nginx proxies to it internally |
| 8090 | Sleutelmantelcontainer | Nginx-proxy's intern |
| 3306 | MySQL | Alleen intern Docker-netwerk |

---

## Problemen oplossen

### Controleer het installatielogboek

```bash
tail -200 /var/log/stackscript.log
```

### Controleer het SSL-logboek

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Bekijk de containerstatus

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
