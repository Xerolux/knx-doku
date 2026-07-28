# 12 – Zentralfunktionen

## Zentral Licht – aktueller Stand

Die tatsächlich umgesetzte zentrale Lichtsteuerung verwendet eine gemeinsame 1-Bit-Gruppenadresse für Ein und Aus:

| Gruppenadresse | Funktion | DPT | Wert |
|---:|---|---|---|
| 0/4/0 | Alle Lichter schalten | 1.001 | `1` = Ein, `0` = Aus |

### Taster 1.1.20

Die Tasten 1/2 sind als Zwei-Tastenfunktion **Schalten** mit der Belegung **Ein / Aus** parametriert.

```text
1.1.20 Objekt 0  T1/2: Alle Lichter – Schalten Ein/Aus
    -> 0/4/0 Alle Lichter schalten
```

### Schaltaktor 1.1.3

Beim MDT AKS-2416.03 wird die Gruppenadresse nicht auf jeden einzelnen Kanal gezogen, sondern auf das zentrale Kommunikationsobjekt:

```text
0/4/0 Alle Lichter schalten
    -> 1.1.3 Objekt 289 Zentralfunktion – Schalten EIN/AUS
```

Bei jedem Aktorkanal, der ein Licht schaltet, muss in den Parametern die Teilnahme an der Zentralfunktion aktiviert werden. Steckdosen, technische Verbraucher und Reservekanäle dürfen nicht teilnehmen.

Objekt 291 **Zentralfunktion – In Betrieb** bleibt ohne konkreten Diagnosezweck zunächst unverknüpft.

### Statusanzeige

Das Statusobjekt des Tastenpaares wird nicht direkt mit einem einzelnen Lichtstatus verbunden. Bei mehreren Lichtkreisen wäre nicht eindeutig, ob die Zentralfunktion als Ein oder Aus angezeigt werden soll. Eine spätere Logik kann einen Sammelstatus bilden:

- mindestens ein Licht ist an
- alle ausgewählten Lichter sind an
- alle ausgewählten Lichter sind aus

## Abgrenzung zu 0/0/0

Die ältere Planungsadresse `0/0/0 Zentral Aus` beschreibt nur einen einseitigen Ausschaltbefehl. Die aktuelle Zwei-Tastensteuerung läuft über `0/4/0`. Beide Adressen dürfen nicht ohne klaren Zweck parallel dieselbe Funktion steuern. Für die aktuelle Umsetzung ist `0/4/0` verbindlich.

## Hauszustände

| Gruppenadresse | Funktion | DPT | Zweck |
|---:|---|---|---|
| 0/0/0 | Zentral Aus | 1.001 | ältere Planung; nur bei separatem Einweg-Ausschaltbefehl verwenden |
| 0/0/1 | Haus verlassen | 1.001 | Abwesenheitsmodus auslösen |
| 0/0/2 | Nachtmodus | 1.001 | Nachtbetrieb aktiv |
| 0/0/3 | Urlaub | 1.001 | längere Abwesenheit |
| 0/0/4 | Panik | 1.001 | definierte Notfunktion |

## Rollladen zentral

| Gruppenadresse | Funktion | DPT | Zweck |
|---:|---|---|---|
| 0/1/0 | Alle Rollladen Auf / Ab | 1.008 | gemeinsame Fahrtrichtung |
| 0/1/1 | Alle Rollladen Stop / Schritt | 1.007 | Fahrt stoppen oder Schritt fahren |

## Beschattung zentral

| Gruppenadresse | Funktion | DPT | Richtung |
|---:|---|---|---|
| 0/2/0 | Beschattungsautomatik Freigabe | 1.001 | Befehl |
| 0/2/1 | Beschattungsautomatik Status | 1.001 | Rückmeldung |
| 0/2/2 | Markise Einfahren Schutz | 1.008 | Schutzbefehl |
| 0/2/3 | Wetterschutz Aktiv Status | 1.001 | Rückmeldung |

## Heizung zentral

| Gruppenadresse | Funktion | DPT | Richtung |
|---:|---|---|---|
| 0/3/0 | Heizung Zentral Betriebsart Soll | 20.102 | Befehl |
| 0/3/1 | Heizung Zentral Betriebsart Status | 20.102 | Rückmeldung |

Eine zentrale Betriebsart verhindert widersprüchliche Parallelbefehle wie gleichzeitig „Komfort“ und „Eco“. Welcher Wert welcher Betriebsart entspricht, wird anhand der Kommunikationsobjekte der Heizungsaktoren und Raumregler festgelegt.

## Programmierung und Test

1. Taster `1.1.20` vollständig programmieren.
2. Schaltaktor `1.1.3` vollständig programmieren.
3. Im Gruppenmonitor prüfen, dass die linke Taste auf `0/4/0` den Wert 1 und die rechte Taste den Wert 0 sendet.
4. Kontrollieren, dass ausschließlich als Licht gekennzeichnete Kanäle reagieren.
5. Einzelbedienung der Lichtkreise danach erneut testen.
