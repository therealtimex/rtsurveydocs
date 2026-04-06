---
title: "Používateľské rozhranie"
description: "Preskúmajte kľúčové funkcie mobilnej aplikácie rtSurvey vrátane vyplňovania formulárov, úprav, odosielania, oznámení, správy úloh, reportovania a GPS mapovania"
icon: "apps"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 314
---

Mobilná aplikácia rtSurvey ponúka komplexnú sadu funkcií navrhnutých na zefektívnenie procesu prieskumu. Tu sú kľúčové funkcie:

## Vyplniť formulár
Funkcia Vyplniť formulár je miestom, kde anketári môžu pristupovať k prázdnym prieskumným formulárom a zadávať dáta. Táto funkcia umožňuje efektívny a presný zber dát v teréne. Kľúčové body zahŕňajú:

1. Zoznam formulárov: Po vstupe do sekcie Vyplniť formulár sa používateľom zobrazí zoznam všetkých dostupných prázdnych formulárov, ktoré sú im priradené.

2. Automatické stiahnutie formulára: Na rozdiel od niektorých iných nástrojov prieskumu mobilná aplikácia rtSurvey automaticky stiahne formuláre, ku ktorým používateľ dostal prístup od správcu prieskumu alebo projektového manažéra. Tým sa eliminuje potreba anketárov manuálne získavať prázdne formuláre.

3. Priamy vstup dát: Anketári môžu vybrať formulár zo zoznamu a začať priamo zadávať odpovede prieskumu do aplikácie.

4. Aktualizácie v reálnom čase: Pri prideľovaní nových formulárov alebo vykonávaní aktualizácií sa zoznam dostupných formulárov automaticky obnoví, čím sa zaistí, že anketári majú vždy prístup k najnovším prieskumom.

5. Offline schopnosť: Formuláre možno stiahnuť pri dostupnosti internetového pripojenia, čo umožňuje anketárom ich vyplňovať aj v oblastiach so slabým alebo žiadnym sieťovým pokrytím.

## Upraviť formulár

Funkcia Upraviť formulár v rtSurvey ponúka komplexný a flexibilný prístup k správe inštancií prieskumu, čím sa odlišuje od iných CAPI aplikácií. Táto funkcia zabezpečuje presnosť a úplnosť dát prostredníctvom troch odlišných kariet:

1. **Uložené**:
   - Prístup k neúplným inštanciám rozhovoru uloženým na zariadení anketára a ich úprava.
   - Podobné tradičným CAPI aplikáciám, čo umožňuje používateľom pokračovať a dokončiť nedokončené prieskumy.

2. **Vrátené** (exkluzívne pre rtSurvey):
   - Úprava inštancií prieskumu, ktoré boli predtým dokončené, finalizované a odoslané na server.
   - Táto funkcia, jedinečná pre rtSurvey, umožňuje úpravy po odoslaní, keď sú potrebné ďalšie informácie alebo opravy.

3. **Presmerované** (exkluzívne pre rtSurvey):
   - Prístup k inštanciám prieskumu pôvodne vytvoreným na inom zariadení a ich úprava.
   - Táto inovatívna funkcia podporuje rôzne scenáre:
     * Supervízori môžu kontrolovať a upravovať odoslania od anketárov.
     * Používatelia môžu pokračovať v práci na inom zariadení, ak ich pôvodné zariadenie bolo stratené alebo poškodené.
     * Umožňuje spoluprácu pri úpravách a procesy kontroly kvality.

Kľúčové výhody:
- Vylepšená kvalita dát prostredníctvom viacerých príležitostí na kontrolu a úpravu.
- Vylepšená flexibilita pracovného postupu pre terénne tímy a supervízorov.
- Bezproblémové pokračovanie práce naprieč zariadeniami, čím sa znižujú výpadky a riziká straty dát.


## Odoslať formulár
Odosielanie 100% dokončených formulárov na centrálny server. Táto funkcia umožňuje prenos dát v reálnom čase, čo umožňuje okamžitú analýzu a rozhodovanie.

