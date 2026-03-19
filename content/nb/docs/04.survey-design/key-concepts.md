---
title: "Nøkkelbegreper"
description: "Oversikt over skjemadesign"
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 210
---

## Hva er et XLSForm?
rtSurvey bruker en utvidet versjon av [XLSForm](https://xlsform.org/)-standarden for skjemadesign, og tilbyr kraftige funksjoner for å lage avanserte spørreundersøkelser. Denne veiledningen introduserer deg til nøkkelbegrepene i skjemadesign i rtSurvey, fra grunnleggende XLSForm-struktur til avanserte rtSurvey-spesifikke funksjoner.

Med XLSForm kan du lage skjemaer i et menneskevennlig format ved hjelp av det kjente Excel-verktøyet, noe som gjør det tilgjengelig for nesten alle.
Denne standarden gjør det enkelt å dele og samarbeide om skjemautforming.

Selv om XLSForm er brukervennlig for nybegynnere, lar den også erfarne brukere lage komplekse skjemaer.

rtSurvey gir en konsekvent måte å inkorporere avanserte funksjoner som hopplogikk i skjemaer på tvers av ulike nett- og mobilbaserte datainnsamlingsplattformer.

## XLSForm-struktur
Et XLSForm består vanligvis av to hovedregneark:

1. **survey**: Definerer strukturen og innholdet i skjemaet.
2. **choices**: Angir svaralternativer for flervalgsspørsmål.

Et valgfritt **settings**-regneark kan gi ytterligere skjemaspesifikasjoner.

Det er viktig å merke seg at de obligatoriske kolonnene i survey- og choices-regnearket må være til stede for at skjemaet skal fungere riktig. Valgfrie kolonner i begge regneark gir ytterligere kontroll over oppførselen til hvert element i skjemaet, men er ikke nødvendige.

Kolonnene i Excel-arbeidsboken kan vises i hvilken som helst rekkefølge, og valgfrie kolonner kan stå tomme. Det er imidlertid avgjørende å bruke den nøyaktige syntaksen og navnekonvensjonene som er spesifisert i XLSForm-dokumentasjonen for at skjemaet skal fungere korrekt.

### Survey-regnearket
**Survey-regnearket** er der du definerer strukturen til skjemaet og gir innholdet. Hver rad i survey-regnearket representerer et spørsmål eller element i skjemaet. Følgende kolonner er obligatoriske i survey-regnearket:

- `type`: Angir hvilken type inndata som forventes for spørsmålet.
- `name`: Angir det unike variabelnavnet for innlegget. Navn må starte med en bokstav eller understrek og kan bare inneholde bokstaver, sifre, bindestreker, understrek og punktum. Navn skiller mellom store og små bokstaver.
- `label`: Inneholder den faktiske teksten du ser for spørsmålet i skjemaet.

| type                | name     | label                |
| ------------------- | -------- | -------------------- |
| today               | today    |                      |
| select_one gender   | gender   | Respondentens kjønn? |
| integer             | age      | Respondentens alder? |

### Choices-regnearket
**`choices`**-regnearket brukes til å angi svaralternativer for flervalgsspørsmål.
Hver rad representerer et svaralternativ. Følgende kolonner er obligatoriske i choices-regnearket:

- **`list_name`**: Grupperer et sett med relaterte svaralternativer.
- **`name`**: Angir det unike variabelnavnet for svaralternativet.
- **`label`**: Viser svaralternativet nøyaktig slik du vil at det skal vises på skjemaet.

| list_name           | name        | label                |
| ------------------- | ----------- | -------------------- |
| gender              | transgender | Transperson          |
| gender              | female      | Kvinne               |
| gender              | male        | Mann                 |
| gender              | other       | Annet                |

Kolonnene du legger til i Excel-arbeidsboken, enten de er obligatoriske eller valgfrie, kan vises i hvilken som helst rekkefølge. Valgfrie kolonner kan utelates helt. Rader eller kolonner kan stå tomme for bedre lesbarhet, men data etter 20 tilstøtende tomme kolonner eller rader på et ark vil ikke bli behandlet. All .xlsx-formatering ignoreres, så du kan bruke skillelinjer, skyggelegging og annen skriftformatering for å gjøre skjemaet mer lesbart.

En ting å huske på når du lager skjemaer i Excel, er at syntaksen du bruker må være presis. Hvis du for eksempel skriver **Choices** eller **choice** i stedet for **choices**, vil ikke skjemaet fungere.

### Settings-regnearket

Settings-regnearket er valgfritt, men lar deg angi metadata og adferd på skjemanivå. Vanlige kolonner i settings-regnearket inkluderer:

| Kolonne | Beskrivelse |
|---------|-------------|
| form_title | Tittelen på skjemaet slik den vises for brukere |
| form_id | En unik identifikator for skjemaet, brukt i databehandling og API-kall |
| default_language | Standard språkkode for flerspråklige skjemaer (f.eks. 'en' for engelsk) |
| version | Versjonsnummeret til skjemaet, nyttig for å spore endringer |
| instance_name | Uttrykk for å generere et unikt navn for hvert skjemainnsendelse |
| generation | Heltall som markerer generasjonen til skjemaet. Inkrementer for strukturelle endringer |
| family | Identifikator for å gruppere relaterte skjemaer på tvers av strukturelle endringer |

Settings-regnearket i rtSurvey kan også inneholde ytterligere konfigurasjoner spesifikke for rtSurveys utvidede funksjoner. Se rtSurvey-dokumentasjonen for en fullstendig liste over støttede innstillinger.

## Nøkkelkomponenter i survey-regnearket

Survey-regnearket er kjernen i skjemadesignet. Her er en oversikt over nøkkelkomponentene:

| Komponent | Beskrivelse |
|-----------|-------------|
| [type](#spørsmålstyper) | Angir spørsmålstypen (f.eks. text, integer, select_one) |
| [name](#navnekonvensjoner) | Unik identifikator for spørsmålet |
| [label](#etiketter-og-oversettelser) | Teksten som vises for respondenten |
| [hint](#hint-og-hjelpetekst) | Ytterligere veiledning for respondenten |
| [appearance](#utseendealternativer) | Endrer hvordan spørsmålet vises |
| [relevant](#relevans-og-hopplogikk) | Bestemmer når spørsmålet skal stilles (hopplogikk) |
| [constraint](#begrensninger-og-validering) | Validerer svaret |
| [calculation](#beregninger) | Beregner verdier basert på andre svar |
| [required](#obligatoriske-felt) | Angir om spørsmålet må besvares |

### Spørsmålstyper
XLSForm støtter en rekke spørsmålstyper. Her er noen av alternativene du kan legge inn i **`type`**-kolonnen i **`survey`**-regnearket i XLSForm:

| Spørsmålstype             | Inndata                                                                                 |
| ------------------------- | --------------------------------------------------------------------------------------- |
| integer                   | Heltall (dvs. et helt tall) inndata.                                                    |
| decimal                   | Desimaltall inndata.                                                                    |
| range                     | [Område](#område) inndata (inkludert vurdering)                                         |
| text                      | Fritekstsvar.                                                                           |
| select_one [options]      | [Flervalgsspørsmål](#flervalg); bare ett svar kan velges.                               |
| select_multiple [options] | [Flervalgsspørsmål](#flervalg); flere svar kan velges.                                  |
| select_one_from_file [file]| [Flervalg fra fil](#flervalg-fra-fil); bare ett svar kan velges.                       |
| select_multiple_from_file [file]| [Flervalg fra fil](#flervalg-fra-fil); flere svar kan velges.                    |
| rank [options]            | [Rangering](#rangering); ranger en liste.                                               |
| note                      | Vis en merknad på skjermen, tar ingen inndata.                                          |
| geopoint                  | Samle inn ett [GPS-koordinat](#gps).                                                    |
| geotrace                  | Registrer en [linje av to eller flere GPS-koordinater](#gps).                           |
| geoshape                  | Registrer et [polygon av flere GPS-koordinater](#gps); siste punkt er det samme som det første. |
| date                      | Datoinput.                                                                              |
| time                      | Klokkeslettinput.                                                                       |
| dateTime                  | Aksepterer både dato og klokkeslettinput.                                               |
| image                     | Ta et bilde eller last opp en [bildefil](#bilde).                                       |
| audio                     | Ta opp lyd eller last opp en lydfil.                                                    |
| background-audio          | Lyd tas opp i bakgrunnen mens skjemaet fylles ut.                                       |
| video                     | Ta opp video eller last opp en videofil.                                                |
| file                      | Generell filinput (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                           |
| barcode                   | Skann en strekkode, krever at strekkodeskanner-appen er installert.                     |
| calculate                 | Utfør en beregning; se [Beregning](#beregning)-avsnittet nedenfor.                     |
| acknowledge               | Bekreftelsesprompt som setter verdien til "OK" hvis valgt.                              |
| hidden                    | Et felt uten tilknyttet UI-element som kan brukes til å lagre en konstant               |
| xml-external              | Legger til en referanse til en [ekstern XML-datafil](#ekstern-xml-data)                 |

### Etiketter

Etiketter er teksten som vises for respondentene for hvert spørsmål. De er avgjørende for tydelig kommunikasjon i spørreundersøkelser.

- **Grunnleggende bruk**: I `label`-kolonnen skriver du inn spørsmålsteksten.
- **Flere språk**: Bruk tilleggskolonner som `label::English` og `label::French` for flerspråklige spørreundersøkelser.
- **Formatering**: rtSurvey støtter grunnleggende HTML-formatering i etiketter for vektlegging eller struktur.

### Hint

Hint gir ytterligere veiledning til respondentene uten å rote til den primære spørsmålsteksten.

- **Bruk**: Legg til hint i `hint`-kolonnen.
- **Synlighet**: Hint vises vanligvis under den primære spørsmålsteksten.
- **Flerspråklig**: I likhet med etiketter kan hint angis for flere språk ved hjelp av `hint::Språk`-kolonner.

### Utseende

`appearance`-kolonnen i rtSurvey tillater tilpasning av hvordan spørsmål vises.

- **Standardalternativer**: Inkluderer 'multiline' for tekst, 'horizontal' for select-spørsmål.
- **rtSurvey-utvidelser**:
  - Tidsinput: Ulike klokkevalgalternativer (f.eks. `inline`, `inline-1line`)
  - Fargetilpasning: Bruk `colors()`-funksjonen for å endre ikonfargene

### Relevant

`relevant`-kolonnen implementerer hopplogikk og bestemmer når et spørsmål skal vises.

- **Syntaks**: Bruk XPath-uttrykk for å definere betingelser.
- **Variabler**: Referer til andre spørsmålsnavn med `${spørsmålsnavn}`.

### Required

`required`-kolonnen angir om et spørsmål må besvares.

- **Grunnleggende bruk**: Bruk 'yes' eller 'true' for å gjøre et spørsmål obligatorisk.
- **Avansert**: Kan bruke uttrykk for betinget krav.

### Repeats

Repeats lar en gruppe spørsmål besvares flere ganger.

- **Bruk**: Bruk `begin repeat`- og `end repeat`-rader for å definere en gjentakende gruppe.
- **Navngiving**: Gi hver gjentakingsgruppe et unikt navn.

### Media

rtSurvey støtter ulike medietyper i spørreundersøkelser, inkludert bilder, lyd og video.

- **Spørsmålstyper**: Bruk 'image', 'audio' eller 'video' i type-kolonnen.
- **Media i etiketter**: Referer til mediefiler i etiketter ved hjelp av HTML-koder.

### Read-only

Read-only-spørsmål viser informasjon uten å tillate brukerinput.

- **Bruk**: Legg til 'readonly' i `appearance`-kolonnen.
- **Beregninger**: Brukes ofte med calculate-type for å vise beregnede verdier.

## rtSurvey-utvidelser

rtSurvey utvider XLSForm-standarden ved å støtte ytterligere funksjoner som `grid layout`, `html format` og mange nye `widgets`.

### Grid layout
rtSurvey lar skjemaet ditt etterligne utseendet til tradisjonelle papirspørreundersøkelser ved å komprimere flere spørsmål i én rad.

### Skjemainnstillinger

### Datainnstillinger

### Typeform-stil

### Utvidelse av pulldata()

### Utseendebaserte utvidelser

### Webbox-utvidelser
