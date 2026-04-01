---
title: "Izbor iz datoteke"
description: "select_one_from_file i select_multiple_from_file dinamički učitavaju opcije iz spoljne CSV ili XML datoteke priložene formularu."
icon: "file-earmark-spreadsheet"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 241
---

`select_one_from_file` i `select_multiple_from_file` funkcionišu kao `select_one` i `select_multiple`, ali umesto definisanja opcija u **radnom listu choices**, opcije se učitavaju iz **spoljne CSV ili XML datoteke** priložene formularu. Ovo je korisno kada je lista opcija veoma dugačka, često se menja, ili treba biti ažurirana bez ponovnog izgradnje celog formulara.

## Osnovna XLSForm specifikacija

| type | name | label |
|------|------|-------|
| select_one_from_file health_facilities.csv | facility | Izaberite zdravstvenu ustanovu |
| select_multiple_from_file crops.csv | crops | Koje useve domaćinstvo gaji? |

Naziv datoteke posle naziva tipa mora odgovarati nazivu datoteke koji priložite kada otpremate formular.

## Format CSV datoteke

Vaša CSV datoteka mora imati najmanje dve kolone: `name` (sačuvana vrednost) i `label` (prikazani tekst). Možete dodati bilo koji broj dodatnih kolona za filtriranje.

**health_facilities.csv:**

```
name,label,district,type
HF001,Nairobi Central Clinic,Nairobi,clinic
HF002,Westlands Health Centre,Nairobi,health_centre
HF003,Kisumu District Hospital,Kisumu,hospital
```

## Filtriranje opcija

Koristite kolonu `choice_filter` za prikaz samo onih opcija koje odgovaraju trenutnom kontekstu. Referencujte CSV kolone direktno sa njihovim imenom kolone (bez `${}`):

| type | name | label | choice_filter |
|------|------|-------|---------------|
| select_one districts.csv | district | Izaberite okrug | |
| select_one_from_file health_facilities.csv | facility | Izaberite ustanovu | district = ${district} |

U ovom primeru, prikazuju se samo ustanove u izabranom okrugu. `district` u `choice_filter` se odnosi na kolonu `district` u CSV datoteci; `${district}` se odnosi na polje formulara nazvano `district`.

## Upotrebe

Pitanja sa izborom iz datoteke se uobičajeno koriste za:

1. **Dugačke liste opcija** — zdravstvene ustanove, škole, sela, liste vrsta (stotine ili hiljade stavki)
2. **Često ažurirane liste** — kada se matična lista menja između rundi ankete, ažurirajte samo CSV bez ponovne izgradnje formulara
3. **Deljeni referentni podaci** — jedna CSV datoteka korišćena u više formulara
4. **Filtrirani kaskadni izbori** — učitajte sve regione/okruge/sela u jednu datoteku, zatim filtrirajte prema nadređenom izboru

## Prilaganje datoteke

Kada otpremate formular na rtSurvey, priložite CSV datoteku kao **medijski prilog**. Naziv datoteke u definiciji formulara mora tačno odgovarati nazivu datoteke priloga.

{{% alert icon=" " context="warning" %}}
Nazivi datoteka su osetljivi na velika/mala slova. `Health_Facilities.csv` i `health_facilities.csv` se tretiraju kao različite datoteke.
{{% /alert %}}

## Korišćenje `choice-label()` sa from-file

Za prikaz oznake izabrane opcije u polju napomene ili proračuna:

| type | name | label | calculation |
|------|------|-------|-------------|
| select_one_from_file health_facilities.csv | facility | Izaberite ustanovu | |
| calculate | facility_label | | choice-label(${facility}, ${facility}) |
| note | summary | Izabrana ustanova: ${facility_label} | |

## Najbolje prakse

1. Zadržite CSV datoteke ispod 5.000 redova za dobre performanse na mobilnim uređajima.
2. Uvek uključite kolone `name` i `label` — dodatne kolone su opcione.
3. Za kaskadne izbore, koristite jednu CSV sa kolonom roditeljskog elementa i filtrirajte sa `choice_filter`.
4. Verzionirajte nazive CSV datoteka (npr. `facilities_v3.csv`) kada pravite prelomne promene u strukturi kolona.
5. Pažljivo testirajte izraze filtriranja — greška u pisanju u `choice_filter` će tiho prikazati nula opcija.

## Ograničenja

- Veoma velike CSV datoteke (10.000+ redova) mogu usporiti učitavanje formulara, posebno na uređajima nižeg ranga.
- CSV datoteke moraju biti otpremljene zajedno sa formularom — ne mogu biti preuzete sa URL-a u vreme izvođenja (koristite `search()` ili `pulldata()` za dinamička pretraživanja).
- `select_multiple_from_file` je manje uobičajeno podržan u klijentima — proverite kompatibilnost pre upotrebe.

## Poređenje sa `search()`

| | `select_one_from_file` | Izgled `search()` |
|--|----------------------|----------------------|
| Izvor opcija | Priložena CSV/XML datoteka | Upit baze podataka na strani servera |
| Radi van mreže | Da (datoteka je priložena) | Zahteva vezu |
| Broj opcija | Ograničen memorijom uređaja | Neograničen (paginiran) |
| Podaci u realnom vremenu | Ne | Da |

Za velike, često promenjive ili serverske skupove podataka, pogledajte [Dinamičku pretragu](../advanced-extension/dynamic-search).
