---
weight: 150
date: "2023-05-03T22:37:22+01:00"
draft: false
author: "RealTimeX"
title: "Zbieranie danych"
icon: "rocket_launch"
toc: true
description: "Skrócony przewodnik po prowadzeniu ankiety za pomocą rtSurvey"
publishdate: "2023-05-03T22:37:22+01:00"
tags: ["Beginners"]
---

Po wdrożeniu formularza i przypisaniu ankieterów można rozpocząć zbieranie danych. **rtSurvey** obsługuje płynne zbieranie danych zarówno przez przeglądarki internetowe, jak i dedykowane aplikacje mobilne, zapewniając elastyczność niezależnie od tego, czy Twój zespół ma dostęp do internetu, czy pracuje w odległych obszarach bez połączenia.

## Wybór odpowiedniej metody zbierania

W zależności od geografii i łączności projektu możesz wybrać optymalną metodę dla swoich ankieterów:

- **Przeglądarka internetowa (online):** Najlepsza dla centrów telefonicznych, wprowadzania danych w biurze lub respondentów wypełniających samodzielnie administrowane publiczne ankiety.
- **Aplikacja mobilna rtWork / rtSurvey (online i offline):** Najlepsza dla operacji terenowych, odległych obszarów z niestabilnym internetem i ankiet wymagających załączników multimedialnych (zdjęcia, współrzędne GPS, mapy offline).

---

## Metoda 1: Zbieranie danych przez przeglądarkę internetową

Korzystanie z interfejsu Webform umożliwia ankieterom natychmiastowe rozpoczęcie zbierania danych bez instalowania żadnego oprogramowania.

### 1. Uzyskaj dostęp do URL Webform
Z pulpitu nawigacyjnego **Zarządzanie formularzami** w Panelu sterowania znajdź docelowy formularz i kliknij przycisk **URL Webform**, aby wygenerować bezpieczny link.

### 2. Wypełnianie formularza
- Otwórz podany URL w dowolnej nowoczesnej przeglądarce internetowej.
- Jeśli formularz wymaga uwierzytelnienia, ankieter musi zalogować się przy użyciu swoich danych. Jeśli jest ustawiony na „Widoczność publiczna", może przejść bezpośrednio.
- Wypełnij pytania ankiety. Interfejs automatycznie wymusi logikę, wzorce pomijania i reguły walidacji.
- **Przechwytywanie mediów:** Jeśli formularz zawiera pytania dotyczące obrazów, audio lub wideo, przeglądarka poprosi o przesłanie pliku z komputera lub użycie kamery/mikrofonu urządzenia, jeśli są dostępne.

### 3. Przesyłanie
Po dotarciu do ostatniej strony kliknij **Prześlij**. Przeglądarka wymaga aktywnego połączenia internetowego do sfinalizowania przesłania. Po pomyślnym przesłaniu dane natychmiast pojawią się w interfejsie **Zarządzanie zgłoszeniami**.

---

## Metoda 2: Zbieranie danych przez aplikację mobilną (offline)

W przypadku solidnego terenowego zbierania danych aplikacje mobilne zapewniają pełne możliwości offline.

### 1. Instalacja i uwierzytelnienie
- Pobierz aplikację **rtWork** (lub **rtSurvey**) ze sklepu Google Play lub Apple App Store.
- Otwórz aplikację i zaloguj się przy użyciu przypisanych danych ankietera.

### 2. Pobieranie formularzy (wymaga internetu)
- Przejdź do sekcji **Formularze** lub **Zadania** w aplikacji.
- Dotknij ikony **Synchronizuj** lub **Pobierz**, aby pobrać najnowsze projekty kwestionariuszy z serwera. Po pobraniu formularze są przechowywane lokalnie na urządzeniu.

### 3. Zbieranie danych (offline)
- Otwórz pobrany formularz i rozpocznij wywiad.
- Możesz bezpiecznie zbierać dane w pełni offline.
- **Przechwytywanie mediów:** Aplikacja mobilna natywnie integruje się ze sprzętem urządzenia. Możesz robić zdjęcia, nagrywać audio, nagrywać wideo i rejestrować dokładne współrzędne GPS bezpośrednio w aplikacji, nawet bez połączenia internetowego.
- Po zakończeniu wywiadu sfinalizuj rekord. Sfinalizowane rekordy są bezpiecznie kolejkowane w skrzynce nadawczej aplikacji.

### 4. Synchronizacja zgłoszeń (wymaga internetu)
- Gdy ankieter wróci do obszaru z dostępem do internetu (Wi-Fi lub dane komórkowe), musi przejść do interfejsu **Skrzynka nadawcza** lub **Synchronizuj**.
- Poleć aplikacji wysłanie sfinalizowanych formularzy. Aplikacja bezpiecznie prześle kolejkowane rekordy i wszystkie dołączone pliki multimedialne do serwera, po czym pojawią się w siatce danych do przeglądu.
