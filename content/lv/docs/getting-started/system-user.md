---
weight: 15
date: "2026-03-04T00:00:00+00:00"
draft: false
title: "Sistēmas lietotājs"
icon: "people"
toc: true
description: "Pārvaldiet lomas, atļaujas un iekārtošanu visiem platformas dalībniekiem."
tags: ["Lietotāji", "Piekļuves kontrole", "Iekārtošana", "Lomas"]
---

# Sistēmas lietotāju pārvaldība

Modulis **Sistēmas lietotājs** (`/cpms/cpmsSystemUser/admin`) ir visaptverošs pārvaldības interfeiss, kas kontrolē, kam ir piekļuve jūsu Real-Time Survey platformai (RT-CPMS) un kādas darbības viņi var veikt.

![Sistēmas lietotāja interfeiss](/images/system_user.png)

## Vienotā pārvaldības pieeja

RT-CPMS sistēmā **enumerators** ir vienkārši konkrēta loma, kas piešķirta sistēmas lietotājam. Nav atsevišķas "enumeratora" datu bāzes. Neatkarīgi no tā, vai lietotājs ir augsta līmeņa administrators, kas uzrauga tīmekļa portālu, vai lauka enumerators, kas vāc datus ar mobilo lietotni — visi tiek pārvaldīti šajā vienotajā satvarā.

## Galvenās funkcijas

### 1. Lietotāju direktorijs un režģa skats
Galvenais interfeiss parāda visu darba vietai pievienoto lietotāju lapu sarakstu. Galvenie atribūti ietver:
* **Organizācijas ID un nosaukums**: Lietotāju loģiskā grupēšana pa konkrētām organizatoriskajām vienībām (piemēram, `rta`, `partner_org`).
* **Loma**: Norāda lietotāja atļaujas līmeni (piemēram, `Administrators`, `Komandas vadītājs`, `Enumerators`).
* **Grupa**: Telpiskās vai loģiskās grupēšanas piešķīrumi (piemēram, konkrēti apgabali vai operacionālās komandas).
* **Ir sinhronizēts**: Norāda, vai konts ir veiksmīgi integrēts ar centrālo vienas pieteikšanās (SSO) sistēmu.
* **Statuss**: Vizuālie indikatori, kas apstiprina, vai konts ir `Aktīvs`, `Neaktīvs`, `Dzēsts` vai `Bloķēts`.

**Globālās darbības:**
* **Pievienot sistēmas lietotāju**: Manuāli izveidojiet atsevišķu profilu.
* **Importēt sistēmas lietotāju**: Lielapjoma kontu augšupielāde, izmantojot Excel veidni. Varat atrisināt konfliktus, izmantojot `Izlaist` vai `Aizstāt` režīmus, un tieši sinhronizēt ar SSO.
* **Lielapjoma dzēšana**: Vairāku atlasi atbalsts kontu lielapjoma noņemšanai.

### 2. Piekļuves kontrole un drošība
Veidojot vai rediģējot lietotāja profilu, ir pieejami vairāki kritiski drošības un darbplūsmas lauki:
* **Lietotāja kods**: Unikāls identifikators, kas saista lokālo CPMS kontu ar centrālo SSO repozitoriju.
* **Ierīces maiņas kods**: Stabils drošības žetons, kas nepieciešams, kad enumeratoram jāpārslēdzas uz citu mobilo ierīci datu vākšanai.
* **Jaudas līmenis**: Granulāra prioritātes/piekļuves skala no 0 (zemākā) līdz 20 (augstākā).
* **Uzraudzības pārslēgšana**: Izvēles rūtiņa, kas uzreiz paaugstina standarta lietotāju uz pārvaldības statusu.
* **Darbplūsmas automatizācija**: Iespēja "Automātiski apstiprināt rediģēšanas pieprasījumu", kas vienkāršo datu tīrīšanas un verifikācijas procesu uzticamiem lietotājiem.

### 3. Kodu pārvaldība (automatizēta iekārtošana)
Atrodama cilnē "Kods", šī funkcija pārvalda jaucēj-bāzētas reģistrācijas un uzaicinājumu saites, vienkāršojot lielām komandām iekārtošanas procesu.

* **Reģistrācija pret uzaicinājumu**: Izvēlieties, vai lietotāji var pašreģistrēties, izmantojot izplatītu saiti, vai viņiem nepieciešams tiešs administratora uzaicinājums.
* **Derīguma datumi**: Ierobežojiet iekārtošanu uz konkrētiem laika logiem.
* **Lietošanas ierobežojumi**: Ierobežojiet lietotāju skaitu, kas var pievienoties, izmantojot vienu ģenerētu kodu.
* **Iepriekš piešķirtās lomas**: Lietotāji, kuri pievienojas, izmantojot šos kodus, automātiski manto iepriekš definēto lomu un jaudas līmeni, nodrošinot, ka viņi ir gatavi strādāt nekavējoties bez manuālas administratora iejaukšanās.
