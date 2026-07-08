# KNX-Dokumentation Xerolux

Dieses Repository dokumentiert die KNX-Planung für das Wohnhausprojekt von Xerolux.

Ziel ist eine saubere Grundlage für die spätere ETS-Programmierung. Eine echte `.knxproj`-Datei wird nicht automatisch erzeugt, aber die Struktur, Gruppenadressen und Kanalbelegungen sind so vorbereitet, dass sie in ETS nachgebaut bzw. teilweise importiert werden können.

## Grundprinzip

Die Basisfunktionen sollen direkt und autark auf KNX laufen:

- Licht ein/aus über Relais-/Schaltaktoren
- Rollläden und Markise über Jalousieaktor
- Fußbodenheizung über Heizungsaktor
- Fensterstatus über KNX RF Fenstergriffe
- Wetter- und Windschutz über Wetterstation
- Präsenz-/Bewegungserkennung über Präsenzmelder
- Sicherheits- und Abwesenheitslogik über KNX

Home Assistant wird nur ergänzend genutzt:

- Visualisierung
- Komfortautomationen
- Statistiken
- Benachrichtigungen
- Fernzugriff

## Ordnerstruktur

```text
docs/
  01_topologie.md
  02_geraeteliste.md
  03_raeume_funktionen.md
  04_gruppenadressen.md
  05_kanalbelegung.md
  06_heizung_fenster.md
  07_beschattung_wetter.md
  08_rf_fenstergriffe.md
  09_home_assistant.md
  10_glastaster_bedienkonzept.md
ets-import/
  gruppenadressen.csv
  physikalische-adressen.csv
```

## Aktueller Stand

Erstplanung auf Basis der vorhandenen Hardware und der genannten Räume.

Neu ergänzt:

- Bedienkonzept für MDT Glastaster Smart II
- Glastaster steuern raumweise Licht und Rollläden
- Wohnzimmer-Glastaster steuert zusätzlich die Markise

Offene Punkte:

- finale Anzahl der MDT Glastaster Smart II
- finale Lichtkreise je Raum
- genaue Kanalbelegung der Relaisaktoren
- genaue Heizkreisanzahl je Raum
- genaue Position der Präsenzmelder
- finale Zuordnung der KNX RF Fenstergriffe
- Entscheidung, ob DALI/RGBW sofort oder später genutzt wird
