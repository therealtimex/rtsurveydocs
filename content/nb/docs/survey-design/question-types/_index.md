---
title: "Spørsmålstyper"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey støtter alle standard XLSForm-spørsmålstyper, pluss flere utvidelser. Hver spørsmålstype kontrollerer hvilken type data som samles inn og hvordan inndatawidgeten gjengis på enheten.

For å angi spørsmålstypen, skriv inn typenavnet i `type`-kolonnen i **survey**-regnearket i XLSForm.

## Tekstinndata

| Type | Beskrivelse |
|------|-------------|
| [text](text) | Fritekstsvar — alle tegn er tillatt |
| [integer](integer) | Heltall (ingen desimaler) |
| [decimal](decimal) | Tall med desimaler |
| [range](range) | Tall valgt fra en glidebryter innenfor et definert min/maks-område |

## Valg

| Type | Beskrivelse |
|------|-------------|
| [select_one listenavn](select-one) | Velg nøyaktig ett alternativ fra en liste |
| [select_multiple listenavn](select-multiple) | Velg ett eller flere alternativer fra en liste |
| [select_one_from_file filnavn](select-one-from-file) | Velg ett alternativ lastet fra en ekstern CSV-fil |
| [rank listenavn](rank) | Ranger valg etter preferanse eller prioritet |

## Dato og klokkeslett

| Type | Beskrivelse |
|------|-------------|
| [date](date) | Kalenderdata (år, måned, dag) |
| [time](time) | Klokkeslett (timer, minutter) |
| [datetime](datetime-date-time) | Kombinert dato og klokkeslett |

## Plassering

| Type | Beskrivelse |
|------|-------------|
| [geopoint](geopoint) | Enkelt GPS-koordinat (breddegrad, lengdegrad, høyde, nøyaktighet) |
| [geotrace](geotrace) | En sti — serie med GPS-punkter som danner en linje |
| [geoshape](geoshape) | Et område — lukket polygon av GPS-punkter |

## Medier

| Type | Beskrivelse |
|------|-------------|
| [image](image) | Bildeopptak eller bildeopplasting |
| [audio](audio) | Lydopptak |
| [video](video) | Videoopptak |
| [file](file) | Generell filopplasting (PDF, dokument, osv.) |

## Annet

| Type | Beskrivelse |
|------|-------------|
| [barcode](barcode) | Skann en strekkode eller QR-kode |
| [note](note) | Skrivebeskyttet visingstekst — viser instruksjoner eller beregnede sammendrag |
| [calculate](calculate) | Skjult felt som lagrer en beregnet verdi |
| [hidden](hidden) | Skjult felt som lagrer en statisk eller forhåndsutfylt verdi |
| [trigger / acknowledge](trigger) | En avkrysningsboks som telleren må huke av for å bekrefte at de har lest en uttalelse |
| [meta](meta) | Automatiske metadata: tidsstempler, enhets-ID, tellerinformasjon |

## Hvordan type og utseende fungerer sammen

`type` bestemmer **hvilke data som samles inn**. `appearance`-kolonnen kontrollerer **hvordan widgeten ser ut**. Mange typer støtter flere utseender — for eksempel kan `select_one` vises som radioknapper, en nedtrekksmeny, en Likert-skala eller et kompakt grid.

Se [Utseende](../appearance) for hele listen over alternativer.
