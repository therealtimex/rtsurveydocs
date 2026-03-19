---
title: "Média"
description: ""
icon: "code"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 286
---

Az rtSurvey gazdag médiaintegráció-támogatást biztosít a felmérésekhez, lehetővé téve a kérdőívek kiegészítését képekkel, hanggal és videóval. Ez a funkció jelentősen javíthatja a válaszadói élményt és az összegyűjtött adatok minőségét.

## Támogatott médiatípusok

Az rtSurvey a következő médiatípusokat támogatja:
- Képek (jpg, png, gif)
- Hang (mp3, wav)
- Videó (mp4, webm)

## Média hozzáadása a felméréshez

Az rtSurvey-űrlapba média beillesztéséhez használja az alábbi oszlopokat az XLSForm-ban:

- `image`: Képek megjelenítéséhez
- `audio`: Hangfájlok lejátszásához
- `video`: Videófájlok lejátszásához

Példa:

```
| type | name          | label         | image        | audio       | video       |
|------|---------------|---------------|--------------|-------------|-------------|
| note | media_example | Média példa   | example.jpg  | sound.mp3   | clip.mp4    |
```

## Médiafájlok kezelése

### Webes felmérések
A webes felmérésekhez az rtSurvey médiakezelő felületet biztosít, ahol feltöltheti és rendszerezheti a médiafájlokat. Ezek a fájlok ezután automatikusan elérhetővé válnak a felmérésekben.

### Mobilalkalmazás
Az rtSurvey mobilalkalmazás használatakor:
1. Helyezze a médiafájlokat az eszközön a `/rtSurvey/forms/[form-name]-media/` mappába.
2. Hivatkozzon a pontos fájlnévre az XLSForm-ban.

## rtSurvey-specifikus funkciók

### Dinamikus médiatöltés
Az rtSurvey támogatja a felmérési válaszokon alapuló dinamikus médiatöltést:

```
| type         | name      | label              | image                    |
|--------------|-----------|--------------------|--------------------------| 
| select_one species | animal | Válasszon állatot | ${animal}.jpg            |
```

### Média a válaszlehetőségekben
Az rtSurvey lehetővé teszi média használatát a kiválasztós kérdések válaszlehetőségeinél:

```
| type                | name    | label           | media::image |
|---------------------|---------|-----------------|--------------|
| select_one_from_file animals | Válasszon állatot |              |
```

A choices lapon:
```
| list_name | name  | label | media::image |
|-----------|-------|-------|--------------|
| animals   | dog   | Kutya | dog.jpg      |
| animals   | cat   | Macska | cat.jpg     |
```

### Médiarögzítés
Az rtSurvey kiterjeszti az XLSForm-ot médiarögzítési lehetőségekkel:

```
| type  | name        | label               |
|-------|-------------|---------------------|
| image | photo       | Készítsen fényképet |
| audio | voice_note  | Rögzítsen hangüzenetet |
| video | video_clip  | Rögzítsen videót    |
```

## Média használatának bevált módszerei

1. **Optimalizálja a fájlméreteket**: A nagy médiafájlok lelassíthatják a felmérés betöltését és beküldését.
2. **Használja a megfelelő formátumokat**: Tartsa be a széles körben támogatott formátumokat (jpg képekhez, mp3 hanghoz, mp4 videóhoz).
3. **Biztosítson alternatívákat**: Mindig adjon szöveges alternatívát az akadálymentesség érdekében.
4. **Alaposan tesztelje**: Győződjön meg arról, hogy a média megfelelően jelenik meg az összes céleszközön.
5. **Vegye figyelembe az offline használatot**: Offline is elvégezhető felmérések esetén győződjön meg arról, hogy az összes média elérhető helyi tárhelyen.

## Többnyelvű médiatámogatás

Az rtSurvey nyelvspecifikus médiát is támogat. Használja a `::nyelv` utótagot:

```
| type | name  | label    | image::Magyar | image::English |
|------|-------|----------|----------------|----------------|
| note | intro | Üdvözlet | welcome_hu.jpg | welcome_en.jpg |
```

## Média az adatexportban

Az rtSurvey-ből adatok exportálásakor:
- Webes felmérések esetén a média URL-jei szerepelnek az exportban.
- Mobilalkalmazásos felmérések esetén a fájlelérési utak szerepelnek.

## Mobilalkalmazás szempontjai

- Médiaintenzív felmérésekhez biztosítson elegendő tárhelyet az eszközökön.
- Az rtSurvey mobilalkalmazás offline médialejátszást és -rögzítést támogat.
- A nagy médiafájlok csökkenthetik az alkalmazás teljesítményét alacsony kategóriájú eszközökön.

## Ismert korlátozások

- Egyes régebbi böngészők esetleg nem támogatják az összes médiaformátumot.
- Nagyon nagy videófájlok alacsony sávszélességű helyzetekben problémákat okozhatnak.

## Médiaproblémák hibaelhárítása

1. **Média nem jelenik meg**: Ellenőrizze a fájlelérési utakat és neveket a pontosság érdekében.
2. **Lejátszási problémák**: Győződjön meg arról, hogy a médiaformátum támogatott a céleszközökön.
3. **Lassú betöltés**: Fontolja meg a fájlméretek optimalizálását vagy a média előzetes betöltését.

## Haladó médiatámogatás

### Geocímkézés
Az rtSurvey automatikusan geocímkézheti a felmérések során rögzített médiát:

```
| type  | name        | label        | appearance |
|-------|-------------|--------------|------------|
| image | photo       | Fénykép      | geotag     |
```

### Képannotációk
Engedélyezze a válaszadóknak a képek annotálását:

```
| type  | name        | label        | appearance |
|-------|-------------|--------------|------------|
| image | photo       | Annotálja a képet | annotate |
```

Az rtSurvey-ben a média hatékony használatával vonzóbb, informatívabb és pontosabb felméréseket hozhat létre. Ne feledje egyensúlyt tartani a média befoglalásának előnyei és a teljesítményre vonatkozó szempontok között, különösen korlátozott internetkapcsolattal rendelkező területeken vagy alacsony kategóriájú eszközökön végzett felmérések esetén.
