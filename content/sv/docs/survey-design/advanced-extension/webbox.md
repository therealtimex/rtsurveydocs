---
title: "Webbox"
description: "Webbox bäddar in en extern webbsida inuti undersökningen som ett modalt iframe-fönster, vilket gör det möjligt för räknare att se referenser eller interagera med externa verktyg utan att lämna formuläret."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 299
---

**Webbox** bäddar in en extern webbsida i undersökningen som ett **modalt popup-fönster** (iframe). Räknaren trycker på en knapp i etiketten eller noten, sidan öppnas i ett helskärmsöverlägg inom formuläret, och när de stänger det återvänder de till exakt där de var. Detta låter dig visa referensmaterial, kartor, instrumentpaneler eller anpassade verktyg utan att öppna en separat webbläsarflik.

---

## Syntax

Infoga en `<webbox>` HTML-tagg direkt i en `label`- eller `note`-etikettkolumn:

```html
<webbox src='https://example.com/reference' title='Referensguide'>Öppna referensguide</webbox>
```

| Attribut | Beskrivning |
|----------|-------------|
| `src` | URL:en att ladda in i iframe. Stöder både enkla och dubbla citationstecken. |
| `title` | Text som visas i modalens rubrikrad. Stöder vanlig text. |
| *(innehåll)* | Den klickbara knapptexten som visas i undersökningsfältet |

---

## Grundläggande exempel

| type | name | label |
|------|------|-------|
| note | ref_guide | `<webbox src='https://docs.example.com/field-guide' title='Fältguide'>Öppna fältguide</webbox>` |

Detta renderar en knapp märkt "Öppna fältguide". När man trycker på den öppnas ett modalt fönster som visar fältguidewebbplatsen.

---

## Bädda in en karta

| type | name | label |
|------|------|-------|
| note | area_map | `<webbox src='https://maps.example.com/survey-area' title='Undersökningsområdeskarta'>Visa karta</webbox>` |

---

## Skicka formulärvärden till den inbäddade sidan

Lägg till formulärfältvärden till URL:en med `concat()` i `calculation`-kolumnen och referera till resultatet i etiketten:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | webbox_url | | `concat('https://dashboard.example.com/household?id=', ${household_id})` |
| note | hh_dash | `<webbox src='${webbox_url}' title='Hushållsinstrumentpanel'>Öppna instrumentpanel</webbox>` |

{{% alert icon=" " context="warning" %}}
Attributet `src` i `<webbox>`-taggen stöder `${fieldname}`-referenser när etiketten beräknas från ett `calculate`-fält. Konstruera den fullständiga URL:en i ett `calculate`-fält och referera till det.
{{% /alert %}}

---

## Upprepningsinteraktion: borttagningsknappar

Webbox stöder även speciella åtgärdstaggar för att hantera upprepningsgrupper inuti etiketter:

```html
<delete-repeat-current>Ta bort denna rad</delete-repeat-current>
<delete-repeat-last>Ta bort sista raden</delete-repeat-last>
```

Dessa renderas som knappar som tar bort upprepningsinstanser när man trycker på dem. Placera dem i ett `note`-fält inne i (eller precis efter) upprepningsgruppen:

| type | name | label |
|------|------|-------|
| begin_repeat | items | Objekt |
| text | item_name | Objektets namn |
| note | delete_btn | `<delete-repeat-current>Ta bort detta objekt</delete-repeat-current>` |
| end_repeat | | |

---

## Kommunikation med den inbäddade sidan (postMessage)

Webbox-iframen och det överordnade formuläret kan kommunicera med hjälp av webbläsarens `postMessage` API. Det överordnade skickar ett `init`-meddelande till iframen när den öppnas. Den inbäddade sidan kan svara med:

- `delete-repeat-current` — utlöser borttagning av den aktuella upprepningsinstansen
- `delete-repeat-last` — utlöser borttagning av den sista upprepningsinstansen

Detta gör det möjligt för anpassade webbverktyg (t.ex. ritverktyg, interaktiva kartor) att utlösa formuläråtgärder när användaren bekräftar en åtgärd inuti iframen.

---

## Bästa praxis

1. Använd webbox för **referensmaterial** (riktlinjer, söktabeller, kartor) — inte för att samla in data som bör finnas i formuläret självt.
2. Se till att den inbäddade URL:en är tillgänglig från enhetens nätverk — webbox kräver anslutning.
3. Håll den inbäddade sidan mobilvänlig — modalen är maximalt 800px bred och 80% av viewport-höjden.
4. Använd beskrivande knapptexts (t.ex. "Visa bykarta") snarare än generiska etiketter ("Klicka här").
5. Informera räknare om att stänga modalen returnerar dem till undersökningen — vissa användare kanske inte vet hur man stänger ett iframe-överlägg.

## Begränsningar

- Webbox kräver nätverksanslutning för att ladda den inbäddade URL:en.
- Vissa externa webbplatser blockerar inbäddning i iframes via `X-Frame-Options`- eller `Content-Security-Policy`-headers — dessa webbplatser kan inte användas med webbox.
- Modalen stängs när räknaren navigerar bort från frågan — eventuellt osparat tillstånd i iframen förloras.
- Webbox är ett rtSurvey webbformulär-tillägg och fungerar kanske inte i andra ODK-kompatibla klienter.
