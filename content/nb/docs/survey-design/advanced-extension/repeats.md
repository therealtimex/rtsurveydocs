---
title: "Avanserte repeats"
description: "Avanserte mønstre for repeat-grupper: dynamiske antall, nestede repeats, sammendrag av repeat-data og referering til verdier på tvers av repeats."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 295
---

Denne siden dekker avanserte mønstre for arbeid med repeat-grupper i rtSurvey. For grunnleggende informasjon om oppsett av en repeat-gruppe, se [Gruppering og repeats](../repeats).

---

## Dynamisk repeat-antall

Som standard bestemmer telleren hvor mange ganger det skal gjentas. Du kan fikse antall gjentagelser ved hjelp av `repeat_count`:

| type | name | label | repeat_count |
|------|------|-------|--------------|
| begin_repeat | household_members | Husholdningsmedlem | `${num_members}` |
| text | member_name | Medlemsnavn | |
| integer | member_age | Alder | |
| end_repeat | | | |

Gjentagelsen kjører nøyaktig `${num_members}` ganger, der `num_members` ble samlet inn tidligere i skjemaet. Telleren kan ikke legge til eller fjerne instanser.

---

## Indeksert tilgang: `indexed-repeat()`

Gå til et spesifikt repeat-instanses feltverdi fra **utenfor** repeat-gruppen ved hjelp av `indexed-repeat(repeatedField, repeatGroup, index)`:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | first_name | | `indexed-repeat(${member_name}, ${household_members}, 1)` |
| calculate | second_name | | `indexed-repeat(${member_name}, ${household_members}, 2)` |

Dette er nyttig for å bygge sammendragsfelt eller referere til "primære" medlemmets data etter repeat-en.

---

## Gjeldende instansposisjon: `index()`

Inne i en repeat-gruppe returnerer `index()` den 1-baserte posisjonen til gjeldende instans. Bruk det til å merke hver gjentagelse eller lage unike identifikatorer:

| type | name | label |
|------|------|-------|
| begin_repeat | plots | Plot |
| note | plot_label | Plotnummer ${index()} |
| text | plot_id | Plot-ID |
| end_repeat | | |

---

## Referere til felt i samme instans

Inne i en repeat, bruk `${feltnavn}` for å referere til et annet felt **i samme repeat-instans**. Det er ikke nødvendig med `indexed-repeat()` innenfor samme løkke:

| type | name | label | relevant |
|------|------|-------|----------|
| begin_repeat | members | Medlem | |
| text | member_name | Navn | |
| integer | member_age | Alder | |
| text | school_name | Skolenavn | `${member_age} < 18` |
| end_repeat | | | |

---

## Referere til overordnede felt fra innsiden av en repeat

Felt utenfor (over) repeat-gruppen kan refereres til normalt med `${feltnavn}`:

| type | name | label |
|------|------|-------|
| text | village | Landsbynavn |
| begin_repeat | plots | Jordbruksplot |
| note | plot_context | Plotter i ${village} |
| end_repeat | | |

---

## Oppsummering av repeat-data

Bruk repeat-aggregatfunksjoner **utenfor** repeat-gruppen for å oppsummere:

| Funksjon | Eksempel | Beskrivelse |
|----------|---------|-------------|
| `count(group)` | `count(${household_members})` | Antall instanser |
| `sum(field)` | `sum(${loan_amount})` | Sum av et numerisk felt |
| `min(field)` | `min(${member_age})` | Minimumsverdi |
| `max(field)` | `max(${member_age})` | Maksimumsverdi |
| `join(sep, field)` | `join(', ', ${member_name})` | Kommaseparert liste |
| `count-if(group, expr)` | `count-if(${members}, ${member_age} < 18)` | Betinget telling |
| `sum-if(field, expr)` | `sum-if(${loan_amount}, ${loan_amount} > 500)` | Betinget sum |
| `join-if(sep, field, expr)` | `join-if(', ', ${name}, ${age} >= 18)` | Betinget join |

### Eksempel: Husholdningssammendrag

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

## Nestede repeats

En repeat-gruppe kan inneholde en annen repeat-gruppe. Bruk dette med forsiktighet — nestede repeats legger til kompleksitet og kan forvirre tellere.

| type | name | label |
|------|------|-------|
| begin_repeat | households | Hushold |
| text | hh_id | Hushold-ID |
| begin_repeat | hh_members | Medlem |
| text | member_name | Medlemsnavn |
| end_repeat | | |
| end_repeat | | |

For å referere til et felt i en ytre repeat fra den indre repeat-en, bruk `${feltnavn}` — det løses til nærmeste samsvarende forfedre:

Inne i `hh_members`-repeaten returnerer `${hh_id}` ID-en til **gjeldende** hushold, ikke alle hushold.

---

## Rangering inne i repeat-grupper: `rank-index()`

Når et `rank`-felt eksisterer inne i en repeat, bruk `rank-index(instanceNumber, repeatedField)` fra utsiden for å få den ordinale rangeringen til en spesifikk instans:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | top_scorer | | `rank-index(1, ${score})` |

`rank-index(1, ${score})` returnerer instansindeksen til den høyeste poengsummen.

---

## Beste praksis

1. Bruk alltid `repeat_count` når antall gjentagelser er kjent på forhånd — det forhindrer tellere fra å tilfeldigvis legge til eller fjerne instanser.
2. Hold repeat-grupper fokuserte — en repeat med 20+ spørsmål per instans er vanskelig å navigere.
3. Navngi repeat-grupper tydelig (f.eks. `household_members`, ikke `repeat1`) — navnet vises i funksjonskall og eksporterte data.
4. Test med maksimalt forventet antall instanser for å verifisere ytelsen.
5. Bruk `field-list`-utseende på repeat-gruppen for å vise alle felt på én skjerm per instans (mobil).

---

## Begrensninger

- `indexed-repeat()` krever en gyldig indeks (1 til antall instanser) — indekser utenfor rekkevidde returnerer tom.
- Nestede repeats utover 2 nivåer anbefales ikke og kan forårsake visningsproblemer på noen klienter.
- Aggregatfunksjoner (`sum`, `count`, osv.) opererer på hele repeat-gruppen — du kan ikke aggregere en delmengde av instanser uten `*-if`-varianter.
