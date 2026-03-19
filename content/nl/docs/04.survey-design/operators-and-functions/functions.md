---
title: "Functies"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

### Tekenreeksfuncties

{{% alert icon=" " context="warning" %}}
Bij het werken met tekenreeksen in expressies is het belangrijk om enkelvoudige aanhalingstekens ('') te gebruiken om letterlijke tekenreeksen te omsluiten. Een uitzondering doet zich voor wanneer u enkelvoudige aanhalingstekens binnen een letterlijke tekenreeks wilt opnemen. In dat geval kunt u dubbele aanhalingstekens ("") gebruiken om de gehele tekenreeks te omsluiten.

Bijvoorbeeld:
- Correct: if(${yesno} = 1, "een tekenreeks met 'enkelvoudige aanhalingstekens' erin", "geen enkelvoudige aanhalingstekens hier")
- Incorrect: if(${yesno} = 1, 'een tekenreeks met 'enkelvoudige aanhalingstekens' erin', 'geen enkelvoudige aanhalingstekens hier')

Wat betreft slimme aanhalingstekens: het is cruciaal u bewust te zijn van hun aanwezigheid, omdat ze problemen kunnen veroorzaken in expressies. Veel tekstverwerkingsprogramma's converteren rechte aanhalingstekens ("" of '') automatisch naar slimme of gebogen aanhalingstekens ("" of ''), wat kan leiden tot syntaxfouten of onverwacht gedrag. Gebruik consequent rechte aanhalingstekens ('') in uw expressies.
{{% /alert %}}

rtSurvey ondersteunt verschillende functies, waaronder:

1. `string(veld)`: Converteert een veld naar een tekenreeks.
   - Voorbeeld: `string(34.8)` wordt geconverteerd naar `'34.8'`.

2. `string-length(veld)`: Geeft de lengte van een tekenreeksveld terug.
   - Voorbeeld: `string-length(.) > 3 and string-length(.) < 10` kan worden gebruikt om te zorgen dat het huidige veld tussen 3 en 10 tekens heeft.

3. `substr(veldoftekenreeks, beginindex, eindindex)`: Geeft een deeltekenreeks terug die begint bij `beginindex` en eindigt net voor `eindindex`. Indexes beginnen bij 0 voor het eerste teken in de tekenreeks.
   - Voorbeeld: `substr(${phone}, 0, 3)` geeft de eerste drie cijfers van een telefoonnummer terug.

4. `concat(a, b, c, ...)`: Voegt velden (en/of tekenreeksen) samen.
   - Voorbeeld: `concat(${firstname}, ' ', ${lastname})` geeft een volledige naam terug door de waarden in de velden `firstname` en `lastname` te combineren.

5. `linebreak()`: Geeft een regeleinde-teken terug.
   - Voorbeeld: `concat(${field1}, linebreak(), ${field2}, linebreak(), ${field3})` geeft een lijst van drie veldwaarden terug met regeleinden ertussen.

6. `lower()`: Converteert een tekenreeks naar alle kleine letters.
   - Voorbeeld: `lower('Street Name')` geeft "street name" terug.

7. `upper()`: Converteert een tekenreeks naar alle hoofdletters.
   - Voorbeeld: `upper('Street Name')` geeft "STREET NAME" terug.

### select_one- en select_multiple-functies

1. `count-selected(veld)`: Geeft het aantal geselecteerde items in een select_multiple-veld terug.
   - Voorbeeld: `count-selected(.) = 3` kan worden gebruikt als beperkingsexpressie om te zorgen dat precies drie keuzes zijn geselecteerd.

2. `selected(veld, waarde)`: Geeft true of false terug afhankelijk van of de opgegeven waarde is geselecteerd in het select_one- of select_multiple-veld.
   - Voorbeeld: `selected(${color}, 'Blue')` kan worden gebruikt als relevantie-expressie om een groep of veld alleen te tonen als de respondent "Blue" heeft geselecteerd als favoriete kleur.
   - Let op: De tweede parameter moet altijd de keuzewaarde specificeren, niet het keuzelabel. Gebruik de waarde uit de waardekolom in het choices-werkblad van de formulierformulering.

