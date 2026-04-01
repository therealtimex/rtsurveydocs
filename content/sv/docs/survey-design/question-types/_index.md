---
title: "Frågtyper"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 220
---

rtSurvey stöder alla standardfrågtyper i XLSForm plus flera tillägg. Varje frågtyp styr vilken typ av data som samlas in och hur inmatningswidgeten renderas på enheten.

För att ange frågtypen anger du typnamnet i kolumnen `type` i kalkylbladet **survey** i ditt XLSForm.

## Textinmatning

| Typ | Beskrivning |
|-----|-------------|
| [text](text) | Fritextsvar — alla tecken tillåtna |
| [integer](integer) | Heltal (inga decimaler) |
| [decimal](decimal) | Tal med decimaler |
| [range](range) | Tal valt från en reglage inom ett definierat min/max-intervall |

## Urval

| Typ | Beskrivning |
|-----|-------------|
| [select_one listname](select-one) | Välj exakt ett alternativ från en lista |
| [select_multiple listname](select-multiple) | Välj ett eller flera alternativ från en lista |
| [select_one_from_file filename](select-one-from-file) | Välj ett alternativ laddat från en extern CSV-fil |
| [rank listname](rank) | Rangordna alternativ efter preferens eller prioritet |

## Datum och tid

| Typ | Beskrivning |
|-----|-------------|
| [date](date) | Kalenderdatum (år, månad, dag) |
| [time](time) | Tid på dygnet (timmar, minuter) |
| [datetime](datetime-date-time) | Kombinerat datum och tid |

## Plats

| Typ | Beskrivning |
|-----|-------------|
| [geopoint](geopoint) | Enskild GPS-koordinat (latitud, longitud, altitud, noggrannhet) |
| [geotrace](geotrace) | En väg — serie GPS-punkter som bildar en linje |
| [geoshape](geoshape) | Ett område — sluten polygon av GPS-punkter |

## Media

| Typ | Beskrivning |
|-----|-------------|
| [image](image) | Fototagning eller bilduppladdning |
| [audio](audio) | Ljudinspelning |
| [video](video) | Videoinspelning |
| [file](file) | Allmän filuppladdning (PDF, dokument osv.) |

## Övrigt

| Typ | Beskrivning |
|-----|-------------|
| [barcode](barcode) | Skanna en streckkod eller QR-kod |
| [note](note) | Skrivskyddad visningstext — visar instruktioner eller beräknade sammanfattningar |
| [calculate](calculate) | Dolt fält som lagrar ett beräknat värde |
| [hidden](hidden) | Dolt fält som lagrar ett statiskt eller förhandsifyllt värde |
| [trigger / acknowledge](trigger) | En kryssruta som räknaren måste bocka för att bekräfta att de läst ett påstående |
| [meta](meta) | Automatiska metadata: tidsstämplar, enhets-ID, räknarinformation |

## Hur typ och utseende fungerar tillsammans

`type` bestämmer **vilka data som samlas in**. Kolumnen `appearance` styr **hur widgeten ser ut**. Många typer stöder flera utseenden — till exempel kan `select_one` visas som radioknappar, en rullgardinsmeny, en Likert-skala eller ett kompakt rutnät.

Se [Utseende](../appearance) för den fullständiga listan med alternativ.
