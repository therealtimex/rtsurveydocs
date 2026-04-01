---
title: "Decimal"
description: "Pyetjet decimal lejojnë hyrje numerike me pjesë fraksionale në sondazhin tuaj."
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 223
---

Lloji i pyetjes decimal në XLSForms dhe rtSurvey përdoret për të mbledhur përgjigje numerike që mund të përfshijnë pjesë fraksionale. Ky lloj pyetjeje është thelbësor për mbledhjen e të dhënave numerike të sakta si matje, çmime, ose përqindje.

## Specifikimi bazë XLSForm

| type    | name   | label                    |
|---------|--------|--------------------------|
| decimal | weight | Shkruani peshën tuaj në kg |

Për më shumë detaje mbi llojin bazë të pyetjes decimal, shikoni [specifikimin XLSForm](https://xlsform.org/en/#question-types).

## Përdorimet

Pyetjet decimal përdoren zakonisht për:

1. Matje (p.sh., pesha, lartësia, distanca)
2. Të dhëna financiare (p.sh., çmimet, pagat)
3. Përqindjet
4. Mbledhja e të dhënave shkencore
5. Çdo të dhënë numerike që kërkon saktësi përtej numrave të plotë

## Praktikat më të mira

1. Përdorni etiketa të qarta dhe të qarta për të specifikuar hyrjen e pritur dhe njësinë e matjes.
2. Zbatoni kufizime diapazoni për të parandaluar hyrjet jorealike ose të gabuara.
3. Konsideroni përdorimin e tekstit hint për të dhënë shembuj ose sqaruar formatin e pritur.
4. Specifikoni numrin e dëshiruar të shifrave decimale në etiketë ose hint nëse saktësia është e rëndësishme.

## Kufizimet dhe validimi

Mund të shtoni kufizime për të siguruar që vlera e futur bie brenda një diapazoni specifik:

| type    | name   | label                    | constraint        | constraint_message                    |
|---------|--------|--------------------------|-------------------|---------------------------------------|
| decimal | height | Shkruani lartësinë tuaj në metra | .>0 and .<=3 | Lartësia duhet të jetë midis 0 dhe 3 metra |

## Shembull i përdorimit

Ja një shembull se si mund të përdorni pyetjet decimal në një sondazh shëndetësor:

| type    | name           | label                                     | constraint | constraint_message                |
|---------|----------------|-------------------------------------------|------------|-----------------------------------|
| decimal | weight         | Shkruani peshën tuaj në kg               | .>0 and .<=500 | Pesha duhet të jetë midis 0 dhe 500 kg |
| decimal | height         | Shkruani lartësinë tuaj në metra         | .>0 and .<=3 | Lartësia duhet të jetë midis 0 dhe 3 metra |
| decimal | body_temp      | Shkruani temperaturën e trupit tuaj në Celsius | .>=35 and .<=42 | Temperatura duhet të jetë midis 35°C dhe 42°C |
| calculate | bmi          |                                           |            |                                   |

Në rreshtin calculate për BMI, mund të përdorni:

```
calculation | ${weight} / (${height} * ${height})
```

Kjo do të llogarisë BMI duke përdorur peshën dhe lartësinë e futura.

## Zgjerime të rtSurvey

Ndërsa specifikimi bazë XLSForm për pyetjet decimal është i thjeshtë, rtSurvey ofron veçori ose personalizime shtesë:

1. Kontrolli i saktësisë (numri i shifrave decimale)
2. Formatet e personalizuara të hyrjes (p.sh., përqindje, monedhë)
3. Rregullat e avancuara të validimit

## Kufizimet

- Saktësia e numrave decimal mund të kufizohet nga sistemi ose baza e të dhënave themelore.
- Përdoruesit mund të kenë nevojë për udhëzime mbi ndarësin e pritur decimal (pikë ose presje) në varësi të vendndodhjes.
- Numrat e mëdhenj decimal mund të jenë të vështirë për t'u lexuar ose futur saktësisht në pajisjet mobile.
