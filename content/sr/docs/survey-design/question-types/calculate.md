---
title: "Calculate"
description: ""
icon: "calculate"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 235
---

Pitanja tipa calculate u XLSForm-ovima i rtSurvey-u se koriste za obavljanje proračuna zasnovanih na drugim poljima ili vrednostima u vašem formularu. Ova pitanja se ne prikazuju korisniku, već se izvršavaju u pozadini, čuvajući rezultate za kasniju upotrebu ili slanje.

## Sintaksa

U XLSForm-u, pitanje tipa calculate je definisano na sledeći način:

| type      | name     | label | calculation |
|-----------|----------|-------|-------------|
| calculate | calc_q1  |       | ${q1} + ${q2} |

- **type**: Uvek "calculate" za ovaj tip pitanja.
- **name**: Jedinstveno ime za pitanje tipa calculate.
- **label**: Obično ostavljeno praznim jer se pitanja tipa calculate ne prikazuju korisnicima.
- **calculation**: Formula koja se evaluira.

## Upotrebe

Pitanja tipa calculate se uobičajeno koriste za:

1. Obavljanje aritmetičkih operacija
2. Spajanje stringova
3. Primenu složene logike ili funkcija
4. Čuvanje međurezultata za kasniju upotrebu

## Primeri

### Osnovna aritmetika

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | total    | ${price} * ${quantity} |
```

### Spajanje stringova

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | full_name| concat(${first_name}, ' ', ${last_name}) |
```

### Korišćenje funkcija

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | age      | int((today() - ${date_of_birth}) / 365.25) |
```

## Napredna upotreba u rtSurvey-u

### Funkcija pulldata()

rtSurvey podržava funkciju `pulldata()` u poljima calculate, dozvoljavajući vam da preuzimate podatke iz spoljnih CSV datoteka:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | city     | pulldata('cities', 'city_name', 'zip_code', ${zip_input}) |
```

#### Sintaksa

Osnovna sintaksa za pulldata() je:

```
pulldata('naziv_csv_datoteke', 'kolona_za_povrat', 'kljucna_kolona', ${vrednost_za_trazenje})
```

- 'naziv_csv_datoteke': Naziv CSV datoteke (bez ekstenzije .csv)
- 'kolona_za_povrat': Naziv kolone koja sadrži podatke koje želite da preuzmete
- 'kljucna_kolona': Naziv kolone za podudaranje
- ${vrednost_za_trazenje}: Vrednost za traženje u ključnoj koloni (često promenljiva iz formulara)

#### Važne napomene

1. CSV datoteka mora biti otpremljena zajedno sa vašim XLSForm-om prilikom primene ankete.
2. Koristite zareze kao separatore u vašoj CSV datoteci, ne tačke-zareze.
3. Izbegavajte zareze unutar polja podataka vaše CSV datoteke, jer mogu izazvati probleme pri parsiranju.
4. pulldata() podržava samo odnose 1-prema-1. Ako se pronađe više podudaranja, vraća samo prvo.
5. Mogu postojati ograničenja dužine teksta koji se može preuzeti (oko 76 karaktera).
6. Možete koristiti pulldata() u ograničenjima za validaciju unosa prema CSV podacima.

### Uslovni proračuni

Možete koristiti if() iskaze za uslovne proračune:

```
| type      | name     | calculation |
|-----------|----------|-------------|
| calculate | discount | if(${total} > 1000, ${total} * 0.1, 0) |
```

## Najbolje prakse

1. Koristite smislena imena za polja calculate da biste poboljšali čitljivost formulara.
2. Izbegavajte previše složene proračune u jednom polju; po potrebi ih razložite.
3. Temeljno testirajte vaše proračune, posebno kada koristite složene formule ili spoljne podatke.
4. Zapamtite da polja calculate se izvršavaju svaki put kada se formular evaluira, što može uticati na performanse za veoma složene ili brojne proračune.
5. Kada koristite pulldata(), osigurajte da su vaše CSV datoteke ispravno formatirane i temeljno testirajte sa vašim specifičnim podacima i strukturom formulara.

## Ograničenja

- Polja calculate nije moguće direktno uređivati od strane korisnika.
- Rezultat polja calculate nije odmah vidljiv osim ako nije referenciran u polju za prikaz ili korišćen u logici formulara.
