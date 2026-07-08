# 07 – Beschattung und Wetter

## Geräte

- MDT JAL-0810M.02 Jalousieaktor 8-fach
- Gira Wetterstation Pro / 5110 00
- MDT Logikmodul für Verknüpfungen

## Kanäle

| Kanal | Funktion |
|---|---|
| A | Rollladen Wohnzimmer links |
| B | Rollladen Wohnzimmer rechts |
| C | Rollladen Arbeitszimmer |
| D | Rollladen Schlafzimmer links |
| E | Rollladen Schlafzimmer rechts |
| F | Rollladen Badezimmer |
| G | Markise |
| H | Reserve |

## Wetterwerte

```text
4/0/0 Außentemperatur
4/0/1 Windgeschwindigkeit
4/0/2 Regen
4/0/3 Helligkeit Ost
4/0/4 Helligkeit Süd
4/0/5 Helligkeit West
```

## Grundfunktionen

- Windschutz für Markise
- Regenschutz für Markise
- Helligkeitsabhängige Beschattung als spätere Erweiterung
- Zentralbefehle für alle Rollläden

## Empfehlung

Wetterschutz muss direkt in KNX laufen und darf nicht von Home Assistant abhängig sein.
