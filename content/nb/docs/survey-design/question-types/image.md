---
title: "Bilde"
description: "Bildespørsmål lar respondenter ta og sende inn bilder som en del av spørreundersøkelsen."
icon: "image"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 227
---

Bildespørsmålstypen i XLSForm og rtSurvey lar respondenter ta og sende inn bilder som en del av spørreundersøkelsessvaret. Denne funksjonen er særlig nyttig for innsamling av visuelle data, dokumentering av observasjoner eller innhenting av bevis i feltundersøkelser.

## Grunnleggende XLSForm-spesifikasjon

| type  | name        | label                           |
|-------|-------------|--------------------------------|
| image | photo       | Ta et bilde av stedet           |

## Brukstilfeller

Bildespørsmål brukes vanligvis for:

1. Dokumentere feltforhold eller observasjoner
2. Registrere visuelt bevis i forskningsstudier
3. Samle inn før-og-etter-bilder i konsekvensanalyser
4. Verifisere fullføring av oppgaver eller tilstedeværelse på steder
5. Samle inn visuelle data for ekstern analyse

## Beste praksis

1. Gi klare instruksjoner om hva som skal fotograferes.
2. Vurder personvernimplikasjoner og informer respondentene om hvordan bildene vil bli brukt.
3. Vær oppmerksom på filstørrelser og lagringsbegrensninger, spesielt for undersøkelser i områder med begrenset internettilkobling.
4. Sørg for at enheten har tilstrekkelig lagringsplass og at kameratillatelser er gitt.

## Eksempelbruk

| type  | name           | label                                      | hint                                        |
|-------|----------------|--------------------------------------------|--------------------------------------------|
| image | storefront     | Ta et bilde av butikkens inngang           | Sørg for at butikknavnet er tydelig synlig  |

## rtSurvey-utvidelser

rtSurvey kan tilby ytterligere funksjoner eller tilpasninger:

1. Bildekvalitetsinnstillinger (f.eks. lav, middels, høy oppløsning)
2. Mulighet til å legge til bildetekster eller koder til bilder
3. Integrasjon med enhetens native kameraapp eller galleri

For avansert vannmerking av bilder og mediagrid-widget, se [Avanserte bilder](../advanced-extension/images).

## Datahåndtering

Bilder samlet inn gjennom denne spørsmålstypen er vanligvis:

1. Lagret i et vanlig bildeformat (f.eks. JPG, PNG)
2. Lagret ved siden av andre spørreundersøkelsesdata, ofte i en separat mediemappe
3. Tilgjengelig for visning og analyse via spørreundersøkelsesstyringsplattformen

## Begrensninger

- Bildefiler kan være store, noe som kan påvirke dataoverføring og lagring.
- Ikke alle enheter kan ha høykvalitetskamera eller tilstrekkelig lagringsplass.
- Å analysere store mengder bilder kan være tidkrevende.
- Det kan være personvernbekymringer ved bildetaking, spesielt på offentlige steder.

## rtSurvey bildeudvidelser

### watermark()

`watermark()`-utseendet legger et tekstvannmerke over bilder tatt med dette feltet. Vannmerket inneholder vanligvis metadata som teller-navn, dato/tid eller GPS-koordinater, stemplet direkte på bildet før det lagres.

| type | name | label | appearance |
|------|------|-------|------------|
| image | site_photo | Ta et bilde av stedet | `watermark("${enumerator_id} ${today()}")` |

Argumentet til `watermark()` er et XPath-uttrykk som evalueres ved opptakstidspunktet. Den resulterende strengen gjengis som vannmerketekst.

### editable

`editable`-utseendet lar respondenten kommentere eller tegne på det tatte bildet etter å ha tatt det. En tegningsverktøylinje vises over bildet.

| type | name | label | appearance |
|------|------|-------|------------|
| image | annotated_photo | Fotografer og merk bekymringsområder | editable |

{{% alert icon=" " context="info" %}}
`editable` kan kombineres med `watermark()`: `appearance: editable watermark("${id}")`
{{% /alert %}}
