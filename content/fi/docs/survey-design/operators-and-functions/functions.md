---
title: "Funktiot"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

### Merkkijono-funktiot

{{% alert icon=" " context="warning" %}}
Kun käsittelet merkkijonoja lausekkeiden sisällä, on tärkeää käyttää yksittäisiä lainausmerkkejä ('') literaalisten merkkijonojen ympärillä. Poikkeus kuitenkin syntyy, kun haluat sisällyttää yksittäisiä lainausmerkkejä literaaliseen merkkijonoon. Tällaisissa tapauksissa voit käyttää kaksoislainausmerkkejä ("") koko merkkijonon ympärillä.

Esimerkiksi:
- Oikein: if(${yesno} = 1, "merkkijono 'yksittäisillä lainausmerkeillä' siinä", "ei yksittäisiä lainausmerkkejä tässä")
- Väärin: if(${yesno} = 1, 'merkkijono 'yksittäisillä lainausmerkeillä' siinä', 'ei yksittäisiä lainausmerkkejä tässä')

Älykkäiden lainausmerkkien osalta on tärkeää olla tietoinen niiden läsnäolosta, sillä ne voivat aiheuttaa ongelmia lausekkeissa. Monet rikkaan tekstin editorit muuntavat suorat lainausmerkit ("" tai '') automaattisesti älykkäiksi tai kaareviksi lainausmerkeiksi ("" tai ''), mikä saattaa aiheuttaa syntaksivirheitä tai odottamatonta käyttäytymistä. Vältä tätä käyttämällä aina suoria lainausmerkkejä ('') lausekkeissasi.
{{% /alert %}}

rtSurvey tukee erilaisia funktioita, mukaan lukien:

1. `string(field)`: Muuntaa kentän merkkijonoksi.
   - Esimerkki: `string(34.8)` muunnetaan arvoksi `'34.8'`.

2. `string-length(field)`: Palauttaa merkkijonokentän pituuden.
   - Esimerkki: `string-length(.) > 3 and string-length(.) < 10` voidaan käyttää varmistamaan, että nykyinen kenttä on 3–10 merkin välillä.

3. `substr(fieldorstring, startindex, endindex)`: Palauttaa osajonon alkaen `startindex`:stä ja päättyen juuri ennen `endindex`:ä. Indeksit alkavat 0:sta merkkijonon ensimmäiselle merkille.
   - Esimerkki: `substr(${phone}, 0, 3)` palauttaa puhelinnumeron kolme ensimmäistä numeroa.

4. `concat(a, b, c, ...)`: Yhdistää kentät (ja/tai merkkijonot) toisiinsa.
   - Esimerkki: `concat(${firstname}, ' ', ${lastname})` palauttaa koko nimen yhdistämällä `firstname`- ja `lastname`-kenttien arvot.

5. `linebreak()`: Palauttaa rivinvaihtomerkin.
   - Esimerkki: `concat(${field1}, linebreak(), ${field2}, linebreak(), ${field3})` palauttaa kolmen kenttäarvon listan rivinvaihdoilla niiden välissä.

6. `lower()`: Muuntaa merkkijonon pieniksi kirjaimiksi.
   - Esimerkki: `lower('Street Name')` palauttaa arvon "street name".

7. `upper()`: Muuntaa merkkijonon suuriksi kirjaimiksi.
   - Esimerkki: `upper('Street Name')` palauttaa arvon "STREET NAME".

### select_one- ja select_multiple-funktiot

1. `count-selected(field)`: Palauttaa select_multiple-kentässä valittujen kohteiden lukumäärän.
   - Esimerkki: `count-selected(.) = 3` voidaan käyttää rajoituslausekkeena varmistamaan, että täsmälleen kolme valintaa on tehty.

2. `selected(field, value)`: Palauttaa tosi tai epätosi riippuen siitä, valittiinko määritetty arvo select_one- tai select_multiple-kentässä.
   - Esimerkki: `selected(${color}, 'Blue')` voidaan käyttää relevanssillausekkeena näyttämään ryhmä tai kenttä vain, jos vastaaja valitsi "Sininen" suosikkiväreikseen.
   - Huomio: Toisen parametrin tulisi aina määritellä valinnan arvo, ei valinnan otsikko. Käytä arvoa lomakemäärittelyn choices-laskentataulukon value-sarakkeesta.

