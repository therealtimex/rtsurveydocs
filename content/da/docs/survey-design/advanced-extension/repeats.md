---
title: "Avancerede gentagelser"
description: "Avancerede mønstre for gentagelsesgrupper: dynamiske antal, indlejrede gentagelser, opsummering af gentagelsesdata og krydsreferencer mellem gentagelser."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

Denne side dækker avancerede mønstre for arbejde med gentagelsesgrupper i rtSurvey. For det grundlæggende om opsætning af en gentagelsesgruppe, se [Grupperinger og gentagelser](../repeats).

---

## Dynamisk gentagelsesantal

Som standard bestemmer intervieweren, hvor mange gange der skal gentages. Du kan fastlåse antallet af gentagelser ved hjælp af `repeat_count`:

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | Husholdningsmedlem | `${num_members}` |
| text | member_name | Medlemsnavn | |
| integer | member_age | Alder | |
| end_repeat | | | |

Gentagelsen kører præcis `${num_members}` gange, hvor `num_members` er indsamlet tidligere i formularen. Intervieweren kan ikke tilføje eller fjerne instanser.

---

## Indekseret adgang: `indexed-repeat()`

Adgang til en specifik gentagelsesinstans' feltværdi fra **udenfor** gentagelsesgruppen ved hjælp af `indexed-repeat(gentagetFelt, gentagelsesGruppe, indeks)`:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

Dette er nyttigt til at opbygge opsummeringsfelter eller referere til det "primære" members data efter gentagelsen.

---

## Aktuel instansposition: `index()`

Inden for en gentagelsesgruppe returnerer `index()` den 1-baserede position for den aktuelle instans. Brug det til at mærke hver gentagelse eller oprette unikke identifikatorer:

| type | name | label |
|------|------|-------|
| begin_repeat | plots | Plot |
| note | plot_label | Plotnummer ${index()} |
| text | plot_id | Plot-ID |
| end_repeat | | |

---

## Krydsreferencer til felter i den samme instans

Inden for en gentagelse bruges `${feltnavn}` til at referere til et andet felt **i den samme gentagelsesinstans**. Der er ikke brug for `indexed-repeat()` inden for den samme løkke:

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | Medlem | |
| text | member_name | Navn | |
| integer | member_age | Alder | |
| text | school_name | Skolenavn | `${member_age} < 18` |
| end_repeat | | | |

---

## Krydsreferencer til overordnede felter fra en gentagelse

Felter uden for (over) gentagelsesgruppen kan refereres normalt med `${feltnavn}`:

| type | name | label |
|------|------|-------|
| text | village | Landsbynavn |
| begin_repeat | plots | Landbrugsplot |
| note | plot_context | Plot i ${village} |
| end_repeat | | |

---

## Opsummering af gentagelsesdata

Brug aggregatfunktioner for gentagelser **udenfor** gentagelsesgruppen til at opsummere:

| Funktion | Eksempel | Beskrivelse |
|----------|---------|-------------|
| `count(group)` | `count(${household_members})` | Antal instanser |
| `sum(field)` | `sum(${loan_amount})` | Sum af et numerisk felt |
| `min(field)` | `min(${member_age})` | Minimumsværdi |
| `max(field)` | `max(${member_age})` | Maksimumsværdi |
| `join(sep, field)` | `join(', ', ${member_name})` | Kommasepareret liste |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | Betinget tælling |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | Betinget sum |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | Betinget sammenføjning |

### Eksempel: Husholdningsopsummering

| type | name | label | calculation |
|------|------|-------|-------------|
| integer | num_members | Hvor mange medlemmer? | |
| begin_repeat | members | Medlem | `${num_members}` |
| text | member_name | Navn | |
| integer | member_age | Alder | |
| end_repeat | | | |
| calculate | total_members | | `count(${members})` |
| calculate | children_count | | `count-if(${members}, ${member_age} < 18)` |
| calculate | adult_names | | `join-if(', ', ${member_name}, ${member_age} >= 18)` |
| note | summary | ${total_members} medlemmer; ${children_count} under 18. Voksne: ${adult_names} | |

---

## Indlejrede gentagelser

En gentagelsesgruppe kan indeholde en anden gentagelsesgruppe. Brug dette forsigtigt — indlejrede gentagelser tilføjer kompleksitet og kan forvirre interviewere.

| type | name | label |
|------|------|-------|
| begin_repeat | households | Husholdning |
| text | hh_id | Husholdnings-ID |
| begin_repeat | hh_members | Medlem |
| text | member_name | Medlemsnavn |
| end_repeat | | |
| end_repeat | | |

For at referere til et felt i en ydre gentagelse fra den indre gentagelse bruges `${feltnavn}` — det opløser til den nærmeste matchende forfader:

Inden i `hh_members`-gentagelsen returnerer `${hh_id}` ID'et for den **aktuelle** husholdning, ikke alle husholdninger.

---

## Rang inden for gentagelsesgrupper: `rank-index()`

Når et `rank`-felt findes inden i en gentagelse, bruges `rank-index(instansNummer, gentagetFelt)` udefra for at få den ordinale rang for en specifik instans:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})` returnerer instansindekset for den højeste score.

---

## Bedste praksis

1. Brug altid `repeat_count`, når antallet af gentagelser er kendt på forhånd — det forhindrer interviewere i utilsigtet at tilføje eller fjerne instanser.
2. Hold gentagelsesgrupper fokuserede — en gentagelse med 20+ spørgsmål pr. instans er svær at navigere.
3. Navngiv gentagelsesgrupper tydeligt (f.eks. `household_members`, ikke `repeat1`) — navnet vises i funktionskald og eksporterede data.
4. Test med det maksimalt forventede antal instanser for at verificere ydelsen.
5. Brug `field-list` appearance på gentagelsesgruppen for at vise alle felter på én skærm pr. instans (mobil).

---

## Begrænsninger

- `indexed-repeat()` kræver et gyldigt indeks (1 til antal instanser) — indekser uden for intervallet returnerer tomme værdier.
- Indlejrede gentagelser ud over 2 niveauer anbefales ikke og kan forårsage visningsproblemer på nogle klienter.
- Aggregatfunktioner (`sum`, `count` osv.) opererer på hele gentagelsesgruppen — du kan ikke aggregere en delmængde af instanser uden `*-if`-varianterne.