3. `selected-at(veld, getal)`: Geeft het geselecteerde item op de opgegeven positie in een select_multiple-veld terug. Wanneer het doorgegeven getal 0 is, geeft het het eerste geselecteerde item terug; wanneer het getal 1 is, geeft het het tweede geselecteerde item terug, enzovoort.
   - Voorbeeld: `selected-at(${fruits}, 0) = 'Apple'` kan worden gebruikt als relevantie-expressie om een groep of veld alleen te tonen als de eerste geselecteerde keuze "Apple" is.
   - Let op: De teruggegeven waarde is de keuzewaarde, niet het keuzelabel.

4. `choice-label(veld, waarde)`: Geeft het label terug voor een select_one- of select_multiple-veldkeuze, zoals gedefinieerd in het choices-werkblad van de formulierformulering.
   - Voorbeeld 1: `choice-label(${country}, ${country})` geeft het keuzelabel terug voor de momenteel geselecteerde keuze in het veld `country`.
   - Voorbeeld 2: `choice-label(${languages}, selected-at(${languages}, 0))` geeft het label terug voor de eerste geselecteerde keuze in het veld `languages`.
   - Let op: Deze functie haalt het keuzelabel op, niet de waarde.

### Herhaalde veldfuncties

In rtSurvey kunt u, als u dezelfde vraag(en) meerdere keren wilt stellen, een veld in een herhalingsgroep plaatsen. Dit resulteert in meerdere instanties van hetzelfde veld. De volgende functies kunnen u helpen met deze herhaalde velden en de herhaalde gegevens die ze produceren.

1. `join(tekenreeks, herhaaldveld)`: Genereert voor een veld binnen een herhalingsgroep een met een scheidingsteken gescheiden lijst van waarden. De eerste parameter specificeert het scheidingsteken.
   - Voorbeeld: `join(', ', ${member_name})` genereert een enkele met komma's gescheiden lijst van alle ingevoerde namen.

2. `join-if(tekenreeks, herhaaldveld, expressie)`: Werkt precies zoals `join()`, maar controleert elke instantie in de herhalingsgroep met de opgegeven expressie. Als de expressie false oplevert, wordt het item weggelaten.
   - Voorbeeld: `join-if(', ', ${member_name}, ${age} >= 18)` genereert een met komma's gescheiden lijst van namen van alleen volwassen leden (leeftijd 18 en ouder).

3. `count(herhalingsgroep)`: Geeft het huidige aantal keren dat een herhalingsgroep is herhaald terug.
   - Voorbeeld: `count(${groupname})` geeft het aantal instanties van de groep terug.

4. `count-if(herhalingsgroep, expressie)`: Werkt precies zoals `count()`, maar controleert elke instantie met de opgegeven expressie. Als de expressie false oplevert, wordt het item weggelaten.
   - Voorbeeld: `count-if(${members}, ${age} >= 18)` geeft het aantal volwassen leden terug op basis van het leeftijdsveld in de herhalingsgroep "members".

5. `sum(herhaaldveld)`: Berekent voor een veld binnen een herhalingsgroep de som van alle waarden.
   - Voorbeeld: `sum(${loan_amount})` geeft de totale waarde van alle leningen terug.

6. `sum-if(herhaaldveld, expressie)`: Werkt precies zoals `sum()`, maar controleert elke instantie met de opgegeven expressie. Als de expressie false oplevert, wordt het item weggelaten.
   - Voorbeeld: `sum-if(${loan_amount}, ${loan_amount} > 500)` geeft de totale waarde terug van alle leningen boven 500. Kleinere leningen worden genegeerd.

7. `min(herhaaldveld)`: Berekent voor een veld binnen een herhalingsgroep het minimum van alle waarden.
   - Voorbeeld: `min(${member_age})` geeft de leeftijd van het jongste lid in de groep terug.

8. `min-if(herhaaldveld, expressie)`: Werkt precies zoals `min()`, maar controleert elke instantie met de opgegeven expressie.
   - Voorbeeld: `min-if(${member_age}, ${member_age} >= 18)` geeft de leeftijd van de jongste volwassene in de groep terug. Degenen jonger dan 18 worden genegeerd.