## Oznámenia
Prijímajte dôležité upozornenia a aktualizácie zo servera. Tým sú všetci členovia tímu informovaní o vývoji projektu, zmenách alebo naliehavých záležitostiach.

## Úlohy
Pristupujte k úlohám priradeným serverom a spravujte ich. Táto funkcia pomáha organizovať záťaž a uprednostňovať prieskumné aktivity pre terénnych anketárov.

## Správy
Zobrazujte všetky správy zaslané zo servera na tablet. Táto funkcia umožňuje používateľom pristupovať k výsledkom analýz a projektovým prehľadom priamo na ich zariadení.

## Skontrolovať formulár

Funkcia Skontrolovať formulár v rtSurvey ponúka komplexný systém na preskúmanie a správu finalizovaných inštancií prieskumu, čím zabezpečuje robustnú kontrolu kvality a overovanie dát. Táto funkcia je rozdelená do štyroch odlišných kariet, každá slúžiaca na konkrétny účel v procese správy dát:

1. **Finalizované**:
   - Obsahuje dokončené a finalizované inštancie, ktoré ešte neboli odoslané na server.
   - Umožňuje záverečné kontroly pred odoslaním.

2. **Odoslané**:
   - Obsahuje finalizované inštancie, ktoré boli úspešne odoslané na server.
   - Poskytuje záznam prenesených dát.

3. **Presunuté**:
   - Zobrazuje dokončené inštancie, ktoré boli presunuté na iné zariadenia.
   - Uľahčuje sledovanie pohybu dát medzi zariadeniami.

4. **Prijaté**:
   - Zobrazuje dokončené inštancie pôvodne vytvorené na inom zariadení a presunuté na aktuálne zariadenie.
   - Umožňuje spoluprácu a zdieľanie dát medzi členmi tímu.

Kľúčové funkcie:
- **Prístup iba na čítanie**: Všetky inštancie v týchto kartách sú pôvodne iba na čítanie, čím sa zachováva integrita dát finalizovaných formulárov.
- **Systém žiadostí o úpravu**: Používatelia môžu požiadať o úpravu inštancie, ak sú potrebné opravy.
  - Žiadosti môžu byť schválené automaticky alebo manuálne správcami alebo projektovými manažérmi.
  - Po schválení sa inštancia stane upraviteľnou, čo umožňuje potrebné zmeny.

Výhody:
- Zvyšuje kvalitu dát prostredníctvom viacerých fáz kontroly.
- Poskytuje jasnú auditovú stopu odoslaní dát a prenosov.
- Ponúka flexibilitu správy dát pri zachovaní kontroly nad finalizovanými dátami.
- Podporuje spoluprácu v pracovných postupoch a procesy zabezpečenia kvality.

Tento pokročilý systém Skontrolovať formulár odlišuje rtSurvey tým, že ponúka štruktúrovaný prístup k správe finalizovaných dát, zabezpečeniu presnosti a umožneniu kontrolovaných úprav po finalizácii, keď je to potrebné. Vytvára rovnováhu medzi integritou dát a potrebou príležitostných opráv, čo z neho robí neoceniteľný nástroj pre prieskumné projekty vyžadujúce vysokú úroveň kvality dát a zodpovednosti.

## Mapa
Využite GPS funkciu na presné určenie miesta, kde sa vykonáva rozhovor. Táto funkcia zvyšuje presnosť dát a pomáha pri priestorovej analýze výsledkov prieskumu.

## Ukončiť
Zatvorte aplikáciu bez odhlásenia sa z účtu rtSurvey. Tým je umožnené rýchle znovu vstúpenie do aplikácie bez potreby opakovanej autentifikácie.

Tieto funkcie spolupracujú na vytvorení výkonného, užívateľsky prívetivého mobilného nástroja na prieskum, ktorý vyhovuje rôznym rolám v procese prieskumu, od zberu dát po analýzu a správu projektu.
