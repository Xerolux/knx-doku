# 18 – Gira KNX-Modul für Rauchwarnmelder

## Gerät

- **Gira 2343 00** KNX-Modul für Rauchwarnmelder Dual/VdS und Dual Q
- physikalische Adresse: **1.1.41**
- Medium: **KNX TP**
- Montage: direkt am dafür vorgesehenen Rauchwarnmelder

Das Modul bindet den zugehörigen Rauchwarnmelder an KNX an. Weitere über die Vernetzungsklemme gekoppelte Rauchwarnmelder sind keine eigenen KNX-Teilnehmer und erhalten keine eigene physikalische Adresse.

## Geplante Gruppenadressen

```text
10/0/0  Rauchalarm
10/0/1  Rauchwarnmelder Störung
10/0/2  Rauchwarnmelder Batterie schwach
10/0/3  Rauchwarnmelder Verschmutzung
10/0/4  Rauchwarnmelder Testalarm
```

Nach dem Einfügen der Produktdatenbank werden nur die Gruppenadressen mit tatsächlich vorhandenen und typgleichen Kommunikationsobjekten verbunden. Die Produktdatenbank und die technische Dokumentation des Geräts sind verbindlich.

## Sinnvolle Reaktionen bei Rauchalarm

- Fluchtwegbeleuchtung einschalten
- Rollläden und Jalousien hochfahren
- Meldung in Visualisierung und Home Assistant anzeigen
- Alarmstatus speichern beziehungsweise protokollieren

Entriegelungen von Türen oder andere sicherheitskritische Automatiken dürfen nur passend zur realen Türtechnik und zum Brandschutzkonzept umgesetzt werden. Die Rauchwarnfunktion selbst muss auch ohne KNX, Visualisierung oder Home Assistant erhalten bleiben.

## Inbetriebnahme

1. Gira-Produktdatenbank für Bestellnummer 2343 00 importieren.
2. Gerät auf Linie 1.1 einfügen und Adresse 1.1.41 vergeben.
3. Applikationsvariante passend zum vorhandenen Rauchwarnmelder auswählen.
4. Kommunikationsobjekte mit den vorhandenen Gruppenadressen 10/0/x verbinden.
5. Alarm, Störung und Testfunktion einzeln prüfen.
6. Ergebnis und Datum im Wartungsprotokoll dokumentieren.
