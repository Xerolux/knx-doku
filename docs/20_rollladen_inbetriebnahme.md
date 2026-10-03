# 20 – Rollladen: ETS-Zuordnung, Inbetriebnahme und Prüfung

Stand: 03.10.2026

## Gerät und Grundprinzip

Verwendet wird ein MDT `JAL-0810M.02` Jalousieaktor mit acht Kanälen und automatischer Fahrzeitmessung für 230-V-Antriebe.

Je Rollladenmotor werden die beiden geschalteten Richtungsleiter an den Ausgang des zugehörigen Kanals angeschlossen. Neutralleiter und Schutzleiter werden nicht über die Richtungsrelais geschaltet. Die Anschlussbelegung und die gemeinsame Einspeisung der Kanalgruppen sind immer mit der MDT-Montageanleitung und der realen Verdrahtung abzugleichen. Arbeiten an 230 V dürfen nur durch eine Elektrofachkraft erfolgen.

## Einheitliche Namenskonvention

Die Rollladen-Gruppenadressen wurden in ETS eindeutig nach Raum und Bauform benannt. Die bisherigen Bezeichnungen `links` und `rechts` werden nicht mehr als Hauptbezeichnung verwendet.

```text
Wohnzimmer Rollladen Fenster
Wohnzimmer Rollladen Türe
Schlafzimmer Rollladen Fenster
Schlafzimmer Rollladen Türe
Arbeitszimmer Rollladen
Markise
```

Die Gruppenadressen selbst bleiben unverändert.

## Aktueller ETS-Kanalplan

| JAL-Kanal | ETS-Bezeichnung | Auf/Ab | Stopp | Position Status | Stand |
|---|---|---:|---:|---:|---|
| A | Schlafzimmer Rollladen Türe | `2/2/0` | `2/2/1` | `2/2/3` | Statusobjekt aktiviert; Verbindung prüfen |
| B | Schlafzimmer Rollladen Fenster | `2/2/10` | `2/2/11` | `2/2/13` | Statusobjekt aktiviert und verbunden |
| C | Arbeitszimmer Rollladen | `2/1/0` | `2/1/1` | `2/1/3` | Statusverknüpfung prüfen |
| D | Wohnzimmer Rollladen Fenster | `2/0/0` | `2/0/1` | `2/0/3` | Statusverknüpfung prüfen |
| E | Badezimmer Rollladen | `2/3/0` | `2/3/1` | `2/3/3` | ETS-Bezeichnung und Verknüpfungen am 03.10.2026 bestätigt; Download und Test offen |
| F | Küche | – | – | – | in ETS benannt, Gruppenadressen noch nicht verbunden |
| G | Markise | `2/4/0` | `2/4/1` | `2/4/3` | Statusverknüpfung prüfen |
| H | Wohnzimmer Rollladen Türe | `2/0/10` | `2/0/11` | `2/0/13` | Statusverknüpfung prüfen |

## Zentrale Gruppenadressen

| Objekt | Funktion | Gruppenadresse | Verwendung |
|---:|---|---:|---|
| 0 | Rollladen Auf/Ab | `0/1/0` | alle freigegebenen Rollladen auf oder ab fahren |
| 1 | Lamellenverstellung/Stopp | frei | nur für Jalousiekanäle mit Lamellen relevant |
| 2 | Stopp | `0/1/1` | zentraler Stopp für alle Kanäle |
| 3 | Absolute Position | vorerst frei | optional für spätere Zentralpositionen |
| 4 | Absolute Lamellenposition | frei | bei Rollläden nicht benötigt |

Für A, B, C, D, E und H ist **Zentrale Objekte = nur Auf/Ab** vorgesehen; G (Markise) bleibt **nicht aktiv**. Die Einstellung von E ist nach dem Screenshot vom 03.10.2026 noch zu prüfen und gegebenenfalls zu setzen. Das separate zentrale Objekt 2 dient als Stoppbefehl.

## Parameter je verwendetem Kanal

Für A, B, C, D, E, G und H sind folgende Parameter vorgesehen (Parameter von E noch zu bestätigen):

- Kanaltyp: `Rollladen`
- Automatische Fahrzeitmessung: `aktiv`
- Laufende Fahrzeitkorrektur: `aktiv`
- Relais ausschalten: `über Motorstrom`
- Fahrzeitverlängerung: `5 %`
- Status aktuelle Position: `aktiv`
- Status senden: `nach Fahrende`
- Zentrale Objekte: A, B, C, D, E und H `nur Auf/Ab`; G (Markise) `nicht aktiv`
- Verhalten bei Busspannungsausfall: `keine Aktion`
- Verhalten bei Busspannungswiederkehr: `keine Aktion`

## Positionsanzeige am MDT Glastaster

