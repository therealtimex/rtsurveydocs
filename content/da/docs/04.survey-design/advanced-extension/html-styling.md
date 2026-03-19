---
title: "HTML-styling"
description: "rtSurvey understøtter HTML-tags i labels og hints, hvilket muliggør formatering af rig tekst, links og dynamisk farvetemaer."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 297
---

rtSurvey gengiver **label**- og **hint**-tekst som HTML på webformularer. Det betyder, at du kan bruge standard HTML-tags til at formatere tekst, tilføje linjeskift, oprette links og anvende farver. Dette er særligt nyttigt til note-felter, sektionsinstruktioner og dynamiske opsummeringer.

{{% alert icon=" " context="warning" %}}
HTML i labels gengives på **webformularen** og rtSurvey-mobilapps. Det gengives muligvis ikke i alle ODK-kompatible klienter. Test altid på din målplatform.
{{% /alert %}}

---

## Understøttede HTML-tags

### Tekstformatering

| Tag | Resultat |
|-----|---------|
| `<strong>tekst</strong>` eller `<b>tekst</b>` | **Fed tekst** |
| `<em>tekst</em>` eller `<i>tekst</i>` | *Kursiv tekst* |
| `<u>tekst</u>` | Understreget tekst |
| `<br>` | Linjeskift |
| `<span style="...">tekst</span>` | Inline-styling |

### Links

```html
<a href="https://example.com" target="_blank">Klik her</a>
```

Åbnes i en ny fane. Brug til referencedokumenter, retningslinjer eller eksterne ressourcer, som intervieweren bør konsultere.

### Farver

Brug `<span>` med inline-styles:

```html
<span style="color: red;">Advarsel: værdien er uden for intervallet</span>
<span style="color: #009688;">Sektionen er gennemført</span>
```

---

## Farvemetavariabler

rtSurvey understøtter **farvemetavariable**, der tilpasser sig appens konfigurerede tema. Brug syntaksen `__FARVE_TEMA_NAVN__`:

```html
<span style="color: var(--color-theme-primary);">Primær farvetekst</span>
```

Eller ved brug af token-forkortelsen i labelteksten:

```
<font color="var(--COLOR_THEME_PRIMARY)">Vigtig note</font>
```

Dette konverteres automatisk til den tilsvarende `<span>` med en CSS-variabel ved gengivelsestidspunktet.

---

## Flersprogede labels

Omslut indhold i sprogtags for at understøtte flere sprog i én labelcelle:

```
<en>Enter the household size</en><vi>Nhập quy mô hộ gia đình</vi>
```

rtSurvey udtrækker indholdet, der matcher det aktuelle appsprog. Hvis intet matchende sprogtag findes, vises den fulde streng som den er.

---

## Eksempler i note-felter

### Sektionsinstruktion med fed skrift og linjeskift

| type | name | label |
|------|------|-------|
| note | section_intro | `<strong>Sektion 3: Arealanvendelse</strong><br>Stil alle spørgsmål i denne sektion kun til husstandsoverhoveder.` |

### Dynamisk opsummering med beregnede referencer

| type | name | label |
|------|------|-------|
| calculate | total | | `${adults} + ${children}` |
| note | summary | `Samlede husholdningsmedlemmer: <strong>${total}</strong><br><span style="color: gray;">Voksne: ${adults} · Børn: ${children}</span>` |

### Advarsel i rødt

| type | name | label | relevant |
|------|------|-------|----------|
| note | age_warning | `<span style="color: red;"><strong>Advarsel:</strong> Indtastet alder (${age}) er usædvanligt høj. Venligst verificer.</span>` | `${age} > 100` |

### Link til et referencedokument

| type | name | label |
|------|------|-------|
| note | guidelines_link | `Se <a href="https://docs.example.com/guidelines" target="_blank">Feltretningslinjerne</a>, inden du starter denne sektion.` |

---

## Specielle rtSurvey HTML-tags

### `<webbox src='url' title='titel'>...</webbox>`

Indlejrer en knap, der åbner en URL i en modal-dialog inden for formularen. Se [Webbox](webbox) for fulde detaljer.

### `<delete-repeat-current>label</delete-repeat-current>`

Gengiver en knap inde i en gentagelsesgruppe, der sletter den aktuelle gentagelsesinstans, når der trykkes på den.

### `<delete-repeat-last>label</delete-repeat-last>`

Gengiver en knap, der sletter den sidste gentagelsesinstans.

Eksempel på brug i en gentagelsesgruppe:

| type | name | label |
|------|------|-------|
| note | delete_btn | `<delete-repeat-current>Fjern dette medlem</delete-repeat-current>` |

---

## Bedste praksis

1. Brug HTML sparsomt — overformaterede labels er sværere at læse, ikke lettere.
2. Foretrække `<strong>` til fed skrift og `<em>` til kursiv frem for de forældede `<b>` og `<i>`.
3. Hold farvebrugen meningsfuld — brug rødt til advarsler, ikke til dekoration.
4. Test altid HTML-gengivelse på både mobilapp og webformular, da gengivelsen kan afvige en smule.
5. Undgå `<table>`-tags inde i labels — de gengives sjældent godt på mobilskærme.
6. Brug ikke JavaScript (`<script>`) — det fjernes eller forårsager fejl.

## Begrænsninger

- Kompleks HTML (tabeller, formularer, scripts) understøttes ikke og kan ødelægge gengivelsen.
- Nogle ældre mobilklienter kan vise HTML-tags som bogstavelig tekst — test på alle målenheder.
- `<a>`-links åbnes i en browser eller WebView — intervieweren forlader formularen, hvilket kan være forstyrrende på mobil.