3. `selected-at(field, number)`: Palauttaa valitun kohteen määritetyssä sijainnissa select_multiple-kentässä. Kun välitetty numero on 0, se palauttaa ensimmäisen valitun kohteen; kun numero on 1, se palauttaa toisen valitun kohteen ja niin edelleen.
   - Esimerkki: `selected-at(${fruits}, 0) = 'Apple'` voidaan käyttää relevanssillausekkeena näyttämään ryhmä tai kenttä vain, jos ensimmäinen valittu vaihtoehto on "Apple".

4. `choice-label(field, value)`: Palauttaa select_one- tai select_multiple-kentän valinnan otsikon lomakemäärittelyn choices-laskentataulukossa.
   - Esimerkki 1: `choice-label(${country}, ${country})` palauttaa otsikon tällä hetkellä valitulle vaihtoehdolle `country`-nimisessä kentässä.
   - Esimerkki 2: `choice-label(${languages}, selected-at(${languages}, 0))` palauttaa otsikon `languages`-nimisessä kentässä ensimmäiselle valitulle vaihtoehdolle.

### Toistettujen kenttien funktiot

1. `join(string, repeatedfield)`: Toistoryhmässä olevalle kentälle luo merkkijono-erotetun listan arvoista. Ensimmäinen parametri määrittää käytettävän erottimen.
   - Esimerkki: `join(', ', ${member_name})` luo yksittäisen pilkuilla erotetun listan kaikista syötetyistä nimistä.

2. `join-if(string, repeatedfield, expression)`: Toimii täsmälleen kuin `join()`, paitsi että se tarkistaa jokaisen toistoryhmän tapauksen annetulla lausekkeella. Jos lauseke arvioidaan epätodeksi, kohde jätetään pois tuloksesta.
   - Esimerkki: `join-if(', ', ${member_name}, ${age} >= 18)` luo pilkuilla erotetun listan vain aikuisten jäsenten nimistä (niistä, joiden ikä on 18 tai yli).

3. `count(repeatgroup)`: Palauttaa nykyisen toistokerran lukumäärän toistoryhmässä.
   - Esimerkki: `count(${groupname})` palauttaa ryhmän tapausten lukumäärän.

4. `count-if(repeatgroup, expression)`: Toimii täsmälleen kuin `count()`, paitsi että se tarkistaa jokaisen toistoryhmän tapauksen annetulla lausekkeella. Jos lauseke arvioidaan epätodeksi, kohde jätetään pois.
   - Esimerkki: `count-if(${members}, ${age} >= 18)` palauttaa aikuisten jäsenten lukumäärän perustuen "members"-toistoryhmän age-kenttään.

5. `sum(repeatedfield)`: Toistoryhmässä olevalle kentälle laskee kaikkien arvojen summan.
   - Esimerkki: `sum(${loan_amount})` palauttaa kaikkien lainojen kokonaisarvon.

6. `sum-if(repeatedfield, expression)`: Toimii täsmälleen kuin `sum()`, paitsi että se tarkistaa jokaisen toistoryhmän tapauksen annetulla lausekkeella.
   - Esimerkki: `sum-if(${loan_amount}, ${loan_amount} > 500)` palauttaa kaikkien yli 500 euron lainojen kokonaisarvon.

7. `min(repeatedfield)`: Toistoryhmässä olevalle kentälle laskee kaikkien arvojen minimin.
   - Esimerkki: `min(${member_age})` palauttaa ryhmän nuorimman jäsenen iän.

8. `min-if(repeatedfield, expression)`: Toimii täsmälleen kuin `min()`, paitsi että se tarkistaa jokaisen toistoryhmän tapauksen annetulla lausekkeella.
   - Esimerkki: `min-if(${member_age}, ${member_age} >= 18)` palauttaa ryhmän nuorimman aikuisen iän.

9. `max(repeatedfield)`: Toistoryhmässä olevalle kentälle laskee kaikkien arvojen maksimin.
   - Esimerkki: `max(${member_age})` palauttaa ryhmän vanhimman jäsenen iän.

