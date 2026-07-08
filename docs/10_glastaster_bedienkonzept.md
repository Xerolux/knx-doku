# 10 – MDT Glastaster Smart II Bedienkonzept

## Grundidee

Die Glastaster sollen nicht nur Licht schalten, sondern auch die Rollläden im jeweiligen Raum bedienen.

Wichtig: Die Glastaster bekommen dafür keine eigenen Rollladen-Gruppenadressen. Sie senden direkt auf die Gruppenadressen der jeweiligen Rollläden.

## Wohnzimmer

Der Wohnzimmer-Glastaster steuert:

- Wohnzimmer Licht
- Rollladen Wohnzimmer links
- Rollladen Wohnzimmer rechts
- Markise
- Szenen / Reserve

Vorschlag Tastenbelegung:

| Taste | Kurz drücken | Lang drücken |
|---|---|---|
| 1 | Licht Wohnzimmer umschalten | Reserve |
| 2 | Rollladen links hoch/runter | Stop / Position |
| 3 | Rollladen rechts hoch/runter | Stop / Position |
| 4 | Markise aus/ein | Stop / Position |
| 5 | Szene Fernsehen | Reserve |
| 6 | Zentral Wohnzimmer | Reserve |

## Arbeitszimmer

- Licht Arbeitszimmer
- Rollladen Arbeitszimmer

## Schlafzimmer

- Licht Schlafzimmer
- Rollladen Schlafzimmer links
- Rollladen Schlafzimmer rechts

## Badezimmer

- Licht Badezimmer
- Rollladen Badezimmer

## Esszimmer

- Licht Esszimmer
- optional Szene Essen
- keine Beschattung geplant

## Küche

- Licht Küche
- optional Szene Küche
- keine Beschattung geplant

## Gang

Drei Glastaster im Gang:

- Ganglicht
- Zentral Aus
- Nachtmodus
- Anwesenheit / Abwesenheit
- optional alle Rollläden hoch/runter

## ETS-Hinweis

Die Kommunikationsobjekte der Taster werden direkt mit den vorhandenen Gruppenadressen verbunden:

Beispiel Wohnzimmer Rollladen links:

```text
Taster Objekt Auf/Ab  -> 2/0/0 Wohnzimmer Rollladen links Auf Ab
Taster Objekt Stop    -> 2/0/1 Wohnzimmer Rollladen links Stop
Taster Objekt Position -> 2/0/2 Wohnzimmer Rollladen links Position Soll
```

Dadurch bleiben Aktor, Taster und Visualisierung sauber synchron.
