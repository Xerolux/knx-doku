# 07 – Beschattung und Wetter

Stand: 04.08.2026

## Geräte

- MDT `JAL-0810M.02` Jalousieaktor 8-fach mit Fahrzeitmessung
- Gira Wetterstation Pro / 5110 00
- MDT Logikmodul für spätere Verknüpfungen

## Aktuelle JAL-Kanäle

| Kanal | Funktion | Auf/Ab | Stopp | Position Status |
|---|---|---:|---:|---:|
| A | Schlafzimmer Tür / links | `2/2/0` | `2/2/1` | `2/2/3` |
| B | Schlafzimmer Fenster / rechts | `2/2/10` | `2/2/11` | `2/2/13` |
| C | Arbeitszimmer | `2/1/0` | `2/1/1` | `2/1/3` |
| D | Wohnzimmer Fenster / links | `2/0/0` | `2/0/1` | `2/0/3` |
| E | noch ungeklärt | – | – | – |
| F | Küche, noch ohne Zuordnung | – | – | – |
| G | Markise | `2/4/0` | `2/4/1` | `2/4/3` |
| H | Wohnzimmer Tür / rechts | `2/0/10` | `2/0/11` | `2/0/13` |

Die reale Motorzuordnung ist vor der Abnahme mit der Verdrahtung zu vergleichen. Die frühere Planung im Repository war nicht identisch mit der aktuellen ETS-Bezeichnung.

## Zentrale Rollladensteuerung

```text
JAL Objekt 0 Rollladen Auf/Ab -> 0/1/0 Alle Rollladen Auf / Ab
JAL Objekt 1 Lamellenverstellung/Stopp -> frei
JAL Objekt 2 Stopp -> 0/1/1 Alle Rollladen Stop / Schritt
```

Objekt 1 ist für Jalousien mit Lamellen vorgesehen. Für die vorhandenen Rollladenkanäle wird der zentrale Stopp über Objekt 2 ausgeführt.

Bei jedem verwendeten Kanal ist `Zentrale Objekte = nur Auf/Ab` eingestellt. Die Auswahl legt fest, dass der Kanal auf zentrale Auf- und Ab-Befehle reagiert. Der separate zentrale Stoppbefehl bleibt auf Objekt 2.

## Status und Prozentanzeige

Je verwendetem Kanal gilt:

```text
Status aktuelle Position = aktiv
Status senden = nach Fahrende
```

Das neu eingeblendete 1-Byte-Objekt `Status aktuelle Position` wird mit der jeweiligen Gruppenadresse `2/x/3` beziehungsweise `2/x/13` verbunden. Der Glastaster empfängt dieselbe Gruppenadresse über sein Objekt `Status der Jalousie für Anzeige`.

Damit gilt:

- obere Endlage: `0 %`
- untere Endlage: `100 %`
- Zwischenposition: nach Fahrtende als Prozentwert

## Fahrzeitmessung

Für A, B, C, D, G und H ist die automatische Fahrzeitmessung vorgesehen. Nach einem vollständigen Applikationsdownload des JAL wird die Messung je Kanal einzeln gestartet:

1. Kanal am Aktor auswählen.
2. Auf- und Ab-Taste gleichzeitig drücken und halten.
3. Automatische Messfahrt vollständig ablaufen lassen.

Alternativ wird auf das jeweilige Objekt `Fahrzeitmessung starten` eine `1` gesendet. Während der Messung dürfen keine weiteren Fahrbefehle gesendet werden.

Empfohlene Parameter:

```text
Automatische Fahrzeitmessung = aktiv
Laufende Fahrzeitkorrektur = aktiv
Relais ausschalten = über Motorstrom
Fahrzeitverlängerung = 5 %
Status aktuelle Position = aktiv
Status senden = nach Fahrende
```

Die vollständige Prüfanweisung steht in [20 – Rollladen: ETS-Zuordnung, Inbetriebnahme und Prüfung](20_rollladen_inbetriebnahme.md).

## Wetterwerte

```text
4/0/0 Außentemperatur
4/0/1 Windgeschwindigkeit
4/0/2 Regen
4/0/3 Dämmerung
4/1/0 Helligkeit Ost
4/1/1 Helligkeit Süd
4/1/2 Helligkeit West
```

## Schutz- und Automatikfunktionen

Geplant sind:

- Windschutz für die Markise
- Regenschutz für die Markise
- Frost-/Eisschutz nach dokumentierter Freigabe
- helligkeits- und sonnenstandsabhängige Beschattung als spätere Erweiterung
- Zentralbefehle für alle freigegebenen Rollläden
- Aussperrschutz für Terrassen- und Fenstertüren nach Einbindung der Fensterkontakte

Schutzfunktionen dürfen erst aktiviert werden, wenn Sensoradresse, Auslösewert, Priorität, Rücknahmebedingung und Verhalten je Kanal dokumentiert und geprüft sind.

## Grundsatz

Wetterschutz und grundlegende Beschattungsfunktionen laufen direkt auf KNX. Home Assistant darf visualisieren und Komfortfunktionen ergänzen, ist aber keine Voraussetzung für Schutz- oder Grundfunktionen.

## Herstellerunterlagen

- [MDT Jalousieaktor JAL – Produktseite](https://www.mdt.de/produkte/produktdetail/aktorik/jalousieaktoren/jalousieaktor-jal.html)
- [Technisches Handbuch JAL-0410M.02 / JAL-0810M.02](https://www.mdt.de/fileadmin/user_upload/MDT_THB_JAL_02_Jalousieaktor_Fahrzeitmessung_V11.pdf)