9. `max(herhaaldveld)`: Berekent voor een veld binnen een herhalingsgroep het maximum van alle waarden.
   - Voorbeeld: `max(${member_age})` geeft de leeftijd van het oudste lid in de groep terug.

10. `max-if(herhaaldveld, expressie)`: Werkt precies zoals `max()`, maar controleert elke instantie met de opgegeven expressie.
    - Voorbeeld: `max-if(${member_age}, ${member_age} >= 18)` geeft de leeftijd van de oudste volwassene in de groep terug. Degenen jonger dan 18 worden genegeerd.

11. `index()`: Wanneer aangeroepen binnen een herhalingsgroep, geeft het het indexnummer terug voor de huidige groep of instantie.
    - Voorbeeld: `index()` wanneer gebruikt binnen een herhalingsgroep geeft 1 terug voor de eerste instantie, 2 voor de tweede, enzovoort.

12. `indexed-repeat(herhaaldveld, herhalingsgroep, index)`: Verwijst vanuit buiten de herhalingsgroep naar een veld of groep die zich binnen de herhalingsgroep bevindt. De eerste parameter specificeert het herhaalde veld of de groep, de tweede specificeert de herhalingsgroep, en de derde specificeert het instantienummer binnen de herhalingsgroep.
    - Voorbeeld 1: `indexed-repeat(${name}, ${names}, 1)` geeft de eerste naam terug wanneer het naamveld zich in een eerdere herhalingsgroep genaamd "names" bevindt.
    - Voorbeeld 2: `indexed-repeat(${name}, ${names}, index())` haalt de naam op die overeenkomt met het instantienummer van de huidige herhalingsgroep.

13. `rank-index(index, herhaaldveld)`: Berekent de ordinale rang van de opgegeven instantie van een herhaald veld voor gebruik buiten de herhalingsgroep. Een rang van 1 wordt toegewezen aan de instantie met de hoogste waarde, een rang van 2 aan de instantie met de op een na hoogste waarde, enzovoort.
    - Voorbeeld: `rank-index(1, ${random_draw})` berekent de rang van de eerste instantie op basis van de waarde van het veld `random_draw` vergeleken met de waarden van andere instanties.

14. `rank-index-if(index, herhaaldveld, expressie)`: Werkt vergelijkbaar met `rank-index()`, maar controleert elke instantie met de opgegeven expressie. Als de expressie false oplevert, wordt het item weggelaten uit de berekening.
    - Voorbeeld: `rank-index-if(1, ${age}, ${age} >= 18)` berekent de leeftijdsrang binnen de set volwassenen, alleen rekening houdend met instanties waar de leeftijd groter dan of gelijk aan 18 is.

### Getaalfuncties

{{< table >}}
| Operator | Bewerking | Voorbeeld | Voorbeeldantwoord |
|----------|-----------|-----------|-------------------|
| `+` | Optelling | 1 + 1 | 2 |
| `-` | Aftrekking | 3 - 2 | 1 |
| `*` | Vermenigvuldiging | 3 * 2 | 6 |
| `div` | Deling | 10 div 2 | 5 |
| `mod` | Modulus | 9 mod 2 | 1 |
{{< /table >}}

rtSurvey ondersteunt getaalfuncties, waaronder:
- `number(veld)`: Converteert de waarde van het veld naar een getal.
  - Voorbeeld: `number('34.8')` = 34.8

- `int(veld)`: Converteert de waarde van het veld naar een integer.
  - Voorbeeld: `int('39.2')` = 39

- `min(veld1, ..., veldx)`: Geeft de minimumwaarde terug van de doorgegeven velden.
  - Voorbeeld: `min(${father_age}, ${mother_age})` geeft de leeftijd terug van ofwel de moeder of de vader, degene die kleiner is.

- `max(veld1, ..., veldx)`: Geeft de maximumwaarde terug van de doorgegeven velden.
  - Voorbeeld: `max(${father_age}, ${mother_age})` geeft de leeftijd terug van ofwel de moeder of de vader, degene die groter is.

