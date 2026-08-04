# 20 – Rollladen: ETS-Zuordnung, Inbetriebnahme und Prüfung

Stand: 04.08.2026

## Gerät und Grundprinzip

Verwendet wird ein MDT `JAL-0810M.02` Jalousieaktor mit acht Kanälen und automatischer Fahrzeitmessung für 230-V-Antriebe.

Je Rollladenmotor werden die beiden geschalteten Richtungsleiter an den Ausgang des zugehörigen Kanals angeschlossen. Neutralleiter und Schutzleiter werden nicht über die Richtungsrelais geschaltet. Die Anschlussbelegung und die gemeinsame Einspeisung der Kanalgruppen sind immer mit der MDT-Montageanleitung und der realen Verdrahtung abzugleichen. Arbeiten an 230 V dürfen nur durch eine Elektrofachkraft erfolgen.

MDT weist darauf hin, dass je zwei L-Anschlüsse des Aktors intern gebrückt sind. Das ersetzt nicht die Prüfung der tatsächlichen Einspeisung, Absicherung und Leiterzuordnung.

## Aktueller ETS-Kanalplan

| JAL-Kanal | ETS-Bezeichnung | Auf/Ab | Stopp | Position Status | Stand |
|---|---|---:|---:|---:|---|
| A | Schlafzimmer Tür / links | `2/2/0` | `2/2/1` | `2/2/3` | Statusobjekt aktiviert; Verknüpfung in ETS prüfen |
| B | Schlafzimmer Fenster / rechts | `2/2/10` | `2/2/11` | `2/2/13` | Statusobjekt aktiviert und verbunden |
| C | Arbeitszimmer | `2/1/0` | `2/1/1` | `2/1/3` | Statusverknüpfung prüfen |
| D | Wohnzimmer Fenster / links | `2/0/0` | `2/0/1` | `2/0/3` | Statusverknüpfung prüfen |
| E | noch ungeklärt | – | – | – | reale Belegung feststellen |
| F | Küche | – | – | – | in ETS benannt, Gruppenadressen noch nicht verbunden |
| G | Markise | `2/4/0` | `2/4/1` | `2/4/3` | Statusverknüpfung prüfen |
| H | Wohnzimmer Tür / rechts | `2/0/10` | `2/0/11` | `2/0/13` | Statusverknüpfung prüfen |

Die frühere Kanalbelegung in der Planung war nicht identisch mit dem aktuellen ETS-Stand. Für die Abnahme ist die Tabelle gegen die reale Motorverdrahtung zu prüfen.

## Zentrale Gruppenadressen

Die zentralen Kommunikationsobjekte des JAL sind wie folgt zu verbinden:

| Objekt | Funktion | Gruppenadresse | Verwendung |
|---:|---|---:|---|
| 0 | Rollladen Auf/Ab | `0/1/0` | alle freigegebenen Rollladen auf oder ab fahren |
| 1 | Lamellenverstellung/Stopp | frei | nur für Jalousiekanäle mit Lamellen relevant |
| 2 | Stopp | `0/1/1` | zentraler Stopp für alle Kanäle |
| 3 | Absolute Position | vorerst frei | optional für spätere Zentralpositionen |
| 4 | Absolute Lamellenposition | frei | bei Rollläden nicht benötigt |

Bei jedem verwendeten Rollladenkanal ist der Parameter **Zentrale Objekte** auf **nur Auf/Ab** eingestellt. Dadurch nimmt der Kanal an zentralen Auf-/Ab-Befehlen teil. Das separate zentrale Objekt 2 dient als Stoppbefehl für alle Kanäle.

## Parameter je verwendeten Kanal

Für A, B, C, D, G und H gilt als Sollzustand:

- Kanaltyp: `Rollladen`
- Automatische Fahrzeitmessung: `aktiv`
- Laufende Fahrzeitkorrektur: `aktiv`
- Relais ausschalten: `über Motorstrom`
- Fahrzeitverlängerung: `5 %`
- Status aktuelle Position: `aktiv`
- Status senden: `nach Fahrende`
- Zentrale Objekte: `nur Auf/Ab`
- Verhalten bei Busspannungsausfall: `keine Aktion`
- Verhalten bei Busspannungswiederkehr: `keine Aktion`

Nicht benötigte Automatik-, Beschattungs-, Szenen-, Lüftungs-, Sperr- und Alarmfunktionen bleiben zunächst deaktiviert. Schutzfunktionen werden später bewusst und mit dokumentierten Gruppenadressen aktiviert.

## Positionsanzeige am MDT Glastaster

Der Glastaster erhält nicht die Sollposition, sondern die Positionsrückmeldung des Aktors:

```text
JAL: Status aktuelle Position
    -> Gruppenadresse 2/x/3 beziehungsweise 2/x/13
    -> Glastaster: Status der Jalousie für Anzeige
```

Beispiele:

```text
Schlafzimmer links:  2/2/3
Schlafzimmer rechts: 2/2/13
Arbeitszimmer:        2/1/3
Wohnzimmer links:     2/0/3
Wohnzimmer rechts:    2/0/13
Markise:              2/4/3
```

