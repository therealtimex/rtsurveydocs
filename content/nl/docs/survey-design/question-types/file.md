---
title: "Bestand"
description: "Bestandsvragen staan respondenten toe documenten en andere bestanden te uploaden als onderdeel van hun enquêteresponsen."
icon: "upload_file"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 230
---

Het vraagtype `file` stelt respondenten in staat **elk bestand te uploaden** van hun apparaat — documenten, spreadsheets, PDF's of andere bestandstypen. In tegenstelling tot `image`, `audio` en `video` die specifieke vastleggingstools starten, opent `file` een algemene bestandspicker.

## Basis XLSForm-specificatie

| type | name      | label                        |
|------|-----------|------------------------------|
| file | document  | Upload uw document           |

## Toepassingen

Bestandsvragen worden veelgebruikt voor:

1. Ondersteunende documenten verzamelen (bonnen, certificaten, contracten, rapporten)
2. Ingescande papieren formulieren uploaden
3. Spreadsheets of gegevensexports uit andere systemen verzamelen
4. Elk digitaal bestandstype dat afbeelding/audio/video niet dekt

## rtSurvey-uitbreidingen

### Geaccepteerde bestandstypen

Gebruik de kolom `parameters` om te beperken welke bestandstypen kunnen worden geselecteerd:

| type | name | label | parameters |
|------|------|-------|------------|
| file | report | Upload het inspectierapport | `accept=.pdf` |
| file | spreadsheet | Upload het gegevensbestand | `accept=.xlsx,.csv` |

## Aanbevolen werkwijzen

1. Gebruik `accept` om bestandstypen te beperken — dit voorkomt dat enumeratoren per ongeluk verkeerde bestanden uploaden.
2. Neem altijd richtlijnen voor grootte en formaat op in de kolom `hint`.
3. Gebruik voor foto's en afbeeldingen het type `image` — dit biedt betere compressie en consistente formaatverwerking.

## Beperkingen

- Bestandsvragen valideren de bestandsinhoud niet — alleen de bestandsextensiecontrole via `accept` wordt afgedwongen op UI-niveau.
- Zeer grote bestanden (100 MB+) kunnen time-outen bij het uploaden in omgevingen met lage connectiviteit.
- Offline enumeratoren kunnen bestanden bijvoegen maar ze worden pas geüpload wanneer de connectiviteit wordt hersteld.