Der Glastaster erhält die Positionsrückmeldung des Aktors:

```text
JAL: Status aktuelle Position
    -> Status-Gruppenadresse
    -> Glastaster: Status der Jalousie für Anzeige
```

| Funktion | Statusadresse |
|---|---:|
| Schlafzimmer Rollladen Türe | `2/2/3` |
| Schlafzimmer Rollladen Fenster | `2/2/13` |
| Arbeitszimmer Rollladen | `2/1/3` |
| Wohnzimmer Rollladen Fenster | `2/0/3` |
| Wohnzimmer Rollladen Türe | `2/0/13` |
| Badezimmer Rollladen | `2/3/3` (ETS-Verknüpfung bestätigt) |
| Markise | `2/4/3` |

Am Glastaster wird `Jalousie/Rollladen` verwendet. Langdruck fährt, Kurzdruck stoppt. Bei KNX-Rollladenpositionen entspricht `0 %` der oberen und `100 %` der unteren Endlage.

## Vollständige Programmierung

Nach Änderungen an Parametern, Namen oder Kommunikationsobjekten werden vollständig programmiert:

1. JAL `1.1.4`
2. alle betroffenen MDT Glastaster
3. gegebenenfalls der zentrale Glastaster `1.1.20`

ETS kann nach reinen Namensänderungen ebenfalls **Programmieren notwendig** anzeigen. Entscheidend ist, dass alle Geräte mit geänderten Parametern oder Objektverknüpfungen ihr Applikationsprogramm erhalten.

## Automatische Fahrzeitmessung

Die Messung wird je verwendetem Kanal einzeln ausgeführt.

### Direkt am JAL

1. Kanal auswählen.
2. Auf- und Ab-Taste gleichzeitig gedrückt halten.
3. Messfahrt vollständig ablaufen lassen.
4. Während der Messung keine Bedienbefehle senden.

### Über ETS

Auf das jeweilige 1-Bit-Objekt **Fahrzeitmessung starten** eine `1` senden.

## Prüfung

1. Handbedienung am JAL: Auf, Ab und Stopp.
2. Glastaster: Langdruck fährt, Kurzdruck stoppt.
3. Obere Endlage zeigt ungefähr `0 %`.
4. Untere Endlage zeigt ungefähr `100 %`.
5. Zwischenpositionen werden nach Fahrtende plausibel angezeigt.
6. Zentral Auf/Ab über `0/1/0` erreicht alle freigegebenen Kanäle.
7. Zentral Stopp über `0/1/1` stoppt laufende Fahrten.
8. Im ETS-Gruppenmonitor sind Befehl und Positionsstatus sichtbar.

## Bad: Schalter verbinden und in „Alle Rollläden“ aufnehmen

### Belegter Stand vom 03.10.2026

Der erste Taster-Screenshot zeigte T3/4 `Rolladen Bad` noch ohne Gruppenadressverknüpfung. Der nachgereichte Screenshot bestätigt Objekt 10 Auf/Ab → `2/3/0`, Objekt 11 Stopp/Lamellen → `2/3/1` und Objekt 13 Positionsanzeige → `2/3/3`. Die physikalische Adresse des Bad-Tasters ist im Ausschnitt nicht sichtbar. Lichtobjekte 0 und 3 sind bereits mit `1/6/0` und `1/6/1` verbunden.

Der Aktor-Screenshot zeigt Kanal E `Bad`: Objekt 139 Auf/Ab, 141 Stopp, 146 Absolute Position, 148 Status aktuelle Position und 151 Fahrzeitmessung starten. Der erste Ausschnitt zeigte diese Objekte unverknüpft. Der nachgereichte Screenshot bestätigt Objekt 139 → `2/3/0`, Objekt 141 → `2/3/1` und Objekt 148 → `2/3/3`. Objekt 146 und 151 bleiben ohne Gruppenadresse; die optionale Sollposition ist damit nicht eingerichtet. Die Screenshots bestätigen weder die reale Verdrahtung noch Zentralparameter, Applikationsdownload oder Busfunktion.

### ETS-Anleitung

1. Projekt sichern. Den Bad-Taster anhand der Bezeichnung und der vorhandenen Lichtverknüpfung `1/6/0` identifizieren; seine physikalische Adresse prüfen.
2. Unter Gruppenadressen die bestehenden Badezimmer-Adressen prüfen. Sie sind bereits in den Repository-Importdateien enthalten; keine neuen Adressen erforderlich.
3. Folgende Objekte jeweils mit derselben Gruppenadresse verbinden:

