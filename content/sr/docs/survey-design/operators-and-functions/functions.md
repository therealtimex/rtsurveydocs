---
title: "Funkcije"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 293
---

### Funkcije za stringove

{{% alert icon=" " context="warning" %}}
Kada radite sa stringovima unutar izraza, važno je koristiti jednostruke navodnike ('') za zatvaranje literalnih stringova. Međutim, izuzetak nastaje kada želite da uključite jednostruke navodnike unutar literalnog stringa. U takvim slučajevima, možete koristiti dvostruke navodnike ("") za zatvaranje celog stringa.

Na primer:
- Tačno: if(${yesno} = 1, "string sa 'jednostrukim navodnicima' u njemu", "bez jednostrukih navodnika ovde")
- Netačno: if(${yesno} = 1, 'string sa 'jednostrukim navodnicima' u njemu', 'bez jednostrukih navodnika ovde')

Kada su u pitanju pametni navodnici, ključno je biti svestan njihovog prisustva, jer mogu izazvati probleme u izrazima. Mnogi urednici bogatog teksta automatski konvertuju prave navodnike ("" ili '') u pametne ili zaobljene navodnike ("" ili ''), što može rezultovati sintaksnim greškama ili neočekivanim ponašanjem. Da biste to izbegli, osigurajte da dosljedno koristite prave navodnike ('') u vašim izrazima.
{{% /alert %}}

rtSurvey podržava različite funkcije, uključujući:

1. `string(polje)`: Konvertuje polje u string.
   - Primer: `string(34.8)` biće konvertovano u `'34.8'`.

2. `string-length(polje)`: Vraća dužinu polja tipa string.
   - Primer: `string-length(.) > 3 and string-length(.) < 10` može se koristiti da osigura da je trenutno polje između 3 i 10 karaktera.

3. `substr(polje_ili_string, pocetni_indeks, krajnji_indeks)`: Vraća podniz koji počinje od `pocetni_indeks` i završava se neposredno pre `krajnji_indeks`. Indeksi počinju od 0 za prvi karakter u stringu.
   - Primer: `substr(${phone}, 0, 3)` će vratiti prve tri cifre broja telefona.

4. `concat(a, b, c, ...)`: Spaja polja (i/ili stringove) zajedno.
   - Primer: `concat(${firstname}, ' ', ${lastname})` će vratiti puno ime kombinovanjem vrednosti u poljima `firstname` i `lastname`.

5. `linebreak()`: Vraća karakter za prelom reda.
   - Primer: `concat(${field1}, linebreak(), ${field2}, linebreak(), ${field3})` će vratiti listu od tri vrednosti polja sa prelomima redova između njih.

6. `lower()`: Konvertuje string u sva mala slova.
   - Primer: `lower('Naziv ulice')` će vratiti "naziv ulice".

7. `upper()`: Konvertuje string u sva velika slova.
   - Primer: `upper('Naziv ulice')` će vratiti "NAZIV ULICE".

### Funkcije za select_one i select_multiple

1. `count-selected(polje)`: Vraća broj stavki izabranih u polju select_multiple.
   - Primer: `count-selected(.) = 3` može se koristiti kao izraz ograničenja da osigura da su tačno tri opcije izabrane.

2. `selected(polje, vrednost)`: Vraća tačno ili netačno u zavisnosti od toga da li je navedena vrednost izabrana u polju select_one ili select_multiple.
   - Primer: `selected(${color}, 'Blue')` može se koristiti kao izraz relevantnosti za prikazivanje grupe ili polja samo ako je ispitanik izabrao "Plavo" kao omiljenu boju.
   - Napomena: Drugi parametar treba uvek da navodi vrednost opcije, ne oznaku opcije. Koristite vrednost iz kolone vrednosti u radnom listu choices definicije formulara.

