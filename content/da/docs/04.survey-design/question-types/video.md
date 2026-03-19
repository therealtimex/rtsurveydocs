---
title: "Video"
description: "Videospørgsmål giver respondenter mulighed for at optage og indsende videofiler som en del af undersøgelsen."
icon: "videocam"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 229
---

Spørgsmålstypen `video` giver respondenter mulighed for at **optage video** eller uploade en eksisterende videofil som en del af deres undersøgelsessvar. Det er nyttigt til at fange visuelt bevis, demonstrationer, miljøforhold eller enhver information, der har gavn af bevægelse og lyd sammen.

## Grundlæggende XLSForm-specifikation

| type  | name        | label                              |
|-------|-------------|-------------------------------------|
| video | demo_video  | Optag venligst en kort demonstration |

For flere detaljer om standard video-spørgsmålstypen, se [XLSForm-specifikationen](https://xlsform.org/en/#question-types).

## Anvendelser

Videospørgsmål bruges typisk til:

1. Dokumentering af feltforhold — vejskader, infrastrukturtilstand, afgrødehelbred
2. Optagelse af produktdemonstrationer eller procedureoverholdelsestjek
3. Indsamling af videoudtalelser fra respondenter
4. Fangst af beviser, der kræver rumlig kontekst (f.eks. størrelse og omfang af et problemområde)
5. Før/efter-dokumentation til overvågnings- og evalueringsundersøgelser

## Dataformat

Videofiler gemmes som binære vedhæftninger:

- **Format:** MP4 eller MOV (mobiloptagelse)
- **Navngivning:** `{instanceID}-{feltnavn}.mp4` (eller tilsvarende)
- **Lagring:** Uploadet til serverens mediemappe og knyttet til indsendelsesposten
- **Adgang:** Kan afspilles og downloades fra indsendelseshåndteringsgrænsefladen

## rtSurvey-udvidelser

### Maksimal varighed

Brug kolonnen `parameters` til at begrænse optagelseslængden:

| type | name | label | parameters |
|------|------|-------|------------|
| video | site_visit | Optag stedsforholdene | `max-duration=60` |

`max-duration` er i sekunder. Optagelsen stopper automatisk ved grænsen.

### Kvalitet / opløsning

Styr optagelsesopløsningen via `parameters`:

| type | name | label | parameters |
|------|------|-------|------------|
| video | evidence | Optag videobevis | `quality=low` |

Understøttede værdier: `low` (hurtigere upload), `normal` (standard), `high`. Brug `low` i områder med begrænset forbindelseskvalitet.

### Upload af eksisterende video

På mobil kan respondenten vælge at **uploade en eksisterende video** fra enhedsgalleriet i stedet for at optage en ny. Dette er aktiveret som standard i den native kamera/galleri-integration.

### Afspilning inden indsendelse

På mobil kan det optagne klip gennemses, inden man fortsætter. Ingen yderligere konfiguration er nødvendig.

## Eksempler på brug

### Stedsinspektionsvideo med grænse

| type | name | label | hint | parameters |
|------|------|-------|------|------------|
| video | site_video | Optag vandpunktet | Gå rundt om hele faciliteten. Maks. 90 sekunder. | `max-duration=90 quality=normal` |

### Betinget video — kun hvis skader rapporteres

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| select_one janer | damage_found | Blev der fundet skader? | | |
| video | damage_video | Optag video af skaderne | `${damage_found} = 'yes'` | `${damage_found} = 'yes'` |

## Bedste praksis

1. Angiv `max-duration` — ubegrænsede videooptagelser kan nemt overstige 100 MB og mislykkes ved upload på svage forbindelser.
2. Brug `quality=low` til overvågningsundersøgelser, hvor visuelt bevis er påkrævet, men fine detaljer ikke er nødvendige — det reducerer filstørrelsen dramatisk.
3. Skriv specifikke optagelsesinstruktioner i kolonnen `hint` (f.eks. "Gå rundt om hele bygningen, hold kameraet stille").
4. Overvej om video er nødvendigt — et foto (`image`) er normalt tilstrækkeligt til statisk bevis og producerer meget mindre filer.
5. Test uploadydelsen på det faktiske feltnetværk inden udrulning.

## Begrænsninger

- Videofiler er meget store — en 1-minutters video ved normal kvalitet er typisk 20–60 MB afhængigt af enheden.
- Upload af store videofiler kræver en god netværksforbindelse; overvej at kræve Wi-Fi-synkronisering til videooptungede formularer.
- Ikke alle webbrowsere understøtter videooptagelse via MediaRecorder — Chrome er den mest pålidelige.
- Analyse af videosvar er manuel og tidskrævende; brug sparsomt og kun når videoindhold tilføjer unik værdi.
