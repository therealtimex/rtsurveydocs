---
weight: 4
title: "Nastavení SSL"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "lock"
toc: true
description: "Nakonfigurujte HTTPS pro váš server rtSurvey. Vyžadováno před přihlášením."
---

SSL musí být nakonfigurován, než se budete moci přihlásit. Když otevřete aplikaci poprvé, budete automaticky přesměrováni na obrazovku nastavení SSL.

---

## Možnosti nastavení SSL

![Možnosti nastavení SSL](/img/ssl-setup/ssl-setup-options.png)

Zvolte jednu ze tří možností:

| Možnost | Kdy použít |
|---------|-----------|
| **Bezplatná subdoména rtsurvey.com** *(Doporučeno)* | Není potřeba nastavení DNS. Záznam vytvoříme za vás. Připraveno za 2–5 minut. |
| **Vlastní doména** | Již máte doménu a její DNS míří na tento server. |
| **Ruční instalace certifikátu** | Podnikové nebo vlastní CA. Vyžaduje přístup SSH. |

---

## Možnost 1 — Bezplatná subdoména rtsurvey.com *(Doporučeno)*

Toto je nejrychlejší možnost. Nevyžaduje registraci domény ani změny DNS.

1. Klikněte na **Bezplatná subdoména rtsurvey.com** pro rozbalení sekce
2. Zadejte požadovaný název subdomény

   > Používejte malá písmena, čísla a pomlčky. 3–30 znaků.
   > Příklad: `myproject` → `myproject.rtsurvey.com`

3. Klikněte na **Vytvořit https://[subdomain].rtsurvey.com**

<!-- SCREENSHOT NEEDED: subdomain input filled in, before clicking Create -->

4. Počkejte 2–5 minut na vydání certifikátu

<!-- SCREENSHOT NEEDED: certificate being issued / progress state -->

5. Jakmile je certifikát připraven, budete automaticky přesměrováni na novou HTTPS adresu

<!-- SCREENSHOT NEEDED: success state / redirect to login -->

---

## Možnost 2 — Vlastní doména

Použijte, pokud máte existující doménu a její DNS `A` záznam již míří na IP tohoto serveru.

1. Klikněte na **Vlastní doména** pro rozbalení
2. Zadejte celé doménové jméno (např. `survey.myorganization.org`)
3. Klikněte na **Vytvořit certifikát**

<!-- SCREENSHOT NEEDED: own domain input form -->

Let's Encrypt ověří vaši doménu a vydá certifikát. DNS musí být správně nastaven předem — jinak požadavek selže.

---

## Možnost 3 — Ruční instalace certifikátu

Pro podniková prostředí s vlastním nebo interním CA. Umístíte soubory certifikátu na server přes SSH a poté zadáte doménu v aplikaci.

### Předpoklady

- SSH přístup k serveru
- Platný certifikát a privátní klíč pro vaši doménu (formát PEM)

### Krok 1 — SSH na server

```bash
ssh root@<server-ip>
```

### Krok 2 — Umístěte soubory certifikátu

Vytvořte adresář a zkopírujte soubory:

```bash
mkdir -p /etc/letsencrypt/live/<your-domain>
```

Zkopírujte soubory s přesnými názvy:

| Soubor | Popis |
|--------|-------|
| `fullchain.pem` | Váš certifikát + mezilehlé CA certifikáty (zřetězené) |
| `privkey.pem` | Váš privátní klíč |

Příklad:

```bash
# Kopírování z lokálního počítače (spusťte lokálně, ne na serveru)
scp fullchain.pem root@<server-ip>:/etc/letsencrypt/live/<your-domain>/fullchain.pem
scp privkey.pem  root@<server-ip>:/etc/letsencrypt/live/<your-domain>/privkey.pem
```

Nastavte správná oprávnění:

```bash
chmod 644 /etc/letsencrypt/live/<your-domain>/fullchain.pem
chmod 600 /etc/letsencrypt/live/<your-domain>/privkey.pem
```

### Krok 3 — Zadejte doménu v aplikaci

<!-- SCREENSHOT NEEDED: manual certificate form -->

1. Na obrazovce nastavení SSL klikněte na **Ruční instalace certifikátu**
2. Zadejte doménové jméno (musí odpovídat Common Name nebo SAN certifikátu)
3. Klikněte na **Použít**

Server nakonfiguruje Nginx s vaším certifikátem a automaticky se znovu načte.

---

## Další krok

Jakmile je SSL aktivní, pokračujte na [První přihlášení](first-login).
