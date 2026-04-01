---
title: "Palvelimeen yhdistäminen"
description: "Opi yhdistämään rtSurvey-mobiilisovellus projektipalvelimeesi, käyttämään roolipohjaisia toimintoja ja aloittamaan yhteistyö useissa projekteissa."
icon: "cloud_sync"
date: "2023-05-22T00:34:57+01:00"
lastmod: "2023-05-22T00:34:57+01:00"
draft: false
weight: 313
---

rtSurvey-sovelluksen yhdistäminen palvelimeen on välttämätön askel sovelluksen käytön aloittamiseksi tiedonkeruuseen, hallintaan ja analyysiin. Tämä prosessi varmistaa, että kaikki kyselyn roolit voivat käyttää tarvittavia toimintoja ja tietoja reaaliajassa.

## Tärkeimmät erot ODK Collectiin verrattuna

rtSurvey tarjoaa parannettuja toimintoja verrattuna ODK Collectiin eri kyselyn rooleja varten:
- **Järjestelmänvalvoja**: Viestintä, ilmoitukset päivityksistä (tietojen lähetys, uudet raportit, uudet tilit), lomakkeiden täyttäminen ja analyysiraporttien tarkastelu.
- **Projektipäällikkö**: Vastaavat toiminnot kuin järjestelmänvalvojilla, mukaan lukien projektin asetus ja hallinta.
- **Kyselyn suunnittelija**: Viestintä, ilmoitukset, lomakkeiden täyttäminen ja analyysiraporttien tarkastelu.
- **Kenttähaastattelija**: Lomakkeiden täyttäminen, viestintä, ilmoitukset ja edistymisraportit.
- **Data-analyytikko**: Viestintä, ilmoitukset ja pääsy analytiikkaraportteihin.

## Vaiheet rtSurvey-sovelluksen yhdistämiseksi palvelimeen

### 1. Varmista, että sinulla on tili

Yhdistääksesi palvelimeen tarvitset tilin. Tilit voi luoda järjestelmänvalvoja tai henkilöstö järjestelmänvalvojan asettaman tilinluonti-URL:n avulla.

### 2. Avaa rtSurvey-sovellus

Käynnistä rtSurvey-sovellus mobiililaitteellasi. Jos et ole vielä asentanut sitä, katso [rtSurvey-sovelluksen asentaminen](#installing-rtsurvey-app) -sivu.

### 3. Käytä palvelinyhteyden asetuksia

1. Avaa sovellus ja siirry asetusvalikkoon.
2. Valitse vaihtoehto yhdistääksesi palvelimeen.

### 4. Syötä tilitiedot ja valitse projekti

Yhdistäessäsi rtSurveyhin prosessi on virtaviivainen tilisi konfiguraation perusteella:

- **Käyttäjätunnus**: Syötä tilisi käyttäjätunnus.
- **Salasana**: Syötä tilisi salasana.

Tunnistetietojen syöttämisen jälkeen:

- Jos tilisi on liitetty vain yhteen kyselyprojektiin:
  - Sovellus kirjaa sinut automaattisesti kyseisen projektin palvelimeen.
  - Sinun ei tarvitse syöttää palvelimen URL-osoitetta tai valita projektia manuaalisesti.

- Jos tilisi on liitetty useisiin kyselyprojekteihin:
  - Onnistuneen todennuksen jälkeen näet luettelon projekteista, joihin sinulla on pääsy.
  - Valitse projekti, jolla haluat työskennellä, tästä luettelosta.

### 5. Todennus

Palvelintietojen syöttämisen jälkeen napauta "Yhdistä" tai "Kirjaudu sisään" -painiketta. Sovellus todentaa tunnistetietosi ja muodostaa yhteyden palvelimeen.

```mermaid
flowchart TD
    A["📱 Käynnistä rtSurvey-sovellus"] --> B["🔑 Syötä käyttäjätunnus<br>ja salasana"]
    style A fill:#4CAF50,stroke:#666666,stroke-width:3px,color:white
    style B fill:#2196F3,stroke:#666666,stroke-width:3px,color:white

    B --> C{"🌳 Useita<br>projekteja?"}
    style C fill:#FFC107,stroke:#666666,stroke-width:3px,color:black

    C -->|Kyllä| D["📋 Näytä<br>projektiluettelo"]
    C -->|Ei| E["🔄 Yhdistä automaattisesti<br>yhteen projektiin"]
    style D fill:#FF9800,stroke:#666666,stroke-width:3px,color:white
    style E fill:#009688,stroke:#666666,stroke-width:3px,color:white

    D --> F["👆 Käyttäjä valitsee<br>projektin"]
    style F fill:#FF5722,stroke:#666666,stroke-width:3px,color:white

    E --> G["☁️ Yhdistä palvelimeen"]
    F --> G
    style G fill:#3F51B5,stroke:#666666,stroke-width:3px,color:white
    G --> H["👥 Käytä roolipohjaisia<br>toimintoja"]
    style H fill:#9C27B0,stroke:#666666,stroke-width:3px,color:white

    H --> I["👨‍💼 Järjestelmänvalvoja/<br>Projektipäällikkö"]
    H --> J["🎨 Kyselyn suunnittelija"]
    H --> K["📝 Kenttähaastattelija"]
    H --> L["📊 Data-analyytikko"]
    style I fill:#E91E63,stroke:#666666,stroke-width:3px,color:white
    style J fill:#795548,stroke:#666666,stroke-width:3px,color:white
    style K fill:#607D8B,stroke:#666666,stroke-width:3px,color:white
    style L fill:#8BC34A,stroke:#666666,stroke-width:3px,color:white

    I --> M["💬 Viestintä<br>🔔 Ilmoitukset<br>📄 Lomakkeiden täyttäminen<br>📈 Raporttien tarkastelu"]
    J --> N["💬 Viestintä<br>🔔 Ilmoitukset<br>🧪 Lomakkeiden testaus<br>📈 Raporttien tarkastelu"]
    K --> O["📝 Lomakkeiden täyttäminen<br>💬 Viestintä<br>🔔 Ilmoitukset<br>📊 Edistymisraportit"]
    L --> P["💬 Viestintä<br>🔔 Ilmoitukset<br>📊 Analytiikkaraportit"]
    style M fill:#FF4081,stroke:#666666,stroke-width:3px,color:white
    style N fill:#9E9E9E,stroke:#666666,stroke-width:3px,color:white
    style O fill:#00BCD4,stroke:#666666,stroke-width:3px,color:white
    style P fill:#CDDC39,stroke:#666666,stroke-width:3px,color:white
```

## Yhteysongelmien vianmääritys

Jos kohtaat ongelmia palvelimeen yhdistämisessä:

1. **Tarkista Internet-yhteys**: Varmista, että laitteesi on yhdistettynä Internetiin.
2. **Vahvista tunnistetiedot**: Varmista, että käyttäjätunnus ja salasana ovat oikein.
3. **Käynnistä sovellus uudelleen**: Sulje ja avaa rtSurvey-sovellus uudelleen.
4. **Ota yhteyttä tukeen**: Jos ongelmat jatkuvat, ota yhteyttä järjestelmänvalvojaasi tai rtSurveyn tukeen.

## Johtopäätös

rtSurvey-sovelluksen yhdistäminen palvelimeen on yksinkertainen prosessi, joka mahdollistaa sovelluksen täysien ominaisuuksien hyödyntämisen. Noudattamalla yllä esitettyjä vaiheita voit varmistaa saumattoman tiedonkeruun, -hallinnan ja -analyysin, joka on räätälöity kyselyroolillesi.
