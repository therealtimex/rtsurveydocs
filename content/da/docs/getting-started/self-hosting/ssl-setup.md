---
weight: 4
title: "Konfigurer SSL"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Konfigurer HTTPS til din rtSurvey-server. Påkrævet før du kan logge ind."
---

SSL skal konfigureres, før du kan logge ind. Når du åbner appen første gang, bliver du automatisk omdirigeret til SSL-opsætningsskærmen.

---

## SSL-opsætningsmuligheder

![SSL-opsætningsmuligheder](/img/ssl-setup/ssl-setup-options.png)

Vælg en af ​​tre muligheder:

| Valgmulighed | Hvornår skal bruges |
|--------|-------------|
| **Gratis rtsurvey.com underdomæne** *(Anbefales)* | Ingen DNS-opsætning nødvendig. Vi opretter rekorden for dig. Klar på 2-5 minutter. |
| **Mit eget domæne** | Du har allerede et domæne, og dets DNS peger på denne server. |
| **Installer certifikat manuelt** | Enterprise eller tilpasset CA. Kræver SSH-adgang. |

---

## Mulighed 1 - Gratis rtsurvey.com underdomæne (anbefalet)

Dette er den hurtigste mulighed. Ingen domæneregistrering eller DNS-ændringer påkrævet.

1. Click Free rtsurvey.com subdomain to expand the section
2. Indtast dit ønskede underdomænenavn i indtastningsfeltet

   > Brug små bogstaver, tal og bindestreger. 3-30 tegn.
   > Eksempel: `myproject` → `myproject.rtsurvey.com`

3. Klik på Opret **https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Vent 2-5 minutter, mens certifikatet udstedes

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Når certifikatet er klar, vil du automatisk blive omdirigeret til din nye HTTPS URL

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Mulighed 2 — Mit eget domæne

Brug dette, hvis du har et eksisterende domæne, og dets DNS A-record peger allerede på denne servers IP.

1. Klik på Mit eget domæne for at udvide sektionen
2. Indtast dit fulde domænenavn (e.g. `survey.myorganization.org`)
3. Klik på Opret certifikat

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt vil bekræfte dit domæne og udstede et certifikat. Dette kræver, at DNS peges korrekt først - anmodningen vil ellers mislykkes.

---

## Mulighed 3 — Installer certifikat manuelt

Til virksomhedsmiljøer, der bruger en brugerdefineret eller intern CA. Du placerer dine certifikatfiler på serveren via SSH, og indtaster derefter dit domæne i appen.

### Forudsætninger

- SSH-adgang til serveren
- Et gyldigt certifikat og privat nøgle til dit domæne (PEM-format)

### Trin 1 — SSH ind i serveren

```bash
ssh root@<server-ip>
```

### Trin 2 — Placer dine certifikatfiler

Opret mappen og kopier dine filer:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Kopier dine filer til den mappe med disse nøjagtige navne:

| Fil | Beskrivelse |
|------|-------------|
| `fullchain.pem` | Dit certifikat + eventuelle mellemliggende CA-certifikater (sammenkædet) |
| `privkey.pem` | Din private nøgle |

Eksempel:

```bash
# Kopiér fra din lokale maskine (kør dette lokalt, ikke på serveren)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Indstil korrekte tilladelser:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Trin 3 — Indtast dit domæne i appen

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. Klik på Installer certifikat manuelt på SSL-opsætningsskærmen
2. Indtast dit domænenavn (skal matche certifikatets fællesnavn eller SAN)
3. Klik på Anvend

Serveren konfigurerer Nginx med dit certifikat og genindlæser automatisk.

---

## Næste skridt

Når SSL er aktiv, skal du fortsætte til Første login [first-login](first-login).
