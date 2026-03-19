---
weight: 4
title: "Google Cloud (GCP)"
date: "2026-03-16T00:00:00+07:00"
lastmod: "2026-03-16T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "travel_explore"
toc: true
description: "Ota rtCloud käyttöön Google Cloud Compute Enginellä käyttämällä gcp-compute.sh-käynnistysskriptiä."
---

Käytä `gcp-compute.sh`-skriptiä **Startup script** -skriptinä Compute Engine -virtuaalikoneinstanssia luotaessa. Skripti ajetaan automaattisesti ensimmäisellä käynnistyksellä.

**Lataa skripti:** [gcp-compute.sh](/scripts/gcp-compute.sh)

---

## Vaihe 1 — Täytä konfiguraatio

Avaa skripti ja muokkaa yläosassa olevaa `CONFIGURATION`-lohkoa:

```bash
# --- Pakolliset ---
PROJECT_ID="rtsurvey"
ADMIN_PASSWORD="admin"                       # Vaihda ensimmäisen kirjautumisen jälkeen

# --- Verkkotunnus + SSL ---
DOMAIN="myapp.example.com"
LETSENCRYPT_EMAIL="admin@example.com"

# --- Upotettu Keycloak ---
EMBED_KEYCLOAK="true"
KEYCLOAK_ADMIN_PASSWORD="${ADMIN_PASSWORD}"  # Oletuksena ADMIN_PASSWORD
```

| Kenttä | Pakollinen | Kuvaus |
|-------|----------|-------------|
| `PROJECT_ID` | Kyllä | Käytetään tietokannan nimenä ja Keycloakin asiakastunnuksena. Pienet kirjaimet, ei välilyöntejä. |
| `ADMIN_PASSWORD` | Ei | Sovelluksen järjestelmänvalvojan ja Keycloakin salasana. Oletuksena `admin` — **vaihda ensimmäisen kirjautumisen jälkeen**. |
| `DOMAIN` | Ei | Verkkotunnuksesi HTTPS:lle. Jätä tyhjäksi vain HTTP-tilaan. |
| `LETSENCRYPT_EMAIL` | Kyllä (jos DOMAIN asetettu) | Sähköposti Let's Encryptin ilmoituksia varten. |
| `EMBED_KEYCLOAK` | Ei | `true` ottaa käyttöön upotetun Keycloakin (vaatii 4 Gt RAM). |

> **Turvallisuus:** Kaikki salasanat ovat oletuksena `admin`. Vaihda ne välittömästi ensimmäisen kirjautumisen jälkeen.

---

## Vaihe 2 — Luo virtuaalikoneinstanssi

[Google Cloud Consolessa](https://console.cloud.google.com/compute):

1. Napsauta **Luo instanssi**
2. **Konekonfiguraatio:**
   - Sarja: `E2`
   - Konetyyppi: `e2-medium` (4 Gt RAM) tai suurempi
3. **Käynnistyslevy:**
   - Käyttöjärjestelmä: Ubuntu
   - Versio: Ubuntu 22.04 LTS
   - Koko: 40 Gt tai enemmän
4. **Palomuuri:** valitse **Salli HTTP-liikenne** ja **Salli HTTPS-liikenne**
5. **Lisäasetukset** → **Hallinta** → **Automaatio** → **Käynnistysskripti** → liitä koko skriptin sisältö
6. Napsauta **Luo**

---

## Vaihe 3 — Lisää DNS-tietue

Virtuaalikoneen käynnistyessä lisää **A-tietue** DNS-palveluntarjoajallesi:

```
Tyyppi  : A
Nimi    : myapp
Arvo    : <vm-ulkoinen-ip>
TTL     : 300
```

Etsi ulkoinen IP-osoite virtuaalikonelistasta konsolissa.

---

## Vaihe 4 — Seuraa edistymistä

`gcloud` CLI:n avulla:

```bash
gcloud compute ssh <instanssin-nimi> -- tail -f /var/log/rtcloud-setup.log
```

Tai SSH suoraan:

```bash
ssh <käyttäjätunnus>@<vm-ulkoinen-ip>
tail -f /var/log/rtcloud-setup.log
```

---

## Vaihe 5 — Käytä sovellusta

Kun asennus on valmis, loki näyttää yhteenvedon sovelluksesi URL-osoitteella ja tunnistetiedoilla. Kirjaudu sisään käyttäjätunnuksella `admin` ja salasanalla `admin`, vaihda sitten salasanasi välittömästi.

---

## Palomuurisäännöt

GCP:n **Salli HTTP/HTTPS** -valintaruudut avaavat portit 80 ja 443. Salliaksesi suoran Shiny-pääsyn portissa 3838, lisää palomuurisääntö:

```bash
gcloud compute firewall-rules create allow-shiny \
  --allow tcp:3838 \
  --target-tags http-server
```

Tai lisää se konsolin kautta: **VPC Network** → **Firewall** → **Luo sääntö**.

> **Älä** avaa porttia 3306 (MySQL) — sen ei pitäisi olla julkisesti käytettävissä.

---

## Staattinen IP (valinnainen)

GCP määrittää oletuksena lyhytaikaisen ulkoisen IP-osoitteen, joka muuttuu virtuaalikoneen uudelleenkäynnistyksen yhteydessä. Säilyttääksesi vakaan IP-osoitteen:

1. Siirry kohtaan **VPC Network** → **IP-osoitteet**
2. Napsauta **Varaa ulkoinen staattinen osoite**
3. Liitä se virtuaalikoneinstanssiisi

---

## Käyttöönoton jälkeen

### Vaihda salasana

```bash
nano /opt/rtcloud/.env
docker compose -f /opt/rtcloud/docker-compose.production.yml up -d --force-recreate rtcloud
```

### Tarkastele kaikkia kontteja

```bash
docker compose -f /opt/rtcloud/docker-compose.production.yml ps
```