3. `selected-at(polje, broj)`: Vraća izabranu stavku na navedenoj poziciji u polju select_multiple. Kada je prosleđeni broj 0, vraća prvu izabranu stavku; kada je broj 1, vraća drugu izabranu stavku, i tako dalje.
   - Primer: `selected-at(${fruits}, 0) = 'Apple'` može se koristiti kao izraz relevantnosti za prikazivanje grupe ili polja samo ako je prvi izabrani izbor "Jabuka".
   - Napomena: Vraćena vrednost će biti vrednost opcije, ne oznaka opcije. Koristite vrednost iz kolone vrednosti u radnom listu choices definicije formulara.

4. `choice-label(polje, vrednost)`: Vraća oznaku za izbor polja select_one ili select_multiple, kako je definisano u radnom listu choices definicije formulara.
   - Primer 1: `choice-label(${country}, ${country})` će vratiti oznaku opcije za trenutno izabrani izbor u polju nazvanom `country`.
   - Primer 2: `choice-label(${languages}, selected-at(${languages}, 0))` će vratiti oznaku za prvi izabrani izbor u polju nazvanom `languages`.
   - Napomena: Ova funkcija dohvata oznaku opcije, ne vrednost. Koristi kolonu oznake iz radnog lista choices definicije formulara.

### Funkcije za ponavljajuća polja

U rtSurvey-u, ako želite da postavljate ista pitanja više puta, možete staviti polje unutar grupe ponavljanja. Ovo rezultuje u više instanci istog polja. Sledeće funkcije vam mogu pomoći u radu sa ovim ponavljajućim poljima i ponavljajućim podacima koje oni proizvode. Pogledajte temu pomoći o ponavljajućim poljima za više detalja.

1. `join(string, ponavljajuce_polje)`: Za polje unutar grupe ponavljanja, generiše listu vrednosti razdvojenu stringom. Prvi parametar navodi delimiter koji se koristi za razdvajanje vrednosti.
   - Primer: `join(', ', ${member_name})` će generisati jednu listu razdvojenu zarezima od svih unetih imena.

2. `join-if(string, ponavljajuce_polje, izraz)`: Funkcioniše tačno kao `join()`, osim što proverava svaku instancu u grupi ponavljanja koristeći navedeni izraz. Ako se izraz evaluira kao netačno, stavka će biti izostavljena iz izlaza.
   - Primer: `join-if(', ', ${member_name}, ${age} >= 18)` će generisati listu razdvojenu zarezima sa imenima samo odraslih članova (onih sa godinama 18 i više).

3. `count(grupa_ponavljanja)`: Vraća trenutni broj puta da se grupa ponavljanja ponovila.
   - Primer: `count(${groupname})` će vratiti broj instanci grupe.

4. `count-if(grupa_ponavljanja, izraz)`: Funkcioniše tačno kao `count()`, osim što proverava svaku instancu u grupi ponavljanja koristeći navedeni izraz. Ako se izraz evaluira kao netačno, stavka će biti izostavljena iz izlaza.
   - Primer: `count-if(${members}, ${age} >= 18)` će vratiti broj odraslih članova na osnovu polja za godine unutar grupe ponavljanja "members".

5. `sum(ponavljajuce_polje)`: Za polje unutar grupe ponavljanja, izračunava zbir svih vrednosti.
   - Primer: `sum(${loan_amount})` će vratiti ukupnu vrednost svih zajmova.

6. `sum-if(ponavljajuce_polje, izraz)`: Funkcioniše tačno kao `sum()`, osim što proverava svaku instancu u grupi ponavljanja koristeći navedeni izraz. Ako se izraz evaluira kao netačno, stavka će biti izostavljena iz izlaza.
   - Primer: `sum-if(${loan_amount}, ${loan_amount} > 500)` će vratiti ukupnu vrednost svih zajmova koji su veći od 500. Manji zajmovi će biti ignorisani.

7. `min(ponavljajuce_polje)`: Za polje unutar grupe ponavljanja, izračunava minimum svih vrednosti.
   - Primer: `min(${member_age})` će vratiti godine najmlađeg člana u grupi.

