---
title: "Funkcijas"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

### Virknes funkcijas

{{% alert icon=" " context="warning" %}}
Strādājot ar virknēm izteiksmēs, svarīgi izmantot vienpēdiņas ('') literālu virkņu ierobežošanai. Tomēr izņēmums rodas, ja vēlaties iekļaut vienpēdiņas literālā virknē. Šādā gadījumā varat izmantot dubultpēdiņas (""), lai ierobežotu visu virkni.

Piemēram:
- Pareizi: if(${yesno} = 1, "a string with 'single quotes' in it", "no single quotes here")
- Nepareizi: if(${yesno} = 1, 'a string with 'single quotes' in it', 'no single quotes here')

Attiecībā uz viedajām pēdiņām, ir svarīgi apzināties to klātbūtni, jo tās var radīt problēmas izteiksmēs. Daudzi bagātā teksta redaktori automātiski pārveido taisnas pēdiņas ("" vai '') uz viedajām vai izliekajām pēdiņām ("" vai ''), kas var izraisīt sintakses kļūdas vai neparedzētu uzvedību. Lai no tā izvairītos, nodrošiniet, ka izteiksmēs konsekventi izmantojat taisnas pēdiņas ('').
{{% /alert %}}

rtSurvey atbalsta dažādas funkcijas, tostarp:

1. `string(field)`: Pārveido lauku par virkni.
   - Piemērs: `string(34.8)` tiks pārveidots par `'34.8'`.

2. `string-length(field)`: Atgriež virknes lauka garumu.
   - Piemērs: `string-length(.) > 3 and string-length(.) < 10` var izmantot, lai nodrošinātu, ka pašreizējais lauks ir no 3 līdz 10 rakstzīmēm.

3. `substr(fieldorstring, startindex, endindex)`: Atgriež apakšvirkni sākot no `startindex` un beidzot tieši pirms `endindex`. Indeksi sākas ar 0 virknes pirmajai rakstzīmei.
   - Piemērs: `substr(${phone}, 0, 3)` atgriezīs tālruņa numura pirmos trīs ciparus.

4. `concat(a, b, c, ...)`: Savieno laukus (un/vai virknes) kopā.
   - Piemērs: `concat(${firstname}, ' ', ${lastname})` atgriezīs pilnu vārdu, apvienojot `firstname` un `lastname` lauku vērtības.

5. `linebreak()`: Atgriež rindas pārtraukuma rakstzīmi.
   - Piemērs: `concat(${field1}, linebreak(), ${field2}, linebreak(), ${field3})` atgriezīs trīs lauku vērtību sarakstu ar rindas pārtraukumiem starp tiem.

6. `lower()`: Pārveido virkni uz mazajiem burtiem.
   - Piemērs: `lower('Street Name')` atgriezīs "street name".

7. `upper()`: Pārveido virkni uz lielajiem burtiem.
   - Piemērs: `upper('Street Name')` atgriezīs "STREET NAME".

### select_one un select_multiple funkcijas

1. `count-selected(field)`: Atgriež atlasīto vienumu skaitu select_multiple laukā.
   - Piemērs: `count-selected(.) = 3` var izmantot kā ierobežojuma izteiksmi, lai nodrošinātu, ka tiek atlasītas tieši trīs izvēles.

2. `selected(field, value)`: Atgriež true vai false atkarībā no tā, vai norādītā vērtība tika atlasīta select_one vai select_multiple laukā.
   - Piemērs: `selected(${color}, 'Blue')` var izmantot kā relevances izteiksmi, lai rādītu grupu vai lauku tikai tad, ja respondents atlasīja "Blue" kā savu iecienīto krāsu.
   - Piezīme: Otrais parametrs vienmēr jānorāda kā izvēles vērtība, nevis izvēles etiķete. Izmantojiet vērtību no formas definīcijas izvēļu darblapas vērtību kolonnas.

3. `selected-at(field, number)`: Atgriež atlasīto vienumu norādītajā pozīcijā select_multiple laukā. Kad padotais skaitlis ir 0, atgriež pirmo atlasīto vienumu; kad skaitlis ir 1, atgriež otro atlasīto vienumu, un tā tālāk.
   - Piemērs: `selected-at(${fruits}, 0) = 'Apple'` var izmantot kā relevances izteiksmi, lai rādītu grupu vai lauku tikai tad, ja pirmā atlasītā izvēle ir "Apple".
   - Piezīme: Atgrieztā vērtība būs izvēles vērtība, nevis izvēles etiķete.

