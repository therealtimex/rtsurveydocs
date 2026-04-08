---
title: "Utseende"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 288
---

Kolumnen `appearance` i rtSurvey låter dig anpassa den visuella presentationen och beteendet hos frågor i dina undersökningar. Denna funktion förbättrar användarupplevelsen och kan avsevärt förbättra datainsamlingseffektiviteten. rtSurvey stöder standard XLSForm-utseendeattribut och utökar dem med ytterligare alternativ.

## Standard XLSForm-utseendeattribut

rtSurvey stöder följande standard XLSForm-utseendeattribut:

| Utseendeattribut | Frågetyper | Beskrivning |
|----------------------|----------------|-------------|
| multiline | text | Skapar en flerradig textruta (bäst för webbklienter) |
| minimal | select_one, select_multiple | Visar alternativ i en rullgardinsmeny |
| quick | select_one | Avancerar automatiskt till nästa fråga efter val (endast mobil) |
| no-calendar | date | Undertrycker kalendervisningen (endast mobil) |
| month-year | date | Tillåter val av månad och år endast |
| year | date | Tillåter val av år endast |
| horizontal-compact | select_one, select_multiple | Visar alternativ horisontellt (endast webb) |
| horizontal | select_one, select_multiple | Visar alternativ horisontellt i kolumner (endast webb) |
| likert | select_one | Presenterar alternativ som en Likert-skala |
| compact | select_one, select_multiple | Visar alternativ sida vid sida med minimal utfyllnad |
| quickcompact | select_one | Kombinerar kompakt visning med automatisk avancering (endast mobil) |
| field-list | grupper | Visar hela gruppen på en skärm (endast mobil) |
| label | select_one, select_multiple | Visar alternativens etiketter utan inmatning |
| list-nolabel | select_one, select_multiple | Visar inmatning utan etiketter (används med `label`) |
| table-list | grupper | Visar frågor i tabellformat |
| signature | image | Aktiverar signaturfångst (endast mobil) |
| draw | image | Tillåter frihandsteckning (endast mobil) |
| map, quick map | select_one, select_one_from_file | Aktiverar val från kartfunktioner |

## Bästa praxis för att använda utseende

1. **Konsekvens**: Använd utseendeattribut konsekvent i hela din undersökning för ett enhetligt utseende.
2. **Mobil kontra webb**: Tänk på hur utseenden renderas på olika enheter och plattformar.
3. **Prestanda**: Var försiktig med utseendeattribut som kan sakta ned formulärladdning (t.ex. `table-list` för stora grupper).
4. **Användarupplevelse**: Välj utseenden som gör datainmatning enklare och mer intuitiv för respondenter.
5. **Testning**: Testa alltid ditt formulär på målenheter för att säkerställa att utseenden fungerar som förväntat.

## rtSurvey Utökade utseendeattribut

Förutom standard XLSForm-utseenden stöder rtSurvey följande plattformsspecifika alternativ:

### Data- och visningskontroll

| Utseendeattribut | Frågetyper | Beskrivning |
|----------------------|----------------|-------------|
| `invisible` | valfri | Döljer fältet från visning samtidigt som det fortfarande samlar in eller beräknar sitt värde. |
| `displaytitle` | valfri | Tvingar visning av fältets etikett/titel. |
| `autopull` | select_one, select_multiple | Hämtar automatiskt externa data för att fylla i alternativ när formuläret laddas. |
| `floating_hint` | text, integer, decimal | Visar tipstext som en flytande etikett ovanför inmatningsfältet. |
| `calculate-button` | calculate | Lägger till en synlig knapp som utlöser omberäkning av fältet på begäran. |

### Layout

| Utseendeattribut | Frågetyper | Beskrivning |
|----------------------|----------------|-------------|
| `1screen` | grupp | Tvingar hela gruppen att visas på en enda skärm. |
| `columns(n)` | select_one, select_multiple | Visar alternativ i `n` kolumner. Exempel: `columns(3)` visar tre kolumner med radioknappar. |
| `gridformat<row=R col=C colspan=S align=center>` | valfri | Placerar fältet i en CSS-rutnätslayout. |
| `ignore-simplify` | valfri | Instruerar formulärrenderaren att hoppa över automatisk förenkling av fältets layout. |
| `required-but-simplify` | valfri | Fältet är obligatoriskt men dess layout förenklas ändå av renderaren (åsidosätter standardbeteendet där obligatoriska fält undantas från förenkling). |
| `embed` | valfri | Renderar fältet i inbäddat/inline-visningsläge, undertrycker den yttre omslutaren och etikettcontainern — används när en fråga är inbäddad i anpassad HTML. |
| `popup` | select_one, select_multiple | Renderar valslistan i ett popup/modal-överlägg istället för inline. |
| `auto-hide-empty` | boxtag, select | Döljer hela frågewidgeten när valslistan är tom (t.ex. inga API-resultat returnerades). |
| `text-nolabel` | select_one, select_multiple | Döljer textetiketten för varje alternativ och visar bara inmatningskontrollen. Liknande `list-nolabel` men appliceras per alternativ snarare än som kolumndelning. |

