---
title: "Kvalitātes pārvaldība"
description: "Uzraugiet datu vākšanas progresu, skatiet interviju kartes un analizējiet enumeratoru sniegumu."
icon: "cloud"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 316
---

Modulis **Kvalitātes pārvaldība** (pieejams caur informācijas paneli) nodrošina reāllaika analītiku un telpiskās vizualizācijas, lai uzraudzītu datu vākšanas progresu un enumeratoru sniegumu. Tas piedāvā projektu vadītājiem dalīta skata interfeisu, lai ātri pārslēgtos starp atsevišķām aptaujām un pielāgotajām analītiskajām atskaitēm.

![Kvalitātes pārvaldības informācijas panelis](/images/manage_quality.png)

## Informācijas paneļa pārskats

Kvalitātes pārvaldības informācijas panelis ir sadalīts divās primārajās navigācijas cilnēs: **Formas** un **Atskaites**. Šī sānu izvēlne ļauj lietotājiem efektīvi meklēt un atlasīt konkrēto datu kopu vai atskaiti, ko vēlas analizēt.

### Formu analīze

Atlasot konkrētu formu no saraksta, informācijas panelis nodrošina vairākus iebūvētus vizualizācijas rīkus iesnieguma kvalitātes un biežuma izsekošanai:

- **Skaits pēc sākuma laika:** Stabiņu diagramma, kas vizualizē interviju uzsākšanas biežumu laika grafikā.
- **Skaits pēc beigu laika:** Stabiņu diagramma, kas vizualizē, kad intervijas tika pabeigtas.
- **Skaits pēc iesniegšanas datuma:** Izseko ikdienas datu apjomu, kas tiek sinhronizēts ar serveri.
- **Skaits pēc lietotājvārda:** Stabiņu diagramma, kas identificē visproduktīvākos enumeratorus, pamatojoties uz viņu kopējo iesniegumu skaitu.
- **Interviju karte:** Ģeogrāfisks izkaisīšanas zīmējums (darbināts ar Leaflet), kurā redzami GPS koordinātas, kur notika katrs iesniegums, ļaujot vadītājiem pārbaudīt lauka darba atrašanās vietas.

### Pielāgotas atskaites

Cilne **Atskaites** nodrošina piekļuvi iepriekš konfigurētiem R Markdown analītiskajiem projektiem un citai pielāgotai statistikai. Kad atskaite ir atlasīta, galvenās skata zona dinamiski ielādē ģenerēto analīzi caur iebūvētu skatītāju, ļaujot veikt dziļāku statistisku savākto datu verifikāciju.

## Meklēšana un filtrēšana

Virs sānjoslas saraksta ir pieejama ātrās meklēšanas josla, kas ļauj lietotājiem ātri atrast konkrētas formas vai atskaites pēc nosaukuma.
