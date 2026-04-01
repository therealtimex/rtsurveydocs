---
title: "App API"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 300
---

AppAPI umożliwia użytkownikom ładowanie metadanych systemowych z aplikacji przy użyciu różnych metod w FormEngine i DMView. Zapewnia dostęp do różnych kluczy danych do pobierania konkretnych informacji z aplikacji.

W xlsform możesz użyć funkcji `pulldata()` z następującą składnią:

{{< alert context="light" text="pulldata('app-api', 'data-key')" />}}

- `'app-api'`: To słowo kluczowe informuje FormEngine o ładowaniu danych z App API.
- `'data-key'`: To klucz danych, które chcesz załadować z App API.
- Jeśli klucz danych jest nieprawidłowy lub nieobsługiwany, obliczenie zwróci "n/a".

Oto obsługiwane klucze danych, których możesz używać z App-API:

`osPlatform`: Zwraca bieżącą nazwę systemu operacyjnego (Android lub iOS) i wersję systemu operacyjnego. Platformy webowe zwrócą pustą wartość.

`appPlatform`: Zwraca nazwę platformy aplikacji, którą jest `rtSurvey`.

`appVersion`: Zwraca nazwę wersji aplikacji.

`getDisplayWidth`: Zwraca szerokość ekranu urządzenia w pikselach.

`getDisplayHeight`: Zwraca wysokość ekranu urządzenia w pikselach.

`getScreenSize`: Zwraca rozmiar ekranu urządzenia w calach.

`projectCode`: Zwraca bieżący kod projektu witryny, do której użytkownik się loguje.

`projectURL`: Zwraca bieżący URL projektu witryny, do której użytkownik się loguje. Domyślna/awaryjna wartość to pusty tekst ("").

`startingPoint`: Zwraca ścieżkę punktu, który uruchamia formularz.

`serverTime`: Zwraca najlepsze dostępne przybliżenie daty i godziny na serwerze.

`user.[attribute]`: Zwraca bieżące atrybuty użytkownika na podstawie określonego klucza atrybutu. Połącz poniższe klucze atrybutów z "user." w parametrach `pulldata()`, aby pobrać informacje o bieżącym użytkowniku. Na przykład użyj `user.username`, `user.email` itd.

| Klucz atrybutu       | Opis                                         |
|----------------------|----------------------------------------------|
| username             | Nazwa użytkownika                             |
| name                 | Pełne imię i nazwisko użytkownika            |
| staffCode            | Kod personelu użytkownika                     |
| phone                | Numer telefonu użytkownika                    |
| email                | Adres email użytkownika                       |
| description          | Tekst opisu w informacjach o użytkowniku      |
| organization_id      | ID organizacji, do której należy użytkownik   |
| organization_name    | Nazwa organizacji, do której należy użytkownik|
| team_id              | ID zespołu, do którego należy użytkownik      |
| supervisor_id        | ID przełożonego użytkownika                   |
| is_supervisor        | 1 jeśli użytkownik jest przełożonym, 0 jeśli nie|

`instancePath`: Zwraca bieżącą ścieżkę folderu instancji.

`appLanguage`: Zwraca bieżący język aplikacji ustawiony w ustawieniach aplikacji (np. pl, en).

`openArgs.[attribute]`: Zwraca argument otwierania formularza przekazany z ActionButton. Domyślna/awaryjna wartość to pusty tekst ("").

`primaryAppColor`: Pobiera podstawowy kolor aplikacji.

---

## Przykłady użycia

### Przechowuj nazwę użytkownika i organizację ankietera

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | enumerator_name | | `pulldata('app-api', 'user.name')` |
| calculate | enumerator_org | | `pulldata('app-api', 'user.organization_name')` |
| calculate | enumerator_email | | `pulldata('app-api', 'user.email')` |

Użyj ich w etykietach notatek do celów audytu:
```
note | interviewer_info | Ankieter: ${enumerator_name} (${enumerator_org})
```

### Informacje o urządzeniu i ekranie

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | device_platform | | `pulldata('app-api', 'osPlatform')` |
| calculate | app_ver | | `pulldata('app-api', 'appVersion')` |
| calculate | screen_w | | `pulldata('app-api', 'getDisplayWidth')` |

### Czas serwera zamiast czasu urządzenia

Zegary urządzeń mogą być nieprawidłowe. Użyj `serverTime` dla bardziej wiarygodnego znacznika czasu:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | server_ts | | `pulldata('app-api', 'serverTime')` |

### Logika warunkowa oparta na roli użytkownika

Pokaż sekcję tylko dla przełożonych:

| type | name | label | relevant |
|------|------|-------|----------|
| calculate | is_supervisor | | `pulldata('app-api', 'user.is_supervisor')` |
| begin_group | supervisor_section | Przegląd przełożonego | `${is_supervisor} = '1'` |
| text | supervisor_notes | Notatki przełożonego | |
| end_group | | | |

---

## Uwagi

- Wszystkie wywołania `pulldata('app-api', ...)` są oceniane przy otwarciu formularza i nie są ponownie oceniane dynamicznie podczas sesji (z wyjątkiem `serverTime` i `now()`).
- Jeśli klucz jest nieobsługiwany lub dane są niedostępne, funkcja zwraca `'n/a'` (nie pusty ciąg — testuj używając `!= 'n/a'` zamiast `!= ''`).
- Wartości `openArgs` są dostępne tylko gdy formularz jest uruchamiany z przycisku akcji; w przeciwnym razie zwracają pusty ciąg.