8. `min-if(ponavljajuce_polje, izraz)`: Funkcioniše tačno kao `min()`, osim što proverava svaku instancu u grupi ponavljanja koristeći navedeni izraz. Ako se izraz evaluira kao netačno, stavka će biti izostavljena iz izlaza.
   - Primer: `min-if(${member_age}, ${member_age} >= 18)` će vratiti godine najmlađeg odraslog u grupi. Oni mlađi od 18 godina će biti ignorisani.

9. `max(ponavljajuce_polje)`: Za polje unutar grupe ponavljanja, izračunava maksimum svih vrednosti.
   - Primer: `max(${member_age})` će vratiti godine najstarijeg člana u grupi.

10. `max-if(ponavljajuce_polje, izraz)`: Funkcioniše tačno kao `max()`, osim što proverava svaku instancu u grupi ponavljanja koristeći navedeni izraz. Ako se izraz evaluira kao netačno, stavka će biti izostavljena iz izlaza.
    - Primer: `max-if(${member_age}, ${member_age} >= 18)` će vratiti godine najstarijeg odraslog u grupi. Oni mlađi od 18 godina će biti ignorisani.

11. `index()`: Pozvano unutar grupe ponavljanja, vraća indeksni broj za trenutnu grupu ili instancu.
    - Primer: `index()` kada se koristi unutar grupe ponavljanja vratiće 1 za prvu instancu, 2 za drugu, i tako dalje.

12. `indexed-repeat(ponavljajuce_polje, grupa_ponavljanja, indeks)`: Referencira polje ili grupu koja je unutar grupe ponavljanja spolja te grupe ponavljanja. Prvi parametar navodi ponavljajuće polje ili grupu od interesa, drugi navodi grupu ponavljanja unutar koje se polje ili grupa nalazi, a treći navodi broj instance unutar grupe ponavljanja koja se koristi.
    - Primer 1: `indexed-repeat(${name}, ${names}, 1)` će vratiti prvo dostupno ime kada je polje name unutar prethodne grupe ponavljanja nazvane "names".
    - Primer 2: `indexed-repeat(${name}, ${names}, index())` će povući ime koje odgovara broju instance trenutne grupe ponavljanja.

13. `rank-index(indeks, ponavljajuce_polje)`: Ova funkcija izračunava redni rang navedene instance ponavljajućeg polja za upotrebu izvan grupe ponavljanja. Rang 1 se dodeljuje instanci sa najvišom vrednošću, rang 2 instanci sa sledećom najvišom vrednošću, i tako dalje. Ako prosledite nevažeći indeks ili indeks na instancu sa nenumeričkom vrednošću, vratiće se rang 999.
    - Primer: `rank-index(1, ${random_draw})` izračunava rang prve instance na osnovu vrednosti njenog polja `random_draw` u poređenju sa vrednostima ostalih instanci.

14. `rank-index-if(indeks, ponavljajuce_polje, izraz)`: Ova funkcija radi slično kao `rank-index()`, ali proverava svaku instancu u grupi ponavljanja ponavljajućeg polja koristeći navedeni izraz. Ako se izraz evaluira kao netačno, stavka će biti izostavljena iz proračuna. Indeks koji se koristi zasniva se na punom skupu instanci pre evaluacije izraza za svaku instancu. Ako prosledite indeks za instancu koja je bila ignorisana jer nije zadovoljila izraz, smatra se nevažećim indeksom i vratiće se rang 999.
    - Primer: `rank-index-if(1, ${age}, ${age} >= 18)` izračunava rang godina unutar skupa odraslih, uzimajući u obzir samo instance gde su godine veće ili jednake 18.

### Numeričke funkcije

{{< table >}}
| Operator | Operacija | Primer | Primer odgovora |
|----------|-----------|--------|-----------------|
| `+` | Sabiranje | 1 + 1 | 2 |
| `-` | Oduzimanje | 3 - 2 | 1 |
| `*` | Množenje | 3 * 2 | 6 |
| `div` | Deljenje | 10 div 2 | 5 |
| `mod` | Moduo | 9 mod 2 | 1 |
{{< /table >}}

