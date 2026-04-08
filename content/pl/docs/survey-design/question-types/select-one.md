---
title: "Select_one"
description: "Pytania select_one umożliwiają respondentom wybranie dokładnie jednej opcji z predefiniowanej listy odpowiedzi."
icon: "radio_button_checked"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 224
---

Typ pytania `select_one` umożliwia respondentowi wybranie **dokładnie jednej opcji** z predefiniowanej listy. Domyślnie opcje są wyświetlane jako przyciski radiowe, ale dostępny jest szeroki zakres opcji wyglądu umożliwiających zmianę układu i zachowania.

## Podstawowa specyfikacja XLSForm

**Arkusz survey:**

| type | name | label |
|------|------|-------|
| select_one yesno | consent | Czy respondent wyraził zgodę? |

**Arkusz choices:**

| list_name | name | label |
|-----------|------|-------|
| yesno | yes | Tak |
| yesno | no | Nie |

Wartość `listname` w `select_one listname` musi odpowiadać kolumnie `list_name` w arkuszu choices.

Więcej szczegółów znajdziesz w [specyfikacji XLSForm](https://xlsform.org/en/#question-types).

## Zastosowania

Pytania select_one są używane do:

1. Pytań tak/nie
2. Pytań jednokrotnego wyboru (np. poziom wykształcenia, płeć, stan cywilny)
3. Ocen kategorycznych (np. słaby / dostateczny / dobry / doskonały)
4. Kaskadowych (powiązanych) list wyboru, gdzie opcje są filtrowane na podstawie poprzedniej odpowiedzi
5. Wyboru kraju, regionu, powiatu lub innej jednostki administracyjnej

## Opcje wyglądu

Podaj wartość w kolumnie `appearance`, aby zmienić sposób wyświetlania opcji:

{{< table >}}
| Wygląd | Opis |
|--------|------|
| *(brak)* | Domyślne przyciski radiowe, jeden w wierszu |
| `minimal` | Pojedyncza lista rozwijana zamiast przycisków radiowych |
| `quick` | Automatyczne przejście do następnego pytania natychmiast po wyborze (tylko mobilne) |
| `compact` | Zwarta siatka opcji — liczba kolumn dostosowuje się do szerokości ekranu |
| `compact-N` | Zwarta siatka z wymuszeniem N kolumn (np. `compact-3`) |
| `quickcompact` | Łączy `quick` i `compact` |
| `quickcompact-N` | Łączy `quick` i `compact` z N wymuszonymi kolumnami |
| `horizontal` | Opcje ułożone w poziomym rzędzie (web) |
| `horizontal-compact` | Poziome, zwarte odstępy (web) |
| `likert` | Wiersz skali Likerta — etykiety powyżej, przyciski radiowe poniżej |
| `label` | Pokazuje tylko etykiety opcji bez pól wyboru (użyj w parze z `list-nolabel`) |
| `list-nolabel` | Pokazuje tylko pola wyboru bez etykiet (użyj w parze z `label`) |
| `columns(N)` | Wyświetlanie w N kolumnach (rozszerzenie rtSurvey, np. `columns(3)`) |
| `distress` | Widget ikon emocji Kessler Psychological Distress (K10) |
| `search-api(...)` | Dynamiczne wyszukiwanie — ładuje opcje z API w czasie rzeczywistym |
| `tagging` | Wyświetla opcje jako klikalne chipsy tagów zamiast przycisków radiowych |
| `boxtag` | Wyświetla opcje jako stylowe prostokątne pola, które użytkownik dotyka, aby wybrać |
| `boxtag -search` | Układ boxtag z polem wyszukiwania/filtrowania nad polami |
| `duolingo-style1` | Układ kart inspirowany Duolingo — duże klikalne karty z ikonami |
| `rating_box` | Pola oceny w siatce — najlepsze dla opcji numerycznych lub skali |
| `star_rating` | Widget oceniania gwiazdkami — opcje wyświetlane jako 1–N gwiazdek |
| `choices-noshow` | Początkowo wyświetla tylko pierwsze 10 opcji; ujawnia pozostałe na żądanie |
| `noshow` | Całkowicie ukrywa listę opcji; wartość jest ustawiana programowo |
| `checkall` | Dodaje opcję "Zaznacz wszystkie" na górze listy |
| `max-items(N)` | Ogranicza liczbę widocznych opcji do N |
{{< /table >}}

### Przykład: Skala Likerta

| type | name | label | appearance |
|------|------|-------|------------|
| select_one satisfaction | service_rating | Jak bardzo jesteś zadowolony z usługi? | likert |

### Przykład: Zwarte 3 kolumny

| type | name | label | appearance |
|------|------|-------|------------|
| select_one regions | region | Wybierz region | compact-3 |

## Kaskadowe listy wyboru

Kaskadowa (powiązana) lista wyboru filtruje opcje na podstawie wartości wybranej w poprzednim pytaniu. Użyj kolumny `choice_filter` z nazwą kolumny z arkusza choices.

**survey:**

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one province | province | Wybierz województwo | |
| select_one district | district | Wybierz powiat | province_name = ${province} |

**choices:**

| list_name | name | label | province_name |
|-----------|------|-------|---------------|
| province | nairobi | Nairobi | |
| province | mombasa | Mombasa | |
| district | westlands | Westlands | nairobi |
| district | kasarani | Kasarani | nairobi |
| district | nyali | Nyali | mombasa |
| district | likoni | Likoni | mombasa |

Gdy respondent wybierze `nairobi`, na liście powiatów pojawią się tylko `Westlands` i `Kasarani`.

{{% alert icon=" " context="warning" %}}
Nazwa kolumny używana w `choice_filter` (np. `province_name`) musi istnieć w arkuszu choices. `${province}` odwołuje się do pola ankiety o nazwie `province`.
{{% /alert %}}

## Używanie wybranej wartości w wyrażeniach

Odwołaj się do wybranej **wartości** (nie etykiety) za pomocą `${fieldname}`:

```
relevant: ${consent} = 'yes'
```

Aby uzyskać etykietę opcji zamiast wartości, użyj `choice-label()`:

```
calculate: choice-label(${education_level}, ${education_level})
```

## Opcja „inne" z polem tekstowym

Powszechnym wzorcem jest dodanie opcji „inne", która odsłania pole tekstowe:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one occupation | job | Jaki jest Twój zawód? | |
| text | job_other | Proszę podać | `${job} = 'other'` |

**choices:**

| list_name | name | label |
|-----------|------|-------|
| occupation | farmer | Rolnik |
| occupation | trader | Handlarz |
| occupation | student | Student |
| occupation | other | Inne (proszę podać) |

## Najlepsze praktyki

1. Utrzymuj krótkie i wzajemnie wykluczające się listy — jeśli respondenci mogą wybrać więcej niż jedną opcję, użyj `select_multiple`.
2. Umieść najczęstszą odpowiedź na początku lub posortuj alfabetycznie w przypadku długich list.
3. Zawsze uwzględniaj opcję „Nie wiem" lub „Wolę nie odpowiadać" tam, gdzie jest to właściwe.
4. Używaj `minimal` (lista rozwijana) dla list z ponad 7–8 opcjami na urządzeniach mobilnych, aby oszczędzać miejsce na ekranie.
5. W przypadku kaskadowych list, przed zbudowaniem formularza dodaj wszystkie kolumny filtrów w arkuszu choices.

## Ograniczenia

- Respondent może wybrać tylko jedną opcję — do pytań z wieloma odpowiedziami użyj `select_multiple`.
- Wygląd `likert` działa najlepiej z 5–7 opcjami mieszczącymi się w jednej linii.
- Automatyczne przejście `quick` jest dostępne tylko na urządzeniach mobilnych — nie ma efektu w formularzach webowych.
