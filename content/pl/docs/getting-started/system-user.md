---
weight: 15
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Użytkownik systemu"
icon: "people"
toc: true
description: "Zarządzaj rolami, uprawnieniami i onboardingiem wszystkich uczestników platformy."
tags: ["Users", "Access Control", "Onboarding", "Roles"]
---

# Zarządzanie użytkownikami systemu

Moduł **Użytkownik systemu** (`/cpms/cpmsSystemUser/admin`) to kompleksowy interfejs zarządzania kontrolujący, kto ma dostęp do Twojej platformy Real-Time Survey (RT-CPMS) i jakie działania może wykonywać.

![Interfejs użytkownika systemu](/images/system_user.png)

## Zunifikowane podejście do zarządzania

W RT-CPMS **Ankieter** to po prostu konkretna rola przypisana Użytkownikowi systemu. Nie istnieje oddzielna baza danych „Ankieterów". Niezależnie od tego, czy użytkownik jest administratorem wysokiego szczebla monitorującym portal internetowy, czy terenowym Ankieterem zbierającym dane przez aplikację mobilną — wszyscy są zarządzani w ramach tego jednego, ujednoliconego systemu.

## Kluczowe funkcje

### 1. Katalog użytkowników i widok siatki
Główny interfejs wyświetla stronicowaną listę wszystkich użytkowników połączonych z obszarem roboczym. Kluczowe atrybuty obejmują:
* **ID i nazwa organizacji**: Logiczne grupowanie użytkowników w ramach konkretnych podmiotów organizacyjnych (np. `rta`, `partner_org`).
* **Rola**: Określa poziom uprawnień użytkownika (np. `Administrator`, `Leadteam`, `Enumerator`).
* **Grupa**: Przypisania przestrzennych lub logicznych grup (np. konkretne powiaty lub zespoły operacyjne).
* **Zsynchronizowany**: Wskazuje, czy konto jest pomyślnie zintegrowane z centralnym systemem Single Sign-On (SSO).
* **Status**: Wizualne wskaźniki potwierdzające, czy konto jest `Active`, `Inactive`, `Deleted` lub `Blocked`.

**Działania globalne:**
* **Dodaj użytkownika systemu**: Ręcznie utwórz indywidualny profil.
* **Importuj użytkownika systemu**: Masowe przesyłanie kont przy użyciu szablonu Excel. Możesz rozwiązywać konflikty używając trybów `Skip` lub `Replace` i synchronizować bezpośrednio z SSO.
* **Usuń masowo**: Obsługa wielokrotnego wyboru do masowego usuwania kont.

### 2. Kontrola dostępu i bezpieczeństwo
Podczas tworzenia lub edytowania profilu użytkownika dostępnych jest kilka krytycznych pól bezpieczeństwa i przepływu pracy:
* **Kod użytkownika**: Unikalny identyfikator łączący lokalne konto CPMS z centralnym repozytorium SSO.
* **Kod zmiany urządzenia**: Solidny token bezpieczeństwa wymagany, gdy ankieter musi przełączyć urządzenie mobilne używane do zbierania danych.
* **Poziom uprawnień**: Szczegółowa skala priorytetu/dostępu od 0 (najniższy) do 20 (najwyższy).
* **Przełącznik nadzorczy**: Pole wyboru natychmiast podnoszące standardowego użytkownika do statusu zarządzającego.
* **Automatyzacja przepływu pracy**: Opcja „Automatycznie zatwierdzaj prośbę o edycję", która usprawnia proces czyszczenia danych i weryfikacji dla zaufanych użytkowników.

### 3. Zarządzanie kodami (automatyczny onboarding)
Dostępna w zakładce podrzędnej „Kod", ta funkcja zarządza linkami do rejestracji i zaproszeń opartymi na skrótach, usprawniając proces onboardingu dla dużych zespołów.

* **Rejestracja vs zaproszenie**: Wybierz, czy użytkownicy mogą samodzielnie rejestrować się przy użyciu rozprowadzonego linku, czy wymagają bezpośredniego zaproszenia od administratora.
* **Daty wygaśnięcia**: Ogranicz onboarding do określonych przedziałów czasowych.
* **Limity użytkowania**: Ogranicz liczbę użytkowników, którzy mogą dołączyć przy użyciu jednego wygenerowanego kodu.
* **Wstępnie przypisane role**: Użytkownicy dołączający przez te kody automatycznie dziedziczą wstępnie zdefiniowaną rolę i poziom uprawnień, zapewniając im gotowość do pracy natychmiast bez ręcznej interwencji administratora.