rtSurvey podržava numeričke funkcije, uključujući:
- `number(polje)`: Konvertuje vrednost polja u broj.
  - Primer: `number('34.8')` = 34.8

- `int(polje)`: Konvertuje vrednost polja u integer.
  - Primer: `int('39.2')` = 39

- `min(polje1, ..., poljeX)`: Vraća minimalnu vrednost među prosleđenim poljima.
  - Primer: `min(${father_age}, ${mother_age})` će vratiti godine oca ili majke, koja god je manja.

- `max(polje1, ..., poljeX)`: Vraća maksimalnu vrednost među prosleđenim poljima.
  - Primer: `max(${father_age}, ${mother_age})` će vratiti godine oca ili majke, koja god je veća.

- `format-number(polje)`: Formatira vrednost integer ili decimal polja prema korisničkim lokalnim podešavanjima.
  - Primer: `format-number(${income})` Ovaj izraz može formatirati "120000" kao "120,000".

- `round(polje, cifre)`: Zaokružuje numeričku vrednost polja na navedeni broj cifara iza decimalne tačke.
  - Primer: `round(${interest_rate}, 2)`

- `abs(broj)`: Vraća apsolutnu vrednost broja.

- `pow(osnova, eksponent)`: Vraća vrednost prvog parametra podignuto na stepen drugog parametra.
  - Svaki parametar može biti polje, broj ili izraz.

- `log10(polje_ili_vrednost)`: Vraća logaritam baze deset polja ili vrednosti prosleđene.

- `sin(polje_ili_vrednost)`: Vraća sinus polja ili vrednosti prosleđene, izražen u radijanima.

- `cos(polje_ili_vrednost)`: Vraća kosinus polja ili vrednosti prosleđene, izražen u radijanima.

- `tan(polje_ili_vrednost)`: Vraća tangens polja ili vrednosti prosleđene, izražen u radijanima.

- `asin(polje_ili_vrednost)`: Vraća arkus sinus polja ili vrednosti prosleđene, izražen u radijanima.

- `acos(polje_ili_vrednost)`: Vraća arkus kosinus polja ili vrednosti prosleđene, izražen u radijanima.

- `atan(polje_ili_vrednost)`: Vraća arkus tangens polja ili vrednosti prosleđene, izražen u radijanima.

- `atan2(x, y)`: Vraća ugao u radijanima koji zaklapa koordinatni početak sa tačkom koordinata (x, y) i pozitivnom x-osom. Rezultat je u opsegu od -pi() do pi().

- `sqrt(polje_ili_vrednost)`: Vraća nenegativan kvadratni koren polja ili vrednosti prosleđene.

- `exp(x)`: Vraća vrednost e^x.

- `pi()`: Vraća vrednost pi.

### Funkcije za datum i vreme

{{% alert icon=" " context="warning" %}}
Vrednosti datuma u rtSurvey-u se čuvaju kao stringovi u formatu `YYYY-MM-DD`. Vrednosti datetime se čuvaju kao ISO 8601 stringovi (`YYYY-MM-DDTHH:MM:SS`). Koristite `decimal-date-time()` za konverziju u broj radi aritmetike (npr. izračunavanje trajanja).
{{% /alert %}}

1. `today()`: Vraća današnji datum kao string u formatu `YYYY-MM-DD`. Evaluira se jednom kada se formular otvori.
   - Primer: `today()` → `'2024-03-15'`
   - Uobičajena upotreba: Kolona `default` za prethodno popunjavanje današnjeg datuma, ili u `relevant`/`constraint` za poređenje sa poljem datuma.

2. `now()`: Vraća trenutni datum i vreme kao ISO 8601 string. Evaluira se svaki put kada se izraz izračunava.
   - Primer: `now()` → `'2024-03-15T14:32:00.000+03:00'`
   - Uobičajena upotreba: Beleženje tačne vremenske oznake određenog događaja tokom ankete.