### Widgetar

| Utseendeattribut | Frågetyper | Beskrivning |
|----------------------|----------------|-------------|
| `likert` | select_one | Presenterar alternativ som en Likert-skalarad. |
| `distress` | select_one | Renderar alternativ som den psykologiska stressskalans (K10) visuella widget med emotionella ikoner. |

### Visuella select-widgetar

Dessa utseenden ändrar hela renderingen av select-valslistor.

| Utseendeattribut | Frågetyper | Beskrivning |
|----------------------|----------------|-------------|
| `tagging` | select_one, select_multiple | Alternativ renderas som pillformade klickbara taggchips. |
| `boxtag` | select_one, select_multiple | Alternativ renderas som rektangulära stiliserade rutor som användaren trycker på. |
| `boxtag -search` | select_one, select_multiple | Boxtag-layout med en live sök-/filterinmatning ovanför rutorna. |
| `duolingo-style1` | select_one, select_multiple | Stort kortlayout inspirerat av Duolingo — passar korta listor med ikoner. |
| `rating_box` | select_one, select_multiple | Rutnät av tryckvänliga numrerade rutor — passar skala- eller NPS-frågor. |
| `star_rating` | select_one | Alternativ renderas som stjärnor; antalet stjärnor är lika med antalet alternativ. |
| `choices-noshow` | select_one, select_multiple | Visar initialt bara de första 10 alternativen med en "Visa mer"-kontroll. |
| `noshow` | select_one, select_multiple | Döljer valslistan helt; värdet ställs in programmatiskt via `calculate` eller API. |
| `checkall` | select_multiple | Lägger till en "Välj alla"-genväg högst upp i valslistan. |
| `max-items(N)` | select_one, select_multiple | Begränsar den synliga valslistan till N objekt. Exempel: `max-items(5)`. |

### Visuella textwidgetar

| Utseendeattribut | Frågetyper | Beskrivning |
|----------------------|----------------|-------------|
| `richtext` | text | Ersätter det vanliga textfältet med en riktexteditor (fetstil, kursiv, listor, länkar). Lagrar HTML. |
| `typingtest` | text | Skrivtestwidget — etikettexten är passagen; widgetten registrerar det skrivna svaret och tidtagningen. |

### Mediatillägg

| Utseendeattribut | Frågetyper | Beskrivning |
|----------------------|----------------|-------------|
| `watermark("uttryck")` | image | Lägger ett textvattenmärke över tagna foton. Argumentet är ett XPath-uttryck som utvärderas vid tagningsstunden. Exempel: `watermark("${id} ${today()}")`. |
| `editable` | image | Möjliggör anteckning/ritning ovanpå det tagna fotot innan det sparas. |

### Inline visningskonfiguration

Modifikatorerna `display{}` och `results{}` kan läggas till `inline`-utseenden för att styra ikonjustering och resultatvisning. Dessa används tillsammans med `inline`-tidsinmatningsutökningen på `text`-fält och med medieupptagningswidgetar.

#### `display{}`-parametrar

```
inline display{left}
inline display{right,small}
inline display{top,large,inline-icon}
```

| Parameter | Värden | Beskrivning |
|-----------|--------|-------------|
| Justering | `left`, `right`, `top`, `bottom`, `center` | Position av ikonen relativt inmatningsfältet |
| Storlek | `small`, `medium`, `large` | Ikonstorlek (motsvarar 2,5 rem, 5 rem, 8 rem) |
| Läge | `inline-icon` | Renderar utlösaren som ikon enbart (ingen knappkant) |
| Läge | `inline-button` | Renderar utlösaren som en fullständig knapp |

#### `results{}`-parametrar

```
inline results{right}
inline results{left,hide(seconds)}
```

| Parameter | Värden | Beskrivning |
|-----------|--------|-------------|
| Justering | `left`, `right`, `top`, `bottom`, `center` | Position av resultatvärdesvisningen |
| `hide(fält)` | valfritt underfältsnamn | Döljer en specifik komponent av resultatet (t.ex. `hide(seconds)`) |

### API-integration

| Utseendeattribut | Frågetyper | Beskrivning |
|----------------------|----------------|-------------|
| `callapi` | text, integer, decimal, select_one | Aktiverar API-anropsintegration för detta fält. |
| `callapi-verify(params)` | text, integer, decimal | Utlöser ett API-verifieringsanrop med statiska parametrar. |
| `callapi-verify(dynamicParams)` | text, integer, decimal | Samma som `callapi-verify` men med parametrar härrörda från andra fältvärden vid körning. |

## Kända begränsningar

- Komplexa utseenden kanske inte renderas identiskt på alla plattformar.
- Vissa avancerade rtSurvey-utseenden kanske inte stöds i offlineläge.

## Felsökning av utseendeproblem

1. **Utseende tillämpas inte**: Kontrollera om det finns stavfel i utseendekolumnen.
2. **Inkonsekvent rendering**: Verifiera kompatibilitet med frågetypen och plattformen.
3. **Prestandaproblem**: Överväg att förenkla komplexa utseenden, särskilt för stora undersökningar.
