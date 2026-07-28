# 10 – MDT Glastaster Smart II Bedienkonzept

## Aktueller Gerätebestand

Im ETS-Projekt sind die MDT Glastaster II Smart mit Temperatursensor unter `1.1.20` bis `1.1.29` angelegt. Die Geräte `1.1.20` bis `1.1.28` sind programmiert; der vollständige Programmierstand von `1.1.29` muss noch geprüft werden.

Der Taster `1.1.20` ist dem Eingang beziehungsweise Gang zugeordnet und dient aktuell als Referenz für das Bedienkonzept.

## Taster 1.1.20 – Zentral Licht

Die Tasten 1/2 sind als **Zwei-Tastenfunktion – Schalten** parametriert:

| Taste | Beschriftung | Sendewert |
|---|---|---:|
| links | Ein | 1 |
| rechts | Aus | 0 |

Die Tastenbelegung ist **Ein / Aus**. Beide Tasten verwenden dasselbe Kommunikationsobjekt und dieselbe Gruppenadresse:

```text
1.1.20 Objekt 0  T1/2: Alle Lichter – Schalten Ein/Aus
    -> 0/4/0 Alle Lichter schalten
```

Das Objekt `T1/2: Alle Lichter – Status für Anzeige` bleibt zunächst frei. Ein einzelner Statuswert wäre bei mehreren unabhängig geschalteten Lichtkreisen nicht eindeutig. Später kann eine Logik einen definierten Sammelstatus erzeugen, beispielsweise „mindestens ein Licht ist an“.

## Zeit und Datum

Für die Anzeige wird der kombinierte Datum-/Uhrzeitwert bevorzugt:

```text
0/5/2 Datum/Uhrzeit
    -> 1.1.20 Objekt 114 Uhrzeit/Datum – aktuelle Werte empfangen
```

Alternativ kann nur die Uhrzeit verwendet werden:

```text
0/5/0 Uhrzeit
    -> 1.1.20 Objekt 112 Uhrzeit – aktuellen Wert empfangen
```

Für die normale Anzeige ist einer der beiden Wege ausreichend. Der Zeitmaster und die genaue Parametrierung sind in [19 – Zeit, Datum, Temperatur und Display](19_zeit_datum_temperatur.md) beschrieben.

## Temperatur

Der Glastaster `1.1.20` besitzt einen internen Temperatursensor. In ETS muss unter **Temperaturmessung / Grundeinstellung** die Messung aktiviert sein. Für die lokale Anzeige wird die interne Temperatur in der Info- beziehungsweise Standbyanzeige ausgewählt.

Soll der Wert auf dem KNX-Bus verfügbar sein, wird das Sendeobjekt der gemessenen Temperatur mit der Isttemperaturadresse des Raumes verbunden. Für Eingang/Gang ist vorgesehen:

```text
1.1.20 gemessene Temperatur senden
    -> 3/4/1 Gang Isttemperatur
```

Vor der endgültigen Verknüpfung ist zu bestätigen, dass `1.1.20` dauerhaft dem Bereich Gang zugeordnet bleibt.

## Display-Standby

Empfohlenes Verhalten:

- Display nach einer festgelegten Zeit in Standby versetzen, beispielsweise nach 20 Sekunden.
- Standbyanzeige dunkel beziehungsweise Display aus.
- Der erste Tastendruck weckt nur das Display.
- Der zweite Tastendruck führt die eigentliche Funktion aus.

Alternativ kann der erste Tastendruck das Display aufwecken und gleichzeitig schalten. Das ist schneller, kann bei einem dunklen Display aber zu unbeabsichtigten Befehlen führen.

## Raumbezogene Funktionen

Die Glastaster sollen je Raum Licht, Beschattung und Statusanzeigen bedienen. Sie erhalten dafür keine zusätzlichen, tastereigenen Gruppenadressen, sondern verwenden die Funktionsadressen des jeweiligen Raumes.

Beispiel Wohnzimmer Rollladen links:

```text
Taster Objekt Auf/Ab   -> 2/0/0 Wohnzimmer Rollladen links Auf Ab
Taster Objekt Stop     -> 2/0/1 Wohnzimmer Rollladen links Stop
Taster Objekt Position -> 2/0/2 Wohnzimmer Rollladen links Position Soll
```

Dadurch bleiben Aktor, Taster und Visualisierung synchron.

## Empfohlene weitere Zuordnung

| Bereich | Funktionen |
|---|---|
| Wohnzimmer | Licht, beide Rollläden, Markise, Szene Fernsehen |
| Arbeitszimmer | Licht und Rollladen |
| Schlafzimmer | Licht und beide Rollläden |
| Badezimmer | Licht und Rollladen |
| Esszimmer | Licht und optionale Szene Essen |
| Küche | Licht und optionale Szene Küche |
| Gang/Eingang | Ganglicht, Zentral Licht, Nachtmodus, Anwesenheit und optional alle Rollläden |

Die konkrete Zuordnung der Adressen `1.1.21` bis `1.1.29` zu den Räumen muss noch aus dem realen Einbau übernommen werden.
