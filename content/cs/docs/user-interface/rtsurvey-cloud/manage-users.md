---
title: "Správa uživatelů"
description: "Vytváření, organizace a správa systémových uživatelů a terénního personálu."
icon: "cloud"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 314
---

Modul **Správa uživatelů** (často označovaný jako **Správa personálu** v nabídce Nastavení) je centralizovaný adresář pro zpracování všech účtů v prostředí CPMS. Poskytuje administrátorům projektů nástroje potřebné pro registraci personálu, přiřazování rolí a určování úrovní geografického přístupu.

![Rozhraní správy uživatelů](/images/manage_users.png)

## Přehled mřížky uživatelů

Hlavní rozhraní obsahuje komplexní mřížku zobrazující všechny registrované členy personálu. Toto zobrazení umožňuje administrátorům rychle vyhledávat, filtrovat a kontrolovat stavy účtů.

### Klíčové datové sloupce

Mřížka zahrnuje následující základní podrobnosti pro každého uživatele:

- **Uživatelské jméno a celé jméno:** Primární identifikátory člena personálu.
- **E-mail:** Kontaktní e-mailová adresa spojená s účtem.
- **Uživatelská role:** Označuje systémová oprávnění udělená uživateli (např. administrátor, zaměstnanec, monitor, host).
- **Skupina:** Zobrazuje konkrétní skupinu uživatelů nebo tým, do které člen personálu patří.
- **Stav:** Označuje, zda je účet aktuálně **Aktivní** nebo **Neaktivní**.
- **Datum vytvoření:** Časové razítko registrace účtu.

## Akce správy personálu

Administrátoři mají přístup k sadě nástrojů pro registraci a udržování uživatelských účtů, přístupných z horního ovládacího panelu:

- **Přidat personál:** Otevírá podrobný formulář pro vytvoření k ručnímu zadání profilu nového uživatele, včetně jeho role, přiřazených regionů a kontaktních informací.
- **Importovat personál:** Umožňuje hromadné vytváření účtů nahráním tabulky Excel. Je to zvláště užitečné pro rychlé vytváření velkých terénních týmů.
- **Stáhnout šablonu importu:** Poskytuje standardizovanou šablonu `.xlsx` vyžadovanou pro hromadný import.
- **Exportovat do Excelu:** Generuje stahovatelnou zprávu obsahující aktuálně filtrovaný seznam uživatelů a jejich detaily.
- **Smazat:** Trvale odebere vybrané uživatelské účty ze systému.

## Uživatelské profily a přiřazení

Při vytváření nebo úpravě konkrétního uživatele (přes tlačítko **Přidat personál** nebo kliknutím na uživatelské jméno) mohou administrátoři konfigurovat podrobné profily:

- **Osobní informace:** Pole pro datum narození, pohlaví, identifikační číslo a avatar.
- **Kontaktní údaje:** Číslo mobilního telefonu a podrobné informace o poloze (provincie, okres, obec, adresa).
- **Systémová přiřazení:** Klíčové pro bezpečnost dat — administrátoři mohou propojit uživatele s konkrétními **regiony** a přiřadit přesné **uživatelské role**.
- **Konfigurace dohledu:** V pokročilých nastaveních mohou být uživatelé přiřazeni specifickým kódům dohledu nebo namapováni na konkrétní tablety (zařízení).
