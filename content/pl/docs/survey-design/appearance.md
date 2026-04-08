---
title: "Wygląd"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Kolumna `appearance` w rtSurvey pozwala dostosować wizualną prezentację i zachowanie pytań w ankietach. Ta funkcja poprawia doświadczenie użytkownika i może znacznie zwiększyć efektywność zbierania danych. rtSurvey obsługuje standardowe atrybuty wyglądu XLSForm i rozszerza je o dodatkowe opcje.

## Standardowe atrybuty wyglądu XLSForm

rtSurvey obsługuje następujące standardowe atrybuty wyglądu XLSForm:

| Atrybut wyglądu | Typy pytań | Opis |
|----------------------|----------------|-------------|
| multiline | text | Tworzy wieloliniowe pole tekstowe (najlepsze dla klientów webowych) |
| minimal | select_one, select_multiple | Wyświetla opcje w menu rozwijanym |
| quick | select_one | Automatycznie przechodzi do następnego pytania po wyborze (tylko mobile) |
| no-calendar | date | Ukrywa wyświetlanie kalendarza (tylko mobile) |
| month-year | date | Umożliwia wybór tylko miesiąca i roku |
| year | date | Umożliwia wybór tylko roku |
| horizontal-compact | select_one, select_multiple | Wyświetla opcje poziomo (tylko web) |
| horizontal | select_one, select_multiple | Wyświetla opcje poziomo w kolumnach (tylko web) |
| likert | select_one | Prezentuje opcje jako skalę Likerta |
| compact | select_one, select_multiple | Wyświetla opcje obok siebie z minimalnym odstępem |
| quickcompact | select_one | Łączy kompaktowy wyświetlacz z automatycznym przejściem (tylko mobile) |
| field-list | groups | Wyświetla całą grupę na jednym ekranie (tylko mobile) |
| label | select_one, select_multiple | Pokazuje etykiety opcji bez danych wejściowych |
| list-nolabel | select_one, select_multiple | Pokazuje dane wejściowe bez etykiet (użyj z `label`) |
| table-list | groups | Wyświetla pytania w formacie tabeli |
| signature | image | Umożliwia przechwytywanie podpisu (tylko mobile) |
| draw | image | Umożliwia rysowanie odręczne (tylko mobile) |
| map, quick map | select_one, select_one_from_file | Umożliwia wybór z elementów mapy |

## Najlepsze praktyki używania wyglądu

1. **Spójność**: Używaj atrybutów wyglądu spójnie w całej ankiecie dla jednolitego wyglądu.
2. **Mobile vs. Web**: Rozważ, jak wyglądy będą renderowane na różnych urządzeniach i platformach.
3. **Wydajność**: Zachowaj ostrożność z atrybutami wyglądu, które mogą spowalniać ładowanie formularza (np. `table-list` dla dużych grup).
4. **Doświadczenie użytkownika**: Wybierz wyglądy, które ułatwiają wprowadzanie danych i są intuicyjne dla respondentów.
5. **Testowanie**: Zawsze testuj formularz na docelowych urządzeniach, aby upewnić się, że wyglądy działają zgodnie z oczekiwaniami.

## Zaawansowane techniki

### Łączenie wyglądu

Niektóre atrybuty wyglądu można łączyć dla bardziej złożonych układów:

```
| type | name | label | appearance |
|------|------|-------|------------|
| select_one options | choice | Wybierz jeden: | minimal compact |
```

### Dynamiczny wygląd

rtSurvey umożliwia dynamiczne zmiany wyglądu na podstawie logiki formularza:

```
| type | name | label | appearance | relevant |
|------|------|-------|------------|----------|
| text | time | Wprowadź czas: | inline-[%H:%M] | ${show_time} = 'yes' |
```

## Uwagi dotyczące aplikacji mobilnej

- Niektóre wyglądy (np. `quick`, `signature`) są specyficzne dla urządzeń mobilnych.
- Testuj dokładnie zarówno na Android, jak i iOS, aby zapewnić spójne działanie.

## Rozszerzone atrybuty wyglądu rtSurvey

Oprócz standardowych wyglądów XLSForm, rtSurvey obsługuje następujące opcje specyficzne dla platformy:

### Układ

| Atrybut wyglądu | Typy pytań | Opis |
|-----------------|------------|------|
| `1screen` | group | Wymusza wyświetlenie całej grupy na jednym ekranie niezależnie od jej rozmiaru. |
| `columns(n)` | select_one, select_multiple | Wyświetla opcje w `n` kolumnach. Przykład: `columns(3)` pokazuje trzy kolumny przycisków radiowych. |
| `gridformat<row=R col=C colspan=S align=center>` | dowolny | Umieszcza pole w układzie CSS-grid w wierszu `R`, kolumnie `C`, obejmując `S` kolumn. |
| `ignore-simplify` | dowolny | Instruuje renderer formularza, aby pominął automatyczne upraszczanie układu tego pola. |
| `required-but-simplify` | dowolny | Pole jest wymagane, ale jego układ jest nadal upraszczany przez renderer. |
| `embed` | dowolny | Renderuje pole w trybie wbudowanym/inline, pomijając zewnętrzne opakowanie i kontener etykiety. |
| `popup` | select_one, select_multiple | Renderuje listę opcji w nakładce popup/modal zamiast inline. |
| `auto-hide-empty` | boxtag, select | Ukrywa cały widget pytania, gdy lista opcji jest pusta (np. brak wyników API). |
| `text-nolabel` | select_one, select_multiple | Ukrywa etykietę tekstową każdej opcji, pokazując tylko element sterowania wejściem. |

