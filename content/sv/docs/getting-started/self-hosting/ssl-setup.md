---
weight: 4
title: "Konfigurera SSL"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Konfigurera HTTPS för din rtSurvey-server. Krävs innan du kan logga in."
---

SSL måste konfigureras innan du kan logga in. När du öppnar appen för första gången omdirigeras du automatiskt till SSL-inställningsskärmen.

---

## SSL-inställningar

![SSL-inställningar](/img/ssl-setup/ssl-setup-options.png)

Välj ett av tre alternativ:

| Alternativ | När du ska använda |
|--------|-------------|
| **Gratis rtsurvey.com underdomän** *(Rekommenderad)* | Ingen DNS-installation behövs. Vi skapar skivan åt dig. Klar på 2–5 minuter. |
| **Min egen domän** | Du har redan en domän och dess DNS pekar på den här servern. |
| **Installera certifikat manuellt** | Enterprise eller anpassad CA. Kräver SSH-åtkomst. |

---

## Alternativ 1 — Gratis rtsurvey.com-underdomän (rekommenderas)

Detta är det snabbaste alternativet. Ingen domänregistrering eller DNS-ändringar krävs.

1. Klicka på Gratis rtsurvey.com-underdomän för att expandera avsnittet
2. Skriv ditt önskade underdomännamn i inmatningsfältet

   > Använd små bokstäver, siffror och bindestreck. 3–30 tecken.
   > Exempel: `myproject` → `myproject.rtsurvey.com`

3. Klicka på Skapa **https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Vänta 2–5 minuter medan certifikatet utfärdas

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. När certifikatet är klart omdirigeras du automatiskt till din nya HTTPS-URL

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Alternativ 2 — Min egen domän

Använd detta om du har en befintlig domän och dess DNS A-post redan pekar på denna servers IP.

1. Klicka på Min egen domän för att expandera avsnittet
2. Ange ditt fullständiga domännamn (e.g. `survey.myorganization.org`)
3. Klicka på Skapa certifikat

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt kommer att verifiera din domän och utfärda ett certifikat. Detta kräver att DNS pekas korrekt först – begäran misslyckas annars.

---

## Alternativ 3 — Installera certifikat manuellt

För företagsmiljöer som använder en anpassad eller intern CA. Du placerar dina certifikatfiler på servern via SSH och anger sedan din domän i appen.

### Förutsättningar

- SSH-åtkomst till servern
- Ett giltigt certifikat och privat nyckel för din domän (PEM-format)

### Steg 1 — SSH till servern

```bash
ssh root@<server-ip>
```

### Steg 2 — Placera dina certifikatfiler

Skapa katalogen och kopiera dina filer:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Kopiera dina filer till den katalogen med dessa exakta namn:

| Fil | Beskrivning |
|------|-------------|
| `fullchain.pem` | Ditt certifikat + eventuella mellanliggande CA-certifikat (sammankopplade) |
| `privkey.pem` | Din privata nyckel |

Exempel:

```bash
# Kopiera från din lokala dator (kör detta lokalt, inte på servern)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Ange korrekta behörigheter:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Steg 3 — Ange din domän i appen

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. Klicka på Installera certifikat manuellt på SSL-inställningsskärmen
2. Ange ditt domännamn (måste matcha certifikatets Common Name eller SAN)
3. Klicka på Använd

Servern konfigurerar Nginx med ditt certifikat och laddar om automatiskt.

---

## Nästa steg

När SSL är aktivt, fortsätt till Första inloggningen [first-login](first-login).
