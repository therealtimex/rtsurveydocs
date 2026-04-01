---
title: "Grid-layout"
description: "Układ siatki pozwala na rozmieszczanie pól w siatce CSS wewnątrz grupy, umożliwiając wielokolumnowe projekty formularzy."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 296
---

Funkcja **Układ siatki** pozwala rozmieszczać pytania w **wielokolumnowej siatce** wewnątrz grupy, używając tagu wyglądu `gridformat<>`. Jest to przydatne w gęstych formularzach do wprowadzania danych, gdzie wiele powiązanych pól powinno pojawiać się obok siebie zamiast być ułożone pionowo.

---

## Jak to działa

Układ siatki jest stosowany na dwóch poziomach:

1. **Grupa** — ustaw `appearance: field-list grid(weight=N)`, aby zdefiniować liczbę kolumn siatki
2. **Każde pole wewnątrz grupy** — ustaw `appearance: gridformat<row=R col=C colspan=S/>`, aby ustawić pole

Siatka używa 12-kolumnowego systemu w stylu Bootstrap. `weight=N` definiuje liczbę logicznych kolumn siatki; każda kolumna zajmuje `12/N` kolumn Bootstrap.

---

## Wygląd na poziomie grupy

| Wygląd | Opis |
|--------|------|
| `field-list grid(weight=2)` | Siatka 2-kolumnowa (każda kolumna = 6 kolumn Bootstrap) |
| `field-list grid(weight=3)` | Siatka 3-kolumnowa (każda kolumna = 4 kolumny Bootstrap) |
| `field-list grid(weight=4)` | Siatka 4-kolumnowa (każda kolumna = 3 kolumny Bootstrap) |
| `field-list grid(weight=6)` | Siatka 6-kolumnowa (każda kolumna = 2 kolumny Bootstrap) |

---

## Składnia `gridformat<>` na poziomie pola

```
gridformat<row=R col=C colspan=S/>
gridformat<row=R col=C colspan=S backgroundcolor=COLOR/>
```

| Atrybut | Opis |
|---------|------|
| `row` | Numer wiersza (numeracja od 1) |
| `col` | Numer kolumny (numeracja od 1, w siatce zdefiniowanej przez `weight`) |
| `colspan` | Liczba kolumn zajmowanych przez to pole (domyślnie 1) |
| `backgroundcolor` | Opcjonalny kolor CSS dla tła pola (np. `#f0f0f0`, `lightblue`) |

---

## Przykład: Sekcja badania gospodarstwa domowego w 2 kolumnach

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | demographics | Dane demograficzne | `field-list grid(weight=2)` |
| text | first_name | Imię | `gridformat<row=1 col=1/>` |
| text | last_name | Nazwisko | `gridformat<row=1 col=2/>` |
| integer | age | Wiek | `gridformat<row=2 col=1/>` |
| select_one gender | gender | Płeć | `gridformat<row=2 col=2/>` |
| text | address | Pełny adres | `gridformat<row=3 col=1 colspan=2/>` |
| end_group | | | |

Renderuje się jako:

```
[ Imię              ] [ Nazwisko           ]
[ Wiek              ] [ Płeć               ]
[ Pełny adres (obejmuje obie kolumny)      ]
```

---

## Przykład: Wprowadzanie danych o działce w 3 kolumnach

| type | name | label | appearance |
|------|------|-------|------------|
| begin_group | plot_data | Szczegóły działki | `field-list grid(weight=3)` |
| text | plot_id | ID działki | `gridformat<row=1 col=1/>` |
| decimal | area_ha | Powierzchnia (ha) | `gridformat<row=1 col=2/>` |
| select_one crop_type | crop | Rodzaj uprawy | `gridformat<row=1 col=3/>` |
| decimal | yield | Plon (kg) | `gridformat<row=2 col=1/>` |
| decimal | revenue | Przychód | `gridformat<row=2 col=2/>` |
| text | notes | Uwagi | `gridformat<row=2 col=3/>` |
| end_group | | | |

---

## Kolory tła

Użyj `backgroundcolor`, aby wizualnie odróżnić sekcje:

| type | name | label | appearance |
|------|------|-------|------------|
| note | section_a | Sekcja A | `gridformat<row=1 col=1 colspan=2 backgroundcolor=#e8f4f8/>` |

---

## Najlepsze praktyki

1. Używaj układu siatki tylko dla **intensywnych** ekranów wprowadzania danych, gdzie pola obok siebie naprawdę redukują przewijanie.
2. Utrzymuj pola `colspan=1` krótkie (ID, kody, krótkie pola select) — szerokie etykiety są obcinane w wąskich kolumnach siatki.
3. Używaj `colspan=N` dla pól z długimi etykietami lub wielowierszowymi polami tekstowymi.
4. Testuj na najmniejszym rozmiarze ekranu oczekiwanym dla ankieterów — siatka 4-kolumnowa jest zatłoczona na telefonie.
5. Układ siatki działa najlepiej na urządzeniach webowych i tabletach; na telefonach komórkowych układ 2-kolumnowy to zazwyczaj maksymalna wygodna szerokość.

## Ograniczenia

- `gridformat<>` działa tylko wewnątrz grupy z wyglądem `grid(weight=N)` — nie ma efektu na najwyższym poziomie.
- Układ siatki jest rozszerzeniem formularzy webowych rtSurvey i może nie renderować się poprawnie w innych klientach kompatybilnych z ODK.
- Pozycjonowanie wierszy i kolumn nie jest weryfikowane w czasie budowania formularza — nakładające się pola będą się renderować, ale mogą wyglądać źle.