3. `date(vrednost)`: Konvertuje vrednost (string ili broj) u string datuma. Korisno za prinudno konvertovanje izračunatih vrednosti u tip datuma.
   - Primer: `date('2024-03-15')` → `'2024-03-15'`

4. `date-time(vrednost)`: Konvertuje vrednost u string datetime.
   - Primer: `date-time(${event_timestamp})`

5. `decimal-date-time(vrednost)`: Konvertuje string datuma ili datetime u decimalni broj koji predstavlja milisekunde od Unix epohe podeljene sa 86400000 (tj. frakcione dane od 1970-01-01). Koristite ovo za obavljanje aritmetike nad datumima.
   - Primer: Trajanje u danima između dva datuma:
     `decimal-date-time(${end_date}) - decimal-date-time(${start_date})`
   - Primer: Trajanje u minutama između dva datetime-a:
     `(decimal-date-time(${end_time}) - decimal-date-time(${start_time})) * 1440`

6. `format-date(datum, format)`: Formatira vrednost datuma koristeći string uzorka.
   - Tokeni formata: `%Y` (4-cifrena godina), `%y` (2-cifrena godina), `%m` (mesec 01–12), `%d` (dan 01–31), `%a` (skraćeni naziv dana u sedmici), `%b` (skraćeni naziv meseca)
   - Primer: `format-date(today(), '%d/%m/%Y')` → `'15/03/2024'`
   - Primer: `format-date(${dob}, '%B %d, %Y')` → `'March 15, 1990'`

7. `format-date-time(datetime, format)`: Formatira vrednost datetime koristeći string uzorka. Prihvata sve tokene `format-date` plus:
   - `%H` (sat 00–23), `%h` (sat 01–12), `%M` (minuti 00–59), `%S` (sekunde 00–59), `%3` (milisekunde), `%P` (AM/PM)
   - Primer: `format-date-time(now(), '%d/%m/%Y %H:%M')` → `'15/03/2024 14:32'`
   - Primer: `format-date-time(${event_time}, '%I:%M %p')` → `'02:32 PM'`

---

### Boolean funkcije

1. `boolean(vrednost)`: Konvertuje bilo koju vrednost u boolean. Vraća `true` za neprazne stringove, nenulte brojeve i `true`; vraća `false` za prazne stringove, `0` i `false`.
   - Primer: `boolean(${name})` vraća `true` ako `name` nije prazno.

2. `boolean-from-string(string)`: Vraća `true` ako je string `'1'` ili `'true'` (bez obzira na velika/mala slova); vraća `false` inače.
   - Primer: `boolean-from-string(${enabled_flag})` — korisno kada polje čuva `'true'`/`'false'` kao tekst.

3. `true()`: Vraća boolean vrednost `true`.
   - Primer: U koloni `required`, `true()` je ekvivalent sa `yes`.

4. `false()`: Vraća boolean vrednost `false`.
   - Primer: `if(${skip_section} = 'yes', false(), true())` — dinamički postavljanje obaveznog.

5. `not(izraz)`: Vraća logičku negaciju izraza. Vraća `true` ako je izraz netačan, i obratno.
   - Primer: `not(${consent} = 'yes')` — prikazuje upozorenje kada saglasnost NIJE data.
   - Primer: `not(selected(${issues}, 'none'))` — zahteva detalje samo ako "nijedno" nije izabrano.

---

### Dodatne funkcije za stringove

1. `starts-with(string, prefiks)`: Vraća `true` ako `string` počinje sa `prefiks`.
   - Primer: `starts-with(${phone}, '+254')` proverava da li broj telefona počinje sa keniskim pozivnim brojem.

2. `contains(string, podniz)`: Vraća `true` ako `string` sadrži `podniz`.
   - Primer: `contains(${email}, '@')` proverava da email adresa ima znak `@`.
   - Primer: `contains(${notes}, 'urgent')` pokreće pitanje za praćenje ako beleške pominju "hitno".

