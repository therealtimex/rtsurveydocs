---
title: "Trigger / Acknowledge"
description: "Otázky typu trigger zobrazujú vyhlásenie, ktoré musí anketár výslovne potvrdiť pred pokračovaním."
icon: "check-circle"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 240
---

Typ otázky `trigger` (tiež nazývaný `acknowledge`) zobrazuje **vyhlásenie so zaškrtávacím políčkom**. Anketár musí zaškrtnúť políčko, aby potvrdil, že si vyhlásenie prečítal a pochopil, pred tým, ako mu formulár umožní pokračovať. Neukladajú sa žiadne dátové hodnoty — iba to, či bolo políčko zaškrtnuté.

## Základná špecifikácia XLSForm

| type | name | label |
|------|------|-------|
| trigger | consent_ack | Respondent poskytol verbálny informovaný súhlas. |

Alebo pomocou aliasu `acknowledge`:

| type | name | label |
|------|------|-------|
| acknowledge | consent_ack | Respondent poskytol verbálny informovaný súhlas. |

Oba `trigger` aj `acknowledge` sú ekvivalentné — použite ten, ktorý vaša platforma dokumentuje.

## Použitia

Otázky trigger/acknowledge sa bežne používajú pre:

1. **Informovaný súhlas** — potvrdiť, že anketár získal súhlas pred zaznamenaním citlivých dát
2. **Mäkké upozornenia** — varovanie o nezvyčajnej hodnote a vyžadovanie výslovného potvrdenia pred pokračovaním
3. **Položky kontrolného zoznamu** — potvrdenie dokončenia fyzického pozorovania (napr. „Priamo som pozoroval zdroj vody")
4. **Pokyny** — nútiť anketára potvrdiť pokyn na úrovni sekcie pred pokračovaním
5. **Kontroly kvality** — označenie odľahlých hodnôt a vyžadovanie, aby ich anketár overil

## Príklady použitia

### Potvrdenie súhlasu

| type | name | label | required |
|------|------|-------|----------|
| trigger | consent | Respondent dal verbálny informovaný súhlas s účasťou v tomto prieskume. | yes |

### Mäkké upozornenie pre odľahlé hodnoty

Používa sa spolu s výrazom `relevant` na zobrazenie triggera iba pri zadaní podozrivej hodnoty:

| type | name | label | relevant | required |
|------|------|-------|----------|----------|
| integer | children | Počet detí | | |
| trigger | children_confirm | Zadali ste ${children} detí. Prosím overte s respondentom a klepnite OK na potvrdenie. | `${children} > 10` | `${children} > 10` |

### Potvrdenie pokynov na začiatku sekcie

| type | name | label |
|------|------|-------|
| trigger | section_b_ack | Sekcia B: Využitie poľnohospodárskej pôdy. Všetky otázky v tejto sekcii kladte iba hlavovi domácnosti. |

## Povinnosť triggera

Pridajte `required: yes` na zabránenie postúpeniu, kým políčko nie je zaškrtnuté:

| type | name | label | required | required_message |
|------|------|-------|----------|------------------|
| trigger | safety_check | Všetky bezpečnostné zariadenia sú prítomné a funkčné. | yes | Pred pokračovaním musíte potvrdiť. |

## Podmienené zobrazenie

Zobrazte trigger iba keď je splnená podmienka:

| type | name | label | relevant |
|------|------|-------|----------|
| select_one yesno | has_well | Má domácnosť studňu? | |
| trigger | well_observation | Potvrďte, že ste priamo pozorovali stav studne. | `${has_well} = 'yes'` |

## Rozdiel od `note`

| | `note` | `trigger` |
|--|--------|-----------|
| Zobrazuje text | Áno | Áno |
| Vyžaduje interakciu | Nie | Áno (musí zaškrtnúť) |
| Ukladá dáta | Nie | Nie (iba OK/zaškrtnuté) |
| Môže blokovať postup | Nie | Áno (s `required`) |

## Najlepšie postupy

1. Udržujte popisky triggera stručné a akčné — anketár by mal byť schopný prečítať a potvrdiť za sekundy.
2. Vždy pridávajte `required: yes`, keď je potvrdenie povinné.
3. Používajte triggery pre súhlas a bezpečnostné kontroly, kde potrebujete auditný záznam o tom, že anketár potvrdil.
4. Kombinujte s `relevant` pre podmienené mäkké upozornenia, aby sa trigger zobrazoval iba keď hodnota potrebuje overenie.

## Obmedzenia

- Polia trigger neukladajú zmysluplnú dátovú hodnotu — zaznamenávajú iba to, že políčko bolo zaškrtnuté.
- Widget trigger sa renderuje na väčšine klientov ako jednoduché zaškrtávacie políčko/tlačidlo; nie je to plný elektronický podpis.
