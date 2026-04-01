---
title: "Trigger / Bekræft"
description: "Trigger-spørgsmål viser en erklæring, som intervieweren eksplicit skal bekræfte, inden de fortsætter."
icon: "check-circle"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

Spørgsmålstypen `trigger` (også kaldet `acknowledge`) viser en **erklæring med et afkrydsningsfelt**. Intervieweren skal markere afkrydsningsfeltet for at bekræfte, at de har læst og forstået erklæringen, inden formularen tillader dem at fortsætte. Ingen dataværdi gemmes — kun om afkrydsningsfeltet er markeret.

## Grundlæggende XLSForm-specifikation

| type | name | label |
|------|------|-------|
| trigger | consent_ack | Respondenten har givet mundtligt informeret samtykke. |

Eller ved brug af `acknowledge`-aliaset:

| type | name | label |
|------|------|-------|
| acknowledge | consent_ack | Respondenten har givet mundtligt informeret samtykke. |

Både `trigger` og `acknowledge` er ækvivalente — brug det, din platform dokumenterer.

## Anvendelser

Trigger/acknowledge-spørgsmål bruges typisk til:

1. **Informeret samtykke** — bekræft, at intervieweren indhentede samtykke inden registrering af følsomme data
2. **Bløde advarsler** — advar om en usædvanlig værdi og kræv eksplicit bekræftelse inden fremrykning
3. **Checklistepunkter** — bekræft, at en fysisk observation er gennemført (f.eks. "Jeg har observeret vandkilden direkte")
4. **Instruktioner** — tvingen intervieweren til at bekræfte en sektionsoverinstruktion inden fremrykning
5. **Kvalitetstjek** — marker afvigervardier og kræv, at intervieweren verificerer dem

## Eksempler på brug

### Bekræftelse af samtykke

| type | name | label | required |
|------|------|-------|----------|
| trigger | consent | Respondenten har givet mundtligt informeret samtykke til at deltage i denne undersøgelse. | yes |

### Blød advarsel for afvigerværdier

Bruges sammen med et `relevant`-udtryk til kun at vise triggeren, når en mistænkelig værdi er indtastet:

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| integer | children | Antal børn | | |
| trigger | children_confirm | Du indtastede ${children} børn. Verificer venligst med respondenten og tryk OK for at bekræfte. | `${children} > 10` | `${children} > 10` |

### Instruktionsbekræftelse ved sektionsstart

| type | name | label |
|------|------|-------|
| trigger | section_b_ack | Sektion B: Landbrugsjord. Stil alle spørgsmål i denne sektion kun til husstandsoverhovedet. |

## Gøre triggeren påkrævet

Tilføj `required: yes` for at forhindre fremrykning, inden feltet er markeret:

| type | name | label | required | required_message |
|------|------|-------|----------|------------------|
| trigger | safety_check | Alt sikkerhedsudstyr er til stede og funktionelt. | yes | Du skal bekræfte, inden du fortsætter. |

## Betinget visning

Vis triggeren kun, når en betingelse er opfyldt:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one janer | has_well | Har husstanden en brønd? | |
| trigger | well_observation | Bekræft, at du direkte har observeret brøndens tilstand. | `${has_well} = 'yes'` |

## Forskel fra `note`

| | `note` | `trigger` |
|--|--------|-----------|
| Viser tekst | Ja | Ja |
| Kræver interaktion | Nej | Ja (skal markeres) |
| Gemmer data | Nej | Nej (kun OK/markeret) |
| Kan blokere fremrykning | Nej | Ja (med `required`) |

## Bedste praksis

1. Hold triggerlabels kortfattede og handlingsorienterede — intervieweren skal kunne læse og bekræfte på sekunder.
2. Tilføj altid `required: yes`, når bekræftelsen er obligatorisk.
3. Brug triggere til samtykke og sikkerhedstjek, hvor du har brug for et revisionsspor for, at intervieweren bekræftede.
4. Kombiner med `relevant` til betingede bløde advarsler, så triggeren kun vises, når en værdi kræver verifikation.

## Begrænsninger

- Triggerfelter gemmer ikke en meningsfuld dataværdi — de registrerer kun, at feltet er markeret.
- Trigger-widgetten gengives som et simpelt afkrydsningsfelt/knap på de fleste klienter; det er ikke en fuldt e-signatur.