- `format-number(veld)`: Formatteert de waarde van een integer- of decimaalveld volgens de landinstellingen van de gebruiker.
  - Voorbeeld: `format-number(${income})` kan "120000" formatteren als "120.000".

- `round(veld, cijfers)`: Rondt de numerieke veldwaarde af op het opgegeven aantal cijfers na de komma.
  - Voorbeeld: `round(${interest_rate}, 2)`

- `abs(getal)`: Geeft de absolute waarde van een getal terug.

- `pow(basis, exponent)`: Geeft de waarde terug van de eerste parameter tot de macht van de tweede parameter.
  - Elke parameter kan een veld, getal of expressie zijn.

- `log10(veldofwaarde)`: Geeft de grondtal-tien logaritme terug van het doorgegeven veld of de waarde.

- `sin(veldofwaarde)`: Geeft de sinus terug van het doorgegeven veld of de waarde, uitgedrukt in radialen.

- `cos(veldofwaarde)`: Geeft de cosinus terug van het doorgegeven veld of de waarde, uitgedrukt in radialen.

- `tan(veldofwaarde)`: Geeft de tangens terug van het doorgegeven veld of de waarde, uitgedrukt in radialen.

- `asin(veldofwaarde)`: Geeft de arcsinus terug van het doorgegeven veld of de waarde, uitgedrukt in radialen.

- `acos(veldofwaarde)`: Geeft de arccosinus terug van het doorgegeven veld of de waarde, uitgedrukt in radialen.

- `atan(veldofwaarde)`: Geeft de arctangens terug van het doorgegeven veld of de waarde, uitgedrukt in radialen.

- `atan2(x, y)`: Geeft de hoek in radialen terug die bij de oorsprong wordt ingesloten door het punt met coördinaten (x, y) en de positieve x-as. Het resultaat ligt in het bereik -pi() tot pi().

- `sqrt(veldofwaarde)`: Geeft de niet-negatieve vierkantswortel terug van het doorgegeven veld of de waarde.

- `exp(x)`: Geeft de waarde terug van e^x.

- `pi()`: Geeft de waarde van pi terug.

### Datum- en tijdfuncties

{{% alert icon=" " context="warning" %}}
Datumwaarden in rtSurvey worden opgeslagen als tekenreeksen in het formaat `JJJJ-MM-DD`. Datum-tijdwaarden worden opgeslagen als ISO 8601-tekenreeksen (`JJJJ-MM-DDTHH:MM:SS`). Gebruik `decimal-date-time()` om te converteren naar een getal voor rekenkundige bewerkingen (bijv. het berekenen van duren).
{{% /alert %}}

1. `today()`: Geeft de datum van vandaag terug als een tekenreeks in het formaat `JJJJ-MM-DD`. Wordt eenmalig geëvalueerd wanneer het formulier wordt geopend.
   - Voorbeeld: `today()` → `'2024-03-15'`
   - Veelgebruikt: In de kolom `default` om de datum van vandaag vooraf in te vullen, of in `relevant`/`constraint` om te vergelijken met een datumveld.

2. `now()`: Geeft de huidige datum en tijd terug als een ISO 8601-tekenreeks. Wordt geëvalueerd elke keer dat de expressie wordt berekend.
   - Voorbeeld: `now()` → `'2024-03-15T14:32:00.000+03:00'`
   - Veelgebruikt: Het vastleggen van de exacte tijdstempel van een specifieke gebeurtenis tijdens de enquête.

3. `date(waarde)`: Converteert een waarde (tekenreeks of getal) naar een datumtekenreeks. Nuttig voor het dwingen van berekende waarden naar een datumtype.
   - Voorbeeld: `date('2024-03-15')` → `'2024-03-15'`

4. `date-time(waarde)`: Converteert een waarde naar een datum-tijdtekenreeks.
   - Voorbeeld: `date-time(${event_timestamp})`

