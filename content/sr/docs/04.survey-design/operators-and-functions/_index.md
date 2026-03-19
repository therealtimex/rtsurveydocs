---
title: "Operatori i funkcije"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 290
---

Izrazi u rtSurvey-u su pisani u podskupu **XPath 1.0**, proširenom JavaRosa/ODK funkcijama i prilagođenim rtSurvey funkcijama. Izraze koristite u kolonama `calculate`, `constraint`, `relevant`, `required` i `default` vašeg XLSForm-a.

## Referenciranje vrednosti polja

Koristite `${ime_polja}` za referenciranje vrednosti drugog polja:

```
${age} > 18
```

Koristite `.` (tačku) za referenciranje **vrednosti trenutnog polja** — uobičajeno se koristi u izrazima `constraint`:

```
. >= 0 and . <= 100
```

Koristite `..` za referenciranje roditeljske grupe (napredna upotreba u ponavljanjima).

## Sintaksa izraza

Izrazi prate standardna XPath pravila:

- **Stringovi** moraju biti zatvoreni u jednostruke navodnike: `'yes'`
- **Brojevi** se pišu kao što jesu: `42`, `3.14`
- **Boolean** rezultati se koriste za `relevant`, `required` i `constraint` — svaka neprazna, nenulta vrednost je istinita
- Razmak se ignoriše oko operatora

{{% alert icon=" " context="warning" %}}
Uvek koristite prave navodnike (`'` ili `"`) — nikad "pametne navodnike" (zaobljene navodnike). Urednici bogatog teksta često automatski konvertuju navodnike i to će pokvariti vaše izraze.
{{% /alert %}}

## Sekcije u ovom poglavlju

- **[Operatori](operators)** — operatori poređenja (`=`, `!=`, `>`, `<`, `>=`, `<=`) i logički operatori (`and`, `or`, `not()`)
- **[Funkcije](functions)** — funkcije za stringove, izbor, brojeve, datum/vreme, boolean, geo i korisne funkcije
- **[Reference](references)** — kako referencirati polja i kontekstualne vrednosti

## Brzi primeri

| Slučaj upotrebe | Izraz |
|-----------------|-------|
| Prikaži ako je godine više od 18 | `${age} > 18` |
| Prikaži samo ako je izabrano "da" | `${consent} = 'yes'` |
| Zahtevaj ako drugo polje nije prazno | `${name} != ''` |
| Izračunaj ukupno | `${adults} + ${children}` |
| Spoji ime | `concat(${first_name}, ' ', ${last_name})` |
| Današnji datum | `today()` |
| Proverite da li je opcija izabrana | `selected(${interests}, 'sports')` |
