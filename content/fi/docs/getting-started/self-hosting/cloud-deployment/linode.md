---
weight: 2
title: "Linode (Akamai Cloud)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "dns"
toc: true
description: "Ota rtCloud käyttöön Linode:ssä StackScript:n avulla. Määrityksiä ei tarvita – luo vain palvelin ja seuraa käyttöönoton jälkeisiä vaiheita."
---

## Vaihe 1 – Käynnistä StackScript

**[Deploy rtSurvey on Linode →](https://cloud.linode.com/stackscripts/2049143)**

Tämä avaa StackScript-sivun Linode Cloud Managerissa. Napsauta **Ota käyttöön uusi Linode**.

---

## Vaihe 2 – Täytä Linode:n lomake

Täytä Linode:n vakiopalvelimen luontilomake:

| Kenttä | Suositeltu arvo |
|-------|-------------------|
| **Kuva** | Ubuntu 22.04 LTS |
| **Alue** | Lähimpänä käyttäjiäsi |
| **Suunnitelma** | Jaettu CPU 4 Gt tai suurempi |
| **Root-salasana** | Aseta vahva salasana |
| **Palomuuri** | Ei palomuuria *(suositus)* |
| **Aikavyöhyke** *(ainoa kenttämme)* | Palvelimesi aikavyöhyke (oletus: Aasia/Ho_Chi_Minh) |

> **Miksi ei palomuuria?** Asennusskripti tarvitsee lähtevän Internet-yhteyden (Docker vetää, Let's Encrypt). Porttien estäminen ensimmäisen käynnistyksen aikana voi aiheuttaa käyttöönoton epäonnistumisen. Voit liittää palomuurin asennuksen jälkeen – katso oikeat säännöt alta [Palomuurisäännöt](#firewall-rules-linode-cloud-firewall).

Napsauta **Luo Linode**, kun olet valmis.

---

## Vaihe 3 – Odota, että asennus on valmis

Skripti suoritetaan automaattisesti ensimmäisen käynnistyksen yhteydessä. Se asentaa Docker:n, vetää rtSurvey-kuvan, alustaa tietokannan ja käynnistää kaikki palvelut. Tämä kestää **5–10 minuuttia**.

Voit seurata edistymistä suoraan **Linode Cloud Managerissa** – SSH:ta ei vaadita:

1. Go to your [Linode dashboard](https://cloud.linode.com/linodes)
2. Napsauta äskettäin luotua Linode:ää
3. Napsauta **Käynnistä LISH-konsoli** (Linode-tietosivun oikeassa yläkulmassa).

Selainpääte avautuu ja näyttää live-käynnistyslokin – **Weblish**-välilehti toimii suoraan selaimessasi, eikä SSH-asiakasta tarvita.

![Lish Console showing rtSurvey StackScript running](/img/first-login/lish-console.png)

Odota kunnes näet:

```
============================================================
 rtSurvey deployment complete!
============================================================
 Server IP : <your-server-ip>

 App URL   : http://<your-server-ip>  (HTTP only until domain is set)
 Admin     : admin / admin
============================================================
```

Loki näyttää myös palvelimesi IP-osoitteen – tarvitset sitä seuraavassa vaiheessa.

---

## Vaihe 4 – Määritä SSL

Open your browser at `http://<server-ip>`. The app will redirect you to the SSL setup screen.

Määritä HTTPS noudattamalla **[SSL-asetusopas →](../ssl-setup)**. Ilmainen **rsurvey.com-aliverkkotunnus** on nopein vaihtoehto – DNS-asetuksia ei tarvita.

---

## Vaihe 5 – Vaihda oletussalasana

Kaikki salasanat ovat oletuksena "admin". Vaihda ne heti ensimmäisen kirjautumisen jälkeen:

- **Sovelluksen järjestelmänvalvojan salasana** — tilin asetukset sovelluksen sisällä
- **Keycloak admin** — accessible at `https://your-domain.com/auth/admin` (login: `admin` / `admin`)

---

## Palomuurisäännöt (Linode Cloud Firewall)

Jos liität Linode Cloud Firewallin tähän palvelimeen, käytä seuraavia sääntöjä:

### Saapuva

| Etiketti | Toiminta | Pöytäkirja | Portti | Lähteet | Huomautuksia |
|-------|--------|----------|------|----------|--------|
| `accept-inbound-ssh` | Hyväksy | TCP | 22 | Kaikki IPv4, kaikki IPv6 | SSH-yhteys |
| `accept-inbound-http` | Hyväksy | TCP | 80 | Kaikki IPv4, kaikki IPv6 | Nginx (HTTP + ACME-haaste) |
| `accept-inbound-https` | Hyväksy | TCP | 443 | Kaikki IPv4, kaikki IPv6 | Nginx (HTTPS SSL-asennuksen jälkeen) |
| `accept-inbound-shiny` | Hyväksy | TCP | 3838 | Kaikki IPv4, kaikki IPv6 | Shiny Server (R analytics) |
| `accept-inbound-icmp` | Hyväksy | ICMP | — | Kaikki IPv4, kaikki IPv6 | Ping / diagnostiikka |
| Saapuvien saapuvien viestien oletuskäytäntö | **Drop** | | | | Estä kaikki muu |

### Lähtevä

| Etiketti | Toiminta | Huomautuksia |
|-------|---------|-------|
| Lähtevien viestien oletuskäytäntö | **Hyväksy** | Salli kaikki lähtevät (Docker-vedot, certbot, GoDaddy API jne.) |

### Portteja EI tarvita ulkoisesti

Nämä portit on sidottu vain porttiin "127.0.0.1", eivätkä ne ole koskaan tavoitettavissa palvelimen ulkopuolelta:

| Portti | Palvelu | Syy |
|------|----------|--------|
| 8080 | Sovellussäiliö | Nginx välityspalvelimet siihen sisäisesti |
| 8090 | Keycloak kontti | Nginx välityspalvelimet siihen sisäisesti |
| 3306 | MySQL | Vain sisäinen Docker-verkko |

---

## Vianetsintä

### Tarkista asennusloki

```bash
tail -200 /var/log/stackscript.log
```

### Tarkista SSL-loki

```bash
tail -200 /var/log/rtsurvey-ssl.log
```

### Näytä säilön tila

```bash
docker compose -f /opt/rtsurvey/docker-compose.production.yml ps
```
