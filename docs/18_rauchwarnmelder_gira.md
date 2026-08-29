# 18 – Gira KNX-Modul für Rauchwarnmelder

## Gerät

- **Gira 2343 00** KNX-Modul für Rauchwarnmelder Dual/VdS und Dual Q
- vorgesehene physikalische Adresse: **1.1.41**
- Medium: **KNX TP**
- Montage: direkt am dafür vorgesehenen Rauchwarnmelder

Das Modul bindet den zugehörigen Rauchwarnmelder an KNX an. Weitere über die Vernetzungsklemme gekoppelte Rauchwarnmelder sind keine eigenen KNX-Teilnehmer und erhalten keine eigene physikalische Adresse. Aktuell ist noch kein reales Rauchwarnmelder-KNX-Gerät vorhanden oder in Betrieb genommen; `1.1.41` und die folgenden Gruppenadressen sind Planung.

## Geplante Gruppenadressen

```text
10/1/0  Rauchalarm                              DPT 1.002
10/1/1  Rauchwarnmelder Störung                 DPT 1.002
10/1/2  Rauchwarnmelder Batterie schwach        DPT 1.002
10/1/4  Rauchwarnmelder Testalarm auslösen      DPT 1.003
10/1/5  Rauchwarnmelder Testalarm Status        DPT 1.002
10/1/6  Rauchwarnmelder Störung Rauchkammer     DPT 1.002
```

Eine eigene Meldung nur für „Verschmutzung“ existiert in der Gira-Applikation nicht. Laut Produktdokumentation aktiviert Verschmutzung die allgemeine Störung an Objekt 12. Objekt 16 meldet allgemeiner eine Rauchkammerstörung; deshalb heißt `10/1/6` korrekt **Störung Rauchkammer** und nicht „Verschmutzung“. Untergruppe `10/1/3` bleibt frei. Der Bereich `10/0` darf nicht verwendet werden, weil er dem vorhandenen MDT SCN-SAFE gehört.

| Objekt | Name in der Gira-Applikation | Gruppenadresse |
|---:|---|---:|
| 0 | Alarm beziehungsweise Lokaler Alarm | `10/1/0` |
| 7 | Testalarm | `10/1/4` |
| 8 | Status Testalarm | `10/1/5` |
| 12 | Störung | `10/1/1` |
| 14 | Störung Batterie | `10/1/2` |
| 16 | Störung Rauchkammer | `10/1/6` |

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
4. Kommunikationsobjekte mit den geplanten Gruppenadressen `10/1/x` verbinden.
5. Alarm, allgemeine Störung, Batterie- und Rauchkammerstörung einzeln prüfen.
6. Testalarm über `10/1/4` auslösen und die Rückmeldung auf `10/1/5` prüfen.
7. Ergebnis und Datum im Wartungsprotokoll dokumentieren.
