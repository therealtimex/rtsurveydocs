---
title: "Zarządzanie zgłoszeniami"
description: "Przeglądanie, zarządzanie i eksportowanie surowych wpisów danych i zgłoszeń."
icon: "cloud"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 317
---

Moduł **Zarządzania zgłoszeniami** (dostępny przez przycisk **Data View** w sekcji Form Family) pozwala kierownikom projektów i przełożonym bezpośrednio wchodzić w interakcję z przychodzącymi surowymi danymi. Służy jako ujednolicone miejsce pracy do przeglądania zgłoszeń ankieterów, śledzenia identyfikatorów urządzeń i przeprowadzania operacji jakości danych.

![Interfejs zarządzania zgłoszeniami](/images/manage_submissions.png)

## Przegląd danych i kolumny

Siatka danych dynamicznie wyświetla dane zebrane dla konkretnego formularza. Działa w dwóch głównych trybach: **Official** (Sfinalizowane rekordy) i **Working** (Rzeczywiste, niesfinalizowane rekordy).

### Kluczowe kolumny danych

Niezależnie od niestandardowych pytań zdefiniowanych w formularzu, siatka zawiera kilka standardowych kolumn metadanych pomocnych przy audycie:

- **Submit by:** Identyfikuje platformę źródłową zgłoszenia (np. FA dla aplikacji terenowej, WEB dla formularza webowego, RS dla systemów zdalnych).
- **Detail:** Otwiera skupiony widok pojedynczego rekordu (ikona wyszukiwania) do sprawdzenia każdej zmiennej i odpowiedzi przesłanej dla tej instancji.
- **iNote:** Pozwala przełożonym dołączać notatki boczne lub wewnętrzne komentarze do konkretnego rekordu bez zmiany zebranych danych (reprezentowane przez ikonę ołówka).
- **Pola dat:** Znaczniki czasu wskazujące, kiedy rekord został zainicjowany, zakończony lub zsynchronizowany.
- **Załączniki mediów:** Bezpośrednie linki miniatur do obrazów, podpisów lub plików zebranych podczas ankiety.
- **Grupy powtórzeń:** Dedykowane linki do dostępu do zagnieżdżonych tabel dla powtarzanych pytań w formularzu nadrzędnym.

## Akcje zgłoszeń

Aby ułatwić aktywną kontrolę jakości danych, interfejs zapewnia rozwijane menu akcji, które można wykonać na wybranych rekordach:

- **Utwórz nową instancję:** Pozwala administratorom ręcznie wprowadzić nowy rekord ankiety bezpośrednio do bazy danych.
- **Zwróć instancję:** Odrzuca przesłany rekord i zleca ankieterowi ponowną weryfikację lub zbieranie informacji.
- **Obserwuj instancję:** Oznacza rekord do dalszej uwagi, zazwyczaj wysyłając alert do zespołu terenowego w celu wyjaśnienia.
- **Eksportuj do pliku poleceń zwrotów / pakietu poleceń obserwacji:** Generuje eksporty wsadowe (pliki) zawierające zestawy danych specjalnie oznaczone do zwrotów lub obserwacji.
- **Konwertuj do XML:** Przekształca ustrukturyzowany zestaw danych z powrotem do jego surowego formatu XML do analizy backendowej lub integracji systemowej.
- **Przekaż instancje:** (Dostępne w trybie *Working*) Natychmiast przesyła niesfinalizowane dane na inne urządzenie lub użytkownika.
- **Usuń:** Trwale usuwa wybrane instancje z bazy danych.