10. `max-if(repeatedfield, expression)`: Toimii täsmälleen kuin `max()`, paitsi että se tarkistaa jokaisen toistoryhmän tapauksen annetulla lausekkeella.
    - Esimerkki: `max-if(${member_age}, ${member_age} >= 18)` palauttaa ryhmän vanhimman aikuisen iän.

11. `index()`: Toistoryhmän sisällä kutsuttuna palauttaa nykyisen ryhmän tai tapauksen indeksinumeron.
    - Esimerkki: `index()` toistoryhmässä käytettynä palauttaa 1 ensimmäiselle tapaukselle, 2 toiselle ja niin edelleen.

12. `indexed-repeat(repeatedfield, repeatgroup, index)`: Viittaa kenttään tai ryhmään, joka on toistoryhmän sisällä, sen ulkopuolelta. Ensimmäinen parametri määrittää toistettavan kentän tai ryhmän, toinen määrittää toistoryhmän, jonka sisällä kenttä tai ryhmä sijaitsee, ja kolmas määrittää tapauksen numeron toistoryhmässä.
    - Esimerkki 1: `indexed-repeat(${name}, ${names}, 1)` palauttaa ensimmäisen saatavilla olevan nimen, kun name-kenttä on "names"-nimisessä aiemmassa toistoryhmässä.
    - Esimerkki 2: `indexed-repeat(${name}, ${names}, index())` hakee nimen, joka vastaa nykyisen toistoryhmän tapausnumeroa.

13. `rank-index(index, repeatedfield)`: Tämä funktio laskee toistettavan kentän määritetyn tapauksen ordinaalijarjestyksen toistoryhmän ulkopuolella käytettäväksi. Järjestys 1 annetaan suurimman arvon omaavalle tapaukselle, järjestys 2 seuraavaksi suurimmalle ja niin edelleen. Jos välität virheellisen indeksin tai indeksin tapaukseen, jonka arvo ei ole numeerinen, palautetaan järjestys 999.
    - Esimerkki: `rank-index(1, ${random_draw})` laskee ensimmäisen tapauksen järjestyksen perustuen sen `random_draw`-kentän arvoon verrattuna muiden tapausten arvoihin.

14. `rank-index-if(index, repeatedfield, expression)`: Tämä funktio toimii samoin kuin `rank-index()`, mutta se tarkistaa jokaisen tapauksen toistettavan kentän toistoryhmässä annetulla lausekkeella. Jos lauseke arvioidaan epätodeksi, kohde jätetään pois laskennasta. Käytetty indeksi perustuu täyteen tapausjoukkoon ennen kunkin tapauksen lausekkeen arviointia. Jos välität indeksin tapaukselle, joka jätettiin pois koska se ei täyttänyt lauseketta, se katsotaan virheelliseksi indeksiksi ja palautetaan järjestys 999.
    - Esimerkki: `rank-index-if(1, ${age}, ${age} >= 18)` laskee ikäjärjestyksen aikuisten joukossa ottaen huomioon vain tapaukset, joissa ikä on 18 tai enemmän.

### Numerofunktiot 

{{< table >}}
| Operaattori | Toiminta | Esimerkki | Esimerkkivastaus |
|----------|-----------|---------|----------------|
| `+` | Yhteenlasku | 1 + 1 | 2 |
| `-` | Vähennyslasku | 3 - 2 | 1 |
| `*` | Kertolasku | 3 * 2 | 6 |
| `div` | Jakolasku | 10 div 2 | 5 |
| `mod` | Modulus | 9 mod 2 | 1 |
{{< /table >}}

rtSurvey tukee numerofunktioita, mukaan lukien:
- `number(field)`: Muuntaa kentän arvon numeroksi.
  - Esimerkki: `number('34.8')` = 34.8

- `int(field)`: Muuntaa kentän arvon kokonaisluvuksi.
  - Esimerkki: `int('39.2')` = 39

- `min(field1, ..., fieldx)`: Palauttaa pienimmän arvon välitetyistä kentistä.
  - Esimerkki: `min(${father_age}, ${mother_age})` palauttaa joko isän tai äidin iän, kumpi on pienempi.

- `max(field1, ..., fieldx)`: Palauttaa suurimman arvon välitetyistä kentistä.
  - Esimerkki: `max(${father_age}, ${mother_age})` palauttaa joko isän tai äidin iän, kumpi on suurempi.

