---
title: "Hidden"
description: "Verborgene Felder speichern Werte, die dem Befragten nie angezeigt werden — sie werden verwendet, um Kontext weiterzugeben, Daten vorzubefüllen oder Zwischenergebnisse zu speichern."
icon: "eye-slash"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 239
---

Ein `hidden`-Feld speichert einen Wert, der dem **Befragten nie angezeigt wird**. Im Gegensatz zu `calculate` (das einen Wert berechnet) wird `hidden` verwendet, um einen **extern bereitgestellten Wert** einzubringen — zum Beispiel eine Aufgaben-ID, eine Haushalts-ID aus einem anderen System oder einen Interviewer-Code, der beim Starten des Formulars injiziert wird.

## Grundlegende XLSForm-Spezifikation

| type | name | label |
|------|------|-------|
| hidden | household_id | |

Beschriftungen sind für verborgene Felder nicht erforderlich, da nichts auf dem Bildschirm dargestellt wird.

## Anwendungsbereiche

Verborgene Felder werden häufig verwendet für:

1. Weitergabe einer vorab zugewiesenen ID aus dem Umfrageverwaltungssystem (z. B. Haushalts-ID, Fallnummer, Aufgabencode)
2. Speicherung der Formularversion oder von Bereitstellungsmetadaten
3. Injektion von interviewerspezifischer Konfiguration beim Starten des Formulars
4. Übertragung von Daten aus einem übergeordneten Formular in ein untergeordnetes Formular in verknüpften Arbeitsabläufen
5. Speicherung eines Werts, der aus URL-Parametern abgeleitet wird, wenn das Formular über einen Weblink geöffnet wird

## Standardwert festlegen

Das häufigste Muster ist die Verwendung von `hidden` mit einem `default`-Ausdruck, damit der Wert beim Öffnen des Formulars gesetzt wird:

| type | name | default |
|------|------|---------|
| hidden | deployment_code | 'ZONE_A_2024' |
| hidden | form_version | '3.1' |

## Referenzierung eines verborgenen Feldes in Berechnungen

Verborgene Werte können wie jedes andere Feld mit `${fieldname}` referenziert werden:

| type | name | label | calculation |
|------|------|-------|-------------|
| hidden | zone_code | | |
| calculate | label_prefix | | concat('[', ${zone_code}, '] ') |
| note | intro | ${label_prefix} Willkommen zur Haushaltsumfrage | |

## Verwendung von hidden mit Vorbefüllung / URL-Parametern

Beim Starten eines Webformulars über URL können Sie Parameter übergeben, die verborgene Felder befüllen. Dadurch können Sie eine Haushalts-ID oder einen Aufgabencode vorab laden, ohne dass der Interviewer ihn eintippen muss:

```
https://your-server.com/form/FORMID?household_id=H00123&zone_code=NORTH
```

Das Feld namens `household_id` wird automatisch mit `H00123` befüllt.

## Empfohlene Vorgehensweisen

1. Verwenden Sie `hidden` (nicht `calculate`), wenn der Wert **extern injiziert** wird und nicht neu berechnet werden soll.
2. Verwenden Sie `calculate`, wenn der Wert **aus anderen Feldern** im Formular abgeleitet wird.
3. Setzen Sie immer einen `default`, wenn das verborgene Feld einen Wert haben muss — ein verborgenes Feld ohne Standard ist leer.
4. Benennen Sie verborgene Felder klar, um sie zu unterscheiden (z. B. mit dem Präfix `_hidden_` oder einer konsistenten Namenskonvention).

## Einschränkungen

- Verborgene Felder werden wie jedes andere Feld in den exportierten Daten aufgenommen.
- Sie können nicht bedingt angezeigt werden — sie sind immer vorhanden (aber unsichtbar).
- Wenn Sie ein Feld benötigen, das sich dynamisch berechnet, verwenden Sie stattdessen `calculate`.
