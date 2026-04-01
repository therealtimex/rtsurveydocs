---
title: "Webbox"
description: "Webbox indlejrer en ekstern webside inde i undersøgelsen som en modal iframe, der giver interviewere mulighed for at se referencer eller interagere med eksterne værktøjer uden at forlade formularen."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 299
---

**Webbox** indlejrer en ekstern webside inde i undersøgelsen som en **modal popup** (iframe). Intervieweren trykker på en knap i labelen eller noteteksten, siden åbnes i et fuldskærmsoverlag inden for formularen, og når de lukker den, vender de præcis tilbage til, hvor de var. Dette giver dig mulighed for at vise referencemateriale, kort, dashboards eller brugerdefinerede værktøjer uden at åbne en separat browserfane.

---

## Syntaks

Indsæt et `<webbox>`-HTML-tag direkte i en `label`- eller `note`-labelkolonne:

```html
<webbox src='https://example.com/reference' title='Referenceguide'>Åbn Referenceguide</webbox>
```

| Attribut | Beskrivelse |
|----------|-------------|
| `src` | URL'en, der indlæses i iframen. Understøtter både enkelt- og dobbeltanførselstegn. |
| `title` | Tekst vist i modalens overskriftslinje. Understøtter ren tekst. |
| *(indhold)* | Den klikbare knaplabel vist i undersøgelsesfeltet |

---

## Grundlæggende eksempel

| type | name | label |
|------|------|-------|
| note | ref_guide | `<webbox src='https://docs.example.com/field-guide' title='Feltguide'>📖 Åbn Feltguide</webbox>` |

Dette gengiver en knap mærket "📖 Åbn Feltguide". Når der trykkes på den, åbnes en modal, der viser feltguidens websted.

---

## Indlejring af et kort

| type | name | label |
|------|------|-------|
| note | area_map | `<webbox src='https://maps.example.com/survey-area' title='Undersøgelsesområdekort'>🗺 Se kort</webbox>` |

---

## Videresendelse af formularværdier til den indlejrede side

Tilføj formularfeltværdier til URL'en ved hjælp af `concat()` i `calculation`-kolonnen og referer til resultatet i labelen:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | webbox_url | | `concat('https://dashboard.example.com/household?id=', ${household_id})` |
| note | hh_dash | `<webbox src='${webbox_url}' title='Husholdningsdashboard'>Åbn Dashboard</webbox>` |

{{% alert icon=" " context="warning" %}}
`src`-attributten i `<webbox>`-tagget understøtter `${feltnavn}`-referencer, når labelen beregnes fra et `calculate`-felt. Konstruer den fulde URL i et `calculate`-felt og referer til det.
{{% /alert %}}

---

## Gentagelsesinteraktion: sletteknapper

Webbox understøtter også specielle handlingstags til håndtering af gentagelsesgrupper inde i labels:

```html
<delete-repeat-current>Fjern denne række</delete-repeat-current>
<delete-repeat-last>Fjern sidste række</delete-repeat-last>
```

Disse gengives som knapper, der sletter gentagelsesinstanser, når der trykkes på dem. Placer dem i et `note`-felt inde i (eller lige efter) gentagelsesgruppen:

| type | name | label |
|------|------|-------|
| begin_repeat | items | Element |
| text | item_name | Elementnavn |
| note | delete_btn | `<delete-repeat-current>✕ Fjern dette element</delete-repeat-current>` |
| end_repeat | | |

---

## Kommunikation med den indlejrede side (postMessage)

Webbox-iframen og den overordnede formular kan kommunikere ved hjælp af browserens `postMessage` API. Den overordnede sender en `init`-besked til iframen, når den åbnes. Den indlejrede side kan svare med:

- `delete-repeat-current` — udløser sletning af den aktuelle gentagelsesinstans
- `delete-repeat-last` — udløser sletning af den sidste gentagelsesinstans

Dette giver brugerdefinerede webværktøjer (f.eks. tegneværktøjer, interaktive kort) mulighed for at udløse formularhandlinger, når brugeren bekræfter en handling inde i iframen.

---

## Bedste praksis

1. Brug webbox til **referencemateriale** (retningslinjer, opslagstabeller, kort) — ikke til at indsamle data, der bør være i formularen.
2. Sørg for, at den indlejrede URL er tilgængelig fra enhedens netværk — webbox kræver forbindelse.
3. Hold den indlejrede side mobilvenlig — modalen er maksimalt 800 px bred og 80% af viewport-højden.
4. Brug beskrivende knaptekst (f.eks. "Vis landsbykortet") snarere end generiske labels ("Klik her").
5. Informér interviewere om, at lukning af modalen returnerer dem til undersøgelsen — nogle brugere ved måske ikke, hvordan de lukker et iframe-overlag.

## Begrænsninger

- Webbox kræver netværksforbindelse for at indlæse den indlejrede URL.
- Nogle eksterne websteder blokerer indlejring i iframes via `X-Frame-Options`- eller `Content-Security-Policy`-headere — disse websteder kan ikke bruges med webbox.
- Modalen lukker, når intervieweren navigerer væk fra spørgsmålet — enhver ikke-gemt tilstand i iframen går tabt.
- Webbox er en rtSurvey-webformularudvidelse og fungerer muligvis ikke i andre ODK-kompatible klienter.