3. `substring-before(string, granicnik)`: Vraća deo `stringa` koji se pojavljuje pre prvog pojavljivanja `granicnika`.
   - Primer: `substring-before(${full_name}, ' ')` izvlači prvu reč (ime).

4. `substring-after(string, granicnik)`: Vraća deo `stringa` koji se pojavljuje posle prvog pojavljivanja `granicnika`.
   - Primer: `substring-after(${email}, '@')` izvlači deo domene email adrese.

5. `normalize-space(string)`: Uklanja vodeće i prateće razmake i sve interne sekvence razmaka redukuje na jedan razmak.
   - Primer: `normalize-space(${name})` — čisti ime koje možda ima dodatne razmake.

6. `translate(string, znakovi_za_trazenje, znakovi_za_zamenu)`: Zamenjuje svaki karakter u `stringu` koji se pojavljuje u `znakovi_za_trazenje` odgovarajućim karakterom u `znakovi_za_zamenu`. Karakteri u `znakovi_za_trazenje` bez odgovarajućeg karaktera u `znakovi_za_zamenu` se brišu.
   - Primer: `translate(${code}, 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')` konvertuje u velika slova (ekvivalent sa `upper()`).
   - Primer: `translate(${phone}, ' -()', '')` uklanja razmake, crtice i zagrade iz broja telefona.

---

### Dodatne matematičke funkcije

1. `floor(broj)`: Vraća najveći integer manji ili jednak `broju` (zaokružuje ka negativnoj beskonačnosti).
   - Primer: `floor(4.9)` = 4, `floor(-2.1)` = -3

2. `ceiling(broj)`: Vraća najmanji integer veći ili jednak `broju` (zaokružuje ka pozitivnoj beskonačnosti).
   - Primer: `ceiling(4.1)` = 5, `ceiling(-2.9)` = -2

3. `random()`: Vraća nasumičan decimalni broj između 0.0 (uključivo) i 1.0 (isključivo). Obično se koristi u poljima `calculate` za dodeljivanje nasumičnih vrednosti ili nasumičan redosled pitanja.
   - Primer: `random()` → npr. `0.7341`
   - Primer: `int(random() * 6) + 1` → nasumičan broj 1–6 (bacanje kockice)

4. `coalesce(a, b)`: Vraća `a` ako `a` nije prazno; inače vraća `b`. Korisno kao rezervna opcija kada polje može biti prazno.
   - Primer: `coalesce(${preferred_name}, ${full_name})` — koristi preferirano ime ako je postavljeno, inače se vraća na puno ime.

5. `once(vrednost)`: Evaluira `vrednost` i čuva je, ali samo ako je trenutno polje **prazno**. Ako polje već ima vrednost (npr. prethodno je postavljeno), `once()` vraća postojeću vrednost nepromenjenu. Ovo sprečava ponovni proračun da prepiše korisnički unos.
   - Primer: `once(today())` u koloni `default` postavlja današnji datum jednom i ne ažurira ga ako anketar ponovo otvori formular.
   - Primer: `once(uuid())` generiše UUID jednom i zadržava ga stabilnim tokom ponovnih uređivanja.

---

### Geo funkcije

1. `area(vrednost_geoshape)`: Izračunava **površinu u kvadratnim metrima** unutar geoshape (poligona) vrednosti.
   - Parametar je vrednost geoshape polja u formatu `sirina1 duzina1 0 0; sirina2 duzina2 0 0; ...`
   - Primer: `area(${field_boundary})` — izračunava površinu anketiranog polja u m².
   - Primer: `round(area(${field_boundary}) div 10000, 2)` — konvertuje u hektare.