- `format-number(field)`: Muotoilee kokonaisluku- tai desimaalikenttäarvon käyttäjän lokaalin asetuksien mukaan.
  - Esimerkki: `format-number(${income})` saattaa muotoilla "120000" arvoksi "120,000".

- `round(field, digits)`: Pyöristää numeerisen kenttäarvon määritettyyn desimaalipaikkojen lukumäärään.
  - Esimerkki: `round(${interest_rate}, 2)`

- `abs(number)`: Palauttaa luvun itseisarvon.
  
- `pow(base, exponent)`: Palauttaa ensimmäisen parametrin arvon korotettuna toisen parametrin potenssiin.

- `log10(fieldorvalue)`: Palauttaa välitetyn kentän tai arvon kymmenkantaisen logaritmin.

- `sin(fieldorvalue)`: Palauttaa välitetyn kentän tai arvon sinin radiaaneissa ilmaistuna.
  
- `cos(fieldorvalue)`: Palauttaa välitetyn kentän tai arvon kosinin radiaaneissa ilmaistuna.

- `tan(fieldorvalue)`: Palauttaa välitetyn kentän tai arvon tangentin radiaaneissa ilmaistuna.

- `asin(fieldorvalue)`: Palauttaa välitetyn kentän tai arvon arkussinin radiaaneissa ilmaistuna.

- `acos(fieldorvalue)`: Palauttaa välitetyn kentän tai arvon arkuskosinin radiaaneissa ilmaistuna.

- `atan(fieldorvalue)`: Palauttaa välitetyn kentän tai arvon arkustangentin radiaaneissa ilmaistuna.

- `atan2(x, y)`: Palauttaa origon ja pisteen (x, y) sekä positiivisen x-akselin välisen kulman radiaaneissa. Tulos on välillä -pi() ja pi().

- `sqrt(fieldorvalue)`: Palauttaa välitetyn kentän tai arvon ei-negatiivisen neliöjuuren.

- `exp(x)`: Palauttaa arvon e^x.

- `pi()`: Palauttaa pi:n arvon.

### Päivämäärä- ja aikafunktiot

{{% alert icon=" " context="warning" %}}
Päivämääräarvot rtSurveyssa tallennetaan merkkijonoina `YYYY-MM-DD`-muodossa. Datetime-arvot tallennetaan ISO 8601 -merkkijonoina (`YYYY-MM-DDTHH:MM:SS`). Käytä `decimal-date-time()`:tä muuntaaksesi numeroksi aritmeettisia laskuja varten (esim. kestojen laskeminen).
{{% /alert %}}

1. `today()`: Palauttaa tämän päivän päivämäärän merkkijonona `YYYY-MM-DD`-muodossa. Arvioidaan kerran, kun lomake avautuu.
   - Esimerkki: `today()` → `'2024-03-15'`
   - Yleinen käyttö: `default`-sarakkeessa esitäyttämään tämän päivän päivämäärä tai `relevant`/`constraint`-kohdissa vertailemaan päivämääräkenttää vastaan.

2. `now()`: Palauttaa nykyisen päivämäärän ja ajan ISO 8601 -merkkijonona. Arvioidaan joka kerta, kun lauseke lasketaan.
   - Esimerkki: `now()` → `'2024-03-15T14:32:00.000+03:00'`
   - Yleinen käyttö: Tietyn tapahtuman tarkan aikaleiman tallentaminen kyselyn aikana.

3. `date(value)`: Muuntaa arvon (merkkijono tai numero) päivämäärämerkkijonoksi.
   - Esimerkki: `date('2024-03-15')` → `'2024-03-15'`

4. `date-time(value)`: Muuntaa arvon datetime-merkkijonoksi.
   - Esimerkki: `date-time(${event_timestamp})`

5. `decimal-date-time(value)`: Muuntaa päivämäärä- tai datetime-merkkijonon desimaaliluvuksi, joka edustaa millisekunteja Unix-epookin jälkeen jaettuna 86400000:lla (eli murto-osia päivistä 1970-01-01 alkaen). Käytä tätä aritmeettisiin laskuihin päivämäärien kanssa.
   - Esimerkki: Kesto päivissä kahden päivämäärän välillä:
     `decimal-date-time(${end_date}) - decimal-date-time(${start_date})`
   - Esimerkki: Kesto minuuteissa kahden datetime-arvon välillä:
     `(decimal-date-time(${end_time}) - decimal-date-time(${start_time})) * 1440`

