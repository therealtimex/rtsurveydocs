---
weight: 15
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Systémový uživatel"
icon: "people"
toc: true
description: "Správa rolí, oprávnění a registrace pro všechny účastníky platformy."
tags: ["Uživatelé", "Řízení přístupu", "Registrace", "Role"]
---

# Správa systémových uživatelů

Modul **Systémový uživatel** (`/cpms/cpmsSystemUser/admin`) je komplexní správcovské rozhraní pro kontrolu přístupu uživatelů k platformě Real-Time Survey (RT-CPMS) a akcí, které mohou provádět.

![Rozhraní systémového uživatele](/images/system_user.png)

## Jednotný přístup ke správě

V RT-CPMS je **enumerátor** jednoduše specifická role přiřazená systémovému uživateli. Neexistuje žádná samostatná databáze „enumerátorů". Ať už je uživatel vysokoúrovňový administrátor sledující webový portál nebo terénní enumerátor sbírající data přes mobilní aplikaci, všichni jsou spravováni v rámci tohoto jediného, sjednoceného rámce.

## Klíčové funkce

### 1. Adresář uživatelů a zobrazení mřížky
Hlavní rozhraní zobrazuje stránkovaný seznam všech uživatelů připojených k pracovnímu prostoru. Klíčové atributy zahrnují:
* **ID a název organizace**: Logické seskupení uživatelů pod konkrétní organizační entity (např. `rta`, `partner_org`).
* **Role**: Určuje úroveň oprávnění uživatele (např. `Administrator`, `Leadteam`, `Enumerator`).
* **Skupina**: Prostorová nebo logická přiřazení skupin (např. konkrétní okresy nebo provozní týmy).
* **Je synchronizován**: Indikuje, zda je účet úspěšně integrován s centrálním systémem jednotného přihlášení (SSO).
* **Stav**: Vizuální indikátory potvrzující, zda je účet `Aktivní`, `Neaktivní`, `Smazaný` nebo `Zablokovaný`.

**Globální akce:**
* **Přidat systémového uživatele**: Ruční vytvoření individuálního profilu.
* **Importovat systémového uživatele**: Hromadné nahrávání účtů pomocí šablony Excel. Konflikty lze řešit pomocí režimů `Přeskočit` nebo `Nahradit` a synchronizovat přímo s SSO.
* **Hromadné smazání**: Podpora vícenásobného výběru pro hromadné odebrání účtů.

### 2. Řízení přístupu a bezpečnost
Při vytváření nebo úpravě uživatelského profilu je k dispozici několik kritických polí pro bezpečnost a pracovní postup:
* **Kód uživatele**: Jedinečný identifikátor propojující lokální CPMS účet s centrálním úložištěm SSO.
* **Kód změny zařízení**: Robustní bezpečnostní token vyžadovaný, když enumerátor potřebuje přepnout mobilní zařízení, které používá pro sběr dat.
* **Úroveň oprávnění**: Granulární prioritní/přístupová škála v rozsahu od 0 (nejnižší) do 20 (nejvyšší).
* **Přepínač dohledu**: Zaškrtávací políčko, které okamžitě povýší standardního uživatele na status manažera.
* **Automatizace pracovního postupu**: Možnost „Automaticky schvalovat požadavek na úpravu", která zjednodušuje proces čištění a ověřování dat pro důvěryhodné uživatele.

### 3. Správa kódů (automatizovaná registrace)
Tato funkce, dostupná pod záložkou „Kód", spravuje registrační a pozvánkové odkazy na základě hashů a zjednodušuje proces registrace pro velké týmy.

* **Registrace vs. pozvánka**: Zvolte, zda se uživatelé mohou registrovat sami pomocí distribuovaného odkazu nebo zda vyžadují přímou pozvánku od administrátora.
* **Data vypršení platnosti**: Omezení registrace na konkrétní časová okna.
* **Limity použití**: Omezení počtu uživatelů, kteří se mohou připojit pomocí jediného vygenerovaného kódu.
* **Předem přiřazené role**: Uživatelé připojující se přes tyto kódy automaticky dědí předdefinovanou roli a úroveň oprávnění, čímž jsou okamžitě připraveni k práci bez ruční intervence administrátora.