5. `decimal-date-time(waarde)`: Converteert een datum- of datum-tijdtekenreeks naar een decimaal getal dat milliseconden sinds het Unix-tijdperk gedeeld door 86400000 (d.w.z. fractionele dagen sinds 1970-01-01) vertegenwoordigt. Gebruik dit voor rekenkundige bewerkingen op datums.
   - Voorbeeld: Duur in dagen tussen twee datums:
     `decimal-date-time(${end_date}) - decimal-date-time(${start_date})`
   - Voorbeeld: Duur in minuten tussen twee datum-tijden:
     `(decimal-date-time(${end_time}) - decimal-date-time(${start_time})) * 1440`

6. `format-date(datum, formaat)`: Formatteert een datumwaarde met een patroontekenreeks.
   - Formatttokens: `%Y` (4-cijferig jaar), `%y` (2-cijferig jaar), `%m` (maand 01–12), `%d` (dag 01–31), `%a` (afgekorte weekdag), `%b` (afgekorte maandnaam)
   - Voorbeeld: `format-date(today(), '%d/%m/%Y')` → `'15/03/2024'`
   - Voorbeeld: `format-date(${dob}, '%B %d, %Y')` → `'March 15, 1990'`

7. `format-date-time(datumdtijd, formaat)`: Formatteert een datum-tijdwaarde met een patroontekenreeks. Accepteert alle `format-date`-tokens plus:
   - `%H` (uur 00–23), `%h` (uur 01–12), `%M` (minuten 00–59), `%S` (seconden 00–59), `%3` (milliseconden), `%P` (AM/PM)
   - Voorbeeld: `format-date-time(now(), '%d/%m/%Y %H:%M')` → `'15/03/2024 14:32'`
   - Voorbeeld: `format-date-time(${event_time}, '%I:%M %p')` → `'02:32 PM'`

---

### Boolean-functies

1. `boolean(waarde)`: Converteert een willekeurige waarde naar een boolean. Geeft `true` terug voor niet-lege tekenreeksen, niet-nul getallen en `true`; geeft `false` terug voor lege tekenreeksen, `0` en `false`.
   - Voorbeeld: `boolean(${name})` geeft `true` terug als `name` niet leeg is.

2. `boolean-from-string(tekenreeks)`: Geeft `true` terug als de tekenreeks `'1'` of `'true'` is (niet hoofdlettergevoelig); geeft anders `false` terug.
   - Voorbeeld: `boolean-from-string(${enabled_flag})` — nuttig wanneer een veld `'true'`/`'false'` als tekst opslaat.

3. `true()`: Geeft de boolean-waarde `true` terug.
   - Voorbeeld: In de kolom `required` is `true()` equivalent aan `yes`.

4. `false()`: Geeft de boolean-waarde `false` terug.
   - Voorbeeld: `if(${skip_section} = 'yes', false(), true())` — verplicht dynamisch instellen.

5. `not(expressie)`: Geeft de logische negatie van de expressie terug. Geeft `true` terug als de expressie false is, en vice versa.
   - Voorbeeld: `not(${consent} = 'yes')` — toon een waarschuwing wanneer toestemming NIET is gegeven.
   - Voorbeeld: `not(selected(${issues}, 'none'))` — vereist detail alleen als "none" niet is geselecteerd.

---

### Aanvullende tekenreeksfuncties

1. `starts-with(tekenreeks, voorvoegsel)`: Geeft `true` terug als `tekenreeks` begint met `voorvoegsel`.
   - Voorbeeld: `starts-with(${phone}, '+254')` controleert of het telefoonnummer begint met de landcode van Kenia.

2. `contains(tekenreeks, deeltekenreeks)`: Geeft `true` terug als `tekenreeks` `deeltekenreeks` bevat.
   - Voorbeeld: `contains(${email}, '@')` controleert of een e-mailadres een `@`-teken bevat.
   - Voorbeeld: `contains(${notes}, 'urgent')` activeert een vervolgvraag als de notities "urgent" vermelden.

3. `substring-before(tekenreeks, naald)`: Geeft het deel van `tekenreeks` terug dat voor de eerste occurrence van `naald` staat.
   - Voorbeeld: `substring-before(${full_name}, ' ')` extraheert het eerste woord (voornaam).

