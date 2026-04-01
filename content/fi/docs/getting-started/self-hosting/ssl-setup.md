---
weight: 4
title: "SSL:n asennus"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Määritä HTTPS rtSurvey-palvelimellesi. Vaaditaan ennen kirjautumista."
---

SSL on määritettävä ennen kuin voit kirjautua sisään. Kun avaat sovelluksen ensimmäistä kertaa, sinut ohjataan automaattisesti SSL-asennusnäytölle.

---

## SSL-asennusvaihtoehdot

![SSL-asennusvaihtoehdot](/img/ssl-setup/ssl-setup-options.png)

Valitse yksi kolmesta vaihtoehdosta:

| Vaihtoehto | Milloin käyttää |
|------------|----------------|
| **Ilmainen rtsurvey.com-alidomaini** *(Suositeltu)* | DNS-asetuksia ei tarvita. Luomme tietueen puolestasi. Valmis 2–5 minuutissa. |
| **Oma domain** | Sinulla on jo domain ja sen DNS osoittaa tähän palvelimeen. |
| **Asenna sertifikaatti manuaalisesti** | Yritys tai mukautettu CA. Vaatii SSH-yhteyden. |

---

## Vaihtoehto 1 — Ilmainen rtsurvey.com-alidomaini *(Suositeltu)*

Tämä on nopein vaihtoehto. Domainin rekisteröintiä tai DNS-muutoksia ei tarvita.

1. Napsauta **Ilmainen rtsurvey.com-alidomaini** laajentaaksesi osiota
2. Kirjoita haluamasi alidomainin nimi syöttökenttään

   > Käytä pieniä kirjaimia, numeroita ja väliviivoja. 3–30 merkkiä.
   > Esimerkki: `myproject` → `myproject.rtsurvey.com`

3. Napsauta **Luo https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Odota 2–5 minuuttia, kun sertifikaattia myönnetään

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Kun sertifikaatti on valmis, sinut ohjataan automaattisesti uuteen HTTPS-osoitteeseen

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Vaihtoehto 2 — Oma domain

Käytä tätä, jos sinulla on olemassa oleva domain ja sen DNS `A`-tietue osoittaa jo tämän palvelimen IP-osoitteeseen.

1. Napsauta **Oma domain** laajentaaksesi osion
2. Syötä koko domainin nimi (esim. `survey.myorganization.org`)
3. Napsauta **Luo sertifikaatti**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt vahvistaa domainisi ja myöntää sertifikaatin. DNS täytyy olla oikein osoitettu ensin — muuten pyyntö epäonnistuu.

---

## Vaihtoehto 3 — Asenna sertifikaatti manuaalisesti

Yritysympäristöille, joissa on mukautettu tai sisäinen CA. Sijoitat sertifikaattitiedostot palvelimelle SSH:n kautta, sitten syötät domainisi sovellukseen.

### Edellytykset

- SSH-yhteys palvelimeen
- Kelvollinen sertifikaatti ja yksityinen avain domainillesi (PEM-muoto)

### Vaihe 1 — SSH palvelimelle

```bash
ssh root@<server-ip>
```

### Vaihe 2 — Sijoita sertifikaattitiedostot

Luo hakemisto ja kopioi tiedostosi:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Kopioi tiedostosi näillä tarkkoilla nimillä:

| Tiedosto | Kuvaus |
|----------|--------|
| `fullchain.pem` | Sertifikaattisi + mahdolliset väli-CA-sertifikaatit (yhdistetty) |
| `privkey.pem` | Yksityinen avaimesi |

Esimerkki:

```bash
# Kopioi paikalliselta koneeltasi (suorita paikallisesti, ei palvelimella)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Aseta oikeat käyttöoikeudet:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Vaihe 3 — Syötä domain sovellukseen

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. SSL-asennusnäytöllä napsauta **Asenna sertifikaatti manuaalisesti**
2. Syötä domainin nimi (täytyy vastata sertifikaatin Common Name tai SAN)
3. Napsauta **Käytä**

Palvelin konfiguroi Nginxin sertifikaatillasi ja lataa automaattisesti uudelleen.

---

## Seuraava vaihe

Kun SSL on aktiivinen, siirry kohtaan [Ensimmäinen kirjautuminen](first-login).