4. `choice-label(field, value)`: Atgriež etiķeti select_one vai select_multiple lauka izvēlei, kā definēts formas definīcijas izvēļu darblappā.
   - Piemērs 1: `choice-label(${country}, ${country})` atgriezīs izvēles etiķeti pašlaik atlasītajai izvēlei `country` laukā.
   - Piemērs 2: `choice-label(${languages}, selected-at(${languages}, 0))` atgriezīs etiķeti pirmajai atlasītajai izvēlei `languages` laukā.
   - Piezīme: Šī funkcija izgūst izvēles etiķeti, nevis vērtību.

### Atkārtotu lauku funkcijas

rtSurvey gadījumā, ja vēlaties uzdot tos pašus jautājumus vairākas reizes, varat ievietot lauku atkārtojumu grupā. Tas rezultējas vairākās viena lauka instancēs. Šādas funkcijas var palīdzēt strādāt ar šiem atkārtotajiem laukiem un to saražotajiem datiem.

1. `join(string, repeatedfield)`: Atkārtojumu grupas laukam ģenerē ar virkni atdalītu vērtību sarakstu. Pirmais parametrs norāda izmantojamo atdalītāju.
   - Piemērs: `join(', ', ${member_name})` ģenerēs vienu ar komatu atdalītu sarakstu no visiem ievadītajiem vārdiem.

2. `join-if(string, repeatedfield, expression)`: Darbojas tieši kā `join()`, izņemot to, ka pārbauda katru atkārtojumu grupas instanci, izmantojot padoto izteiksmi. Ja izteiksme novērtējas kā false, vienums tiks izlaists no izvades.
   - Piemērs: `join-if(', ', ${member_name}, ${age} >= 18)` ģenerēs ar komatu atdalītu tikai pieaugušo locekļu vārdu sarakstu.

3. `count(repeatgroup)`: Atgriež pašreizējo reižu skaitu, cik atkārtojumu grupā ir atkārtots.
   - Piemērs: `count(${groupname})` atgriezīs grupas instanču skaitu.

4. `count-if(repeatgroup, expression)`: Darbojas tieši kā `count()`, izņemot to, ka pārbauda katru atkārtojumu grupas instanci, izmantojot padoto izteiksmi.
   - Piemērs: `count-if(${members}, ${age} >= 18)` atgriezīs pieaugušo locekļu skaitu, pamatojoties uz `age` lauku "members" atkārtojumu grupā.

5. `sum(repeatedfield)`: Atkārtojumu grupas laukam aprēķina visu vērtību summu.
   - Piemērs: `sum(${loan_amount})` atgriezīs visu aizdevumu kopējo vērtību.

6. `sum-if(repeatedfield, expression)`: Darbojas tieši kā `sum()`, izņemot to, ka pārbauda katru atkārtojumu grupas instanci, izmantojot padoto izteiksmi.
   - Piemērs: `sum-if(${loan_amount}, ${loan_amount} > 500)` atgriezīs visu aizdevumu virs 500 kopējo vērtību.

7. `min(repeatedfield)`: Atkārtojumu grupas laukam aprēķina visu vērtību minimumu.
   - Piemērs: `min(${member_age})` atgriezīs jaunākā grupas locekļa vecumu.

8. `min-if(repeatedfield, expression)`: Darbojas tieši kā `min()`, izņemot to, ka pārbauda katru atkārtojumu grupas instanci, izmantojot padoto izteiksmi.
   - Piemērs: `min-if(${member_age}, ${member_age} >= 18)` atgriezīs jaunākā pieaugušā vecumu grupā.

9. `max(repeatedfield)`: Atkārtojumu grupas laukam aprēķina visu vērtību maksimumu.
   - Piemērs: `max(${member_age})` atgriezīs vecākā grupas locekļa vecumu.

10. `max-if(repeatedfield, expression)`: Darbojas tieši kā `max()`, izņemot to, ka pārbauda katru atkārtojumu grupas instanci, izmantojot padoto izteiksmi.
    - Piemērs: `max-if(${member_age}, ${member_age} >= 18)` atgriezīs vecākā pieaugušā vecumu grupā.

11. `index()`: Izsaukts atkārtojumu grupas iekšā, atgriež pašreizējās grupas vai instances indeksa numuru.
    - Piemērs: `index()` lietojot atkārtojumu grupas iekšā, atgriezīs 1 pirmajai instancei, 2 otrajai, un tā tālāk.

