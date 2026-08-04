# 20 – Rollladen: ETS-Zuordnung, Inbetriebnahme und Prüfung

Stand: 04.08.2026

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
| E | noch ungeklärt | – | – | – | reale Belegung feststellen |
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

Bei jedem verwendeten Rollladenkanal ist **Zentrale Objekte = nur Auf/Ab** eingestellt. Das separate zentrale Objekt 2 dient als Stoppbefehl.

## Parameter je verwendetem Kanal

Für A, B, C, D, G und H gilt:

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

## Noch offene Punkte

- reale Belegung von Kanal E feststellen
- Funktion und Gruppenadressen von Kanal F `Küche` klären
- Statusverknüpfungen C, D, G und H kontrollieren
- Terrassenlicht am Glastaster `1.1.27` zuordnen
- nach erfolgreicher Prüfung ETS-Projekt und Gruppenadress-Export sichern

Dieses öffentliche Dokument enthält keine ETS-Projektdateien, Schlüsselbunddateien, Passwörter, PINs, Fotos oder Screenshots.
