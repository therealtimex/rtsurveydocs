---
title: "Powtarzające się pytania"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 260
---

Powtórzenia to potężna funkcja rtSurvey, która pozwala zbierać ten sam zestaw informacji wielokrotnie w ramach jednej ankiety. Jest to szczególnie przydatne w scenariuszach takich jak ankiety gospodarstw domowych, gdzie może być konieczne zbieranie danych o wielu członkach gospodarstwa.

## Podstawowa struktura powtórzenia

Aby utworzyć powtórzenie w rtSurvey, użyj konstrukcji `begin repeat` i `end repeat`:

```
| type         | name         | label                 |
|--------------|--------------|----------------------|
| begin repeat | child_repeat |                       |
| text         | name         | Imię dziecka          |
| decimal      | birthweight  | Waga urodzeniowa dziecka |
| select_one male_female | sex | Płeć dziecka         |
| end repeat   |              |                       |
```

W tym przykładzie użytkownik może zbierać informacje o wielu dzieciach, dodając nowe powtórzenia w formularzu.

## Etykietowanie powtórzeń

Chociaż kolumna `label` jest opcjonalna dla `begin repeat`, dodanie etykiety może poprawić nawigację:

```
| type         | name         | label                     |
|--------------|--------------|--------------------------|
| begin repeat | child_repeat | Informacje o dziecku      |
| text         | name         | Imię dziecka              |
| decimal      | birthweight  | Waga urodzeniowa dziecka  |
| select_one male_female | sex | Płeć dziecka            |
| end repeat   |              |                           |
```

## Stała liczba powtórzeń

Aby określić stałą liczbę powtórzeń, użyj kolumny `repeat_count`:

```
| type         | name         | label                     | repeat_count |
|--------------|--------------|--------------------------|--------------|
| begin repeat | child_repeat | Informacje o dziecku      | 3            |
| text         | name         | Imię dziecka              |              |
| decimal      | birthweight  | Waga urodzeniowa dziecka  |              |
| end repeat   |              |                           |              |
```

Spowoduje to utworzenie dokładnie 3 powtórzeń dla dzieci.

## Dynamiczna liczba powtórzeń

rtSurvey obsługuje dynamiczne liczby powtórzeń oparte na poprzednich odpowiedziach:

```
| type     | name             | label                              | repeat_count        |
|----------|------------------|------------------------------------|---------------------|
| integer  | num_hh_members   | Liczba członków gospodarstwa?      |                     |
| begin repeat | hh_member    | Członek gospodarstwa               | ${num_hh_members}   |
| text     | name             | Imię                               |                     |
| integer  | age              | Wiek                               |                     |
| end repeat |                |                                    |                     |
```

## Najlepsze praktyki używania powtórzeń w rtSurvey

1. Używaj znaczących nazw i etykiet dla powtórzeń, aby poprawić analizę danych.
2. Rozważ używanie dynamicznych liczb powtórzeń, aby zmniejszyć błędy wprowadzania danych.
3. Dokładnie testuj formularz, szczególnie przy używaniu złożonych zagnieżdżonych powtórzeń.
4. Używaj funkcji podsumowania, aby pomóc ankieterom w nawigacji po długich listach powtórzeń.
5. Zachowaj ostrożność z dużą liczbą powtórzeń, ponieważ mogą wpływać na wydajność formularza.
