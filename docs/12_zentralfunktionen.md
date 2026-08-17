# 12 – Zentralfunktionen

Stand: 04.08.2026

## Zentral Licht – aktueller Stand

Die zentrale Lichtsteuerung verwendet eine gemeinsame 1-Bit-Gruppenadresse für Ein und Aus:

| Gruppenadresse | Funktion | DPT | Wert |
|---:|---|---|---|
| `0/4/0` | Alle Lichter schalten | 1.001 | `1` = Ein, `0` = Aus |

### Taster 1.1.20

Die Tasten 1/2 sind als Zwei-Tastenfunktion **Schalten** mit der Belegung **Ein / Aus** parametriert.

```text
1.1.20 Objekt 0 T1/2: Alle Lichter – Schalten Ein/Aus
    -> 0/4/0 Alle Lichter schalten
```

### Schaltaktor 1.1.3

```text
0/4/0 Alle Lichter schalten
    -> 1.1.3 Objekt 289 Zentralfunktion – Schalten EIN/AUS
```

Bei jedem Aktorkanal, der ein Licht schaltet, muss die Teilnahme an der Zentralfunktion aktiviert werden. Steckdosen, technische Verbraucher und Reservekanäle dürfen nicht teilnehmen.

Die einzelnen Lichtkanäle des Schaltaktors sind noch nicht vollständig mit den raumbezogenen Schalt- und Statusadressen verbunden. Die Zuordnung erfolgt erst nach Prüfung der realen Ausgangsverdrahtung.

Objekt 291 **Zentralfunktion – In Betrieb** bleibt ohne konkreten Diagnosezweck zunächst unverknüpft.

### Statusanzeige

Das Statusobjekt des zentralen Tastenpaares wird nicht direkt mit einem einzelnen Lichtstatus verbunden. Bei mehreren Lichtkreisen wäre ein einzelner Status nicht eindeutig. Eine spätere Logik kann beispielsweise `mindestens ein Licht ist an` oder `alle Lichter sind aus` bilden.

## Zentral Rollladen – aktueller Stand

| Gruppenadresse | Funktion | DPT | Zweck |
|---:|---|---|---|
| `0/1/0` | Alle Rollladen Auf / Ab | 1.008 | gemeinsamer Fahrbefehl |
| `0/1/1` | Alle Rollladen Stop / Schritt | 1.007 | laufende Fahrten stoppen |

### Taster 1.1.20

Die Tasten 3/4 sind als Zwei-Tastenfunktion **Jalousie/Rollladen** parametriert:

```text
1.1.20 Objekt 10 T3/4: Alle Rollladen – Jalousie Auf/Ab
    -> 0/1/0 Alle Rollladen Auf / Ab

1.1.20 Objekt 11 T3/4: Alle Rollladen – Stop/Lamellen Auf/Zu
    -> 0/1/1 Alle Rollladen Stop / Schritt
```

Der gemeinsame 1-Byte-Status des Tastenpaares bleibt frei, da mehrere Rollladen unterschiedliche Positionen besitzen können.

### MDT JAL-0810M.02

Die zentrale Objektzuordnung am Jalousieaktor lautet:

```text
JAL Objekt 0 Rollladen Auf/Ab
    -> 0/1/0 Alle Rollladen Auf / Ab

JAL Objekt 1 Lamellenverstellung/Stopp
    -> frei

JAL Objekt 2 Stopp
    -> 0/1/1 Alle Rollladen Stop / Schritt
```

Objekt 1 wird nur für Jalousiekanäle mit Lamellen benötigt. Der vorhandene Aufbau verwendet Rollladenkanäle; der zentrale Stopp wird deshalb über Objekt 2 ausgeführt.

Bei A, B, C, D, G und H ist der Kanalparameter **Zentrale Objekte** auf **nur Auf/Ab** zu stellen. Kanal E und F werden erst nach Klärung der tatsächlichen Funktion freigegeben.

### Test

1. JAL und Taster `1.1.20` vollständig programmieren.
2. Im Gruppenmonitor prüfen, dass `0` auf `0/1/0` einen Auf-Befehl und `1` einen Ab-Befehl darstellt.
3. Während einer Fahrt `0/1/1` betätigen und kontrollieren, dass die Fahrt stoppt.
4. Prüfen, dass nur freigegebene Kanäle auf den Zentralbefehl reagieren.
5. Anschließend die Einzelbedienung aller Rollladen erneut testen.

Weitere Details stehen in [20 – Rollladen: ETS-Zuordnung, Inbetriebnahme und Prüfung](20_rollladen_inbetriebnahme.md).