12. `indexed-repeat(repeatedfield, repeatgroup, index)`: Atsaucas uz lauku vai grupu, kas atrodas atkārtojumu grupā, no ārpuses tās atkārtojumu grupas. Pirmais parametrs norāda atkārtoto lauku vai grupu, otrais — atkārtojumu grupu, kurā lauks atrodas, un trešais — instances numuru atkārtojumu grupā.
    - Piemērs 1: `indexed-repeat(${name}, ${names}, 1)` atgriezīs pirmo pieejamo vārdu, ja `name` lauks atrodas iepriekšējā atkārtojumu grupā "names".
    - Piemērs 2: `indexed-repeat(${name}, ${names}, index())` izgūs vārdu, kas atbilst pašreizējās atkārtojumu grupas instances numuram.

13. `rank-index(index, repeatedfield)`: Šī funkcija aprēķina norādītās atkārtotā lauka instances ordinālrangu lietošanai ārpus atkārtojumu grupas. Rangā 1 tiek piešķirts instancei ar augstāko vērtību, rangā 2 — instancei ar nākamo augstāko vērtību, un tā tālāk.
    - Piemērs: `rank-index(1, ${random_draw})` aprēķina pirmās instances rangu, pamatojoties uz tās `random_draw` lauka vērtību salīdzinājumā ar citām instancēm.

14. `rank-index-if(index, repeatedfield, expression)`: Šī funkcija darbojas līdzīgi kā `rank-index()`, bet pārbauda katru atkārtotā lauka atkārtojumu grupas instanci, izmantojot padoto izteiksmi.
    - Piemērs: `rank-index-if(1, ${age}, ${age} >= 18)` aprēķina vecuma rangu pieaugušo kopā, ņemot vērā tikai instances, kur vecums ir lielāks par vai vienāds ar 18.

### Skaitļu funkcijas

{{< table >}}
| Operators | Darbība | Piemērs | Piemēra atbilde |
|----------|-----------|---------|----------------|
| `+` | Saskaitīšana | 1 + 1 | 2 |
| `-` | Atņemšana | 3 - 2 | 1 |
| `*` | Reizināšana | 3 * 2 | 6 |
| `div` | Dalīšana | 10 div 2 | 5 |
| `mod` | Modulis | 9 mod 2 | 1 |
{{< /table >}}

rtSurvey atbalsta skaitļu funkcijas, tostarp:
- `number(field)`: Pārveido lauka vērtību uz skaitli.
  - Piemērs: `number('34.8')` = 34.8

- `int(field)`: Pārveido lauka vērtību uz veselu skaitli.
  - Piemērs: `int('39.2')` = 39

- `min(field1, ..., fieldx)`: Atgriež minimālo vērtību starp padotajiem laukiem.
  - Piemērs: `min(${father_age}, ${mother_age})` atgriezīs vai nu mātes, vai tēva vecumu — kurš ir mazāks.

- `max(field1, ..., fieldx)`: Atgriež maksimālo vērtību starp padotajiem laukiem.
  - Piemērs: `max(${father_age}, ${mother_age})` atgriezīs vai nu mātes, vai tēva vecumu — kurš ir lielāks.

- `format-number(field)`: Formatē vesela skaitļa vai decimāla lauka vērtību atbilstoši lietotāja lokalizācijas iestatījumiem.
  - Piemērs: `format-number(${income})` var formatēt "120000" kā "120,000".

- `round(field, digits)`: Noapaļo skaitliskā lauka vērtību līdz norādītajam ciparu skaitam aiz komata.
  - Piemērs: `round(${interest_rate}, 2)`

- `abs(number)`: Atgriež skaitļa absolūto vērtību.

- `pow(base, exponent)`: Atgriež pirmā parametra vērtību pakāpē, kas norādīta ar otro parametru.

- `log10(fieldorvalue)`: Atgriež padotā lauka vai vērtības desmitnieka logaritmu.

- `sin(fieldorvalue)`: Atgriež padotā lauka vai vērtības sinusu, izteiktu radiānos.

- `cos(fieldorvalue)`: Atgriež padotā lauka vai vērtības kosinusu, izteiktu radiānos.

- `tan(fieldorvalue)`: Atgriež padotā lauka vai vērtības tangensu, izteiktu radiānos.

- `asin(fieldorvalue)`: Atgriež padotā lauka vai vērtības arcsinusu, izteiktu radiānos.

