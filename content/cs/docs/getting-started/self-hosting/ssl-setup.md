---
weight: 4
title: "Nastavte SSL"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Nakonfigurujte HTTPS pro váš server rtSurvey. Povinné před přihlášením."
---

Před přihlášením je nutné nakonfigurovat SSL. Při prvním otevření aplikace budete automaticky přesměrováni na obrazovku nastavení SSL.

---

## Možnosti nastavení SSL

![Možnosti nastavení SSL](/img/ssl-setup/ssl-setup-options.png)

Vyberte jednu ze tří možností:

| Volba | Kdy použít |
|--------|-------------|
| **Zdarma subdoména rtsurvey.com** *(Doporučeno)* | Není potřeba žádné nastavení DNS. Záznam vytvoříme za vás. Připraveno za 2–5 minut. |
| **Moje vlastní doména** | Již máte doménu a její DNS body na tento server. |
| **Nainstalujte certifikát ručně** | Podniková nebo vlastní CA. Vyžaduje přístup SSH. |

---

## Možnost 1 — bezplatná subdoména rtsurvey.com (doporučeno)

Toto je nejrychlejší možnost. Nevyžaduje registraci domény ani změny DNS.

1. Kliknutím na Free rtsurvey.com subdoména rozbalte sekci
2. Do vstupního pole zadejte požadovaný název subdomény

   > Používejte malá písmena, čísla a pomlčky. 3–30 znaků.
   > Příklad: `myproject` → `myproject.rtsurvey.com`

3. Klikněte na Vytvořit **https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Počkejte 2–5 minut, než bude certifikát vydán

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Jakmile bude certifikát připraven, budete automaticky přesměrováni na svou novou HTTPS URL

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Možnost 2 – Moje vlastní doména

Toto použijte, pokud máte existující doménu a její záznam DNS A již ukazuje na IP tohoto serveru.

1. Kliknutím na položku Moje vlastní doména rozbalíte sekci
2. Zadejte celý název domény (e.g. `survey.myorganization.org`)
3. Click Create certificate

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt ověří vaši doménu a vydá certifikát. To vyžaduje, aby byl nejprve správně nasměrován DNS — jinak požadavek selže.

---

## Možnost 3 — Ruční instalace certifikátu

Pro podniková prostředí používající vlastní nebo interní CA. Soubory certifikátů umístíte na server přes SSH a poté do aplikace zadáte svou doménu.

### Předpoklady

- SSH přístup k serveru
- Platný certifikát a soukromý klíč pro vaši doménu (formát PEM)

### Krok 1 — SSH na server

```bash
ssh root@<server-ip>
```

### Krok 2 — Umístěte soubory certifikátů

Vytvořte adresář a zkopírujte soubory:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Copy your files into that directory with these exact names:

| Soubor | Popis |
|------|-------------|
| `fullchain.pem` | Váš certifikát + případné zprostředkující certifikáty CA (zřetězené) |
| `privkey.pem` | Váš soukromý klíč |

Příklad:

```bash
# Zkopírujte z místního počítače (spusťte to lokálně, ne na serveru)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Nastavte správná oprávnění:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Krok 3 — Zadejte svou doménu do aplikace

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. Na obrazovce nastavení SSL klikněte na Instalovat certifikát ručně
2. Zadejte název své domény (musí se shodovat s běžným názvem certifikátu nebo SAN)
3. Klepněte na tlačítko Použít

Server nakonfiguruje Nginx s vaším certifikátem a automaticky se znovu načte.

---

## Další krok

Jakmile je SSL aktivní, přejděte na První přihlášení [first-login](first-login).
