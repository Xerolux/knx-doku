# 26 – SCN-SAFE-Adressreparatur

Stand: 29.08.2026

## Ergebnis

Der Sicherheitsbereich ist wieder eindeutig getrennt:

- `10/0`: MDT SCN-SAFE.01, physikalische Adresse `1.1.9`
- `10/1`: Planung für einen späteren Gira KNX-Rauchwarnmelder

Für den Rauchwarnmelder ist noch kein reales oder in Betrieb genommenes KNX-Gerät bestätigt. Der ETS-Eintrag `1.1.41` und seine Gruppenadressen sind daher Planung.

## Vorfall und Ursache

Eine frühere Rauchwarnmelder-Importdatei belegte irrtümlich die bereits vom SCN-SAFE verwendeten Adressen `10/0/0` bis `10/0/6`. Beim Import übernahm ETS die neuen Namen für die vorhandenen numerischen Gruppenadressen. Dadurch wurden an den Kommunikationsobjekten des SCN-SAFE Rauchwarnmelder-Namen angezeigt, obwohl die numerischen Objektverknüpfungen weiterhin auf `10/0/x` lagen.

Das war eine Kollision in der Importdatei und keine Folge von KNX Secure. Ein ETS-Gruppenadressimport programmiert kein Gerät, kann aber Namen und DPT-Zuordnungen bestehender Gruppenadressen verändern.

## Wiederhergestellte SCN-SAFE-Zuordnung

Die DPTs wurden gegen die offizielle MDT-Produktdatenbank der Applikation `SCN-SAFE.01` abgeglichen.

| Gruppenadresse | Name | DPT | SCN-SAFE-Objekt | Stand in ETS |
|---:|---|---:|---:|---|
| `10/0/0` | Sicherheitsmodus Status | 1.011 | 230 | verbunden; Antwort von `1.1.9` im Gruppenmonitor bestätigt |
| `10/0/1` | Sicherheitsmodus Alarm | 1.005 | 231 | verbunden |
| `10/0/2` | Sicherheitsmodul In Betrieb | 1.011 | 0 | verbunden |
| `10/0/3` | Sicherheitsmodus Befehl Passwort | 16.000 | 229 | verbunden, 14 Byte |
| `10/0/4` | Sicherheitsmodus Alarm quittieren | 1.001 | 228 | verbunden |
| `10/0/5` | Sicherheitsmodus Aktivieren | 1.001 | 227 | Gruppenadresse wiederhergestellt; Objektverknüpfung noch prüfen |

Das Passwort selbst wird weder dokumentiert noch in das Repository aufgenommen.

Der Gruppenmonitor zeigte eine Leseanfrage auf `10/0/0` und die Antwort des SCN-SAFE unter `1.1.9`. Der gelesene Status war zu diesem Zeitpunkt aktiv. Dieser Bus-Test bestätigt nur Statusadresse und Antwortverhalten; er ersetzt keine vollständige Funktionsprüfung aller Objekte.

## Rauchwarnmelder-Planung

Die noch nicht aktive Rauchwarnmelder-Planung wurde auf `10/1` verschoben:

| Gruppenadresse | Name | DPT |
|---:|---|---:|
| `10/1/0` | Rauchalarm | 1.002 |
| `10/1/1` | Rauchwarnmelder Störung | 1.002 |
| `10/1/2` | Rauchwarnmelder Batterie schwach | 1.002 |
| `10/1/4` | Rauchwarnmelder Testalarm auslösen | 1.003 |
| `10/1/5` | Rauchwarnmelder Testalarm Status | 1.002 |
| `10/1/6` | Rauchwarnmelder Störung Rauchkammer | 1.002 |

Vor der späteren Inbetriebnahme müssen Produktvariante, Kommunikationsobjekte, DPTs und physikalische Adresse erneut gegen das dann tatsächlich vorhandene Gerät geprüft werden.

## Reparaturdatei und ETS-Nacharbeit

[gruppenadressen-reparatur-safe-rauchwarnmelder.xml](../ets-import/gruppenadressen-reparatur-safe-rauchwarnmelder.xml) ist ausschließlich für die einmalige Reparatur des betroffenen ETS-Projekts vorgesehen. Sie stellt die richtigen Namen und DPTs auf `10/0` wieder her und legt die Rauchwarnmelder-Planung unter `10/1` an.

ETS-Imports sind additiv. Deshalb gilt nach dem Import:

1. Unter `10/0` prüfen, dass keine Gruppe mehr einen Rauchwarnmelder-Namen trägt.
2. Der Zwischenstand zeigte noch `10/0/5 Rauchwarnmelder Testalarm Status` und `10/0/6 Rauchwarnmelder Störung Rauchkammer`. Die Reparaturdatei weist `10/0/5` wieder dem Sicherheitsmodus Aktivieren zu; `10/0/6` gehört nicht mehr zum kanonischen Stand.
3. Vor dem Umbenennen oder Löschen dieser beiden Altgruppen in ETS prüfen, dass keine Rauchwarnmelder-Kommunikationsobjekte mehr mit ihnen verbunden sind. `10/0/6` erst bei leerer Spalte **Verbunden mit** löschen.
4. `10/0/5 Sicherheitsmodus Aktivieren` mit Objekt 227 verbinden, sofern die Fernaktivierung gemäß Parametrierung gewünscht ist.
5. Keine Rauchwarnmelder-Kommunikationsobjekte verbinden, solange kein reales Gerät vorhanden ist.
6. Geänderte Verknüpfungen nur an tatsächlich betroffene Geräte laden.
7. Status, Alarm, Quittierung und Aktivierung im Gruppenmonitor einzeln prüfen; Passwortwerte nicht protokollieren.
8. Danach einen aktuellen Gruppenadress- und Objektverknüpfungsexport aus ETS erstellen.

## Schutz gegen Wiederholung

Vor einem Git-Commit oder ETS-Import wird ausgeführt:

```powershell
powershell -NoProfile -File scripts/validate-group-addresses.ps1
```

Die Prüfung kontrolliert:

- gültiges XML und eindeutige Adressen innerhalb jeder Importdatei
- identische Namen und DPTs bei absichtlichen Überschneidungen modularer Dateien
- fest definierte SCN-SAFE-Zuordnung unter `10/0`
- ausschließlich Rauchwarnmelder-Namen unter `10/1`
- erwartete Anzahl der Basis- und Wärmepumpen-Adressen

Eine Importdatei wird erst verwendet, wenn diese Prüfung erfolgreich ist und der ETS-Importbericht keine unerwartete Änderung bestehender Adressen zeigt.

Bei Änderungen unter `ets-import/` führt GitHub Actions dieselbe Prüfung automatisch aus. Damit kann eine bekannte Sicherheitsadresskollision nicht unbemerkt in den dokumentierten Importstand gelangen.

## Herstellerquellen

- [MDT SCN-SAFE.01 – Technisches Handbuch, Version 1.1](https://www.mdt.de/fileadmin/user_upload/SCN-SAFE-01_MDT_TM_V11_DE.pdf)
- [MDT Sicherheitsmodul – Produktseite und Produktdatenbank](https://www.mdt.de/produkte/produktdetail/systemkomponenten/systemgeraete/sicherheitsmodul.html)
