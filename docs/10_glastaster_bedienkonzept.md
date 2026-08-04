# 10 – MDT Glastaster Smart II Bedienkonzept

Stand: 04.08.2026

## Aktueller Gerätebestand

Im ETS-Projekt sind MDT Glastaster II Smart mit Temperatursensor unter `1.1.20` bis `1.1.29` angelegt. Die Geräte `1.1.20` bis `1.1.28` sind grundsätzlich vorhanden; der vollständige Programmierstand von `1.1.29` muss weiterhin geprüft werden.

Die konkrete physikalische Adresse aller raumbezogenen Taster ist noch nicht abschließend in der Dokumentation zugeordnet. Deshalb werden nachfolgend nur sichere Zuordnungen und die in ETS sichtbaren Funktionsbelegungen festgehalten.

## Taster 1.1.20 – Eingang/Gang und Zentralfunktionen

### Tasten 1/2 – Alle Lichter

Zwei-Tastenfunktion `Schalten`:

| Taste | Sendewert |
|---|---:|
| links | Ein / `1` |
| rechts | Aus / `0` |

```text
Objekt 0 T1/2: Alle Lichter – Schalten Ein/Aus
    -> 0/4/0 Alle Lichter schalten
```

Das Statusobjekt bleibt frei, solange keine Logik einen eindeutigen Sammelstatus erzeugt.

### Tasten 3/4 – Alle Rollladen

Zwei-Tastenfunktion `Jalousie/Rollladen`:

```text
Objekt 10 T3/4: Alle Rollladen – Jalousie Auf/Ab
    -> 0/1/0 Alle Rollladen Auf / Ab

Objekt 11 T3/4: Alle Rollladen – Stop/Lamellen Auf/Zu
    -> 0/1/1 Alle Rollladen Stop / Schritt
```

Ein gemeinsamer Prozentstatus für mehrere unabhängig stehende Rollladen ist nicht eindeutig. Das 1-Byte-Statusobjekt der Zentralfunktion bleibt deshalb zunächst frei.

## Raumbezogene Lichtfunktionen

In ETS sind folgende Schalt- und Statusadressen an den Glastastern sichtbar:

| Raum | Schalten | Status |
|---|---:|---:|
| Wohnzimmer | `1/0/0` | `1/0/1` |
| Küche | `1/2/0` | `1/2/1` |
| Arbeitszimmer | `1/3/0` | `1/3/1` |
| Gang | `1/4/0` | `1/4/1` |
| Schlafzimmer | `1/5/0` | `1/5/1` |

Diese Tasterverknüpfungen allein schalten noch keinen Ausgang. Die zugehörigen Schalt- und Statusobjekte des Schaltaktors müssen nach Prüfung der realen Kanalverdrahtung ebenfalls mit denselben Gruppenadressen verbunden werden.

## Raumbezogene Rollladenfunktionen

### Arbeitszimmer

```text
T3/4 Auf/Ab  -> 2/1/0
T3/4 Stopp   -> 2/1/1
T3/4 Status  -> 2/1/3
```

### Schlafzimmer

```text
T3/4 Rollladen Tür / links:
  Auf/Ab -> 2/2/0
  Stopp  -> 2/2/1
  Status -> 2/2/3

T5/6 Rollladen Fenster / rechts:
  Auf/Ab -> 2/2/10
  Stopp  -> 2/2/11
  Status -> 2/2/13
```

### Terrasse – Taster 1.1.27

```text
T1/2 Terrassenlicht:
  Gruppenadresse noch offen

T3/4 Wohnzimmer Rollladen Fenster / links:
  Auf/Ab -> 2/0/0
  Stopp  -> 2/0/1
  Status -> 2/0/3

T5/6 Wohnzimmer Rollladen Tür / rechts:
  Auf/Ab -> 2/0/10
  Stopp  -> 2/0/11
  Status -> 2/0/13

T7/8 Markise:
  Auf/Ab -> 2/4/0
  Stopp  -> 2/4/1
  Status -> 2/4/3
```

## Anzeige und Beschriftung der Rollladen

Die Gruppenadressennamen werden nicht automatisch als Text auf dem Display dargestellt. Die sichtbare Beschriftung wird in den Parametern des jeweiligen Tastenpaares festgelegt.

Empfohlene Einstellung:

```text
Zwei-Tastenfunktion: Jalousie/Rollladen
Bedienfunktion: Lang = Auf/Ab / Kurz = Stopp/Lamellen Auf/Zu
Funktionsname: über Texteingabe
Text: z. B. Rollladen Tür, Rollladen Fenster oder Markise
Tastenbeschriftung: Pfeil Ab / Pfeil Auf passend zur Tastenbelegung
Statuswert als Text unter Symbol: anzeigen in Prozent
```

Die Schreibweise wird einheitlich als **Rollladen** verwendet.

Für das dynamische Symbol können getrennte Symbole für folgende Bereiche verwendet werden:

- oben: kleiner als `10 %`
- Mitte: `10–90 %`
- unten: größer als `90 %`

Die Prozentanzeige funktioniert nur, wenn das Statusobjekt des Glastasters mit dem 1-Byte-Objekt `Status aktuelle Position` des passenden JAL-Kanals über dieselbe Gruppenadresse verbunden ist.

Bei Rollladenpositionen gilt:

```text
0 %   = vollständig oben
100 % = vollständig unten
```

## Zeit und Datum

Für die Anzeige wird der kombinierte Datum-/Uhrzeitwert verwendet:

```text
0/5/2 Datum/Uhrzeit
    -> Objekt 114 Uhrzeit/Datum – aktuelle Werte empfangen
```

Das separate Objekt 112 `Uhrzeit – aktuellen Wert empfangen` kann frei bleiben, wenn der kombinierte 8-Byte-Wert genutzt wird.

## Temperatur

Der Glastaster besitzt einen internen Temperatursensor. In ETS muss die Temperaturmessung aktiviert sein. Soll der Messwert auf dem Bus verfügbar sein, wird Objekt 108 `Temperaturmesswert – Ausgang` mit der Isttemperaturadresse des jeweiligen Raums verbunden.

Für den Eingang/Gang ist vorgesehen:

```text
Temperaturmesswert -> 3/4/1 Gang Isttemperatur
```

Die endgültige Verbindung erfolgt erst nach bestätigter Raumzuordnung des jeweiligen Tasters.

## Display-Standby

Empfohlenes Verhalten:

- Display nach einer festgelegten Zeit in Standby versetzen
- Standbyanzeige dunkel oder Display aus
- festlegen, ob der erste Tastendruck nur aufweckt oder gleichzeitig die Funktion ausführt

Die gewählte Bedienlogik muss bei allen Tastern möglichst einheitlich sein.

## Programmierung und Prüfung

Nach Änderungen an Beschriftung, Tastenfunktion oder Kommunikationsobjekten wird der betroffene Glastaster über **Programmieren → Applikationsprogramm** vollständig geladen.

Danach je Tastenpaar prüfen:

1. langer Tastendruck fährt in die richtige Richtung
2. kurzer Tastendruck stoppt die laufende Fahrt
3. Funktionsname und Pfeilsymbole stimmen
4. Positionswert wird nach Fahrtende aktualisiert
5. obere Endlage zeigt ungefähr `0 %`
6. untere Endlage zeigt ungefähr `100 %`

Die vollständige Inbetriebnahmeanweisung steht in [20 – Rollladen: ETS-Zuordnung, Inbetriebnahme und Prüfung](20_rollladen_inbetriebnahme.md).
