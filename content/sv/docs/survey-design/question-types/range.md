---
title: "Intervall"
description: "Intervallfrågor låter respondenter välja ett tal genom att dra ett reglage mellan ett definierat minimum- och maximumvärde."
icon: "sliders"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 238
---

Frågtypen `range` visar ett **reglage** (eller motsvarande inmatning) som låter respondenter välja ett tal inom ett definierat minimum och maximum. Det är idealiskt för att samla in betyg, nöjdhetspoäng eller numeriska värden där du vill begränsa intervallet visuellt snarare än att förlita dig på en textinmatning med begränsningar.

## Grundläggande XLSForm-specifikation

| type | name | label | parameters |
|------|------|-------|------------|
| range | satisfaction | Hur nöjd är du med tjänsten? | start=1 end=5 step=1 |

Kolumnen `parameters` definierar reglagets gränser och stegstorlek:

| Parameter | Beskrivning | Standard |
|-----------|-------------|---------|
| `start` | Minimivärde (inklusivt) | 0 |
| `end` | Maximivärde (inklusivt) | 10 |
| `step` | Ökning mellan giltiga värden | 1 |

För mer detaljer om standardfrågtypen range, se [XLSForm-specifikationen](https://xlsform.org/en/#question-types).

## Användningsområden

Intervallfrågor används vanligtvis för:

1. Nöjdhets- eller betygskalor (t.ex. 1–5 eller 0–10)
2. Likert-liknande numeriska skalor
3. Samla in mätningar där bara diskreta värden är giltiga
4. Åldersgrupper eller poängintervall där ett reglage förbättrar användbarhet över ett textfält

## Exempelanvändning

### Grundläggande betygsska la

| type | name | label | parameters |
|------|------|-------|------------|
| range | overall_rating | Övergripande betyg (0–10) | start=0 end=10 step=1 |

### Decimalsteg

| type | name | label | parameters |
|------|------|-------|------------|
| range | weight_kg | Vikt (kg) | start=0 end=200 step=0.5 |

### Använda värdet i en beräkning

| type | name | label | parameters | calculation |
|------|------|-------|------------|-------------|
| range | score | Testpoäng (0–100) | start=0 end=100 step=5 | |
| calculate | grade | | | if(${score} >= 90, 'A', if(${score} >= 80, 'B', if(${score} >= 70, 'C', 'F'))) |
| note | grade_note | Ditt betyg är: ${grade} | | |

## Utseende

Typen `range` renderas som ett reglage som standard. Du kan kombinera det med `horizontal` för en bredare layout i webbformulär:

| type | name | label | parameters | appearance |
|------|------|-------|------------|------------|
| range | nps | Hur sannolikt är det att du rekommenderar oss? (0–10) | start=0 end=10 step=1 | horizontal |

## Bästa praxis

1. Sätt alltid meningsfulla värden för `start`, `end` och `step` — förlita dig inte på standardvärden.
2. Märk ändarna på din skala i kolumnen `hint` (t.ex. `hint: 0 = Mycket missnöjd, 10 = Mycket nöjd`) för att ge respondenter sammanhang.
3. För 5-punkts Likert-skalor, använd `start=1 end=5 step=1` snarare än 0–4, eftersom respondenter förväntar sig att "1" betyder det lägsta.
4. Använd `range` istället för `integer` + begränsning när det begränsade intervallet är en del av frågans design (reglaget kommunicerar skalan visuellt).

## Begränsningar

- Reglagets widget kanske inte är idealisk för mycket breda intervall (t.ex. 0–10000) — ett text-`integer` med begränsningar är mer användarvänligt i dessa fall.
- På mobila enheter kan fina stegvärden (t.ex. `step=0.1`) vara svåra att kontrollera exakt med ett touchwreglage.
