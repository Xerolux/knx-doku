# 10 – MDT Glastaster Smart II Bedienkonzept

Stand: 04.08.2026

## Gerätebestand

Im ETS-Projekt sind die MDT Glastaster II Smart mit Temperatursensor unter `1.1.20` bis `1.1.28` angelegt und programmiert. Die Adresse `1.1.29` gehört dem OpenKNX RaumController und ist in [24 – OpenKNX RaumController](24_openknx_raumcontroller.md) dokumentiert.

## Grundprinzip

Die MDT Glastaster verwenden dieselben Funktionsadressen wie Aktoren und Visualisierung. Gruppenadressennamen werden nicht automatisch auf dem Display angezeigt; sichtbare Funktionsnamen werden in den Parametern des jeweiligen Tastenpaares als Text hinterlegt.

## Einheitliche Rollladen-Namen

Für die Anzeige und Dokumentation werden folgende Bezeichnungen verwendet:

```text
Wohnzimmer Rollladen Fenster
Wohnzimmer Rollladen Türe
Schlafzimmer Rollladen Fenster
Schlafzimmer Rollladen Türe
Arbeitszimmer Rollladen
Markise
```

Die früheren Zusätze `links` und `rechts` werden nicht mehr als Hauptbezeichnung verwendet.

## Zentralfunktionen am Taster 1.1.20

### Tasten 1/2 – Alle Lichter

```text
Objekt 0 Schalten Ein/Aus
    -> 0/4/0 Alle Lichter schalten
```

### Tasten 3/4 – Alle Rollladen

```text
Objekt 10 Jalousie Auf/Ab
    -> 0/1/0 Alle Rollladen Auf / Ab

Objekt 11 Stop/Lamellen Auf/Zu
    -> 0/1/1 Alle Rollladen Stop / Schritt
```

Ein gemeinsamer Prozentstatus bleibt frei, weil mehrere Rollladen unterschiedliche Positionen besitzen können.

## Raumbezogene Lichtfunktionen

| Raum | Schalten | Status |
|---|---:|---:|
| Wohnzimmer | `1/0/0` | `1/0/1` |
| Küche | `1/2/0` | `1/2/1` |
| Arbeitszimmer | `1/3/0` | `1/3/1` |
| Gang Licht 1 | `1/4/0` | `1/4/1` |
| Gang Licht 2 | `1/4/2` | `1/4/3` |
| Gang beide | `1/4/4` | `1/4/5` aus ODER-Logik `1.1.8`, F1 |
| Schlafzimmer | `1/5/0` | `1/5/1` |

## Raumbezogene Rollladenfunktionen

### Arbeitszimmer

```text
Auf/Ab -> 2/1/0
Stopp  -> 2/1/1
Status -> 2/1/3
```

### Schlafzimmer

```text
Rollladen Türe:
  Auf/Ab -> 2/2/0
  Stopp  -> 2/2/1
  Status -> 2/2/3

Rollladen Fenster:
  Auf/Ab -> 2/2/10
  Stopp  -> 2/2/11
  Status -> 2/2/13
```

### Wohnzimmer / Terrasse

```text
Rollladen Fenster:
  Auf/Ab -> 2/0/0
  Stopp  -> 2/0/1
  Status -> 2/0/3

Rollladen Türe:
  Auf/Ab -> 2/0/10
  Stopp  -> 2/0/11
  Status -> 2/0/13

Markise:
  Auf/Ab -> 2/4/0
  Stopp  -> 2/4/1
  Status -> 2/4/3
```

## Anzeige und Bedienung

Empfohlene Einstellung je Rollladen-Tastenpaar:

```text
Zwei-Tastenfunktion: Jalousie/Rollladen
Bedienfunktion: Lang = Auf/Ab, Kurz = Stopp
Funktionsname: über Texteingabe
Text: Rollladen Fenster, Rollladen Türe oder Markise
Tastenbeschriftung: Pfeil Ab / Pfeil Auf passend zur Tastenbelegung
Statuswert unter Symbol: anzeigen in Prozent
```

Die Prozentanzeige funktioniert nur, wenn das Statusobjekt des Glastasters und `Status aktuelle Position` des JAL dieselbe Status-Gruppenadresse verwenden.

```text
0 %   = vollständig oben
100 % = vollständig unten
```

## Temperaturanzeige

Der interne Temperatursensor wird unter **Temperaturmessung → Grundeinstellung** aktiviert. Für eine Anzeige im Standby muss eine Standbydarstellung mit Statuselementen gewählt werden; bei `Display Aus` wird kein Temperaturwert dauerhaft angezeigt.

Soll die Temperatur zusätzlich auf den Bus gesendet werden, wird Objekt 108 `Temperaturmesswert` mit der Isttemperaturadresse des jeweiligen Raumes verbunden.

Für Eingang/Gang ist als Temperaturadresse vorgesehen:

```text
1.1.20 gemessene Temperatur senden
    -> 3/4/1 Gang Isttemperatur
```

Vor der endgültigen Verknüpfung ist zu bestätigen, dass `1.1.20` dauerhaft dem Bereich Gang zugeordnet bleibt.

## Zeit und Datum

```text
0/5/2 Datum/Uhrzeit
    -> Objekt 114 Uhrzeit/Datum – aktuelle Werte empfangen
```

## Programmierung und Prüfung

Nach Änderungen an Texten, Parametern oder Verknüpfungen den betroffenen Glastaster über **Programmieren → Applikationsprogramm** vollständig laden.

Prüfen:

1. Funktionsname und Symbole stimmen.
2. Langdruck fährt in die richtige Richtung.
3. Kurzdruck stoppt.
4. Positionswert wird nach Fahrtende aktualisiert.
5. Obere Endlage zeigt ungefähr `0 %`.
6. Untere Endlage zeigt ungefähr `100 %`.

## Display-Standby

Empfohlenes Verhalten:

- Display nach einer festgelegten Zeit in Standby versetzen, beispielsweise nach 20 Sekunden.
- Standbyanzeige dunkel beziehungsweise Display aus.
- Der erste Tastendruck weckt nur das Display.
- Der zweite Tastendruck führt die eigentliche Funktion aus.

Alternativ kann der erste Tastendruck das Display aufwecken und gleichzeitig schalten. Das ist schneller, kann bei einem dunklen Display aber zu unbeabsichtigten Befehlen führen.

## Weitere raumbezogene Funktionen

Die Glastaster sollen je Raum Licht, Beschattung und Statusanzeigen bedienen. Sie erhalten dafür keine zusätzlichen, tastereigenen Gruppenadressen, sondern verwenden die Funktionsadressen des jeweiligen Raumes.

## Empfohlene weitere Zuordnung

| Bereich | Funktionen |
|---|---|
| Wohnzimmer | Licht, beide Rollläden, Markise, Szene Fernsehen |
| Arbeitszimmer | Licht und Rollladen |
| Schlafzimmer | Licht und beide Rollläden |
| Badezimmer | Licht und Rollladen |
| Abstellkammer (ehemals Dusche) | Licht über `12/0/0`, Status über `12/0/1` |
| Esszimmer | Licht und optionale Szene Essen |
| Küche | Licht und optionale Szene Küche |
| Gang/Eingang | Ganglicht, Zentral Licht, Nachtmodus, Anwesenheit und optional alle Rollläden |

Die konkrete Zuordnung der Glastaster `1.1.21` bis `1.1.28` zu den Räumen muss noch aus dem realen Einbau übernommen werden.

Dieses Dokument enthält keine Bilder, Passwörter, PINs oder privaten ETS-Dateien.
