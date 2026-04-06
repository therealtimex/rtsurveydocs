---
title: "Tylko do odczytu"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 287
---

Pola tylko do odczytu w rtSurvey pozwalają wyświetlać informacje, których respondent nie może edytować. Ta funkcja jest szczególnie przydatna do wyświetlania wstępnie wypełnionych danych, obliczonych wyników lub informacji, które powinny pozostać stałe przez całą ankietę.

## Podstawowe użycie

Aby uczynić pole tylko do odczytu, użyj kolumny `read_only` w XLSForm:

```
| type    | name | label                    | read_only | default |
|---------|------|--------------------------|-----------|---------|
| integer | num  | Numer pacjenta to:        | yes       | 5       |
```

W tym przykładzie numer pacjenta jest ustawiony na 5 i nie może być zmieniony przez respondenta.

## Łączenie tylko do odczytu z wartościami domyślnymi

Pola tylko do odczytu są często używane w połączeniu z wartościami domyślnymi do wyświetlania z góry określonych lub obliczonych informacji:

```
| type    | name     | label                   | read_only | default         |
|---------|----------|-------------------------|-----------|-----------------|
| text    | username | Zalogowany użytkownik:  | yes       | ${current_user} |
| date    | today    | Dzisiejsza data:        | yes       | today()         |
```

Tutaj nazwa użytkownika i bieżąca data są wyświetlane, ale nie można ich edytować.

## Funkcje specyficzne dla rtSurvey

### Warunkowe tylko do odczytu

rtSurvey rozszerza funkcjonalność tylko do odczytu o logikę warunkową:

```
| type    | name     | label    | read_only                        |
|---------|----------|----------|----------------------------------|
| integer | age      | Wiek:    | ${role} = 'viewer'               |
| text    | comments | Komentarze: | selected(${status}, 'closed') |
```

W tych przykładach:
- Pole 'age' jest tylko do odczytu tylko jeśli rola użytkownika to 'viewer'.
- Pole 'comments' staje się tylko do odczytu jeśli status to 'closed'.

## Najlepsze praktyki używania pól tylko do odczytu

1. **Jasność**: Wyraźnie wskazuj, które pola są tylko do odczytu przez wskazówki wizualne lub etykiety.
2. **Spójność**: Używaj pól tylko do odczytu spójnie w całej ankiecie.
3. **Walidacja**: Mimo że pól tylko do odczytu nie można edytować, uwzględnij je w procesie walidacji danych.
4. **Wydajność**: Zachowaj ostrożność ze złożonymi obliczeniami w polach tylko do odczytu, ponieważ mogą wpływać na czas ładowania formularza.

## Zaawansowane techniki

### Obliczane pola tylko do odczytu

Użyj pól tylko do odczytu do wyświetlania obliczeń opartych na innych odpowiedziach:

```
| type      | name | label | read_only | calculation                         |
|-----------|------|-------|-----------|-------------------------------------|
| calculate | bmi  | BMI:  | yes       | ${weight} / (${height} * ${height}) |
```