- `acos(fieldorvalue)`: Atgriež padotā lauka vai vērtības arckosinusu, izteiktu radiānos.

- `atan(fieldorvalue)`: Atgriež padotā lauka vai vērtības arctangensu, izteiktu radiānos.

- `atan2(x, y)`: Atgriež leņķi radiānos starp pozitīvo x-asi un punktu ar koordinātēm (x, y). Rezultāts ir diapazonā no -pi() līdz pi().

- `sqrt(fieldorvalue)`: Atgriež padotā lauka vai vērtības nenegatīvo kvadrātsakni.

- `exp(x)`: Atgriež e^x vērtību.

- `pi()`: Atgriež pi vērtību.

### Datuma un laika funkcijas

{{% alert icon=" " context="warning" %}}
Datuma vērtības rtSurvey tiek glabātas kā virknes `YYYY-MM-DD` formātā. Datuma-laika vērtības tiek glabātas kā ISO 8601 virknes (`YYYY-MM-DDTHH:MM:SS`). Izmantojiet `decimal-date-time()`, lai pārveidotu uz skaitli aritmētiskai operācijai (piem., ilgumu aprēķiniem).
{{% /alert %}}

1. `today()`: Atgriež šodienas datumu kā virkni `YYYY-MM-DD` formātā. Tiek novērtēts vienreiz, kad forma tiek atvērta.
   - Piemērs: `today()` → `'2024-03-15'`
   - Bieža lietošana: kolonnā `default`, lai sākotnēji aizpildītu šodienas datumu, vai `relevant`/`constraint` salīdzinājumam ar datuma lauku.

2. `now()`: Atgriež pašreizējo datumu un laiku kā ISO 8601 virkni. Tiek novērtēts katru reizi, kad izteiksme tiek aprēķināta.
   - Piemērs: `now()` → `'2024-03-15T14:32:00.000+03:00'`
   - Bieža lietošana: Precīza aptaujā notikušā notikuma laika zīmoga reģistrēšanai.

3. `date(value)`: Pārveido vērtību (virkni vai skaitli) datuma virknē. Noderīgs aprēķināto vērtību piespiešanai datuma tipam.
   - Piemērs: `date('2024-03-15')` → `'2024-03-15'`

4. `date-time(value)`: Pārveido vērtību datuma-laika virknē.
   - Piemērs: `date-time(${event_timestamp})`

5. `decimal-date-time(value)`: Pārveido datuma vai datuma-laika virkni uz decimālo skaitli, kas apzīmē milisekundes kopš Unix epohā dalītas ar 86400000 (t.i., daļveida dienas kopš 1970-01-01). Izmantojiet to, lai veiktu aritmētiku ar datumiem.
   - Piemērs: Ilgums dienās starp diviem datumiem:
     `decimal-date-time(${end_date}) - decimal-date-time(${start_date})`
   - Piemērs: Ilgums minūtēs starp diviem datuma-laika laukiem:
     `(decimal-date-time(${end_time}) - decimal-date-time(${start_time})) * 1440`

6. `format-date(date, format)`: Formatē datuma vērtību, izmantojot formāta virkni.
   - Formāta pilnvaru: `%Y` (4 ciparu gads), `%y` (2 ciparu gads), `%m` (mēnesis 01–12), `%d` (diena 01–31), `%a` (saīsināts nedēļas dienas nosaukums), `%b` (saīsināts mēneša nosaukums)
   - Piemērs: `format-date(today(), '%d/%m/%Y')` → `'15/03/2024'`

7. `format-date-time(datetime, format)`: Formatē datuma-laika vērtību, izmantojot formāta virkni. Pieņem visas `format-date` pilnvaru plus:
   - `%H` (stundas 00–23), `%h` (stundas 01–12), `%M` (minūtes 00–59), `%S` (sekundes 00–59), `%3` (milisekundes), `%P` (AM/PM)
   - Piemērs: `format-date-time(now(), '%d/%m/%Y %H:%M')` → `'15/03/2024 14:32'`

---

### Boolean funkcijas

1. `boolean(value)`: Pārveido jebkuru vērtību uz boolean. Atgriež `true` netukšām virknēm, nenulle skaitļiem un `true`; atgriež `false` tukšām virknēm, `0` un `false`.
   - Piemērs: `boolean(${name})` atgriež `true`, ja `name` nav tukšs.

2. `boolean-from-string(string)`: Atgriež `true`, ja virkne ir `'1'` vai `'true'` (reģistrjutīgs); citādi atgriež `false`.
   - Piemērs: `boolean-from-string(${enabled_flag})` — noderīgs, kad lauks glabā `'true'`/`'false'` kā tekstu.