6. `format-date(date, format)`: Muotoilee päivämääräarvon mallimerkkijonon avulla.
   - Muotoilutunnukset: `%Y` (4-numeroinen vuosi), `%y` (2-numeroinen vuosi), `%m` (kuukausi 01–12), `%d` (päivä 01–31), `%a` (lyhenne viikonpäivästä), `%b` (lyhenne kuukauden nimestä)
   - Esimerkki: `format-date(today(), '%d/%m/%Y')` → `'15/03/2024'`
   - Esimerkki: `format-date(${dob}, '%B %d, %Y')` → `'March 15, 1990'`

7. `format-date-time(datetime, format)`: Muotoilee datetime-arvon mallimerkkijonon avulla. Hyväksyy kaikki `format-date`-tunnukset sekä:
   - `%H` (tunti 00–23), `%h` (tunti 01–12), `%M` (minuutit 00–59), `%S` (sekunnit 00–59), `%3` (millisekunnit), `%P` (AM/PM)
   - Esimerkki: `format-date-time(now(), '%d/%m/%Y %H:%M')` → `'15/03/2024 14:32'`
   - Esimerkki: `format-date-time(${event_time}, '%I:%M %p')` → `'02:32 PM'`

---

### Boolean-funktiot

1. `boolean(value)`: Muuntaa minkä tahansa arvon booleaniksi. Palauttaa `tosi` ei-tyhjille merkkijonoille, nollasta eroaville numeroille ja `true`-arvolle; palauttaa `epätosi` tyhjille merkkijonoille, `0`:lle ja `false`-arvolle.
   - Esimerkki: `boolean(${name})` palauttaa `tosi`, jos `name` ei ole tyhjä.

2. `boolean-from-string(string)`: Palauttaa `tosi`, jos merkkijono on `'1'` tai `'true'` (ei kirjainkooherkkä); muussa tapauksessa palauttaa `epätosi`.
   - Esimerkki: `boolean-from-string(${enabled_flag})` — hyödyllinen, kun kenttä tallentaa `'true'`/`'false'` tekstinä.

3. `true()`: Palauttaa boolean-arvon `tosi`.
   - Esimerkki: `required`-sarakkeessa `true()` vastaa `yes`-arvoa.

4. `false()`: Palauttaa boolean-arvon `epätosi`.
   - Esimerkki: `if(${skip_section} = 'yes', false(), true())` — aseta required dynaamisesti.

5. `not(expression)`: Palauttaa lausekkeen loogisen negaation. Palauttaa `tosi`, jos lauseke on epätosi, ja päinvastoin.
   - Esimerkki: `not(${consent} = 'yes')` — näytä varoitus, kun suostumusta EI annettu.
   - Esimerkki: `not(selected(${issues}, 'none'))` — vaadi yksityiskohdat vain, jos "none" ei ole valittu.

---

### Lisämerkkijono-funktiot

1. `starts-with(string, prefix)`: Palauttaa `tosi`, jos `string` alkaa `prefix`:lla.
   - Esimerkki: `starts-with(${phone}, '+358')` tarkistaa, alkaako puhelinnumero Suomen maakoodilla.

2. `contains(string, substring)`: Palauttaa `tosi`, jos `string` sisältää `substring`:n.
   - Esimerkki: `contains(${email}, '@')` tarkistaa, että sähköpostiosoitteessa on `@`-merkki.
   - Esimerkki: `contains(${notes}, 'urgent')` käynnistää jatkokysymyksen, jos muistiinpanot mainitsevat "urgent".

3. `substring-before(string, needle)`: Palauttaa osan `string`:stä, joka esiintyy ennen `needle`:n ensimmäistä esiintymää.
   - Esimerkki: `substring-before(${full_name}, ' ')` poimii ensimmäisen sanan (etunimen).