4. `substring-after(tekenreeks, naald)`: Geeft het deel van `tekenreeks` terug dat na de eerste occurrence van `naald` staat.
   - Voorbeeld: `substring-after(${email}, '@')` extraheert het domeingedeelte van een e-mailadres.

5. `normalize-space(tekenreeks)`: Verwijdert voor- en achterliggende witruimte en reduceert alle interne witruimtereeksen tot een enkele spatie.
   - Voorbeeld: `normalize-space(${name})` — reinigt een naam die mogelijk met extra spaties is getypt.

6. `translate(tekenreeks, zoektekens, vervangingstekens)`: Vervangt elk teken in `tekenreeks` dat voorkomt in `zoektekens` door het overeenkomende teken in `vervangingstekens`. Tekens in `zoektekens` zonder overeenkomend teken in `vervangingstekens` worden verwijderd.
   - Voorbeeld: `translate(${code}, 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')` converteert naar hoofdletters (equivalent aan `upper()`).
   - Voorbeeld: `translate(${phone}, ' -()', '')` verwijdert spaties, koppeltekens en haakjes uit een telefoonnummer.

---

### Aanvullende wiskundefuncties

1. `floor(getal)`: Geeft het grootste integer terug dat kleiner dan of gelijk aan `getal` is (rondt naar negatief oneindig af).
   - Voorbeeld: `floor(4.9)` = 4, `floor(-2.1)` = -3

2. `ceiling(getal)`: Geeft het kleinste integer terug dat groter dan of gelijk aan `getal` is (rondt naar positief oneindig af).
   - Voorbeeld: `ceiling(4.1)` = 5, `ceiling(-2.9)` = -2

3. `random()`: Geeft een willekeurig decimaal getal terug tussen 0,0 (inclusief) en 1,0 (exclusief). Typisch gebruikt in `calculate`-velden om willekeurige waarden toe te wijzen of vraagvolgorde te randomiseren.
   - Voorbeeld: `random()` → bijv. `0.7341`
   - Voorbeeld: `int(random() * 6) + 1` → willekeurig getal 1–6 (dobbelsteenworp)

4. `coalesce(a, b)`: Geeft `a` terug als `a` niet leeg is; geeft anders `b` terug. Nuttig als terugvaloptie wanneer een veld leeg kan zijn.
   - Voorbeeld: `coalesce(${preferred_name}, ${full_name})` — gebruik voorkeursnaam indien ingesteld, val anders terug op volledige naam.

5. `once(waarde)`: Evalueert `waarde` en slaat het op, maar alleen als het huidige veld **leeg** is. Als het veld al een waarde heeft (bijv. eerder ingesteld), geeft `once()` de bestaande waarde ongewijzigd terug. Dit voorkomt dat herberekening gebruikersinvoer overschrijft.
   - Voorbeeld: `once(today())` in de kolom `default` stelt de datum van vandaag eenmalig in en werkt niet bij als de enumerator het formulier opnieuw opent.
   - Voorbeeld: `once(uuid())` genereert eenmalig een UUID en houdt deze stabiel bij bewerkingen.

---

### Geo-functies

1. `area(geoshape_waarde)`: Berekent de **oppervlakte in vierkante meters** die is ingesloten door een geoshape-waarde (polygoon).
   - De parameter is een geoshape-veldwaarde in het formaat `lat1 lon1 0 0; lat2 lon2 0 0; ...`
   - Voorbeeld: `area(${field_boundary})` — bereken de oppervlakte van een veld in m².
   - Voorbeeld: `round(area(${field_boundary}) div 10000, 2)` — converteren naar hectare.

2. `distance(coördinaten)`: Berekent de **totale padlengte in meters** van een geotrace (lijn), of de afstand tussen twee geopoints.
   - Voor een geotrace: `distance(${route})` geeft de totale padlengte in meters terug.
   - Voor twee geopoints: `distance(concat(${point_a}, ' ', ${point_b}))` geeft de afstand ertussen terug.
   - Voorbeeld: `round(distance(${road_trace}) div 1000, 3)` — weglengte in kilometers.

