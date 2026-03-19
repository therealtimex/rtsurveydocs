---
weight: 150
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "RealTimeX"
title: "Sběr dat"
icon: "rocket_launch"
toc: true
description: "Průvodce rychlým spuštěním průzkumu v rtSurvey"
publishdate: "2023-05-03T22:37:22+01:00"
tags: ["Začátečníci"]
---

Jakmile je formulář nasazen a enumerátoři jsou přiřazeni, může začít sběr dat. **rtSurvey** podporuje bezproblémové shromažďování dat ve webových prohlížečích i v dedikovaných mobilních aplikacích, čímž zajišťuje flexibilitu bez ohledu na to, zda je váš tým připojen k internetu nebo pracuje ve vzdálených offline prostředích.

## Výběr správné metody sběru

V závislosti na geografii a připojení vašeho projektu si můžete vybrat optimální metodu pro vaše enumerátory:

- **Webový prohlížeč (Online):** Nejlepší pro call centra, zadávání dat v kanceláři nebo respondenty vyplňující veřejné průzkumy spravované samostatně.
- **Mobilní aplikace rtWork / rtSurvey (Online i Offline):** Nejlepší pro terénní operace, vzdálené oblasti s nestabilním internetem a průzkumy vyžadující mediální přílohy (fotografie, GPS souřadnice, offline mapy).

---

## Metoda 1: Sběr dat přes webový prohlížeč

Použití rozhraní webového formuláře umožňuje enumerátorům okamžitě zahájit sběr dat bez instalace jakéhokoli softwaru.

### 1. Přístup k URL webového formuláře
Z dashboardu **Správa formulářů** v Ovládacím panelu vyhledejte cílový formulář a klikněte na tlačítko **URL webového formuláře** pro vygenerování bezpečného odkazu.

### 2. Vyplňování formuláře
- Otevřete poskytnutou URL v libovolném moderním webovém prohlížeči.
- Pokud formulář vyžaduje ověření, enumerátor se musí přihlásit pomocí svých přihlašovacích údajů. Pokud je nastaven jako „Veřejná viditelnost", mohou pokračovat přímo.
- Vyplňte otázky průzkumu. Rozhraní automaticky vynucuje logiku, vzory přeskakování a pravidla validace.
- **Zachycení médií:** Pokud formulář obsahuje otázky s obrázky, zvukem nebo videem, webový prohlížeč vás vyzve k nahrání souboru z vašeho počítače nebo použití webové kamery/mikrofonu vašeho zařízení, pokud jsou dostupné.

### 3. Odeslání
Po dosažení poslední stránky klikněte na **Odeslat**. Prohlížeč vyžaduje aktivní připojení k internetu pro dokončení odeslání. Po úspěšném odeslání se data okamžitě zobrazí v rozhraní **Správa odeslání**.

---

## Metoda 2: Sběr dat přes mobilní aplikaci (Offline)

Pro robustní terénní sběr dat poskytují mobilní aplikace plné offline možnosti.

### 1. Instalace a ověření
- Stáhněte aplikaci **rtWork** (nebo **rtSurvey**) z Google Play Store nebo Apple App Store.
- Otevřete aplikaci a přihlaste se pomocí přidělených přihlašovacích údajů enumerátora.

### 2. Stažení formulářů (Vyžaduje internet)
- Přejděte do sekce **Formuláře** nebo **Úkoly** v aplikaci.
- Klepněte na ikonu **Synchronizace** nebo **Stažení** pro načtení nejnovějších návrhů dotazníků ze serveru. Po stažení jsou formuláře uloženy lokálně na zařízení.

### 3. Sběr dat (Offline)
- Otevřete stažený formulář a zahajte rozhovor.
- Data lze bezpečně sbírat zcela offline.
- **Zachycení médií:** Mobilní aplikace nativně integruje s hardwarem vašeho zařízení. Můžete pořizovat fotografie, nahrávat zvuk, nahrávat video a zaznamenávat přesné GPS souřadnice přímo v aplikaci, i bez připojení k internetu.
- Po dokončení rozhovoru záznam finalizujte. Finalizované záznamy jsou bezpečně zařazeny do fronty v outboxu aplikace.

### 4. Synchronizace odeslání (Vyžaduje internet)
- Jakmile se enumerátor vrátí do oblasti s přístupem k internetu (Wi-Fi nebo mobilní data), musí přejít do rozhraní **Outbox** nebo **Synchronizace**.
- Dejte aplikaci pokyn k odeslání finalizovaných formulářů. Aplikace přenese zařazené záznamy a všechny připojené mediální soubory bezpečně na server, načež se zobrazí v datové mřížce ke kontrole.
