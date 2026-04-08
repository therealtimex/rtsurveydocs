---
title: "Typy pytań"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey obsługuje wszystkie standardowe typy pytań XLSForm oraz kilka rozszerzeń. Każdy typ pytania kontroluje, jaki rodzaj danych jest zbierany i jak widget wejściowy jest renderowany na urządzeniu.

Aby ustawić typ pytania, wprowadź nazwę typu w kolumnie `type` arkusza **survey** w XLSForm.

## Dane wejściowe tekstowe

| Typ | Opis |
|------|-------------|
| [text](text) | Odpowiedź wolnotekstowa — dozwolone są wszelkie znaki |
| [integer](integer) | Liczba całkowita (bez części dziesiętnej) |
| [decimal](decimal) | Liczba z miejscami dziesiętnymi |
| [range](range) | Liczba wybrana z suwaka w zdefiniowanym zakresie min/max |

## Wybór

| Typ | Opis |
|------|-------------|
| [select_one listname](select-one) | Wybierz dokładnie jedną opcję z listy |
| [select_multiple listname](select-multiple) | Wybierz jedną lub więcej opcji z listy |
| [rank listname](rank) | Uszereguj opcje według preferencji lub priorytetu |

## Data i godzina

| Typ | Opis |
|------|-------------|
| [date](date) | Data kalendarza (rok, miesiąc, dzień) |
| [time](time) | Godzina dnia (godziny, minuty) |
| [datetime](datetime-date-time) | Połączona data i godzina |

## Lokalizacja

| Typ | Opis |
|------|-------------|
| [geopoint](geopoint) | Pojedyncza współrzędna GPS (szerokość, długość, wysokość, dokładność) |
| [geotrace](geotrace) | Ścieżka — seria punktów GPS tworzących linię |
| [geoshape](geoshape) | Obszar — zamknięty wielokąt punktów GPS |

## Media

| Typ | Opis |
|------|-------------|
| [image](image) | Przechwytywanie zdjęcia lub przesyłanie obrazu |
| [audio](audio) | Nagranie audio |
| [video](video) | Nagranie wideo |
| [file](file) | Ogólne przesyłanie pliku (PDF, dokument itp.) |

## Inne

| Typ | Opis |
|------|-------------|
| [barcode](barcode) | Skanuj barcode lub kod QR |
| [note](note) | Tekst tylko do odczytu — wyświetla instrukcje lub obliczone podsumowania |
| [calculate](calculate) | Ukryte pole przechowujące obliczoną wartość |
| [hidden](hidden) | Ukryte pole przechowujące statyczną lub wstępnie wypełnioną wartość |
| [trigger / acknowledge](trigger) | Pole wyboru, które ankieter musi zaznaczyć, aby potwierdzić przeczytanie oświadczenia |
| [meta](meta) | Automatyczne metadane: znaczniki czasu, ID urządzenia, informacje o ankieterze |

## Rozszerzenia rtSurvey

Te typy są specyficzne dla rtSurvey i nie są częścią standardowej specyfikacji XLSForm.

| Typ | Opis |
|-----|------|
| [search-autocomplete](search-autocomplete) | Wprowadzanie tekstu z sugestiami autouzupełniania opartymi na API w czasie rzeczywistym |
| [mentions](mentions) | Pole tekstowe z autouzupełnianiem wzmianek `@` do oznaczania encji inline |
| [texttags](texttags) | Pole wprowadzania tagów — każdy wpis staje się usuwalnym chipem; przechowywany jako ciąg oddzielony spacjami |

Dla grup powtórzeń, zob. [Repeats](../advanced-extension/repeats)

## Jak typ i wygląd współpracują

`type` określa **jakie dane są zbierane**. Kolumna `appearance` kontroluje **jak wygląda widget**. Wiele typów obsługuje wiele wyglądów — na przykład `select_one` może wyglądać jak przyciski opcji, menu rozwijane, skala Likerta lub kompaktowa siatka.

Pełną listę opcji znajdziesz w [Wygląd](../appearance).
