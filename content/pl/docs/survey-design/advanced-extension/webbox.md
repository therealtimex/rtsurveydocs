---
title: "Webbox"
description: "Webbox osadza zewnętrzną stronę internetową wewnątrz ankiety jako modalny iframe, umożliwiając ankieterom przeglądanie materiałów referencyjnych lub interakcję z zewnętrznymi narzędziami bez opuszczania formularza."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 299
---

**Webbox** osadza zewnętrzną stronę internetową wewnątrz ankiety jako **modalne okno popup** (iframe). Ankieter dotyka przycisku w etykiecie lub polu notatki, strona otwiera się w nakładce pełnoekranowej wewnątrz formularza, a po jej zamknięciu wraca dokładnie tam, gdzie był. Dzięki temu możesz pokazywać materiały referencyjne, mapy, pulpity nawigacyjne lub własne narzędzia bez otwierania oddzielnej karty przeglądarki.

---

## Składnia

Wstaw tag HTML `<webbox>` bezpośrednio w kolumnie `label` lub notatce:

```html
<webbox src='https://example.com/reference' title='Przewodnik referencyjny'>Otwórz Przewodnik referencyjny</webbox>
```

| Atrybut | Opis |
|---------|------|
| `src` | URL do załadowania w iframe. Obsługuje zarówno apostrofy, jak i cudzysłowy. |
| `title` | Tekst wyświetlany na pasku nagłówka modalnego. Obsługuje zwykły tekst. |
| *(zawartość)* | Etykieta klikalnego przycisku wyświetlana w polu ankiety |

---

## Podstawowy przykład

| type | name | label |
|------|------|-------|
| note | ref_guide | `<webbox src='https://docs.example.com/field-guide' title='Przewodnik terenowy'>Otwórz Przewodnik terenowy</webbox>` |

Renderuje przycisk z etykietą „Otwórz Przewodnik terenowy". Po dotknięciu otwiera się modalne okno wyświetlające stronę przewodnika terenowego.

---

## Osadzanie mapy

| type | name | label |
|------|------|-------|
| note | area_map | `<webbox src='https://maps.example.com/survey-area' title='Mapa obszaru badań'>Wyświetl mapę</webbox>` |

---

## Przekazywanie wartości formularza do osadzonej strony

Dołącz wartości pól formularza do URL za pomocą `concat()` w kolumnie `calculation` i odwołaj się do wyniku w etykiecie:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | webbox_url | | `concat('https://dashboard.example.com/household?id=', ${household_id})` |
| note | hh_dash | `<webbox src='${webbox_url}' title='Pulpit nawigacyjny gospodarstwa'>Otwórz pulpit nawigacyjny</webbox>` |

{{% alert icon=" " context="warning" %}}
Atrybut `src` w tagu `<webbox>` obsługuje odwołania `${fieldname}`, gdy etykieta jest obliczana z pola `calculate`. Skonstruuj pełny URL w polu `calculate` i odwołaj się do niego.
{{% /alert %}}

---

## Interakcja z powtórzeniami: przyciski usuwania

Webbox obsługuje również specjalne tagi akcji do zarządzania grupami powtórzeń wewnątrz etykiet:

```html
<delete-repeat-current>Usuń ten wiersz</delete-repeat-current>
<delete-repeat-last>Usuń ostatni wiersz</delete-repeat-last>
```

Renderują się jako przyciski usuwające instancje powtórzeń po dotknięciu. Umieść je w polu `note` wewnątrz (lub tuż po) grupy powtórzeń:

| type | name | label |
|------|------|-------|
| begin_repeat | items | Pozycja |
| text | item_name | Nazwa pozycji |
| note | delete_btn | `<delete-repeat-current>Usuń tę pozycję</delete-repeat-current>` |
| end_repeat | | |

---

## Komunikacja z osadzoną stroną (postMessage)

Iframe webbox i formularz nadrzędny mogą komunikować się za pomocą API `postMessage` przeglądarki. Formularz nadrzędny wysyła wiadomość `init` do iframe po jego otwarciu. Osadzona strona może odpowiedzieć:

- `delete-repeat-current` — wyzwala usunięcie bieżącej instancji powtórzenia
- `delete-repeat-last` — wyzwala usunięcie ostatniej instancji powtórzenia

Umożliwia to niestandardowym narzędziom webowym (np. narzędziom do rysowania, interaktywnym mapom) wyzwalanie akcji formularza, gdy użytkownik potwierdzi akcję wewnątrz iframe.

---

## Najlepsze praktyki

1. Używaj webbox do **materiałów referencyjnych** (wytyczne, tabele przeglądowe, mapy) — nie do zbierania danych, które powinny znajdować się w samym formularzu.
2. Upewnij się, że osadzony URL jest dostępny z sieci urządzenia — webbox wymaga połączenia.
3. Utrzymuj osadzoną stronę przyjazną dla urządzeń mobilnych — modalne okno ma maksymalnie 800px szerokości i 80% wysokości widocznego obszaru.
4. Używaj opisowych etykiet przycisków (np. „Wyświetl mapę wsi") zamiast ogólnych etykiet („Kliknij tutaj").
5. Informuj ankieterów, że zamknięcie modalnego okna wraca do ankiety — niektórzy użytkownicy mogą nie wiedzieć, jak zamknąć nakładkę iframe.

## Ograniczenia

- Webbox wymaga połączenia sieciowego do załadowania osadzonego URL.
- Niektóre zewnętrzne strony blokują osadzanie w iframe za pomocą nagłówków `X-Frame-Options` lub `Content-Security-Policy` — tych stron nie można używać z webbox.
- Modalne okno zamyka się, gdy ankieter przejdzie do innego pytania — każdy niezapisany stan w iframe zostaje utracony.
- Webbox jest rozszerzeniem formularzy webowych rtSurvey i może nie działać w innych klientach kompatybilnych z ODK.
