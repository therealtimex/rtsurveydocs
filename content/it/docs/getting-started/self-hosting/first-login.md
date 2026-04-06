---
weight: 5
title: "Primo accesso"
date: "2026-04-01T00:00:00+07:00"
lastmod: "2026-04-01T00:00:00+07:00"
draft: false
author: "rtSurvey"
icon: "login"
toc: true
description: "Come accedere alla propria istanza rtSurvey per la prima volta dopo la distribuzione."
---

> **SSL deve essere configurato prima dell'accesso.** Se si accede all'applicazione tramite HTTP, verrà visualizzato un avviso di sicurezza e SSO sarà bloccato. Completare prima la [Configurazione SSL](ssl-setup).

Una volta che SSL è attivo, aprire il browser all'URL HTTPS:

```
https://your-domain.com
```

---

## La schermata di accesso

<!-- SCREENSHOT NEEDED: login page over HTTPS — username/password form + SSO button -->

La pagina di accesso mostra:

- Campi **Nome utente** e **Password**
- Un pulsante **Accedi**
- Un pulsante **Accedi con SSO** (sotto un divisore) — per i membri del team con account SSO

---

## Credenziali amministratore predefinite

Inserire le credenziali predefinite e fare clic su **Accedi**:

| Campo | Valore |
|-------|--------|
| Nome utente | `admin` |
| Password | `admin` |

> **Cambiare la password immediatamente dopo il primo accesso.**

---

## Se viene visualizzato un avviso di sicurezza

Se si accede all'applicazione tramite HTTP (prima della configurazione SSL), si vedrà:

- Un banner di avviso giallo nella parte superiore della pagina di accesso
- Un modal quando si fa clic su **Accedi**, che avverte che le credenziali verranno inviate non crittografate

<!-- SCREENSHOT NEEDED: HTTP warning banner on login page -->
<!-- SCREENSHOT NEEDED: SSL warning modal with "Set up SSL" and "Continue anyway" buttons -->

Fare clic su **Configura SSL** per configurare HTTPS, o su **Continua comunque** per accedere senza SSL (non consigliato).

Il login SSO è completamente bloccato tramite HTTP — fare clic su **Accedi con SSO** mostrerà un avviso anziché reindirizzare.

---

## Dopo l'accesso

Una volta dentro, si atterrerà sulla dashboard. Da qui:

1. **Cambiare la password amministratore** — impostazioni account → cambia password
2. **Creare il primo progetto** — Progetti → Nuovo progetto
3. **Caricare o creare un modulo** — Moduli → Carica XLSForm o apri Form Builder
4. **Aggiungere utenti** — Utenti → Invita o crea account per il tuo team
