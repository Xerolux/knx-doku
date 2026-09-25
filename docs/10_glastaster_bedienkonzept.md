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

Für den Glastaster `1.1.21 Eingang Gang` zeigt der ETS-Screenshot vom 25.09.2026 die Verknüpfung:

```text
1.1.21 Objekt 108 Temperaturmesswert
    -> 3/4/1 Gang Isttemperatur
```

Die Gruppenadresse ist als DPT 9.001 (Temperatur, 2 Byte) angelegt. Der Screenshot belegt die Verknüpfung im ETS-Projekt; Applikationsdownload und Telegrammprüfung am Bus sind damit noch nicht bestätigt. Für Home Assistant kann ein KNX-Sensor mit `state_address: "3/4/1"` und `type: temperature` angelegt werden. Die HA-Entität und ihr Live-Wert sind noch nicht geprüft.

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

## Küchen-Raumklima am Glastaster 1.1.22

Die ETS-Screenshots vom 25.09.2026 bestätigen für `1.1.22` die Anzeige-Konfiguration und die Gruppenadressverknüpfungen. Im Wechsel werden Uhrzeit, Feuchte, das berechnete CO2-VOC-Äquivalent und echtes CO2 angezeigt. Der rohe VOC-Wert wird nicht direkt auf dem Glastaster dargestellt. Die Kommunikationsobjekte 122–124 sind aktiviert und verbunden.

### ETS-Gruppenadressen

Die Messwertadressen des RaumControllers bleiben reine Leseadressen. Feuchte und CO2 werden direkt als KNX-Statuswerte empfangen. VOC bleibt auf `13/0/3` unverändert; der Taster bietet für diesen generischen DPT 9 derzeit keinen passenden Statuswerttyp.

| Tasterobjekt `1.1.22` | Gruppenadresse | DPT | Anzeige |
|---|---:|---:|---|
| 122 Statuswert 1 | `13/0/1` RaumController Luftfeuchte | 9.007 | Beschreibung `Feuchte`, Einheit `%` |
| 123 Statuswert 2 | `13/0/5` RaumController CO2-VOC berechnet | 9.008 | Beschreibung `CO2-VOC`, Einheit `ppm`; berechneter CO2-Äquivalentwert |
| 124 Statuswert 3 | `13/0/4` RaumController CO2 | 9.008 | Beschreibung `CO2`, Einheit `ppm`; echter CO2-Messwert |

Der Glastaster bietet bei Statuswerten nur fest definierte DPTs. **DPT 9.005 ist Geschwindigkeit (m/s)** und ist kein passender DPT für VOC. Eine benutzerdefinierte Einheitenbeschriftung ändert die DPT-Bedeutung nicht. Deshalb wird `13/0/3` hier nicht mit einem numerischen Statuswertobjekt des Tasters verbunden. `13/0/5` ist der aus VOC berechnete Vergleichswert und darf nicht als echtes CO2 angezeigt werden.

### ETS-Parameter und Verknüpfung

1. Prüfen, ob die Gruppenadressen `13/0/1`, `13/0/4` und `13/0/5` im ETS-Projekt vorhanden sind. Falls nicht, die Ergänzungsdatei [gruppenadressen-raumcontroller.xml](../ets-import/gruppenadressen-raumcontroller.xml) über **Gruppenadressen → Importieren** einlesen und den Importbericht prüfen.
2. Im ETS-Projekt Gerät `1.1.22 Küche` öffnen und **Parameter → Bedienen / Anzeige → Infoanzeige** wählen.
3. Unter **Statuswert 1** DPT 9.007 (Feuchte), Einheit `%`, Beschreibung `Feuchte` einstellen. Unter **Statuswert 2** DPT 9.008 (Raumluftqualität), Einheit `ppm`, Beschreibung `CO2-VOC` einstellen. Unter **Statuswert 3** DPT 9.008, Einheit `ppm`, Beschreibung `CO2` einstellen.
4. Bei **Standbyanzeige** **einzeln im Wechsel** wählen: **Statuselement 1** = `Uhrzeit`, **Statuselement 2** = `Statuswert 1`, **Statuselement 3** = `Statuswert 2`, **Statuselement 4** = `Statuswert 3`. Eine Wechselzeit festlegen, zum Beispiel 5 Sekunden. **Standbyanzeige bei Nacht** kann auf **Verhalten wie Tag** bleiben.
5. In der ETS-Gruppenadressansicht Objekt 122 mit `13/0/1` (Luftfeuchte), Objekt 123 mit `13/0/5` (berechnetes CO2-VOC) und Objekt 124 mit `13/0/4` (echtes CO2) verbinden. `13/0/3` nicht mit einem Statuswertobjekt verbinden: die MDT-Auswahlliste enthält keinen passenden generischen VOC-DPT.
6. Die Screenshots vom 25.09.2026 belegen die Parametrierung und Verknüpfungen oben. Nach jeder Änderung den Taster `1.1.22` über **Programmieren → Applikationsprogramm** laden und die drei Werte am Display prüfen. ETS-Verknüpfungen allein belegen nicht, dass die aktuelle Applikation bereits auf das Gerät geladen wurde.

Die ETS-Menübezeichnungen können je nach Produktdatenbank-Version leicht abweichen. Maßgeblich sind die Objektfunktion und der DPT in der geladenen Applikation. Das MDT-Handbuch beschreibt bis zu vier wechselnde Infoanzeige-Statuselemente sowie die Objekte 122–124 mit DPT-Auswahl.

### Prüfung und Status

- Statuswert-Objekte 122, 123 und 124 sind aktiviert und den Adressen `13/0/1`, `13/0/5` und `13/0/4` zugeordnet.
- Die Infoanzeige ist auf den Wechsel zwischen Uhrzeit, Feuchte, berechnetem CO2-VOC-Äquivalent und echtem CO2 eingestellt. Screenshot belegt die ETS-Konfiguration; Anzeige am physischen Gerät und Downloadstatus sind separat zu prüfen.
- VOC ist mit den auswählbaren MDT-Statuswert-DPTs nicht direkt darstellbar; dafür wäre ein eigener, korrekt typisierter Anzeigeweg erforderlich.
- VOC kann am RaumController vorerst `0` melden (letzter dokumentierter Bustest vom 17.08.2026); erst einen plausiblen Messwert als funktional bewerten.
- Parametrierung und Verknüpfungen sind laut ETS-Screenshots dokumentiert; die Inbetriebnahme bleibt offen, bis Download und Anzeige am realen Taster bestätigt sind.

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

Die konkrete Zuordnung der Glastaster `1.1.21` bis `1.1.28` muss – außer `1.1.22` Küche – noch aus dem realen Einbau übernommen werden.

Dieses Dokument enthält keine Bilder, Passwörter, PINs oder privaten ETS-Dateien.
