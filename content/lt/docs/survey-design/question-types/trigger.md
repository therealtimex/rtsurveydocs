---
title: "Trigger / Acknowledge"
description: "Trigger klausimai rodo teiginį, kurį surašytojas turi aiškiai patvirtinti prieš tęsdamas."
icon: "check-circle"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

Klausimo tipas `trigger` (taip pat vadinamas `acknowledge`) rodo **teiginį su žymimuoju langeliu**. Surašytojas turi pažymėti langelį, patvirtindamas, kad perskaitė ir suprato teiginį, prieš leidžiant tęsti formą. Duomenų reikšmė nesaugoma — tik tai, ar langelis buvo pažymėtas.

## Pagrindinė XLSForm specifikacija

| type | name | label |
|------|------|-------|
| trigger | consent_ack | Respondentas davė žodinį informuotą sutikimą. |

Arba naudojant `acknowledge` pseudonimą:

| type | name | label |
|------|------|-------|
| acknowledge | consent_ack | Respondentas davė žodinį informuotą sutikimą. |

`trigger` ir `acknowledge` yra lygiaverčiai — naudokite tą, kurį dokumentuoja jūsų platforma.

## Naudojimo atvejai

Trigger/acknowledge klausimai dažnai naudojami:

1. **Informuotam sutikimui** — patvirtinti, kad surašytojas gavo sutikimą prieš įrašant jautrius duomenis
2. **Švelniam įspėjimui** — perspėti apie neįprastą reikšmę ir reikalauti aiškaus patvirtinimo prieš tęsiant
3. **Kontrolinio sąrašo elementams** — patvirtinti, kad fizinis stebėjimas buvo atliktas (pvz., „Aš tiesiogiai stebėjau vandens šaltinį")
4. **Instrukcijoms** — priversti surašytoją patvirtinti sekcijų lygio instrukciją prieš tęsiant
5. **Kokybės patikrinimams** — pažymėti netipinius dydžius ir reikalauti surašytojo juos patikrinti

## Naudojimo pavyzdžiai

### Sutikimo patvirtinimas

| type | name | label | required |
|------|------|-------|----------|
| trigger | consent | Respondentas davė žodinį informuotą sutikimą dalyvauti šioje apklausoje. | yes |

### Švelnusis įspėjimas dėl netipiškų reikšmių

Naudojama kartu su `relevant` išraiška, kad trigger rodytų tik tada, kai įvedama įtartina reikšmė:

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| integer | children | Vaikų skaičius | | |
| trigger | children_confirm | Įvedėte ${children} vaikų. Patikrinkite su respondentu ir spustelėkite Gerai patvirtinti. | `${children} > 10` | `${children} > 10` |

### Instrukcijų patvirtinimas sekcijos pradžioje

| type | name | label |
|------|------|-------|
| trigger | section_b_ack | B sekcija: Žemės ūkio žemės naudojimas. Visus šios sekcijos klausimus užduokite tik namų ūkio galvai. |

## Trigger padarymas privalomas

Pridėkite `required: yes`, kad neleidžiama tęsti, kol langelis nepažymėtas:

| type | name | label | required | required_message |
|------|------|-------|----------|------------------|
| trigger | safety_check | Visa saugos įranga yra ir veikia. | yes | Prieš tęsdami turite patvirtinti. |

## Sąlyginis rodymas

Rodykite trigger tik tada, kai sąlyga yra tenkinama:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_well | Ar namų ūkis turi šulinį? | |
| trigger | well_observation | Patvirtinkite, kad tiesiogiai stebėjote šulinio būklę. | `${has_well} = 'yes'` |

## Skirtumas nuo `note`

| | `note` | `trigger` |
|--|--------|-----------|
| Rodo tekstą | Taip | Taip |
| Reikalauja sąveikos | Ne | Taip (reikia pažymėti) |
| Saugo duomenis | Ne | Ne (tik Gerai/pažymėta) |
| Gali blokuoti tęsimą | Ne | Taip (su `required`) |

## Geriausios praktikos

1. Laikykite trigger etiketes glaustomis ir veiksmingomis — surašytojas turėtų galėti perskaityti ir patvirtinti per kelias sekundes.
2. Visada pridėkite `required: yes`, kai patvirtinimas yra privalomas.
3. Naudokite trigger sutikimui ir saugos patikrinimams, kur reikia audito pėdsako, kad surašytojas patvirtino.
4. Derinkite su `relevant` sąlyginiam švelniam įspėjimui, kad trigger rodytų tik tada, kai reikšmė reikalauja patikrinimo.

## Apribojimai

- Trigger laukai nesaugo prasmingos duomenų reikšmės — jie tik fiksuoja, kad langelis buvo pažymėtas.
- Trigger valdiklis daugelyje klientų atvaizduojamas kaip paprastas žymimasis langelis/mygtukas; tai nėra visavertis elektroninis parašas.
