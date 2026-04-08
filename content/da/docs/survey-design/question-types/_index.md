---
title: "Spørgsmålstyper"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey understøtter alle standard XLSForm-spørgsmålstyper samt adskillige udvidelser. Hver spørgsmålstype styrer, hvilken slags data der indsamles, og hvordan inputwidgetten gengives på enheden.

For at angive spørgsmålstypen skal du skrive typenavnet i kolonnen `type` i regnearket **survey** i din XLSForm.

## Tekstinput

| Type | Beskrivelse |
|------|-------------|
| [text](text) | Fritekstsvar — alle tegn tilladt |
| [integer](integer) | Heltal (ingen decimaler) |
| [decimal](decimal) | Tal med decimaler |
| [range](range) | Tal valgt fra en skyder inden for et defineret min./maks.-interval |

## Valg

| Type | Beskrivelse |
|------|-------------|
| [select_one listenavn](select-one) | Vælg præcis én mulighed fra en liste |
| [select_multiple listenavn](select-multiple) | Vælg en eller flere muligheder fra en liste |
| [rank listenavn](rank) | Ordner valgmuligheder efter præference eller prioritet |

## Dato og tid

| Type | Beskrivelse |
|------|-------------|
| [date](date) | Kalenderdato (år, måned, dag) |
| [time](time) | Tidspunkt (timer, minutter) |
| [datetime](datetime-date-time) | Kombineret dato og tid |

## Placering

| Type | Beskrivelse |
|------|-------------|
| [geopoint](geopoint) | Enkelt GPS-koordinat (breddegrad, længdegrad, højde, nøjagtighed) |
| [geotrace](geotrace) | En sti — serie af GPS-punkter, der danner en linje |
| [geoshape](geoshape) | Et område — lukket polygon af GPS-punkter |

## Medier

| Type | Beskrivelse |
|------|-------------|
| [image](image) | Fotooptagelse eller billedupload |
| [audio](audio) | Lydoptagelse |
| [video](video) | Videooptagelse |
| [file](file) | Generel filopload (PDF, dokument osv.) |

## Andet

| Type | Beskrivelse |
|------|-------------|
| [barcode](barcode) | Scan en stregkode eller QR-kode |
| [note](note) | Skrivebeskyttet visningstekst — viser instruktioner eller beregnede opsummeringer |
| [calculate](calculate) | Skjult felt, der gemmer en beregnet værdi |
| [hidden](hidden) | Skjult felt, der gemmer en statisk eller forudfyldt værdi |
| [trigger / acknowledge](trigger) | Et afkrydsningsfelt, intervieweren skal markere for at bekræfte, at de har læst en erklæring |
| [meta](meta) | Automatiske metadata: tidsstempler, enheds-ID, interviewerinfo |

## rtSurvey-udvidelser

Disse typer er rtSurvey-specifikke og ikke en del af standard XLSForm-specifikationen.

| Type | Beskrivelse |
|------|-------------|
| [search-autocomplete](search-autocomplete) | Tekstinput med realtids API-baserede autoudfyldningsforslag |
| [mentions](mentions) | Tekstfelt med `@`-omtale-autoudfyldning til at tagge enheder inline |
| [texttags](texttags) | Tag-inputfelt — hver indtastning bliver en chip, der kan fjernes; gemt som mellemrumssepareret streng |

For gentagelsesgrupper, se [Repeats](../advanced-extension/repeats)

## Sådan arbejder type og appearance sammen

`type` bestemmer **hvilke data der indsamles**. Kolonnen `appearance` styrer **hvordan widgetten ser ud**. Mange typer understøtter flere appearances — f.eks. kan `select_one` vises som radioknapper, en rullemenu, en Likert-skala eller et kompakt grid.

Se [Appearance](../appearance) for den fulde liste over muligheder.
