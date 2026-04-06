---
weight: 15
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Sistemski korisnik"
icon: "people"
toc: true
description: "Upravljanje ulogama, dozvolama i uključivanjem svih učesnika platforme."
tags: ["Korisnici", "Kontrola pristupa", "Uključivanje", "Uloge"]
---

# Upravljanje sistemskim korisnicima

Modul **Sistemski korisnik** (`/cpms/cpmsSystemUser/admin`) je sveobuhvatan upravljački interfejs za kontrolu ko ima pristup vašoj platformi Real-Time Survey (RT-CPMS) i koje akcije može da obavlja.

![Interfejs sistemskog korisnika](/images/system_user.png)

## Objedinjen pristup upravljanju

U RT-CPMS sistemu, **Anketar** je jednostavno specifična uloga dodeljena sistemskom korisniku. Ne postoji zasebna baza podataka za "Anketare". Bez obzira da li je korisnik visokorangiran administrator koji prati veb portal ili terenski anketar koji prikuplja podatke putem mobilne aplikacije, svi se upravljaju unutar ovog jedinstvenog, objedinjenog okvira.

## Ključne funkcije

### 1. Direktorijum korisnika i prikaz mreže
Glavni interfejs prikazuje paginiranu listu svih korisnika povezanih sa radnim prostorom. Ključni atributi uključuju:
* **ID i naziv organizacije**: Logičko grupisanje korisnika pod određenim organizacionim entitetima (npr. `rta`, `partner_org`).
* **Uloga**: Specificira nivo dozvola korisnika (npr. `Administrator`, `Vođa tima`, `Anketar`).
* **Grupa**: Prostorna ili logička dodeljivanja grupama (npr. određeni okruzi ili operativne ekipe).
* **Sinhronizovano**: Označava da li je nalog uspešno integrisan sa centralnim sistemom jedinstvene prijave (SSO).
* **Status**: Vizualni indikatori koji potvrđuju da li je nalog `Aktivan`, `Neaktivan`, `Obrisan` ili `Blokiran`.

**Globalne akcije:**
* **Dodaj sistemskog korisnika**: Ručno kreiranje individualnog profila.
* **Uvezi sistemske korisnike**: Masovno otpremanje naloga koristeći Excel šablon. Možete rešavati konflikte korišćenjem režima `Preskoči` ili `Zameni` i sinhronizovati direktno sa SSO sistemom.
* **Masovno brisanje**: Podrška za višestruki izbor radi masovnog uklanjanja naloga.

### 2. Kontrola pristupa i bezbednost
Kada kreirate ili uređujete korisnički profil, dostupna su nekoliko kritičnih polja za bezbednost i radni tok:
* **Korisnički kod**: Jedinstveni identifikator koji povezuje lokalni CPMS nalog sa centralnim SSO repozitorijumom.
* **Kod za promenu uređaja**: Robustan bezbednosni token koji je neophodan kada anketar treba da promeni mobilni uređaj koji koristi za prikupljanje podataka.
* **Nivo ovlašćenja**: Granularna skala prioriteta/pristupa koja se kreće od 0 (najniži) do 20 (najviši).
* **Prekidač za nadzor**: Polje za potvrdu koje odmah uzdiže standardnog korisnika na status menadžmenta.
* **Automatizacija radnog toka**: Opcija za "Automatsko odobravanje zahteva za uređivanje", koja pojednostavljuje proces čišćenja i verifikacije podataka za pouzdane korisnike.

### 3. Upravljanje kodovima (automatizovano uključivanje)
Pronađeno pod pod-karticom "Kod", ova funkcija upravlja registracionim i pozivnim vezama zasnovana na heš kodu, pojednostavljujući proces uključivanja za velike ekipe.

* **Registracija vs. pozivnica**: Odaberite da li se korisnici mogu registrovati sami koristeći distribuiranu vezu ili im je potrebna direktna administratorska pozivnica.
* **Datumi isteka**: Ograničite uključivanje na određene vremenske prozore.
* **Ograničenja upotrebe**: Ograničite broj korisnika koji se mogu pridružiti koristeći jedan generisani kod.
* **Unapred dodeljene uloge**: Korisnici koji se pridruže putem ovih kodova automatski nasleđuju unapred definisanu ulogu i nivo ovlašćenja, čime se osigurava da su odmah spremni za rad bez ručnog administratorskog uplitanja.