### Wizualne widgety wyboru

Te wyglądy zmieniają całe renderowanie list opcji select.

| Atrybut wyglądu | Typy pytań | Opis |
|-----------------|------------|------|
| `tagging` | select_one, select_multiple | Opcje renderowane jako klikalne chipsy tagów w kształcie pigułki. |
| `boxtag` | select_one, select_multiple | Opcje renderowane jako prostokątne stylowe pola, które użytkownik dotyka. |
| `boxtag -search` | select_one, select_multiple | Układ boxtag z live polem wyszukiwania/filtrowania nad polami. |
| `duolingo-style1` | select_one, select_multiple | Duży układ kart inspirowany Duolingo — odpowiedni dla krótkich list z ikonami. |
| `rating_box` | select_one, select_multiple | Siatka klikaliwych ponumerowanych pól — odpowiednia dla pytań skali lub NPS. |
| `star_rating` | select_one | Opcje renderowane jako gwiazdki; liczba gwiazdek równa liczbie opcji. |
| `choices-noshow` | select_one, select_multiple | Początkowo pokazuje tylko pierwsze 10 opcji z kontrolką "Pokaż więcej". |
| `noshow` | select_one, select_multiple | Całkowicie ukrywa listę opcji; wartość jest ustawiana programowo przez `calculate` lub API. |
| `checkall` | select_multiple | Dodaje skrót "Zaznacz wszystkie" na górze listy opcji. |
| `max-items(N)` | select_one, select_multiple | Ogranicza widoczną listę opcji do N elementów. Przykład: `max-items(5)`. |

### Wizualne widgety tekstu

| Atrybut wyglądu | Typy pytań | Opis |
|-----------------|------------|------|
| `richtext` | text | Zastępuje zwykłe pole tekstowe edytorem tekstu sformatowanego (pogrubienie, kursywa, listy, linki). Przechowuje HTML. |
| `typingtest` | text | Widget testu pisania — tekst etykiety jest fragmentem; widget rejestruje wpisaną odpowiedź i czas. |

### Rozszerzenia mediów

| Atrybut wyglądu | Typy pytań | Opis |
|-----------------|------------|------|
| `watermark("wyrażenie")` | image | Nakłada tekstowy znak wodny na zrobione zdjęcia. Argument jest wyrażeniem XPath ocenianym w momencie fotografowania. Przykład: `watermark("${id} ${today()}")`. |
| `editable` | image | Umożliwia adnotację/rysowanie na wykonanym zdjęciu przed zapisaniem. |

### Konfiguracja wyświetlania inline

Modyfikatory `display{}` i `results{}` można dołączyć do wyglądów `inline` w celu sterowania wyrównaniem ikon i wyświetlaniem wyników. Są używane razem z rozszerzeniem wprowadzania czasu `inline` na polach `text` i z widgetami przechwytywania multimediów.

#### Parametry `display{}`

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| Parametr | Wartości | Opis |
|----------|---------|------|
| Wyrównanie | `left`, `right`, `top`, `bottom`, `center` | Pozycja ikony względem pola wejściowego |
| Rozmiar | `small`, `medium`, `large` | Rozmiar ikony (odpowiada 2,5 rem, 5 rem, 8 rem) |
| Tryb | `inline-icon` | Renderuje wyzwalacz jako samą ikonę (bez obramowania przycisku) |
| Tryb | `inline-button` | Renderuje wyzwalacz jako pełny przycisk |

#### Parametry `results{}`

```
inline results{right}
inline results{left,hide(seconds)}
```

| Parametr | Wartości | Opis |
|----------|---------|------|
| Wyrównanie | `left`, `right`, `top`, `bottom`, `center` | Pozycja wyświetlania wartości wyniku |
| `hide(pole)` | dowolna nazwa podpola | Ukrywa określony składnik wyniku (np. `hide(seconds)`) |

### Integracja API

| Atrybut wyglądu | Typy pytań | Opis |
|-----------------|------------|------|
| `callapi` | text, integer, decimal, select_one | Włącza integrację wywołania API dla tego pola. Kolumna calculation powinna zawierać wyrażenie `callapi()`. Zobacz [Call API](advanced-extension/call-api). |
| `callapi-verify(params)` | text, integer, decimal | Wyzwala wywołanie weryfikacji API przy użyciu statycznych parametrów. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Jak `callapi-verify`, ale z parametrami pochodzi z innych wartości pól w czasie wykonania. |

## Znane ograniczenia

- Złożone wyglądy mogą nie renderować się identycznie na wszystkich platformach.
- Niektóre zaawansowane wyglądy rtSurvey mogą nie być obsługiwane w trybie offline.

## Rozwiązywanie problemów z wyglądem

1. **Wygląd nie jest stosowany**: Sprawdź literówki w kolumnie wyglądu.
2. **Niespójne renderowanie**: Zweryfikuj kompatybilność z typem pytania i platformą.
3. **Problemy z wydajnością**: Rozważ uproszczenie złożonych wyglądów, szczególnie dla dużych ankiet.
