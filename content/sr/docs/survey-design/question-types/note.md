---
title: "Note"
description: "Pitanja tipa note prikazuju tekst ili medije samo za čitanje radi pružanja informacija ili uputstava u vašoj anketi."
icon: "info"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 255
---

Tip pitanja note u XLSForm-ovima i rtSurvey-u se koristi za prikazivanje teksta ili medija samo za čitanje ispitaniku ankete. Nije pitanje koje zahteva odgovor, već način pružanja informacija, uputstava ili konteksta unutar ankete.

## Osnovna XLSForm specifikacija

| type | name | label |
|------|------|-------|
| note | info_text | Ova anketa se tiče vaših navika čitanja. |

Za više detalja o osnovnom tipu pitanja note, pogledajte [XLSForm specifikaciju](https://xlsform.org/en/#question-types).

## Upotrebe

Pitanja tipa note se uobičajeno koriste za:

1. Pružanje uputstava ili konteksta za naredna pitanja
2. Prikazivanje izračunatih rezultata ili rezimea
3. Prikazivanje slika ili drugih medija
4. Odvajanje sekcija ankete
5. Davanje povratnih informacija zasnovanih na prethodnim odgovorima

## Najbolje prakse

1. Zadržite tekst napomene konciznim i jasnim kako biste održali angažovanje ispitanika.
2. Koristite formatiranje (podebljano, kurziv) da biste naglasili važne informacije.
3. Razmotrite korišćenje medija (slike, audio) za poboljšanje razumevanja kada je to prikladno.
4. Koristite napomene štedljivo kako biste izbegli pretrpavanje ankete.

## Primer upotrebe

Evo primera kako biste mogli koristiti pitanja tipa note u anketi:

| type | name | label |
|------|------|-------|
| note | intro | Dobrodošli u našu anketu o navikama čitanja. Pitaćemo vas o vašim preferencijama i učestalosti čitanja. |
| ... | ... | ... |
| calculate | books_per_month | ${fiction_books} + ${non_fiction_books} |
| note | reading_summary | Čitate otprilike ${books_per_month} knjiga mesečno. |

U ovom primeru, koristimo napomene za uvođenje ankete i pružanje rezimea izračunatih rezultata.

## rtSurvey proširenja

Dok je osnovna XLSForm specifikacija za pitanja tipa note jednostavna, rtSurvey može ponuditi dodatne funkcije ili prilagođavanja:

1. Formatiranje bogatog teksta
2. Podrška za ugrađene medije (slike, audio, video)
3. Dinamički sadržaj zasnovan na prethodnim odgovorima
4. Opcije prilagođenog stila

## Napredna upotreba

### Uslovni prikaz

Možete koristiti izraze relevantnosti za uslovni prikaz napomena:

| type | name | label | relevant |
|------|------|-------|----------|
| note | high_reader_note | Vi ste strastveni čitalac! | ${books_per_month} > 5 |

### Uključivanje proračuna

Napomene mogu uključivati proračune za pružanje dinamičkih povratnih informacija:

| type | name | label |
|------|------|-------|
| note | reading_time | Na osnovu vaših odgovora, provodite otprilike ${books_per_month * 5} sati mesečno čitajući. |

## Ograničenja

- Napomene ne prikupljaju podatke, pa se ne treba koristiti kada je potrebno prikupiti informacije od ispitanika.
- Prekomerna upotreba napomena može anketu učiniti pretrpanom ili previše dugom.
- Neke napredne opcije formatiranja ili medija možda nisu podržane na svim uređajima ili platformama.