## Abgrenzung zu 0/0/0

Die ältere Planungsadresse `0/0/0 Zentral Aus` beschreibt nur einen einseitigen Ausschaltbefehl. Die aktuelle Zwei-Tastensteuerung der Lichter läuft über `0/4/0`. Beide Adressen dürfen nicht ohne klaren Zweck parallel dieselbe Funktion steuern.

## Hauszustände

| Gruppenadresse | Funktion | DPT | Zweck |
|---:|---|---|---|
| `0/0/0` | Zentral Aus | 1.001 | ältere Planung; nur bei separatem Einweg-Ausschaltbefehl verwenden |
| `0/0/1` | Haus verlassen | 1.001 | Abwesenheitsmodus auslösen |
| `0/0/2` | Nachtmodus | 1.001 | Nachtbetrieb aktiv |
| `0/0/3` | Urlaub | 1.001 | längere Abwesenheit |
| `0/0/4` | Panik | 1.001 | definierte Notfunktion |

### Aktuelle ETS-Verknüpfung

Der Eingangstaster `1.1.20` ist der einzige Taster, der die Zentraladressen sendet:

```text
1.1.20 Objekt 10  T3/4 Alle Rollladen – Jalousie Auf/Ab
    -> 0/1/0
    -> 1.1.4 Objekt 0 Zentrale Funktion – Rollladen Auf/Ab

1.1.20 Objekt 11  T3/4 Alle Rollladen – Stop/Lamellen Auf/Zu
    -> 0/1/1
    -> 1.1.4 Objekt 2 Zentrale Funktion – Stopp
```

Am Jalousieaktor `1.1.4` bleiben die zentralen Objekte 1 **Lamellenverstellung/Stopp**, 3 **Absolute Position** und 4 **Absolute Lamellenposition** unverknüpft. Objekt 1 ist für Jalousiekanäle mit verstellbaren Lamellen vorgesehen; die zentral zusammengefassten Antriebe sind als Rollläden parametriert.

Die Teilnahme an der Zentralfunktion ist kanalweise festgelegt:

| Aktorkanal | Einstellung `Zentrale Objekte` | Wirkung |
|---|---|---|
| A–F | `nur Auf/Ab` | nimmt an Alle Rollläden teil |
| G – Markise | `nicht aktiv` | reagiert nicht auf Alle Rollläden |
| H | `nur Auf/Ab` | nimmt an Alle Rollläden teil |

Die raumbezogenen Taster werden später direkt mit den individuellen Kanaladressen unter Hauptgruppe 2 verbunden. Dadurch wirkt die Zentralfunktion nur am Eingangstaster, während jeder andere Taster ausschließlich seine zugeordneten Rollläden beziehungsweise die Markise bedient.

> Stand 3. August 2026: Die Objektverknüpfungen und Kanalparameter sind in ETS gesetzt. Applikationsdownload und Funktionstest sind noch zu bestätigen.

## Beschattung zentral

| Gruppenadresse | Funktion | DPT | Richtung |
|---:|---|---|---|
| `0/2/0` | Beschattungsautomatik Freigabe | 1.001 | Befehl |
| `0/2/1` | Beschattungsautomatik Status | 1.001 | Rückmeldung |
| `0/2/2` | Markise Einfahren Schutz | 1.008 | Schutzbefehl |
| `0/2/3` | Wetterschutz Aktiv Status | 1.001 | Rückmeldung |

## Heizung zentral

| Gruppenadresse | Funktion | DPT | Richtung |
|---:|---|---|---|
| `0/3/0` | Heizung Zentral Betriebsart Soll | 20.102 | Befehl |
| `0/3/1` | Heizung Zentral Betriebsart Status | 20.102 | Rückmeldung |

Eine zentrale Betriebsart verhindert widersprüchliche Parallelbefehle. Welcher Wert welcher Betriebsart entspricht, wird anhand der Kommunikationsobjekte der Heizungsaktoren und Raumregler festgelegt.

## Gesamtprüfung

1. Zentral Licht und Zentral Rollladen vollständig programmieren.
2. Telegramme im ETS-Gruppenmonitor aufzeichnen.
3. Nur vorgesehene Aktorkanäle dürfen reagieren.
4. Einzelbedienung muss nach dem Zentraltest weiterhin funktionieren.
5. Statusobjekte dürfen nicht als gemeinsamer Status verwendet werden, wenn mehrere Verbraucher unterschiedliche Zustände besitzen.
