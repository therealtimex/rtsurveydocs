---
title: "Trigger / Bevestigen"
description: "Triggervragen tonen een verklaring die de enumerator expliciet moet bevestigen voor het verdergaan."
icon: "check-circle"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

Het vraagtype `trigger` (ook wel `acknowledge` genoemd) toont een **verklaring met een selectievakje**. De enumerator moet het selectievakje aanvinken om te bevestigen dat ze de verklaring hebben gelezen en begrepen voordat het formulier hen toestaat verder te gaan. Er wordt geen gegevenswaarde opgeslagen — alleen of het selectievakje is aangevinkt.

## Basis XLSForm-specificatie

| type | name | label |
|------|------|-------|
| trigger | consent_ack | De respondent heeft mondelinge geïnformeerde toestemming gegeven. |

Of de alias `acknowledge` gebruiken:

| type | name | label |
|------|------|-------|
| acknowledge | consent_ack | De respondent heeft mondelinge geïnformeerde toestemming gegeven. |

Zowel `trigger` als `acknowledge` zijn equivalent — gebruik degene die uw platform documenteert.

## Toepassingen

Trigger/bevestigingsvragen worden veelgebruikt voor:

1. **Geïnformeerde toestemming** — bevestigen dat de enumerator toestemming heeft verkregen voor het registreren van gevoelige gegevens
2. **Zachte waarschuwingen** — waarschuwen voor een ongewone waarde en expliciete bevestiging vereisen voor het verdergaan
3. **Checklistitems** — bevestigen dat een fysieke observatie is voltooid
4. **Instructies** — de enumerator dwingen een instructie op sectieniveau te bevestigen voor het verdergaan
5. **Kwaliteitscontroles** — uitbijterwaarden markeren en de enumerator vragen ze te verifiëren

## Voorbeeldgebruik

### Toestemmingsbevestiging

| type | name | label | required |
|------|------|-------|----------|
| trigger | consent | De respondent heeft mondelinge geïnformeerde toestemming gegeven om deel te nemen aan deze enquête. | yes |

### Zachte waarschuwing voor uitbijterwaarden

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| integer | children | Aantal kinderen | | |
| trigger | children_confirm | U heeft ${children} kinderen ingevoerd. Verifieer met de respondent en tik op OK om te bevestigen. | `${children} > 10` | `${children} > 10` |

### Instructiebevestiging bij sectionstart

| type | name | label |
|------|------|-------|
| trigger | section_b_ack | Sectie B: Landbouwgrondgebruik. Stel alle vragen in deze sectie alleen aan het hoofd van het huishouden. |

## De trigger verplicht maken

Voeg `required: yes` toe om vooruitgang te voorkomen totdat het vakje is aangevinkt:

| type | name | label | required | required_message |
|------|------|-------|----------|------------------|
| trigger | safety_check | Alle veiligheidsuitrusting is aanwezig en functioneel. | yes | U moet bevestigen voor het verdergaan. |

## Voorwaardelijke weergave

Toon de trigger alleen wanneer een voorwaarde is voldaan:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_well | Heeft het huishouden een waterput? | |
| trigger | well_observation | Bevestig dat u de waterputomstandigheden direct heeft geobserveerd. | `${has_well} = 'yes'` |

## Verschil van `note`

| | `note` | `trigger` |
|--|--------|-----------|
| Toont tekst | Ja | Ja |
| Vereist interactie | Nee | Ja (moet aanvinken) |
| Slaat gegevens op | Nee | Nee (alleen OK/aangevinkt) |
| Kan voortgang blokkeren | Nee | Ja (met `required`) |

## Aanbevolen werkwijzen

1. Houd triggerlabels beknopt en handelbaar — de enumerator moet in seconden kunnen lezen en bevestigen.
2. Voeg altijd `required: yes` toe wanneer de bevestiging verplicht is.
3. Gebruik triggers voor toestemming en veiligheidscontroles waar u een auditspoor nodig heeft.
4. Combineer met `relevant` voor voorwaardelijke zachte waarschuwingen zodat de trigger alleen verschijnt wanneer een waarde verificatie nodig heeft.

## Beperkingen

- Triggervelden slaan geen betekenisvolle gegevenswaarde op — ze registreren alleen dat het vakje is aangevinkt.
- De triggerwidget wordt weergegeven als een eenvoudig selectievakje/knop op de meeste clients; het is geen volledige e-handtekening.