| Gruppenadresse | Funktion / DPT | Bad-Taster | JAL `1.1.4`, Kanal E |
|---|---|---|---|
| `2/3/0` | Badezimmer Rollladen Auf Ab / 1.008 | 10 Jalousie Auf/Ab | 139 Rollladen Auf/Ab |
| `2/3/1` | Badezimmer Rollladen Stop / 1.010 | 11 Stop/Lamellen Auf/Zu | 141 Stopp |
| `2/3/3` | Badezimmer Rollladen Position Status / 5.001 | 13 Status der Jalousie für Anzeige | 148 Status aktuelle Position |
| `2/3/2` | Badezimmer Rollladen Position Soll / 5.001, optional | kein Objekt aus diesem Ausschnitt | 146 Absolute Position, nur bei gewünschter Prozentvorgabe |

4. T3/4 als Zwei-Tastenfunktion `Jalousie/Rollladen` belassen: Langdruck Auf/Ab, Kurzdruck Stopp; Anzeige in Prozent. Objekt 13 ist der empfangene Positionsstatus, keine Sollposition. Die vorhandenen Lichtverknüpfungen bleiben bestehen.
5. Am JAL Kanal E als `Rollladen` einstellen, Positionsstatus aktivieren und nach Fahrende senden. Fahrzeitmessung und weitere Kanalparameter gemäß diesem Dokument prüfen.
6. **Für „Alle“ am Kanal E `Zentrale Objekte = nur Auf/Ab` setzen.** Am JAL zentrale Verknüpfungen kontrollieren: Objekt 0 → `0/1/0`, Objekt 2 → `0/1/1`. Zentralobjekt 1 bleibt frei. Die Markise G bleibt von „Alle Rollläden“ ausgeschlossen.
7. Am zentralen Taster die vorhandenen Objekte 10 → `0/1/0` und 11 → `0/1/1` kontrollieren. Der Bad-Taster erhält ausschließlich die Bad-Adressen; keine Zentraladressen an seine Objekte 10/11 hängen, sonst würde er alle freigegebenen Rollläden bedienen. Die Einbindung erfolgt über die Kanalteilnahme am Aktor.
8. JAL und Bad-Taster über `Programmieren → Applikationsprogramm` laden. Den zentralen Taster nur bei Änderungen an seiner Applikation ebenfalls laden.
9. Bei noch fehlender Fahrzeitmessung Kanal E messen, zum Beispiel über Objekt 151 `Fahrzeitmessung starten`; während der Messfahrt keine Bedienbefehle senden.
10. Einzelbedienung prüfen: Langdruck fährt nur Bad, Kurzdruck stoppt nur Bad. Im Gruppenmonitor `2/3/0`, `2/3/1` und Rückmeldung `2/3/3` prüfen; oben etwa 0 %, unten etwa 100 %.
11. Zentralbedienung prüfen: „Alle“ Auf/Ab erreicht zusätzlich Bad, zentraler Stopp stoppt auch Bad; Markise bleibt unbewegt. Anschließend Einzelbedienung erneut prüfen und ETS-Projekt samt Export sichern.

**Status:** Einzelverknüpfungen am Bad-Taster (10/11/13) und am JAL Kanal E (139/141/148) sind durch die nachgereichten ETS-Screenshots vom 03.10.2026 bestätigt. Zentralteilnahme E, Status-Sendeparameter, Fahrzeitmessung, reale Motorzuordnung, Applikationsdownload und Einzel-/Zentralfunktionstest sind noch nicht bestätigt. Die Anleitung beschreibt die noch zu prüfenden Schritte; bereits bestätigte Verknüpfungen nur kontrollieren.

## Noch offene Punkte

- Kanal E Bad: bestätigte Verknüpfungen kontrollieren; Zentralteilnahme, Status-Sendeparameter, Fahrzeitmessung, reale Motorzuordnung, Download und Bustest bestätigen
- Funktion und Gruppenadressen von Kanal F `Küche` klären
- Statusverknüpfungen C, D, G und H kontrollieren
- Terrassenlicht am Glastaster `1.1.27` zuordnen
- nach erfolgreicher Prüfung ETS-Projekt und Gruppenadress-Export sichern

Dieses öffentliche Dokument enthält keine ETS-Projektdateien, Schlüsselbunddateien, Passwörter, PINs, Fotos oder Screenshots.

### Nachgereichter Zentralparameter-Ausschnitt

Der weitere Screenshot vom 03.10.2026 zeigt `Zentrale Objekte = nur Auf/Ab`, automatische Beschattung `nicht aktiv` und bei Busspannungsausfall sowie -wiederkehr jeweils `keine Aktion`. Geräte- und Kanalüberschrift fehlen im Ausschnitt. Falls er zu JAL Kanal E gehört, entspricht die Einstellung der vorgesehenen Zentralteilnahme des Bad-Rollladens; die Zuordnung zu E ist noch eindeutig zu bestätigen. Download und Funktionstest sind weiterhin nicht belegt.
