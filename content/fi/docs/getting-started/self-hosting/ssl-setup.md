---
weight: 4
title: "Määritä SSL"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Määritä HTTPS rtSurvey-palvelimellesi. Pakollinen ennen kuin voit kirjautua sisään."
---

SSL on määritettävä ennen kuin voit kirjautua sisään. Kun avaat sovelluksen ensimmäisen kerran, sinut ohjataan automaattisesti SSL-asetusnäyttöön.

---

## SSL-asetusvaihtoehdot

![SSL-asetusvaihtoehdot](/img/ssl-setup/ssl-setup-options.png)

Valitse yksi kolmesta vaihtoehdosta:

| Vaihtoehto | Milloin käyttää |
|--------|-------------|
| **Ilmainen rsurvey.com-aliverkkotunnus** *(Suositeltava)* | DNS-asetuksia ei tarvita. Luomme tietueen sinulle. Valmis 2-5 minuutissa. |
| **Oma domain** | Sinulla on jo verkkotunnus ja sen DNS osoittaa tähän palvelimeen. |
| **Asenna varmenne manuaalisesti** | Enterprise tai mukautettu CA. Vaatii SSH-yhteyden. |

---

## Vaihtoehto 1 – ilmainen rsurvey.com-aliverkkotunnus (suositus)

Tämä on nopein vaihtoehto. Verkkotunnuksen rekisteröintiä tai DNS-muutoksia ei vaadita.

1. Laajenna osio napsauttamalla Ilmainen rsurvey.com-aliverkkotunnus
2. Kirjoita haluamasi aliverkkotunnus syöttökenttään

   > Käytä pieniä kirjaimia, numeroita ja yhdysmerkkejä. 3-30 merkkiä.
   > Esimerkki: `myproject` → `myproject.rtsurvey.com`

3. Napsauta Luo **https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Odota 2–5 minuuttia, kun todistus myönnetään

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Kun varmenne on valmis, sinut ohjataan automaattisesti uuteen HTTPS-URL-osoitteeseen

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Vaihtoehto 2 – Oma verkkotunnus

Käytä tätä, jos sinulla on olemassa oleva toimialue ja sen DNS-tietue A osoittaa jo tämän palvelimen IP-osoitteeseen.

1. Laajenna osio napsauttamalla Oma verkkotunnus
2. Kirjoita koko verkkotunnuksesi nimi (e.g. `survey.myorganization.org`)
3. Napsauta Luo varmenne

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt vahvistaa verkkotunnuksesi ja myöntää varmenteen. Tämä edellyttää, että DNS osoitetaan ensin oikein - pyyntö epäonnistuu muuten.

---

## Vaihtoehto 3 — Asenna varmenne manuaalisesti

Yritysympäristöihin, joissa käytetään mukautettua tai sisäistä CA:ta. Asetat varmennetiedostot palvelimelle SSH:n kautta ja kirjoitat sitten verkkotunnuksesi sovellukseen.

### Edellytykset

- SSH-yhteys palvelimeen
- Kelvollinen varmenne ja yksityinen avain verkkotunnuksellesi (PEM-muoto)

### Vaihe 1 – SSH palvelimelle

```bash
ssh root@<server-ip>
```

### Vaihe 2 – Aseta varmennetiedostot

Luo hakemisto ja kopioi tiedostosi:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Kopioi tiedostosi kyseiseen hakemistoon tarkalla nimellä:

| Tiedosto | Kuvaus |
|------|-------------|
| `fullchain.pem` | Varmenteesi + mahdolliset CA-välivarmenteet (ketjutettu) |
| `privkey.pem` | Yksityinen avaimesi |

Esimerkki:

```bash
# Kopioi paikalliselta koneeltasi (suorita tämä paikallisesti, ei palvelimella)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Aseta oikeat käyttöoikeudet:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Vaihe 3 – Kirjoita verkkotunnuksesi sovellukseen

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. Napsauta SSL-asetusnäytössä Asenna varmenne manuaalisesti
2. Anna verkkotunnuksesi nimi (täytyy vastata varmenteen yleisnimeä tai SAN-tunnusta)
3. Napsauta Käytä

Palvelin määrittää Nginxin varmenteesi kanssa ja lataa sen uudelleen automaattisesti.

---

## Seuraava askel

Kun SSL on aktiivinen, siirry kohtaan Ensimmäinen kirjautuminen [first-login](first-login).
