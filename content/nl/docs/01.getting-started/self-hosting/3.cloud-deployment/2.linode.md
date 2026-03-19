---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-17T01:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Implementeer rtCloud op Linode met StackScripts met een formuliergebaseerde configuratie-UI."
---

Linode gebruikt **StackScripts** — scripts met een formuliergebaseerde UI waar u configuratievelden rechtstreeks in de Linode Manager invult zonder enige code te bewerken.

> Linode StackScripts zijn de eenvoudigste implementatiemethode. Velden verschijnen als een formulier wanneer u een Linode aanmaakt — geen scriptbewerking vereist.

---

## Ingebedde Keycloak (Aanbevolen)

### Stap 1 — Zoek de StackScript

De StackScript is publiek beschikbaar in de Linode-community — geen handmatige installatie nodig:

1. Ga naar **Linodes** → **Linode aanmaken**
2. Selecteer onder **Kies een distributie** de optie **StackScripts** → **Community StackScripts**
3. Zoek naar **`RTA rtSurvey - Self-Hosted with Keycloak SSO`**
4. Selecteer het en vul het configuratieformulier in:

> Als alternatief kunt u [het script downloaden](/scripts/linode-stackscript-keycloak-embed.sh) en uw eigen StackScript aanmaken onder **StackScripts** → **StackScript aanmaken**.

| Veld | Vereist | Beschrijving |
|-------|----------|-------------|
| Project ID | Nee | Unieke identificator (standaard: `rtsurvey`). Gebruikt als databasenaam en Keycloak-client-ID. |
| Keycloak Beheerderswachtwoord | Nee | Wachtwoord voor zowel de Keycloak-beheerconsole als de app-beheerderlogin. Standaard `admin` — **wijzigen na eerste login**. |
| Domein | Ja | Uw domeinnaam. DNS A-record moet naar het IP van deze Linode verwijzen. Vereist voor HTTPS en Keycloak. |
| Let's Encrypt E-mail | Ja | E-mail voor Let's Encrypt-certificaatmeldingen. |
| Docker Image Tag | Nee | Te implementeren image (standaard: `rtawebteam/rta-smartsurvey:survey-dockerize`). |

> **Beveiliging:** Alle wachtwoorden zijn standaard `admin`. Wijzig ze onmiddellijk na uw eerste login.

5. Kies **Ubuntu 22.04 LTS** als de image
6. Kies een **Gedeelde CPU 4 GB**-plan of groter
7. Klik op **Linode aanmaken**

### Stap 2 — Voeg het DNS-record toe

Terwijl de Linode opstart, voegt u een **A-record** toe bij uw DNS-provider:

```
Type  : A
Naam  : mijnapp          (of @ voor rootdomein)
Waarde: <linode-ip>
TTL   : 300
```

### Stap 3 — Monitor de voortgang

```bash
ssh root@<linode-ip>
tail -f /var/log/stackscript.log
```

Het script drukt uw server-IP vroeg af — voeg het DNS-record toe zodra u het ziet.

### Stap 4 — Toegang tot de app

Wanneer de installatie is voltooid, toont het logboek een samenvatting:

```
============================================================
 rtCloud implementatie voltooid! (Ingebedde Keycloak)
============================================================
 App URL   : https://mijnapp.example.com
 Beheerder : admin / admin
 Keycloak  : https://mijnapp.example.com/auth/admin

 !! BEVEILIGING: Alle wachtwoorden zijn standaard 'admin'.
    Wijzig ze onmiddellijk na de eerste login.
============================================================
```

Log in met gebruikersnaam `admin` en wachtwoord `admin`, en wijzig uw wachtwoord onmiddellijk.

---

## Na implementatie

### Een wachtwoord wijzigen

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Alle containers weergeven

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```

### Het logboek controleren

```bash
tail -200 /var/log/stackscript.log
```