Am Glastaster wird die Zwei-Tastenfunktion `Jalousie/Rollladen` verwendet:

- Bedienfunktion: `Lang = Auf/Ab, Kurz = Stopp`
- Funktionsname: über Texteingabe, zum Beispiel `Rollladen Tür`
- linke/rechte Tastenbeschriftung: Pfeil Ab / Pfeil Auf entsprechend der gewählten Tastenbelegung
- Statuswert unter Symbol: `anzeigen in Prozent`

Bei KNX-Rollladenpositionen entspricht `0 %` der oberen und `100 %` der unteren Endlage.

## Vollständige Programmierung

Nach Änderungen an Parametern oder Kommunikationsobjekten:

1. JAL in ETS auswählen.
2. **Programmieren → Applikationsprogramm** vollständig laden.
3. Alle betroffenen Glastaster ebenfalls vollständig programmieren.
4. Prüfen, ob das MDT-Sicherheitsmodul den ETS-Zugriff freigibt, falls ETS `Verbindung verweigert` meldet.

Eine reine partielle Änderung kann bei umfangreichen Parameteränderungen alte Objekt- oder Parameterstände zurücklassen. Für die Inbetriebnahme wird deshalb ein vollständiger Applikationsdownload verwendet.

## Automatische Fahrzeitmessung starten

Die Messung wird für jeden verwendeten Kanal einzeln durchgeführt.

### Direkt am JAL

1. Mit den Kanalauswahltasten den gewünschten Kanal wählen.
2. Die Tasten **Auf** und **Ab** gleichzeitig drücken und halten.
3. Die automatische Messfahrt vollständig ablaufen lassen.
4. Während der Messung keine Bedienbefehle senden und den Fahrweg freihalten.

### Über ETS

Auf das jeweilige 1-Bit-Kommunikationsobjekt **Fahrzeitmessung starten** eine `1` senden. Die Messung ermittelt automatisch die Zeiten für Auf- und Abfahrt. Das Diagnoseobjekt kann die einzelnen Schritte und die ermittelten Zeiten ausgeben.

## Prüfung nach der Messung

Für jeden verwendeten Kanal wird einzeln geprüft:

1. Handbedienung am JAL: Auf, Ab und Stopp.
2. Glastaster: langer Tastendruck fährt, kurzer Tastendruck stoppt.
3. Obere Endlage zeigt ungefähr `0 %`.
4. Untere Endlage zeigt ungefähr `100 %`.
5. Zwischenpositionen werden nach Fahrtende plausibel angezeigt.
6. Zentral Auf/Ab über `0/1/0` erreicht alle freigegebenen Kanäle.
7. Zentral Stopp über `0/1/1` stoppt laufende Fahrten.
8. Im ETS-Gruppenmonitor sind Befehl und Positionsstatus sichtbar.

## Fehlersuche

### Motor fährt über Handbedienung, aber nicht über Glastaster

- Auf/Ab-Objekt von Taster und JAL muss dieselbe Gruppenadresse besitzen.
- Stopp-Objekt von Taster und JAL muss dieselbe Gruppenadresse besitzen.
- JAL und Glastaster vollständig programmieren.
- Telegramme im Gruppenmonitor kontrollieren.
- Aktive Sperren, Alarme oder Fensterfunktionen prüfen.

### Prozentanzeige bleibt leer oder falsch

- `Status aktuelle Position` am JAL aktivieren.
- Das 1-Byte-Statusobjekt mit der richtigen Statusadresse verbinden.
- Dasselbe Statusobjekt am Glastaster mit dieser Adresse verbinden.
- Fahrzeitmessung ausführen.
- JAL und Glastaster vollständig programmieren.

### Motor fährt auch über Handbedienung nicht

- 230-V-Hilfsspannung des Aktors prüfen.
- Einspeisung und Ausgangsverdrahtung prüfen.
- Neutralleiter und Schutzleiter des Motors prüfen.
- Motorschutz beziehungsweise Endabschaltung prüfen.
- Aktive Handbedienungssperre kontrollieren.

## Noch offene Punkte

- reale Belegung von Kanal E feststellen
- Funktion und Gruppenadressen von Kanal F `Küche` klären
- Statusverknüpfungen C, D, G und H nach vollständiger Programmierung kontrollieren
- Terrassenlicht am Glastaster `1.1.27` mit einer passenden Licht-Gruppenadresse verbinden
- Einzelkanäle des Schaltaktors mit den vorhandenen Licht-Gruppenadressen verbinden
- nach erfolgreicher Prüfung ETS-Projekt, Gruppenadress-Export und Dokumentation sichern

## Herstellerunterlagen

- [MDT Jalousieaktor JAL – Produktseite](https://www.mdt.de/produkte/produktdetail/aktorik/jalousieaktoren/jalousieaktor-jal.html)
- [Technisches Handbuch JAL-0410M.02 / JAL-0810M.02](https://www.mdt.de/fileadmin/user_upload/MDT_THB_JAL_02_Jalousieaktor_Fahrzeitmessung_V11.pdf)

Dieses öffentliche Dokument enthält keine ETS-Projektdateien, Schlüsselbunddateien, Passwörter, PINs oder Screenshots.
