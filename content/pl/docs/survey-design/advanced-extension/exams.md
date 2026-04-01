---
title: "Exams"
description: "Funkcja egzaminów dodaje tryb quizu z licznikiem czasu do ankiety, z opcjonalną informacją dźwiękową dla poprawnych i niepoprawnych odpowiedzi."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 298
---

Funkcja **Egzamin** przekształca ankietę w quiz z licznikiem czasu. Respondentowi wyświetlany jest odliczający czas, a ankieta rejestruje, ile czasu pozostało po jego zakończeniu. Opcjonalnie mogą odtwarzać się dźwięki dla poprawnych i niepoprawnych odpowiedzi.

Jest to przydatne do ocen wiedzy, testów umiejętności czytania, sprawdzania kompetencji pracowników terenowych i każdej ankiety, w której czas wykonania jest istotną daną.

---

## Funkcja `check-exam()`

Skonfiguruj egzamin za pomocą `check-exam()` w kolumnie **`calculation`** pola `calculate` umieszczonego na początku formularza:

```
check-exam(examTime, questionToStoreRemainingTime)
check-exam(examTime, questionToStoreRemainingTime, rightSound, wrongSound, excludeQuestion)
```

### Parametry

| # | Parametr | Opis |
|---|----------|------|
| 1 | `examTime` | Całkowity czas trwania egzaminu w sekundach |
| 2 | `questionToStoreRemainingTime` | Nazwa pola `calculate` lub `integer`, w którym zostanie zapisany pozostały czas po zakończeniu egzaminu |
| 3 | `rightSound` | *(Opcjonalny)* Nazwa pliku audio do odtworzenia po poprawnej odpowiedzi (dołącz do formularza jako plik multimedialny) |
| 4 | `wrongSound` | *(Opcjonalny)* Nazwa pliku audio do odtworzenia po błędnej odpowiedzi |
| 5 | `excludeQuestion` | *(Opcjonalny)* Lista nazw pól oddzielona przecinkami, które mają być wykluczone z licznika czasu (np. `'intro_note,consent'`) |

---

## Podstawowa konfiguracja

### Krok 1: Dodaj pola egzaminu

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(600, 'remaining_time')` |
| calculate | remaining_time | | |

`exam_config` uruchamia 600-sekundowy (10-minutowy) licznik. `remaining_time` jest automatycznie wypełniany po zakończeniu egzaminu przez respondenta.

### Krok 2: Dodaj pytania

Licznik czasu obejmuje wszystkie pytania w formularzu z wyjątkiem tych wymienionych w `excludeQuestion`.

| type | name | label |
|------|------|-------|
| select_one yesno | q1 | Stolica Kenii to Nairobi. Prawda czy fałsz? |
| select_one choices | q2 | Który organ pompuje krew w ciele? |
| select_one choices | q3 | Woda wrze w 100°C na poziomie morza. Prawda czy fałsz? |

### Krok 3: Zapisz pozostały czas

Pole podane w parametrze 2 (`remaining_time`) jest automatycznie ustawiane na liczbę sekund pozostałych w momencie przesłania przez respondenta. Wartość `0` oznacza, że czas upłynął; wysoka wartość oznacza szybkie ukończenie.

---

## Z informacją dźwiękową

Dołącz pliki dźwiękowe do formularza (jako załączniki multimedialne), a następnie odwołaj się do nich:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3')` |

- `correct.mp3` odgrywa się, gdy respondent wybierze prawidłową odpowiedź
- `wrong.mp3` odgrywa się, gdy respondent wybierze błędną odpowiedź

{{% alert icon=" " context="warning" %}}
Pliki dźwiękowe muszą być dołączone do formularza jako pliki multimedialne, a nazwa pliku musi dokładnie odpowiadać (z uwzględnieniem wielkości liter), łącznie z rozszerzeniem.
{{% /alert %}}

---

## Wykluczanie pytań z licznika

Podaj listę nazw pól oddzielonych przecinkami, które mają zostać wykluczone z egzaminu (np. wstępne notatki lub pytania o zgodę):

```
check-exam(300, 'remaining_time', '', '', 'intro_note,consent_ack,section_header')
```

Pozostaw `rightSound` i `wrongSound` jako puste ciągi `''`, jeśli nie potrzebujesz dźwięku, ale potrzebujesz wykluczeń.

---

## Kompletny przykład

| type | name | label | calculation |
|------|------|-------|-------------|
| note | intro | Witaj w ocenie wiedzy zdrowotnej. Masz 5 minut na odpowiedź na wszystkie pytania. | |
| trigger | start_ack | Dotknij OK, gdy jesteś gotowy do rozpoczęcia. | |
| calculate | exam_config | | `check-exam(300, 'remaining_time', 'correct.mp3', 'wrong.mp3', 'intro,start_ack')` |
| calculate | remaining_time | | |
| select_one yesno | q1 | Mycie rąk zapobiega rozprzestrzenianiu się chorób. | |
| select_one yesno | q2 | Powinieneś pić co najmniej 2 litry wody dziennie. | |
| select_one yesno | q3 | Malaria jest wywoływana przez wirusa. | |

---

## Najlepsze praktyki

1. Zawsze informuj respondentów o limicie czasu przed rozpoczęciem — użyj `note` lub `trigger` przed polem `check-exam()`.
2. Wykluczaj wstępne notatki i pytania o zgodę z licznika za pomocą parametru `excludeQuestion`.
3. Użyj `remaining_time` w kolejnym obliczeniu, aby wykryć przekroczenie czasu: `if(${remaining_time} = 0, 'Czas minął', 'Ukończono')`.
4. Utrzymuj liczbę pytań proporcjonalną do dozwolonego czasu — 2–3 minuty na pytanie to rozsądna wartość bazowa dla większości ocen wiedzy.
5. Przetestuj pliki audio na rzeczywistym urządzeniu przed wdrożeniem — odtwarzanie dźwięku różni się w zależności od wersji Androida i przeglądarek.

## Ograniczenia

- Licznik jest tylko do wyświetlania — formularz nie przesyła się automatycznie po upływie czasu; respondent nadal musi ręcznie przesłać.
- Informacja dźwiękowa wymaga, aby głośność urządzenia była włączona i niema.
- Funkcja egzaminów jest rozszerzeniem rtSurvey i nie jest częścią standardowej specyfikacji XLSForm.
