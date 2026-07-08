# 06 – Heizung und Fenster

## Räume mit Fußbodenheizung

- Wohnzimmer
- Esszimmer
- Küche
- Arbeitszimmer
- Gang
- Schlafzimmer
- Badezimmer
- Bad vorne

## Fenstergriffe KNX RF

| Raum | Anzahl |
|---|---:|
| Wohnzimmer | 3 |
| Küche | 2 |
| Bad vorne | 1 |
| Arbeitszimmer | 2 |
| Schlafzimmer | 2 |
| Badezimmer | 2 |

## Grundlogik

Fensterstatus wird je Raum zusammengeführt.

```text
Fenster im Raum geschlossen → Heizung normal
Fenster im Raum offen/gekippt → Heizung abgesenkt
```

## Gruppenadressen je Raum

```text
3/x/0 Solltemperatur
3/x/1 Isttemperatur
3/x/2 Betriebsmodus
3/x/3 Ventilstellung
3/x/4 Fensterstatus Raum
```

## Empfehlung

Die Heizungslogik sollte direkt in KNX laufen. Home Assistant darf den Status anzeigen, sollte aber nicht die Grundfunktion ersetzen.
