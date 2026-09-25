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

## Küchen-Raumklima am Glastaster 1.1.22

Der ETS-Screenshot vom 25.09.2026 ordnet `1.1.22` dem Raum Küche zu. Ziel ist, Luftfeuchte, VOC und echtes CO2 in der Standby-Infoanzeige darzustellen. Die Wertelemente werden nacheinander angezeigt; der Wechsel erfolgt gemäß Parameter **Standbyanzeige nach … wechseln**. Das MDT-Handbuch erlaubt bis zu vier Status-Elemente. Für Statuswert 1–3 kann der Taster DPT 9.007 (Feuchte) und DPT 9.008 (ppm) empfangen. Die Kommunikationsobjekte 122–124 erscheinen erst, wenn die Statuswerte in den Parametern aktiviert sind.

### ETS-Gruppenadressen

Die Messwertadressen des RaumControllers bleiben reine Leseadressen. Feuchte, CO2 und VOC werden direkt als KNX-Statuswerte empfangen; für VOC wird am MDT-Taster eine benutzerdefinierte Einheit gesetzt.

| Tasterobjekt `1.1.22` | Gruppenadresse | DPT | Anzeige |
|---|---:|---:|---|
| 122 Statuswert 1 | `13/0/1` RaumController Luftfeuchte | 9.007 | Luftfeuchte in % |
| 123 Statuswert 2 | `13/0/4` RaumController CO2 | 9.008 | CO2 in ppm |
| 124 Statuswert 3 | `13/0/3` RaumController VOC | DPT 9.005 Anzeige / KNX-DPT 9 generisch | VOC als 2-Byte-Float, Anzeigeeinheit `VOC` |

Alle KNX-DPTs 9.xxx verwenden dasselbe 2-Byte-Float-Encoding. Da die MDT-Statuswertauswahl keinen generischen DPT 9 anbietet, wird Statuswert 3 auf DPT 9.005 gesetzt und die automatisch angebotene Einheit mit `VOC` überschrieben. Objekt 124 ist ausschließlich Empfänger; der RaumController bleibt alleiniger Sender auf `13/0/3`. `13/0/5` ist der aus VOC berechnete Vergleichswert und darf nicht als echtes CO2 angezeigt werden.

### ETS-Parameter und Verknüpfung

1. Prüfen, ob die bestehenden Gruppenadressen `13/0/1`, `13/0/3` und `13/0/4` im ETS-Projekt vorhanden sind. Falls nicht, die Ergänzungsdatei [gruppenadressen-raumcontroller.xml](../ets-import/gruppenadressen-raumcontroller.xml) über **Gruppenadressen → Importieren** einlesen und den Importbericht prüfen.
2. Im ETS-Projekt Gerät `1.1.22 Küche` öffnen und **Parameter → Bedienen / Anzeige → Infoanzeige** wählen.
3. Im unteren Parameterblock **Statuswert 1** auf DPT 9.007 (Feuchte), **Statuswert 2** auf DPT 9.008 (Raumluftqualität/CO2) und **Statuswert 3** auf DPT 9.005 stellen. Für die Einheiten `%`, `ppm` und `VOC` eintragen; als **Beschreibung für Messwert** `Feuchte`, `CO2` und `VOC` eintragen. Danach sollten die Kommunikationsobjekte 122–124 erscheinen.
4. Oben bei **Standbyanzeige** **einzeln im Wechsel** wählen. Um Uhrzeit plus alle drei gewünschten Messwerte anzuzeigen, **Statuselement 1** auf `Uhrzeit`, **Statuselement 2** auf `Statuswert 1`, **Statuselement 3** auf `Statuswert 2` und **Statuselement 4** auf `Statuswert 3` stellen. So rotieren Uhrzeit, Feuchte, CO2 und VOC durch die vier Plätze. Eine Wechselzeit festlegen, zum Beispiel 5 Sekunden. **Standbyanzeige bei Nacht** kann auf **Verhalten wie Tag** bleiben.
5. In der ETS-Gruppenadressansicht die Objekte 122, 123 und 124 mit `13/0/1`, `13/0/4` und `13/0/3` verbinden. Die Gruppenadresse `13/0/3` ist als generischer 2-Byte-Float angelegt. DPT 9.005 am empfangenden Anzeigeobjekt verwendet dieselbe Telegrammcodierung; das Objekt sendet nicht auf diese Adresse.
6. Nach Prüfung der Verknüpfungen den Taster `1.1.22` über **Programmieren → Applikationsprogramm** laden. Der ETS-Gruppenmonitor soll die ankommenden Werte auf den drei Messwertadressen zeigen.

Die ETS-Menübezeichnungen können je nach Produktdatenbank-Version leicht abweichen. Maßgeblich sind die Objektfunktion und der DPT in der geladenen Applikation. Das MDT-Handbuch beschreibt bis zu vier wechselnde Infoanzeige-Statuselemente sowie die Objekte 122–124 mit DPT-Auswahl.

### Prüfung und Status

- Nach Parameteraktivierung erscheinen Statuswert-Objekte 122–124.
- Im Gruppenmonitor kommen plausible Werte auf `13/0/1`, `13/0/3` und `13/0/4` an.
- Die Infoanzeige wechselt zwischen Uhrzeit, Feuchte, CO2 und VOC. Bei deaktiviertem Standby ist die Messwertanzeige nicht dauerhaft sichtbar.
- VOC kann am RaumController vorerst `0` melden (letzter dokumentierter Bustest vom 17.08.2026); erst einen plausiblen Messwert als funktional bewerten.
- Die Änderung bleibt **geplant**, bis Parameter, Verknüpfungen, Download und Anzeige am realen Taster bestätigt sind.

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