4. `substring-after(string, needle)`: Palauttaa osan `string`:stä, joka esiintyy `needle`:n ensimmäisen esiintymän jälkeen.
   - Esimerkki: `substring-after(${email}, '@')` poimii sähköpostiosoitteen verkkotunnuksen.

5. `normalize-space(string)`: Poistaa johtavat ja loppuvat välilyönnit ja tiivistää kaikki sisäiset välilyöntisekvenssit yhdeksi välilyönniksi.
   - Esimerkki: `normalize-space(${name})` — puhdistaa nimen, johon saattaa olla kirjoitettu ylimääräisiä välilyöntejä.

6. `translate(string, search_chars, replace_chars)`: Korvaa jokaisen `string`:n merkin, joka esiintyy `search_chars`:ssa, vastaavalla merkillä `replace_chars`:ssa. `search_chars`:ssa olevat merkit, joille ei ole vastaavaa merkkiä `replace_chars`:ssa, poistetaan.
   - Esimerkki: `translate(${code}, 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')` muuntaa isiksi kirjaimiksi (vastaa `upper()`:tä).
   - Esimerkki: `translate(${phone}, ' -()', '')` poistaa välilyönnit, viivat ja sulkeet puhelinnumerosta.

---

### Lisämatemaattiset funktiot

1. `floor(number)`: Palauttaa suurimman kokonaisluvun, joka on pienempi tai yhtä suuri kuin `number` (pyöristää kohti negatiivista ääretöntä).
   - Esimerkki: `floor(4.9)` = 4, `floor(-2.1)` = -3

2. `ceiling(number)`: Palauttaa pienimmän kokonaisluvun, joka on suurempi tai yhtä suuri kuin `number` (pyöristää kohti positiivista ääretöntä).
   - Esimerkki: `ceiling(4.1)` = 5, `ceiling(-2.9)` = -2

3. `random()`: Palauttaa satunnaisen desimaaliluvun väliltä 0,0 (mukaan lukien) ja 1,0 (ei mukaan lukien). Käytetään tyypillisesti `calculate`-kentissä satunnaisten arvojen antamiseen tai kysymysten järjestyksen satunnaistamiseen.
   - Esimerkki: `random()` → esim. `0.7341`
   - Esimerkki: `int(random() * 6) + 1` → satunnaisluku 1–6 (nopan heitto)

4. `coalesce(a, b)`: Palauttaa `a`:n, jos `a` on ei-tyhjä; muussa tapauksessa palauttaa `b`. Hyödyllinen varavalintana, kun kenttä saattaa olla tyhjä.
   - Esimerkki: `coalesce(${preferred_name}, ${full_name})` — käytä suosittua nimeä jos asetettu, muussa tapauksessa käytä koko nimeä.

5. `once(value)`: Arvioi `value`:n ja tallentaa sen, mutta vain jos nykyinen kenttä on **tyhjä**. Jos kentällä on jo arvo (esim. se on aiemmin asetettu), `once()` palauttaa olemassa olevan arvon muuttumattomana. Tämä estää uudelleenlaskennan ylikirjoittamasta käyttäjän syötettä.
   - Esimerkki: `once(today())` `default`-sarakkeessa asettaa tämän päivän päivämäärän kerran eikä päivitä sitä, jos luetteloija avaa lomakkeen uudelleen.
   - Esimerkki: `once(uuid())` luo UUID:n kerran ja pitää sen vakaana uudelleenmuokkausten välillä.

---

### Geo-funktiot

1. `area(geoshape_value)`: Laskee geoshape-arvon (monikulmio) sulkeman **pinta-alan neliömetreinä**.
   - Parametri on geoshape-kentän arvo muodossa `lat1 lon1 0 0; lat2 lon2 0 0; ...`
   - Esimerkki: `area(${field_boundary})` — laske tutkitun pellon pinta-ala m²:ssä.
   - Esimerkki: `round(area(${field_boundary}) div 10000, 2)` — muunna hehtaareiksi.

2. `distance(coordinates)`: Laskee geotrace-reitin (viiva) **kokonaispolun pituuden metreinä** tai kahden geopoint-pisteen välisen etäisyyden.
   - Geotrace:lle: `distance(${route})` palauttaa kokonaispolun pituuden metreinä.
   - Kahdelle geopoint-pisteelle: `distance(concat(${point_a}, ' ', ${point_b}))` palauttaa niiden välisen etäisyyden.
   - Esimerkki: `round(distance(${road_trace}) div 1000, 3)` — tien pituus kilometreissä.

