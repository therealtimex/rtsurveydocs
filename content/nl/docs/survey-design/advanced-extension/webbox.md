---
title: "Webbox"
description: "Webbox sluit een externe webpagina in de enquête in als een modaal iframe, waardoor enumeratoren referenties kunnen bekijken of interacties kunnen uitvoeren met externe tools zonder het formulier te verlaten."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 299
---

**Webbox** sluit een externe webpagina in de enquête in als een **modaal popup** (iframe). De enumerator tikt op een knop in het label of de notitatietekst, de pagina opent in een volledig-scherm overlay binnen het formulier, en wanneer ze het sluiten keren ze terug naar precies waar ze waren. Hiermee kunt u referentiemateriaal, kaarten, dashboards of aangepaste tools tonen zonder een apart browsertabblad te openen.

---

## Syntaxis

Voeg een `<webbox>` HTML-tag rechtstreeks in een `label`- of `note`-labelkolom in:

```html
<webbox src='https://example.com/reference' title='Referentiegids'>Referentiegids openen</webbox>
```

| Attribuut | Beschrijving |
|-----------|-------------|
| `src` | De URL om in het iframe te laden. Ondersteunt zowel enkelvoudige als dubbele aanhalingstekens. |
| `title` | Tekst weergegeven in de modale headerbalk. Ondersteunt platte tekst. |
| *(inhoud)* | Het klikbare knoplabel weergegeven in het enquêteveld |

---

## Basisvoorbeeld

| type | name | label |
|------|------|-------|
| note | ref_guide | `<webbox src='https://docs.example.com/field-guide' title='Veldgids'>📖 Veldgids openen</webbox>` |

Dit rendert een knop met het label "📖 Veldgids openen". Wanneer erop wordt getikt, opent een modaal met de veldgidswebsite.

---

## Een kaart insluiten

| type | name | label |
|------|------|-------|
| note | area_map | `<webbox src='https://maps.example.com/survey-area' title='Enquêtegebiedkaart'>🗺 Kaart bekijken</webbox>` |

---

## Formulierwaarden doorgeven aan de ingebedde pagina

Voeg formulierveldwaarden toe aan de URL met `concat()` in de kolom `calculation` en verwijs naar het resultaat in het label:

| type | name | label | calculation |
|------|------|-------|-------------|
| calculate | webbox_url | | `concat('https://dashboard.example.com/household?id=', ${household_id})` |
| note | hh_dash | `<webbox src='${webbox_url}' title='Huishouden Dashboard'>Dashboard openen</webbox>` |

{{% alert icon=" " context="warning" %}}
Het attribuut `src` in de `<webbox>`-tag ondersteunt `${veldnaam}`-referenties wanneer het label is berekend vanuit een `calculate`-veld. Construeer de volledige URL in een `calculate`-veld en verwijs ernaar.
{{% /alert %}}

---

## Herhalingsinteractie: verwijderknoppen

Webbox ondersteunt ook speciale actietags voor het beheren van herhalingsgroepen binnen labels:

```html
<delete-repeat-current>Deze rij verwijderen</delete-repeat-current>
<delete-repeat-last>Laatste rij verwijderen</delete-repeat-last>
```

Deze worden weergegeven als knoppen die herhalingsinstanties verwijderen wanneer erop wordt getikt. Plaats ze in een `note`-veld binnen (of vlak na) de herhalingsgroep:

| type | name | label |
|------|------|-------|
| begin_repeat | items | Item |
| text | item_name | Itemnaam |
| note | delete_btn | `<delete-repeat-current>✕ Dit item verwijderen</delete-repeat-current>` |
| end_repeat | | |

---

## Communicatie met de ingebedde pagina (postMessage)

Het webbox iframe en het bovenliggende formulier kunnen communiceren via de `postMessage` API van de browser. Het bovenliggende element stuurt een `init`-bericht naar het iframe wanneer het opent. De ingebedde pagina kan reageren met:

- `delete-repeat-current` — activeert verwijdering van de huidige herhalingsinstantie
- `delete-repeat-last` — activeert verwijdering van de laatste herhalingsinstantie

Dit maakt het mogelijk voor aangepaste webtools (bijv. tekenhulpmiddelen, interactieve kaarten) om formulieracties te activeren wanneer de gebruiker een actie bevestigt binnen het iframe.

---

## Aanbevolen werkwijzen

1. Gebruik webbox voor **referentiemateriaal** (richtlijnen, opzoektabellen, kaarten) — niet voor het verzamelen van gegevens die in het formulier zelf zouden moeten staan.
2. Zorg ervoor dat de ingebedde URL toegankelijk is vanuit het netwerk van het apparaat — webbox vereist connectiviteit.
3. Houd de ingebedde pagina mobielvriendelijk — het modaal is maximaal 800px breed en 80% van de viewporthoogte.
4. Gebruik beschrijvende knoptekst (bijv. "Dorpskaart bekijken") in plaats van algemene labels ("Klik hier").
5. Informeer enumeratoren dat het sluiten van het modaal hen terugbrengt naar de enquête — sommige gebruikers weten mogelijk niet hoe ze een iframe-overlay kunnen sluiten.

## Beperkingen

- Webbox vereist netwerkconnectiviteit om de ingebedde URL te laden.
- Sommige externe sites blokkeren het insluiten in iframes via `X-Frame-Options`- of `Content-Security-Policy`-headers — deze sites kunnen niet worden gebruikt met webbox.
- Het modaal sluit wanneer de enumerator wegnavigeert van de vraag — eventuele niet-opgeslagen status in het iframe gaat verloren.
- Webbox is een rtSurvey-webformulieruitbreiding en werkt mogelijk niet in andere ODK-compatibele clients.