---

### Validatiefuncties

1. `regex(waarde, patroon)`: Geeft `true` terug als `waarde` overeenkomt met de reguliere expressie `patroon`. Gebruik in de kolom `constraint` voor patroongebaseerde validatie.
   - Het patroon gebruikt standaard regex-syntaxis (POSIX ERE-subset).
   - Voorbeeld: `regex(., '^[0-9]{10}$')` — valideer een 10-cijferig getal.
   - Voorbeeld: `regex(., '^[A-Z]{2}[0-9]{6}$')` — valideer een paspoortnummerformaat (2 hoofdletters gevolgd door 6 cijfers).
   - Voorbeeld: `regex(., '^[^@]+@[^@]+\.[^@]{2,}$')` — basiscontrole e-mailformaat.

2. `checklist(min, max, v1, v2, ...)`: Evalueert een lijst van boolean-expressies en geeft `true` terug als het aantal `true`-waarden tussen `min` en `max` ligt (inclusief). Geef `-1` door voor `min` of `max` om die grens over te slaan.
   - Voorbeeld: `checklist(2, 3, ${q1} = 'yes', ${q2} = 'yes', ${q3} = 'yes')` — slaagt als precies 2 of 3 van de drie voorwaarden true zijn.
   - Voorbeeld: `checklist(1, -1, ${smoke_alarm}, ${fire_ext}, ${emergency_plan})` — ten minste één veiligheidsmaatregel moet true zijn.

3. `weighted-checklist(min, max, v1, g1, v2, g2, ...)`: Zoals `checklist()`, maar elke waarde heeft een gewicht. De som van gewichten voor `true`-waarden moet tussen `min` en `max` liggen.
   - Voorbeeld: `weighted-checklist(10, -1, ${has_toilet}, 4, ${has_sink}, 3, ${has_shower}, 5)` — som van gewichten voor aanwezige faciliteiten moet ten minste 10 zijn.

---

### Hulpfuncties

1. `uuid()`: Genereert een willekeurige UUID (RFC 4122 v4-formaat) als een tekenreeks.
   - Voorbeeld: `uuid()` → `'a3f8b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c'`
   - Typisch gebruikt met `once()` om een stabiele unieke ID te genereren: `once(uuid())`

2. `version()`: Geeft de waarde van het `version`-attribuut van het formulier terug zoals ingesteld in het settings-werkblad.
   - Voorbeeld: `version()` → `'3.1'`
   - Nuttig in `calculate`-velden om de formulierversie in geëxporteerde gegevens op te nemen.

3. `position()`: Wanneer aangeroepen binnen een **herhalingsgroep**, geeft het de 1-gebaseerde index terug van de huidige herhalingsinstantie.
   - Voorbeeld: `position()` in de eerste instantie geeft `1` terug, in de tweede `2`, enzovoort.
   - Zie ook: `index()` (alias), `indexed-repeat()` voor het verwijzen naar herhalingswaarden vanuit buiten de groep.

4. `thousandsep(lengte, scheidingsteken, waarde)`: Formatteert een getal met een duizendtallenscheidingsteken. `lengte` is de minimale totale tekenreekslengte (aangevuld met spaties indien korter), `scheidingsteken` is het te gebruiken teken (bijv. `','`), en `waarde` is het te formatteren getal.
   - Voorbeeld: `thousandsep(0, ',', 1234567)` → `'1,234,567'`
   - Voorbeeld: `thousandsep(0, '.', ${income})` → formatteert inkomen met punt als duizendtallenscheidingsteken.

5. `substr-jsonpath(waarde, jsonpath)`: Extraheert een deeltekenreeks uit een JSON-tekenreeks met behulp van een JSONPath-expressie.
   - Voorbeeld: `substr-jsonpath(${api_response}, '$.data.name')` — extraheer het veld `name` uit een JSON-tekenreeks opgeslagen in `api_response`.
   - Typisch gebruikt naast `callapi()` om specifieke waarden uit API-responsen te extraheren.
