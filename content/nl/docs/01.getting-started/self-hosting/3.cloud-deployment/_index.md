---
weight: 3
title: "Cloudimplementatie"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "cloud_upload"
toc: true
description: "Implementeer rtCloud bij grote cloudproviders met geautomatiseerde scripts voor DigitalOcean, AWS EC2, Google Cloud en Linode."
---

De implementatierepository bevat geautomatiseerde provisioneringsscripts voor grote cloudproviders. Elk script wordt uitgevoerd bij de eerste start van een verse **Ubuntu 22.04 LTS**-server en voert een volledig onbeheerde installatie uit:

- Installeert Docker en Docker Compose
- Genereert veilige willekeurige wachtwoorden voor alle interne services
- Schrijft `docker-compose.production.yml` en `.env`
- Configureert Nginx als een reverse proxy
- Verkrijgt een gratis TLS-certificaat van Let's Encrypt (automatisch opnieuw proberen totdat DNS is opgelost)
- Configureert de UFW-firewall
- Implementeert optioneel de ingebedde Keycloak SSO-server
- Geeft een volledige implementatiesamenvatting met alle gegevens

De installatie is voltooid in **5–10 minuten** op een standaardinstantie.

---

## Een script kiezen

Er zijn meerdere scriptvarianten afhankelijk van uw cloudprovider en SSO-instelling:

| Script | Provider | SSO-modus | Meest geschikt voor |
|--------|----------|----------|----------|
| `digitalocean-droplet-keycloak-embed.sh` | DigitalOcean | Ingebouwde Keycloak | Eenvoudige, op zichzelf staande SSO |
| `digitalocean-droplet.sh` | DigitalOcean | Keycloak of externe OIDC | Volledige controle |
| `linode-stackscript-keycloak-embed.sh` | Linode | Ingebouwde Keycloak | Formuliergebaseerde installatie, eenvoudigst |
| `linode-stackscript-oidc.sh` | Linode | Alleen externe OIDC | Bestaande identiteitsprovider |
| `linode-stackscript.sh` | Linode | Keycloak of externe OIDC | Volledige controle |
| `aws-ec2.sh` | AWS EC2 | Keycloak of externe OIDC | AWS-implementaties |
| `gcp-compute.sh` | Google Cloud | Keycloak of externe OIDC | GCP-implementaties |

> **Aanbevolen voor de meeste gebruikers:** Gebruik de `keycloak-embed`-variant. Deze bevat een ingebouwde Keycloak-identiteitsserver en vereist de minste configuratievelden.

---

## Servergroottehandleiding

| Gebruiksgeval | RAM | Schijf | Voorbeeld |
|----------|-----|------|---------|
| Evaluatie / ontwikkeling | 2 GB | 25 GB | DO Basic $18/mo, t3.small, e2-small |
| Klein team (< 50 gebruikers) | 4 GB | 40 GB | DO Basic $24/mo, t3.medium, e2-medium |
| Productie (> 50 gebruikers) | 8 GB | 80 GB | DO General $48/mo, t3.large, n2-standard-2 |

> Ingebedde Keycloak vereist minimaal **4 GB RAM**. Gebruik 2 GB alleen voor evaluatie zonder Keycloak.

---

## DNS-instelling

Alle scripts vereisen een domein met een **A-record dat naar het IP van uw server wijst** voordat Let's Encrypt een certificaat kan uitgeven.

Het script drukt vroeg in het installatieproces uw server-IP af:

```
============================================================
 Server IP : 139.162.51.85
 Voeg nu dit DNS A-record toe als u dat nog niet heeft gedaan:
   myapp.example.com  ->  139.162.51.85
 Het script herprobeert Certbot elke 60s totdat DNS is opgelost.
============================================================
```

Het script **herprobeert automatisch** Let's Encrypt elke 60 seconden gedurende maximaal 1 uur. Voeg gewoon het DNS-record toe en wacht — geen herstart nodig.

> **Tariefslimiet:** Let's Encrypt staat maximaal **5 certificaten per domein per 7 dagen** toe. Vermijd herhaald implementeren en verwijderen van servers met hetzelfde domein. Als u de limiet bereikt, toont het script een tijdstempel `opnieuw proberen na` en stopt het onmiddellijk.

---

## Controlelijst na implementatie

- [ ] App opent op `https://uw-domein.nl`
- [ ] Log in met `admin` en het wachtwoord dat u heeft geconfigureerd
- [ ] Alle containers zijn gezond: `docker compose -f /opt/rtcloud/docker-compose.production.yml ps`
- [ ] Let's Encrypt-verlenging werkt: `certbot renew --dry-run`
- [ ] MySQL-poort 3306 is **niet** blootgesteld: `ufw status`
- [ ] Stel een dagelijkse database-back-up in (zie [Onderhoud](../maintenance))

---

## Probleemoplossing

### Controleer het volledige installatielogboek

```bash
# Linode
tail -200 /var/log/stackscript.log

# DigitalOcean / AWS / GCP
tail -200 /var/log/rtcloud-setup.log
```

### Let's Encrypt-tariefslimiet

Als u `too many certificates` in het logboek ziet, heeft u de limiet van 5 certificaten/7 dagen bereikt. Het logboek toont de exacte herprobeertijd:

```
[SSL] ERROR: Let's Encrypt rate limit hit. retry after 2026-03-15 16:22 UTC.
```

Wacht tot die tijd en implementeer opnieuw.

### Keycloak blijft ongezond

Zorg ervoor dat de server minimaal 4 GB RAM heeft en controleer dan de logboeken:

```bash
docker logs rtcloud-keycloak --tail 50
free -h
```

### SSL-configuratie niet toegepast na certbot

Als het certificaat is uitgegeven maar Nginx nog steeds alleen HTTP toont, controleer dan het logboek op de foutmelding en laad Nginx handmatig opnieuw:

```bash
nginx -t && systemctl reload nginx
```
