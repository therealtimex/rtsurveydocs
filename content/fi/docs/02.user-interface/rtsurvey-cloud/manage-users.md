---
title: "Käyttäjien hallinta"
description: "Luo, järjestä ja hallitse järjestelmäkäyttäjiä ja kenttähenkilöstöä."
icon: "cloud"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 314
---

**Käyttäjien hallinta** -moduuli (usein nimeltään **Henkilöstön hallinta** Asennus-valikossa) on keskitetty hakemisto kaikkien CPMS-ympäristösi tilien käsittelyyn. Se tarjoaa projektin järjestelmänvalvojille työkalut henkilöstön perehdyttämiseen, roolien määrittämiseen ja maantieteellisten käyttöoikeustasojen säätelemiseen.

![Käyttäjien hallintakäyttöliittymä](/images/manage_users.png)

## Käyttäjäruudukon yleiskatsaus

Pääkäyttöliittymässä on kattava ruudukko, jossa näkyvät kaikki rekisteröidyt henkilöstön jäsenet. Tämä näkymä antaa järjestelmänvalvojille mahdollisuuden nopeasti hakea, suodattaa ja tarkistaa tilien tilat.

### Tärkeimmät datakolumnit

Ruudukko sisältää seuraavat olennaiset tiedot jokaiselle käyttäjälle:

- **Käyttäjätunnus ja koko nimi:** Henkilöstön jäsenen ensisijaiset tunnisteet.
- **Sähköposti:** Tiliin liitetty yhteydenottosähköposti.
- **Käyttäjärooli:** Ilmaisee käyttäjälle myönnetyt järjestelmäoikeudet (esim. Järjestelmänvalvoja, Henkilöstö, Valvoja, Vieras).
- **Ryhmä:** Näyttää tietyn käyttäjäryhmän tai tiimin, johon henkilöstön jäsen kuuluu.
- **Tila:** Ilmaisee, onko tili tällä hetkellä **Aktiivinen** vai **Epäaktiivinen**.
- **Luomispäivämäärä:** Aikaleima, jolloin tili rekisteröitiin.

## Henkilöstön hallintatoiminnot

Järjestelmänvalvojilla on käytettävissä joukko työkaluja käyttäjätilien perehdyttämiseen ja ylläpitoon, joihin pääsee ylätoimintapaneelista:

- **Lisää henkilöstöä:** Avaa yksityiskohtaisen luomislomakkeen uuden käyttäjän profiilin manuaaliseen syöttämiseen, mukaan lukien heidän roolinsa, määritetyt alueet ja yhteystiedot.
- **Tuo henkilöstöä:** Mahdollistaa tilien joukkoterälyksen lataamalla Excel-taulukon. Tämä on erityisen hyödyllistä suurten kenttätiimien nopeaan perustamiseen.
- **Lataa tuontimalli:** Tarjoaa standardoidun `.xlsx`-mallin, joka vaaditaan joukkotuontiprosessissa.
- **Vie Exceliin:** Luo ladattavan raportin, joka sisältää ruudukon suodatetun käyttäjälistan ja heidän tietonsa.
- **Poista:** Poistaa pysyvästi valitut käyttäjätilit järjestelmästä.

## Käyttäjäprofiilit ja tehtävät

Luotaessa tai muokattaessa tiettyä käyttäjää (**Lisää henkilöstöä** -painikkeen kautta tai napsauttamalla käyttäjätunnusta), järjestelmänvalvojat voivat konfiguroida yksityiskohtaisia profiileja:

- **Henkilökohtaiset tiedot:** Kentät syntymäajalle, sukupuolelle, henkilötunnukselle ja avatarikuvalle.
- **Yhteystiedot:** Matkapuhelinnumero ja yksityiskohtaiset sijaintitiedot (maakunta, piiri, kunta, osoite).
- **Järjestelmämääritykset:** Tietoturvan kannalta kriittisiä — järjestelmänvalvojat voivat linkittää käyttäjiä tiettyihin **alueisiin** ja määrittää tarkat **käyttäjäroolit**.
- **Valvontakonfiguraatio:** Kehittyneissä asennuksissa käyttäjille voidaan määrittää tiettyjä valvontakoodeja tai heitä voidaan kartoittaa tiettyihin tabletteihin (laitteisiin).