---

### Validointifunktiot

1. `regex(value, pattern)`: Palauttaa `tosi`, jos `value` vastaa säännöllistä lauseketta `pattern`. Käytä `constraint`-sarakkeessa mallipohjaiseen validointiin.
   - Kaava käyttää vakio-regex-syntaksia (POSIX ERE -osajoukko).
   - Esimerkki: `regex(., '^[0-9]{10}$')` — validoi 10-numeroinen luku.
   - Esimerkki: `regex(., '^[A-Z]{2}[0-9]{6}$')` — validoi passinnumeromuoto (2 isoa kirjainta ja 6 numeroa).
   - Esimerkki: `regex(., '^[^@]+@[^@]+\.[^@]{2,}$')` — perus sähköpostimuodon tarkistus.

2. `checklist(min, max, v1, v2, ...)`: Arvioi listan boolean-lausekkeita ja palauttaa `tosi`, jos `tosi`-arvojen lukumäärä on välillä `min` ja `max` (mukaan lukien). Välitä `-1` `min`:lle tai `max`:lle ohittaaksesi kyseisen rajan.
   - Esimerkki: `checklist(2, 3, ${q1} = 'yes', ${q2} = 'yes', ${q3} = 'yes')` — täyttyy, jos täsmälleen 2 tai 3 kolmesta ehdosta on tosi.
   - Esimerkki: `checklist(1, -1, ${smoke_alarm}, ${fire_ext}, ${emergency_plan})` — vähintään yhden turvatoimenpiteen on oltava tosi.

3. `weighted-checklist(min, max, v1, w1, v2, w2, ...)`: Kuten `checklist()`, mutta jokaisella arvolla on paino. `tosi`-arvojen painojen summan on oltava välillä `min` ja `max`.
   - Esimerkki: `weighted-checklist(10, -1, ${has_toilet}, 4, ${has_sink}, 3, ${has_shower}, 5)` — olemassa olevien tilojen painojen summan on oltava vähintään 10.

---

### Apufunktiot

1. `uuid()`: Luo satunnaisen UUID:n (RFC 4122 v4 -muoto) merkkijonona.
   - Esimerkki: `uuid()` → `'a3f8b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c'`
   - Käytetään tyypillisesti `once()`:n kanssa vakaan yksilöllisen tunnuksen luomiseen: `once(uuid())`

2. `version()`: Palauttaa lomakkeen `version`-attribuutin arvon settings-laskentataulukossa.
   - Esimerkki: `version()` → `'3.1'`
   - Hyödyllinen `calculate`-kentissä lomakkeen version upottamiseen vietyyn dataan.

3. `position()`: Kutsuttaessa **toistoryhmässä**, palauttaa nykyisen toistotapauksen 1-pohjaisen indeksin.
   - Esimerkki: `position()` ensimmäisessä tapauksessa palauttaa `1`, toisessa `2` ja niin edelleen.
   - Katso myös: `index()` (alias), `indexed-repeat()` toistettavien arvojen viittaamiseen ryhmän ulkopuolelta.

4. `thousandsep(length, separator, value)`: Muotoilee numeron tuhaterottimella. `length` on minimaalinen kokonaismerkkijonon pituus (täytetään välilyönneillä jos lyhyempi), `separator` on käytettävä merkki (esim. `','`), ja `value` on muotoiltava numero.
   - Esimerkki: `thousandsep(0, ',', 1234567)` → `'1,234,567'`
   - Esimerkki: `thousandsep(0, '.', ${income})` → muotoilee tulon pisteellä tuhaterottimena.

5. `substr-jsonpath(value, jsonpath)`: Poimii osajonon JSON-merkkijonosta käyttämällä JSONPath-lauseketta.
   - Esimerkki: `substr-jsonpath(${api_response}, '$.data.name')` — poimii `name`-kentän `api_response`-kohtaan tallennetusta JSON-merkkijonosta.
   - Käytetään tyypillisesti `callapi()`:n ohella tiettyjen arvojen poimimiseen API-vastauksista.
