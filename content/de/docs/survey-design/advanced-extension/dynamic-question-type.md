---
title: "Dynamischer Fragetyp"
description: "Der dynamische Fragetyp ermöglicht es, den Fragetyp und das Widget eines Feldes zur Laufzeit basierend auf einer API-Antwort oder einem berechneten Wert zu bestimmen."
icon: "manage_search"
date: "2023-05-22T00:44:31+01:00"
lastmod: "2023-05-22T00:44:31+01:00"
draft: false
toc: true
weight: 301
---

Die Funktion **Dynamischer Fragetyp** ermöglicht es, das Eingabe-Widget und das Validierungsverhalten eines Feldes **zur Laufzeit** statt beim Formulardesign zu bestimmen. Dies ist eine fortgeschrittene rtSurvey-Erweiterung, die verwendet wird, wenn der zu erfassende Datentyp von einer serverseitigen Konfiguration, einer API-Antwort oder einem vorherigen Feldwert abhängt.

Ein häufiger Anwendungsfall ist eine konfigurierbare Inspektionscheckliste, bei der der Server definiert, welche Felder erforderlich sind, welchen Typ sie haben (text, integer, select usw.) und welche Optionen verfügbar sind — ohne das Formular für jede Konfiguration neu erstellen zu müssen.

---

## Funktionsweise

Ein als dynamischer Fragetyp markiertes Feld verwendet `callapi()`, um seine Konfiguration von einer API abzurufen. Die API-Antwort definiert:

- Den zu rendernden Eingabetyp (text, integer, select_one usw.)
- Die verfügbaren Auswahlmöglichkeiten (für Auswahltypen)
- Validierungsregeln

Das Feld ist intern mit `specialFeature: isDynamicQuestionType` markiert, was der Formular-Engine mitteilt, die API-Antwort zum Aufbau des Widgets zu verwenden, statt der statischen Formulardefinition.

---

## Einrichtung

### Schritt 1: Feldkonfiguration abrufen

Verwenden Sie ein `calculate`-Feld mit `callapi()`, um die dynamische Konfiguration abzurufen:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| calculate | field_config | | callapi | `callapi('POST', 'https://api.example.com/field-config', 1, 2, 0, '$.config', 10000, 0, '', '', '{"form_id": "##form_id##", "field_id": "inspection_result"}')` |

### Schritt 2: Die Konfiguration im dynamischen Feld referenzieren

Das dynamische Feld verwendet `callapi-verify()` in seinem `appearance` oder `constraint`, um die abgerufene Konfiguration zu verknüpfen:

| type | name | label | appearance |
|------|------|-------|------------|
| text | inspection_result | Inspektionsergebnis | `callapi-verify(dynamicParams)` |

Die Formular-Engine liest `field_config` und bestimmt dynamisch, ob `inspection_result` als `text`-, `integer`- oder `select_one`-Feld gerendert werden soll.

---

## API-Antwortformat

Die API sollte ein JSON-Objekt zurückgeben, das die Feldkonfiguration beschreibt. Eine typische Antwort:

```json
{
  "config": {
    "type": "select_one",
    "choices": [
      {"value": "pass", "label": "Bestanden"},
      {"value": "fail", "label": "Nicht bestanden"},
      {"value": "na", "label": "Nicht anwendbar"}
    ],
    "required": true,
    "constraint": ". != ''"
  }
}
```

---

## Beispiel: Konfigurierbares Inspektionsformular

Ein Inspektionsformular, bei dem die Checklistenpunkte und ihre Antworttypen basierend auf der Inspektionskategorie vom Server abgerufen werden:

| type | name | label | appearance | calculation |
|------|------|-------|------------|-------------|
| select_one inspection_type | insp_type | Art der Inspektion | | |
| calculate | checklist_config | | callapi | `callapi('POST', 'https://api.example.com/checklist', 1, 2, 0, '$.items', 10000, 0, '', '', '{"type": "##insp_type##"}')` |
| text | item_1 | Punkt 1 | `callapi-verify(dynamicParams)` | |
| text | item_2 | Punkt 2 | `callapi-verify(dynamicParams)` | |
| text | item_3 | Punkt 3 | `callapi-verify(dynamicParams)` | |

Der Server gibt den korrekten Widget-Typ, die Beschriftung, die Auswahlmöglichkeiten und die Validierung für jeden Punkt basierend auf `insp_type` zurück.

---

## Empfohlene Vorgehensweisen

1. Verwenden Sie dynamische Fragetypen nur, wenn sich die Feldstruktur tatsächlich zur Laufzeit ändert — für statische Formulare verwenden Sie Standard-Fragetypen.
2. Stellen Sie sicher, dass die Konfigurations-API schnell antwortet (unter 2 Sekunden) und im Feldnetzwerk verfügbar ist.
3. Definieren Sie immer einen sinnvollen Fallback im Formular für den Fall, dass die API nicht erreichbar ist — ein einfaches `text`-Feld mit einer Notiz ist besser als ein defektes Widget.
4. Versionieren Sie Ihr API-Antwortschema — Änderungen am Antwortformat wirken sich auf alle aktiven Formulare aus, die diesen Endpunkt verwenden.
5. Testen Sie jede Kombination von Feldtypen, die die API zurückgeben kann, vor dem Einsatz.

## Einschränkungen

- Dynamische Fragetypen erfordern Netzwerkkonnektivität, um die Konfiguration abzurufen.
- Die vollständige Palette der dynamisch verfügbaren Widget-Typen hängt von der rtSurvey-Client-Version ab — testen Sie Ihre Zielversion.
- Dies ist eine fortgeschrittene rtSurvey-Erweiterung ohne Entsprechung in der Standard-XLSForm-Spezifikation.
- Debug-Fehler sind schwerer zu verfolgen, da die Felddefinition teils im Formular und teils in der API-Antwort liegt.
