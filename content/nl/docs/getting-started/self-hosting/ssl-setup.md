---
weight: 4
title: "SSL instellen"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Configureer HTTPS voor uw rtSurvey-server. Vereist voordat u kunt inloggen."
---

SSL moet worden geconfigureerd voordat u kunt inloggen. Wanneer u de app voor de eerste keer opent, wordt u automatisch doorgestuurd naar het SSL-configuratiescherm.

---

## SSL-installatieopties

![SSL-installatieopties](/img/ssl-setup/ssl-setup-options.png)

Kies een van de drie opties:

| Optie | Wanneer te gebruiken |
|--------|-------------|
| **Gratis rtsurvey.com-subdomein** *(Aanbevolen)* | Geen DNS-installatie nodig. Wij maken het record voor u aan. Klaar in 2-5 minuten. |
| **Mijn eigen domein** | U heeft al een domein en de DNS ervan verwijst naar deze server. |
| **Certificaat handmatig installeren** | Enterprise of aangepaste CA. Vereist SSH-toegang. |

---

## Optie 1 — Gratis rtsurvey.com-subdomein (aanbevolen)

Dit is de snelste optie. Geen domeinregistratie of DNS-wijzigingen vereist.

1. Klik op Gratis rtsurvey.com-subdomein om de sectie uit te vouwen
2. Typ de gewenste subdomeinnaam in het invoerveld

   > Gebruik kleine letters, cijfers en koppeltekens. 3–30 tekens.
   > Voorbeeld: `myproject` → `myproject.rtsurvey.com`

3. Klik op Maken **https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Wacht 2 tot 5 minuten terwijl het certificaat wordt uitgegeven

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Zodra het certificaat klaar is, wordt u automatisch doorgestuurd naar uw nieuwe HTTPS-URL

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Optie 2 — Mijn eigen domein

Gebruik dit als u een bestaand domein heeft en het DNS A-record ervan verwijst al naar het IP-adres van deze server.

1. Klik op Mijn eigen domein om de sectie uit te vouwen
2. Voer uw volledige domeinnaam in (e.g. `survey.myorganization.org`)
3. Klik op Certificaat maken

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt verifieert uw domein en geeft een certificaat uit. Hiervoor moet DNS eerst correct worden aangewezen; anders mislukt het verzoek.

---

## Optie 3 — Certificaat handmatig installeren

Voor bedrijfsomgevingen die een aangepaste of interne CA gebruiken. U plaatst uw certificaatbestanden via SSH op de server en voert vervolgens uw domein in de app in.

### Vereisten

- SSH-toegang tot de server
- Een geldig certificaat en privésleutel voor uw domein (PEM-formaat)

### Stap 1 — SSH naar de server

```bash
ssh root@<server-ip>
```

### Stap 2 — Plaats uw certificaatbestanden

Maak de map aan en kopieer uw bestanden:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Kopieer uw bestanden naar die map met de exacte namen:

| Bestand | Beschrijving |
|------|-------------|
| `fullchain.pem` | Uw certificaat + eventuele tussenliggende CA-certificaten (aaneengeschakeld) |
| `privkey.pem` | Uw privésleutel |

Voorbeeld:

```bash
# Kopieer vanaf uw lokale computer (voer dit lokaal uit, niet op de server)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Stel de juiste rechten in:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Stap 3 — Voer uw domein in de app in

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. Klik in het SSL-installatiescherm op Certificaat handmatig installeren
2. Voer uw domeinnaam in (moet overeenkomen met de Common Name of SAN van het certificaat)
3. Klik op Toepassen

De server zal Nginx configureren met uw certificaat en automatisch opnieuw laden.

---

## Volgende stap

Zodra SSL actief is, gaat u verder naar Eerste aanmelding [first-login](first-login).
