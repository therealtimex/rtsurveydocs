---
weight: 10
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Prehľad dashboardu"
icon: "home"
toc: true
description: "Pochopenie dashboardu systému RT-CPMS a nástrojov na dohľad nad projektmi."
tags: ["Dashboard", "Prehľad", "Monitorovanie"]
---

# Systémový dashboard

Dashboard (`/cpms/cpmsDashBoard/indexNew`) slúži ako administratívne veliteľské centrum a hlavná vstupná stránka platformy Real-Time Survey (RT-CPMS).

![Ukážka systémového dashboardu](/images/dashboard_overview.png)

Je navrhnutý tak, aby manažérom prieskumov poskytol okamžitý prehľad aktívnych projektov, rýchle prepojenia na základné nástroje a centralizovaný uzol na navigáciu cez všetky hlavné moduly platformy.

## Kľúčové funkcie

### 1. Výber projektu a formulára
Ľavý panel obsahuje navigátor **Formuláre a správy**. Táto oblasť zobrazuje všetky aktívne prieskumy vo vašom pracovnom priestore.
* Výberom konkrétneho prieskumu (napr. *RTA - PRIESKUM 02*) zacielite dashboard na monitorovanie a metriky výlučne pre daný projekt.

### 2. Filtre vizualizácie a metrík
Nad zoznamom projektov môžete prepínať medzi viacerými kritickými pohľadmi na dáta na sledovanie postupu terénnych prác v reálnom čase:
* **Počet podľa času začiatku / času ukončenia**: Sledujte, kedy anketári začínajú a dokončujú svoje prieskumné sedenia.
* **Počet podľa dátumu odoslania**: Monitorujte celkový denný objem dát prichádzajúcich na server.
* **Počet podľa používateľského mena**: Vyhodnoťte produktivitu a výkon jednotlivých anketárov.
* **Mapa rozhovorov**: Zobrazte geografické (GIS) rozloženie miest, kde sú zbierané odpovede z prieskumu, aby ste zaistili splnenie požiadaviek na priestorové pokrytie.

### 3. Portály aplikácií
Stred dashboardu poskytuje okamžitý prístup k rozhraniam zberu dát. V závislosti od hardvéru vašich anketárov môžete spustiť alebo nasmerovať ich na:
* **Webová aplikácia**: Na zber dát cez prehliadač.
* **Aplikácia pre Android**: Odkaz na Google Play Store alebo APK.
* **Aplikácia pre iOS**: Odkaz na Apple App Store.

### 4. Priame skratky k modulom
Tri výrazné akčné tlačidlá umožňujú rýchly prechod na najčastejšie používané prevádzkové moduly:
* **Vstup formulára a dát**: Priamy prechod na manuálnu správu zozbieraných dát.
* **Analýzy a správy**: Otvorenie sady Business Intelligence (BI) na kríženú tabuláciu a grafiku odpovedí z prieskumu.
* **Konfigurácia oprávnení**: Nastavenie toho, kto má prístup k aktívnemu prieskumu a aké roly zastáva.

### 5. Globálny navigačný panel
Zbaliteľný ľavý panel poskytuje prístup ku kompletnému ekosystému backendových modulov RT-CPMS. Odtiaľ môžete sa ponoriť do:
* **Nastavenie**: Správa personálu a aktívnych zariadení.
* **Správa terénnych prác**: Sledovanie dennej aktivity anketárov.
* **Zabezpečenie kvality**: Implementácia a kontrola pravidiel a príznakov QA.
* **Záverečné výsledky**: Export vyčistených dátových sád do CSV, PDF alebo Stata.