3. `true()`: Atgriež boolean vērtību `true`.
   - Piemērs: Kolonnā `required`, `true()` ir ekvivalents `yes`.

4. `false()`: Atgriež boolean vērtību `false`.
   - Piemērs: `if(${skip_section} = 'yes', false(), true())` — dinamiski iestatīt obligāto.

5. `not(expression)`: Atgriež izteiksmes loģisko negāciju. Atgriež `true`, ja izteiksme ir false, un otrādi.
   - Piemērs: `not(${consent} = 'yes')` — rādīt brīdinājumu, kad piekrišana NAV sniegta.
   - Piemērs: `not(selected(${issues}, 'none'))` — pieprasīt sīkāku informāciju tikai tad, ja "none" nav atlasīts.

---

### Papildu virknes funkcijas

1. `starts-with(string, prefix)`: Atgriež `true`, ja `string` sākas ar `prefix`.
   - Piemērs: `starts-with(${phone}, '+254')` pārbauda, vai tālruņa numurs sākas ar Kenijas valsts kodu.

2. `contains(string, substring)`: Atgriež `true`, ja `string` satur `substring`.
   - Piemērs: `contains(${email}, '@')` pārbauda, vai e-pasta adresē ir `@` zīme.

3. `substring-before(string, needle)`: Atgriež `string` daļu, kas parādās pirms pirmā `needle` parādīšanās.
   - Piemērs: `substring-before(${full_name}, ' ')` izgūst pirmo vārdu (vārds).

4. `substring-after(string, needle)`: Atgriež `string` daļu, kas parādās pēc pirmā `needle` parādīšanās.
   - Piemērs: `substring-after(${email}, '@')` izgūst e-pasta adreses domēna daļu.

5. `normalize-space(string)`: Noņem sākuma un beigu atstarpes un samazina visas iekšējās atstarpes sekvences uz vienu atstarpi.
   - Piemērs: `normalize-space(${name})` — attīra vārdu, kas varētu būt ievadīts ar liekām atstarpēm.

6. `translate(string, search_chars, replace_chars)`: Aizstāj katru rakstzīmi `string`, kas parādās `search_chars`, ar atbilstošo rakstzīmi `replace_chars`. Rakstzīmes `search_chars`, kurām nav atbilstošas rakstzīmes `replace_chars`, tiek dzēstas.
   - Piemērs: `translate(${phone}, ' -()', '')` noņem atstarpes, domuzīmes un iekavas no tālruņa numura.

---

### Papildu matemātikas funkcijas

1. `floor(number)`: Atgriež lielāko veselo skaitli, kas ir mazāks par vai vienāds ar `number` (noapaļo uz negatīvo bezgalību).
   - Piemērs: `floor(4.9)` = 4, `floor(-2.1)` = -3

2. `ceiling(number)`: Atgriež mazāko veselo skaitli, kas ir lielāks par vai vienāds ar `number` (noapaļo uz pozitīvo bezgalību).
   - Piemērs: `ceiling(4.1)` = 5, `ceiling(-2.9)` = -2

3. `random()`: Atgriež nejauši izvēlētu decimālu skaitli starp 0.0 (ieskaitot) un 1.0 (neieskaitot). Parasti izmanto laukos `calculate`, lai piešķirtu nejaušas vērtības vai randomizētu jautājumu secību.
   - Piemērs: `random()` → piem., `0.7341`
   - Piemērs: `int(random() * 6) + 1` → nejaušs skaitlis 1–6 (kauliņu metiens)

4. `coalesce(a, b)`: Atgriež `a`, ja `a` nav tukšs; citādi atgriež `b`. Noderīgs kā rezerves variants, kad lauks varētu būt tukšs.
   - Piemērs: `coalesce(${preferred_name}, ${full_name})` — izmantot vēlamo vārdu, ja ir iestatīts, citādi atgriezties uz pilno vārdu.

5. `once(value)`: Novērtē `value` un saglabā to, bet tikai tad, ja pašreizējais lauks ir **tukšs**. Ja laukam jau ir vērtība, `once()` atgriež esošo vērtību nemainītu. Tas novērš pārrēķinā notiekošu lietotāja ievades pārrakstīšanu.
   - Piemērs: `once(today())` kolonnā `default` iestata šodienas datumu vienreiz un neatjaunina, ja enumerators atkārtoti atver formu.
   - Piemērs: `once(uuid())` ģenerē UUID vienreiz un saglabā to stabilu atkārtotas rediģēšanas laikā.

