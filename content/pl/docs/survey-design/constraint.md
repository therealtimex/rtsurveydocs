---
title: "Walidacja odpowiedzi"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 270
---

Jednym ze sposobów zapewnienia jakości danych jest dodanie ograniczeń do pól danych w formularzu. Ograniczenia pomagają zapobiegać wprowadzaniu przez użytkowników nieprawidłowych lub niemożliwych odpowiedzi. Na przykład przy pytaniu o dochód osoby chcesz unikać nierealistycznych wartości, takich jak liczby ujemne lub bardzo wysokie wartości. Dodawanie ograniczeń danych do formularza jest łatwe. Po prostu wykonaj poniższe kroki:

1. Dodaj nową kolumnę o nazwie „constraint" do formularza.
2. W kolumnie „constraint" wprowadź formułę określającą limity odpowiedzi.

### Przykład

Rozważmy przykład, w którym chcemy dodać ograniczenie dla dochodu osoby. Ograniczenie wymaga, aby dochód wynosił od 0 do 1 000 000 zł. Oto jak możesz skonfigurować ograniczenie:

{{< table >}}
| `name`      | `constraint`                  |
|---------------|-----------------------------|
| Income        | . >= 0 & . <= 1000000      |
{{< /table >}}

W powyższym przykładzie „." w formule odnosi się z powrotem do zmiennej pytania, która reprezentuje wartość wprowadzoną przez użytkownika dla pytania „Income". Ograniczenie „. >= 0 && . <= 1000000" zapewnia, że wprowadzony dochód jest większy lub równy 0 i mniejszy lub równy 1 000 000.

### Twarde ograniczenie

**Twarde ograniczenie** całkowicie blokuje przesłanie formularza, jeśli wprowadzona wartość nie spełnia wyrażenia. Ankieter nie może kontynuować, dopóki nie wprowadzi prawidłowej wartości.

Aby dodać twarde ograniczenie, wprowadź wyrażenie w kolumnie `constraint`. Opcjonalnie dodaj czytelny komunikat w `constraint_message`:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | age | Wiek respondenta | `. > 0 and . <= 120` | Wiek musi wynosić od 1 do 120 lat |
| decimal | temperature | Temperatura ciała (°C) | `. >= 35 and . <= 42` | Temperatura musi wynosić od 35°C do 42°C |
| text | phone | Numer telefonu | `regex(., '^[0-9]{10}$')` | Wprowadź 10-cyfrowy numer telefonu |
{{< /table >}}

#### Wiele warunków

Łącz warunki używając `and` / `or`:

```
. >= 0 and . <= 100
```

```
. = 'yes' or . = 'no'
```

#### Używanie `regex()` do walidacji wzorców

Funkcja `regex(value, pattern)` testuje wartość względem wyrażenia regularnego:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| text | email | Adres email | `regex(., '^[^@]+@[^@]+\.[^@]+$')` | Wprowadź prawidłowy adres email |
| text | zip_code | Kod pocztowy | `regex(., '^[0-9]{2}-[0-9]{3}$')` | Wprowadź prawidłowy kod pocztowy |
{{< /table >}}

#### Odwoływanie się do innych pól w ograniczeniu

Użyj `${nazwa_pola}`, aby odwołać się do wartości z innych pytań:

{{< table >}}
| `type` | `name` | `label` | `constraint` | `constraint_message` |
|--------|--------|---------|--------------|----------------------|
| integer | end_year | Rok zakończenia | `. >= ${start_year}` | Rok zakończenia musi być po roku rozpoczęcia |
| decimal | loan_repaid | Spłacona kwota | `. <= ${loan_amount}` | Nie można spłacić więcej niż kwota pożyczki |
{{< /table >}}

### Miękkie ostrzeżenie

**Miękkie ostrzeżenie** (zwane też miękkim ograniczeniem lub ostrzeżeniem) ostrzega ankietera, że wartość wygląda na niezwykłą, ale nadal pozwala na kontynuację. Jest to przydatne, gdy wartość jest technicznie prawidłowa, ale statystycznie mało prawdopodobna.

rtSurvey obsługuje miękkie ostrzeżenia za pomocą kolumny `constraint` ze specjalnym podejściem `constraint_type` lub przez wygląd `soft` połączony z polem notatki.

Najczęstszym wzorcem jest użycie **notatki** z wyrażeniem `relevant` flagującym podejrzaną wartość, sparowaną z pytaniem **acknowledge** do potwierdzenia:

{{< table >}}
| `type` | `name` | `label` | `relevant` |
|--------|--------|---------|------------|
| integer | children | Liczba dzieci | |
| note | children_warning | Ostrzeżenie: Podałeś ${children} dzieci. Proszę potwierdzić, że jest to prawidłowe. | `. > 15` |
| trigger | children_confirm | Potwierdź, że liczba dzieci jest prawidłowa | `${children} > 15` |
{{< /table >}}

{{% alert icon=" " context="warning" %}}
Rozróżnienie między twardymi a miękkimi ograniczeniami ma znaczenie dla jakości danych. Używaj **twardych ograniczeń** dla logicznie niemożliwych wartości (ujemne wieki, temperatury powyżej 100°C). Używaj **miękkich ostrzeżeń** dla statystycznie mało prawdopodobnych, ale nie niemożliwych wartości — nie chcesz blokować uzasadnionych przypadków brzegowych.
{{% /alert %}}