2. `distance(koordinate)`: Izračunava **ukupnu dužinu puta u metrima** geotrace (linije), ili rastojanje između dva geopoint-a.
   - Za geotrace: `distance(${route})` vraća ukupnu dužinu puta u metrima.
   - Za dva geopoint-a: `distance(concat(${point_a}, ' ', ${point_b}))` vraća rastojanje između njih.
   - Primer: `round(distance(${road_trace}) div 1000, 3)` — dužina puta u kilometrima.

---

### Funkcije za validaciju

1. `regex(vrednost, uzorak)`: Vraća `true` ako `vrednost` odgovara regularnom izrazu `uzorak`. Koristite u koloni `constraint` za validaciju zasnovanu na uzorku.
   - Uzorak koristi standardnu regex sintaksu (podskup POSIX ERE).
   - Primer: `regex(., '^[0-9]{10}$')` — validira 10-cifreni broj.
   - Primer: `regex(., '^[A-Z]{2}[0-9]{6}$')` — validira format broja pasoša (2 velika slova praćena sa 6 cifara).
   - Primer: `regex(., '^[^@]+@[^@]+\.[^@]{2,}$')` — osnovna provera formata email adrese.

2. `checklist(min, max, v1, v2, ...)`: Evaluira listu boolean izraza i vraća `true` ako je broj `true` vrednosti između `min` i `max` (uključivo). Prosledite `-1` za `min` ili `max` da preskočite tu granicu.
   - Primer: `checklist(2, 3, ${q1} = 'yes', ${q2} = 'yes', ${q3} = 'yes')` — prolazi ako su tačno 2 ili 3 od tri uslova tačna.
   - Primer: `checklist(1, -1, ${smoke_alarm}, ${fire_ext}, ${emergency_plan})` — najmanje jedna bezbednosna mera mora biti tačna.

3. `weighted-checklist(min, max, v1, w1, v2, w2, ...)`: Kao `checklist()`, ali svaka vrednost ima težinu. Zbir težina za `true` vrednosti mora biti između `min` i `max`.
   - Primer: `weighted-checklist(10, -1, ${has_toilet}, 4, ${has_sink}, 3, ${has_shower}, 5)` — zbir težina prisutnih objekata mora biti najmanje 10.

---

### Korisne funkcije

1. `uuid()`: Generiše nasumičan UUID (RFC 4122 v4 format) kao string.
   - Primer: `uuid()` → `'a3f8b2c1-4d5e-6f7a-8b9c-0d1e2f3a4b5c'`
   - Obično se koristi sa `once()` za generisanje stabilnog jedinstvenog ID-a: `once(uuid())`

2. `version()`: Vraća vrednost atributa `version` formulara kako je postavljeno u radnom listu settings.
   - Primer: `version()` → `'3.1'`
   - Korisno u poljima `calculate` za ugrađivanje verzije formulara u izvezene podatke.

3. `position()`: Kada se pozove unutar **grupe ponavljanja**, vraća indeks koji počinje od 1 trenutne instance ponavljanja.
   - Primer: `position()` u prvoj instanci vraća `1`, u drugoj vraća `2`, i tako dalje.
   - Pogledajte takođe: `index()` (pseudonim), `indexed-repeat()` za referenciranje vrednosti ponavljanja spolja.

4. `thousandsep(duzina, separator, vrednost)`: Formatira broj sa separatorom hiljada. `duzina` je minimalna ukupna dužina stringa (dopunjena razmacima ako je kraća), `separator` je karakter koji se koristi (npr. `','`), a `vrednost` je broj za formatiranje.
   - Primer: `thousandsep(0, ',', 1234567)` → `'1,234,567'`
   - Primer: `thousandsep(0, '.', ${income})` → formatira prihod sa tačkom kao separatorom hiljada.

5. `substr-jsonpath(vrednost, jsonpath)`: Izvlači podniz iz JSON stringa koristeći JSONPath izraz.
   - Primer: `substr-jsonpath(${api_response}, '$.data.name')` — izvlači polje `name` iz JSON stringa sačuvanog u `api_response`.
   - Obično se koristi uz `callapi()` za izvlačenje specifičnih vrednosti iz API odgovora.