---

### Ģeo funkcijas

1. `area(geoshape_value)`: Aprēķina geoshape (daudzstūra) vērtības iekšā iekļautā **laukuma kvadrātmetros**.
   - Parametrs ir geoshape lauka vērtība formātā `lat1 lon1 0 0; lat2 lon2 0 0; ...`
   - Piemērs: `area(${field_boundary})` — aprēķināt apsekotā lauka laukumu m².
   - Piemērs: `round(area(${field_boundary}) div 10000, 2)` — pārveidot hektāros.

2. `distance(coordinates)`: Aprēķina geotrace (līnijas) **kopējo ceļa garumu metros** vai attālumu starp diviem geopoint laukiem.
   - Geotrace: `distance(${route})` atgriež kopējo ceļa garumu metros.
   - Diviem geopoint laukiem: `distance(concat(${point_a}, ' ', ${point_b}))` atgriež attālumu starp tiem.
   - Piemērs: `round(distance(${road_trace}) div 1000, 3)` — ceļa garums kilometros.

---

### Validācijas funkcijas

1. `regex(value, pattern)`: Atgriež `true`, ja `value` atbilst regulārajai izteiksmei `pattern`. Izmantojiet kolonnā `constraint` modeļbalstītai validācijai.
   - Modeļs izmanto standarta regex sintaksi (POSIX ERE apakškopa).
   - Piemērs: `regex(., '^[0-9]{10}$')` — validēt 10 ciparu skaitli.
   - Piemērs: `regex(., '^[A-Z]{2}[0-9]{6}$')` — validēt pases numura formātu (2 lielie burti, pēc tam 6 cipari).
   - Piemērs: `regex(., '^[^@]+@[^@]+\.[^@]{2,}$')` — pamata e-pasta formāta pārbaude.

2. `checklist(min, max, v1, v2, ...)`: Novērtē boolean izteiksmju sarakstu un atgriež `true`, ja `true` vērtību skaits ir starp `min` un `max` (ieskaitot). Padodiet `-1` par `min` vai `max`, lai izlaistu šo robežu.
   - Piemērs: `checklist(2, 3, ${q1} = 'yes', ${q2} = 'yes', ${q3} = 'yes')` — iziet, ja tieši 2 vai 3 no trim nosacījumiem ir patiesi.

3. `weighted-checklist(min, max, v1, w1, v2, w2, ...)`: Kā `checklist()`, bet katrai vērtībai ir svars. `true` vērtību svaru summai jābūt starp `min` un `max`.
   - Piemērs: `weighted-checklist(10, -1, ${has_toilet}, 4, ${has_sink}, 3, ${has_shower}, 5)` — klātesošo iekārtu svaru summai jābūt vismaz 10.

---

### Utilītu funkcijas

1. `uuid()`: Ģenerē nejaušu UUID (RFC 4122 v4 formāts) kā virkni.
   - Piemērs: `uuid()` → `'a3f8b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c'`
   - Parasti izmanto ar `once()`, lai ģenerētu stabilu unikālu ID: `once(uuid())`

2. `version()`: Atgriež formas `version` atribūta vērtību, kā iestatīts iestatījumu darblappā.
   - Piemērs: `version()` → `'3.1'`

3. `position()`: Izsaukts **atkārtojumu grupas** iekšā, atgriež pašreizējās atkārtojuma instances 1 bāzētu indeksu.
   - Piemērs: `position()` pirmajā instancē atgriež `1`, otrajā atgriež `2`, un tā tālāk.

4. `thousandsep(length, separator, value)`: Formatē skaitli ar tūkstošu atdalītāju. `length` ir minimālais kopējais virknes garums, `separator` ir izmantojamā rakstzīme (piem., `','`), un `value` ir formatējamais skaitlis.
   - Piemērs: `thousandsep(0, ',', 1234567)` → `'1,234,567'`

5. `substr-jsonpath(value, jsonpath)`: Izgūst apakšvirkni no JSON virknes, izmantojot JSONPath izteiksmi.
   - Piemērs: `substr-jsonpath(${api_response}, '$.data.name')` — izgūt `name` lauku no JSON virknes, kas glabājas `api_response`.
   - Parasti izmanto kopā ar `callapi()`, lai izgūtu konkrētas vērtības no API atbildēm.
