---
title: "Kluczowe pojęcia"
description: "Przegląd projektowania formularzy"
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 210
---

## Czym jest XLSForm?
rtSurvey używa rozszerzonej wersji standardu [XLSForm](https://xlsform.org/) do projektowania formularzy, oferując zaawansowane funkcje do tworzenia wyrafinowanych ankiet. Ten przewodnik przedstawia kluczowe pojęcia projektowania formularzy w rtSurvey, od podstawowej struktury XLSForm do zaawansowanych funkcji specyficznych dla rtSurvey.

Dzięki XLSFormom możesz tworzyć formularze w czytelnym dla człowieka formacie przy użyciu znajomego narzędzia Excel, co czyni je dostępnymi dla prawie każdego. Ten standard umożliwia łatwe udostępnianie i współpracę przy tworzeniu formularzy.

Choć XLSFormy są przyjazne dla początkujących, pozwalają również doświadczonym użytkownikom tworzyć złożone formularze.

rtSurvey zapewnia spójny sposób włączania zaawansowanych funkcji takich jak logika pomijania do formularzy na różnych platformach internetowych i mobilnych zbierania danych.

## Struktura XLSForm
XLSForm zazwyczaj składa się z dwóch głównych arkuszy:

1. **survey**: Definiuje strukturę i zawartość formularza.
2. **choices**: Określa opcje odpowiedzi dla pytań wielokrotnego wyboru.

Opcjonalny arkusz **settings** może zawierać dodatkowe specyfikacje formularza.

Należy zauważyć, że obowiązkowe kolumny w arkuszach survey i choices muszą być obecne, aby formularz działał poprawnie. Opcjonalne kolumny w obu arkuszach zapewniają dalszą kontrolę nad zachowaniem każdego wpisu w formularzu, ale nie są niezbędne.

Kolumny w skoroszycie Excel mogą pojawiać się w dowolnej kolejności, a opcjonalne kolumny można pozostawić puste. Jednak kluczowe jest używanie precyzyjnej składni i konwencji nazewnictwa określonych w dokumentacji XLSForm, aby formularz działał poprawnie.

### Arkusz survey
Arkusz **survey** to miejsce, gdzie definiujesz strukturę formularza i dostarczasz treść. Każdy wiersz w arkuszu survey reprezentuje pytanie lub element formularza. Następujące kolumny są obowiązkowe w arkuszu survey:

- `type`: Określa typ wpisu oczekiwanego dla pytania.
- `name`: Określa unikalną nazwę zmiennej dla tego wpisu. Nazwy muszą zaczynać się literą lub podkreśleniem i mogą zawierać tylko litery, cyfry, łączniki, podkreślenia i kropki. Nazwy rozróżniają wielkość liter.
- `label`: Zawiera rzeczywisty tekst pytania wyświetlany w formularzu.

| type                | name     | label                |
| ------------------- | -------- | -------------------- |
| today               | today    |                      |
| select_one gender   | gender   | Płeć respondenta?    |
| integer             | age      | Wiek respondenta?    |

### Arkusz choices
Arkusz **`choices`** służy do określania opcji odpowiedzi dla pytań wielokrotnego wyboru. Każdy wiersz reprezentuje opcję odpowiedzi. Następujące kolumny są obowiązkowe w arkuszu choices:

- **`list_name`**: Grupuje zestaw powiązanych opcji odpowiedzi.
- **`name`**: Określa unikalną nazwę zmiennej dla tej opcji odpowiedzi.
- **`label`**: Pokazuje opcję odpowiedzi dokładnie tak, jak ma się pojawiać w formularzu.

| list_name           | name        | label                |
| ------------------- | ----------- | -------------------- |
| gender              | transgender | Transgender          |
| gender              | female      | Kobieta              |
| gender              | male        | Mężczyzna            |
| gender              | other       | Inne                 |

Kolumny dodawane do skoroszytu Excel, niezależnie od tego czy są obowiązkowe czy opcjonalne, mogą pojawiać się w dowolnej kolejności. Kolumny opcjonalne mogą być całkowicie pominięte. Wiersze lub kolumny mogą być puste w celu poprawy czytelności, ale dane po 20 sąsiednich pustych kolumnach lub wierszach w arkuszu nie będą przetwarzane. Całe formatowanie pliku .xlsx jest ignorowane, więc możesz używać linii podziału, cieniowania i innych formatowań czcionek, aby formularz był bardziej czytelny.

Jedną rzeczą do zapamiętania podczas tworzenia formularzy w Excel jest to, że używana składnia musi być precyzyjna. Na przykład, jeśli napiszesz **Choices** lub **choice** zamiast **choices**, formularz nie będzie działał.

### Arkusz settings

Arkusz settings jest opcjonalny, ale pozwala na określenie metadanych i zachowania na poziomie formularza. Typowe kolumny w arkuszu settings obejmują:

| Kolumna | Opis |
|--------|-------------|
| form_title | Tytuł formularza wyświetlany użytkownikom |
| form_id | Unikalny identyfikator formularza, używany w zarządzaniu danymi i wywołaniach API |
| default_language | Domyślny kod języka dla formularzy wielojęzycznych (np. 'pl' dla polskiego) |
| version | Numer wersji formularza, przydatny do śledzenia zmian |
| instance_name | Wyrażenie do generowania unikalnej nazwy dla każdego przesłania formularza |
| generation | Liczba całkowita oznaczająca generację formularza. Zwiększ dla zmian strukturalnych |
| family | Identyfikator do grupowania powiązanych formularzy w różnych zmianach strukturalnych |

Arkusz settings w rtSurvey może również zawierać dodatkowe konfiguracje specyficzne dla rozszerzonych funkcji rtSurvey. Zapoznaj się z dokumentacją rtSurvey, aby uzyskać pełną listę obsługiwanych ustawień.

## Kluczowe komponenty arkusza survey

Arkusz survey jest rdzeniem projektowania formularza. Oto przegląd jego kluczowych komponentów:

| Komponent | Opis |
|-----------|-------------|
| [type](#question-types) | Określa typ pytania (np. text, integer, select_one) |
| [name](#naming-conventions) | Unikalny identyfikator pytania |
| [label](#labels-and-translations) | Tekst wyświetlany respondentowi |
| [hint](#hints-and-help-text) | Dodatkowe wskazówki dla respondenta |
| [appearance](#appearance-options) | Modyfikuje sposób wyświetlania pytania |
| [relevant](#relevance-and-skip-logic) | Określa, kiedy pytanie ma być zadawane (logika pomijania) |
| [constraint](#constraints-and-validation) | Weryfikuje odpowiedź |
| [calculation](#calculations) | Oblicza wartości na podstawie innych odpowiedzi |
| [required](#required-fields) | Określa, czy pytanie musi być odpowiedzone |

Każdy z tych komponentów odgrywa kluczową rolę w tworzeniu efektywnych i wydajnych ankiet.

### Typy pytań
XLSForm obsługuje wiele typów pytań. Oto niektóre opcje, które możesz wprowadzić w kolumnie **`type`** w arkuszu **`survey`** XLSForm:

| Typ pytania               | Dane wejściowe                                                                                |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| integer                   | Dane wejściowe całkowite (tj. liczba całkowita).                                              |
| decimal                   | Dane wejściowe dziesiętne.                                                                    |
| range                     | Dane wejściowe zakresu (w tym oceny)                                                          |
| text                      | Odpowiedź w formie tekstu wolnego.                                                            |
| select_one [options]      | Pytanie wielokrotnego wyboru; można wybrać tylko jedną odpowiedź.                             |
| select_multiple [options] | Pytanie wielokrotnego wyboru; można wybrać wiele odpowiedzi.                                  |
| select_one_from_file [file]| Wielokrotny wybór z pliku; można wybrać tylko jedną odpowiedź.                              |
| select_multiple_from_file [file]| Wielokrotny wybór z pliku; można wybrać wiele odpowiedzi.                              |
| rank [options]            | Pytanie rankingowe; uszereguj listę.                                                          |
| note                      | Wyświetla notatkę na ekranie, nie przyjmuje danych wejściowych.                              |
| geopoint                  | Zbierz pojedynczą współrzędną GPS.                                                            |
| geotrace                  | Zapisz linię złożoną z dwóch lub więcej współrzędnych GPS.                                   |
| geoshape                  | Zapisz wielokąt z wielu współrzędnych GPS; ostatni punkt jest taki sam jak pierwszy.         |
| date                      | Dane wejściowe daty.                                                                          |
| time                      | Dane wejściowe czasu.                                                                         |
| dateTime                  | Przyjmuje datę i czas jako dane wejściowe.                                                    |
| image                     | Zrób zdjęcie lub prześlij plik obrazu.                                                        |
| audio                     | Nagraj dźwięk lub prześlij plik audio.                                                        |
| background-audio          | Dźwięk jest nagrywany w tle podczas wypełniania formularza.                                   |
| video                     | Nagraj wideo lub prześlij plik wideo.                                                         |
| file                      | Ogólne dane wejściowe pliku (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                       |
| barcode                   | Skanuj barcode, wymaga zainstalowanej aplikacji skanera barcode.                              |
| calculate                 | Wykonaj obliczenie; zob. sekcję Obliczenia poniżej.                                          |
| acknowledge               | Monit potwierdzenia ustawiający wartość na "OK" po wybraniu.                                  |
| hidden                    | Pole bez powiązanego elementu UI, które może być używane do przechowywania stałej            |
| xml-external              | Dodaje odniesienie do zewnętrznego pliku danych XML                                           |

### Etykiety

Etykiety to tekst wyświetlany respondentom dla każdego pytania. Są kluczowe dla jasnej komunikacji w ankietach.

- **Podstawowe użycie**: W kolumnie `label` wprowadź tekst pytania.
- **Wiele języków**: Użyj dodatkowych kolumn takich jak `label::Polish` i `label::English` dla ankiet wielojęzycznych.
- **Formatowanie**: rtSurvey obsługuje podstawowe formatowanie HTML w etykietach dla podkreślenia lub struktury.

Przykład:
```
| type | name | label | label::Polish |
|------|------|-------|---------------|
| text | name | What is your name? | Jak masz na imię? |
```

### Wskazówki

Wskazówki dostarczają respondentom dodatkowych wskazówek bez zaśmiecania tekstu głównego pytania.

- **Użycie**: Dodaj wskazówki w kolumnie `hint`.
- **Widoczność**: Wskazówki są zazwyczaj wyświetlane poniżej tekstu głównego pytania.
- **Wielojęzyczne**: Podobnie jak etykiety, wskazówki mogą być określone dla wielu języków używając kolumn `hint::Język`.

Przykład:
```
| type | name | label | hint |
|------|------|-------|------|
| integer | age | Ile masz lat? | Proszę podać wiek w latach |
```

### Wygląd

Kolumna `appearance` w rtSurvey umożliwia dostosowanie sposobu wyświetlania pytań.

- **Standardowe opcje**: Obejmują 'multiline' dla tekstu, 'horizontal' dla pytań wyboru.
- **Rozszerzenia rtSurvey**:
  - Dane wejściowe czasu: Różne opcje wyświetlania zegara (np. `inline`, `inline-1line`)
  - Dostosowanie kolorów: Użyj funkcji `colors()`, aby zmienić kolory ikon

Przykład:
```
| type | name | label | appearance |
|------|------|-------|------------|
| text | time | Wprowadź czas | inline-[%H:%M] |
```

### Relevant

Kolumna `relevant` implementuje logikę pomijania, określając kiedy pytanie ma być wyświetlane.

- **Składnia**: Użyj wyrażeń XPath do definiowania warunków.
- **Zmienne**: Odwołuj się do innych nazw pytań używając `${nazwa_pytania}`.

Przykład:
```
| type | name | label | relevant |
|------|------|-------|----------|
| text | allergies | Wymień alergie | ${ma_alergie} = 'tak' |
```

### Wymagane

Kolumna `required` określa, czy pytanie musi być odpowiedzone.

- **Podstawowe użycie**: Użyj 'yes' lub 'true', aby pytanie było wymagane.
- **Zaawansowane**: Można używać wyrażeń dla warunkowego wymagania.

Przykład:
```
| type | name | label | required |
|------|------|-------|----------|
| text | email | Adres email | yes |
```

### Powtórzenia

Powtórzenia pozwalają na wielokrotne odpowiadanie na grupę pytań.

- **Użycie**: Użyj wierszy `begin repeat` i `end repeat`, aby zdefiniować grupę powtarzającą.
- **Nazewnictwo**: Nadaj każdej grupie powtórzeń unikalną nazwę.

Przykład:
```
| type | name | label |
|------|------|-------|
| begin repeat | household_member | Członek gospodarstwa domowego |
| text | member_name | Imię |
| integer | member_age | Wiek |
| end repeat | | |
```

### Media

rtSurvey obsługuje różne typy mediów w ankietach, w tym obrazy, audio i wideo.

- **Typy pytań**: Użyj 'image', 'audio' lub 'video' w kolumnie type.
- **Media w etykietach**: Odwołuj się do plików multimedialnych w etykietach używając tagów HTML.

Przykład:
```
| type | name | label |
|------|------|-------|
| image | house_photo | Zrób zdjęcie domu |
| note | | <img src="logo.jpg" /> Witamy w ankiecie |
```

### Tylko do odczytu

Pytania tylko do odczytu wyświetlają informacje bez umożliwienia wprowadzania danych przez użytkownika.

- **Użycie**: Dodaj 'readonly' do kolumny `appearance`.
- **Obliczenia**: Często używane z typem calculate do wyświetlania obliczonych wartości.

Przykład:
```
| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | bmi | BMI | readonly | ${weight} / (${height} * ${height}) |
```

## Rozszerzenia rtSurvey

rtSurvey rozszerza standard XLSForm o obsługę dodatkowych możliwości takich jak `grid layout`, `html format` i wiele nowych `widgetów`.

### Układ siatki
rtSurvey pozwala formularzu naśladować wygląd tradycyjnych ankiet papierowych przez kompaktowanie wielu pytań w jeden wiersz.

### Ustawienia formularza

### Ustawienia danych

### Styl Typeform

### Rozszerzenie pulldata()

### Rozszerzenia oparte na wyglądzie

### Rozszerzenia Webbox
