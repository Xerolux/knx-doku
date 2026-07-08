# 09 – Home Assistant

## Rolle von Home Assistant

Home Assistant ergänzt KNX, ersetzt aber nicht die Grundfunktionen.

KNX übernimmt:

- Licht schalten
- Rollläden fahren
- Heizung regeln
- Fensterstatus auswerten
- Wetterwerte für Beschattung verwenden

Home Assistant übernimmt:

- Visualisierung
- Benachrichtigungen
- Statistik
- Energieauswertung
- Komfortlogiken
- Fernzugriff

## Verbindung

```text
Home Assistant
↕ LAN
MDT SCN-IP100.03
↕ KNX TP
KNX Linie 1.1
```

## Empfehlung

In Home Assistant nur Gruppenadressen einbinden, die wirklich gebraucht werden. Die ETS bleibt die Hauptdokumentation.
