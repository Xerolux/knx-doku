# 04 – Gruppenadressen

## Gruppenadressstil

Das Projekt verwendet den ETS-Stil **3 Ebenen**:

`Hauptgruppe / Mittelgruppe / Untergruppe`

Die Datei [../ets-import/gruppenadressen.xml](../ets-import/gruppenadressen.xml) enthält die Grundstruktur. Ergänzungen werden getrennt gepflegt:

- [../ets-import/gruppenadressen-zentral-zeit.xml](../ets-import/gruppenadressen-zentral-zeit.xml) für Zentral Licht sowie Zeit und Datum
- [../ets-import/gruppenadressen-sicherheit.xml](../ets-import/gruppenadressen-sicherheit.xml) für den Gira-Rauchwarnmelder
- [../ets-import/gruppenadressen-raumcontroller.xml](../ets-import/gruppenadressen-raumcontroller.xml) für die Messwerte des OpenKNX RaumControllers
- [../ets-import/gruppenadressen-waermepumpe.xml](../ets-import/gruppenadressen-waermepumpe.xml) für die KNX-Bridge der IDM-Wärmepumpe

Gruppenadressen sind unabhängig von der physikalischen Linie. Geräte auf KNX TP, KNX RF und IP können dieselben Gruppenadressen verwenden, sofern ihre Kommunikationsobjekte und DPTs zueinander passen.

## Hauptgruppen

| Nr. | Bereich | Inhalt | Stand 29.08.2026 |
|---:|---|---|---|
| 0 | Zentral | Hauszustände, zentrale Funktionen, Zeit und Datum | in ETS vorhanden |
| 1 | Licht | Schalten und Status je Raum | in ETS vorhanden |
| 2 | Beschattung | Rollläden und Markise | in ETS vorhanden |
| 3 | Heizung | Raumregelung und Fensterstatus | in ETS vorhanden |
| 4 | Wetter | Messwerte, Alarme und Automatikfreigaben | in ETS vorhanden |
| 5 | Fenster | einzelne RF-Fenstergriffe und Raumstatus | in ETS vorhanden |
| 6 | Präsenz | Präsenz, Bewegung und Helligkeit | in ETS vorhanden |
| 7 | Szenen | Szenenaufrufe | in ETS vorhanden |
| 8 | Status | hausweite Sammelmeldungen | in ETS vorhanden |
| 9 | Home Assistant | optionale Diagnose- und Anzeigeobjekte | in ETS vorhanden |
| 10 | Sicherheit | Rauchalarm und Zustände des Gira KNX-Rauchwarnmoduls | in ETS vorhanden |
| 11 | IDM Wärmepumpe | Werte und freigegebene Sollvorgaben der Home-Assistant-KNX-Bridge | in ETS importiert; Einzeladressen noch zu exportieren und zu prüfen |
| 13 | Raumklima | Raumklimawerte sowie spätere Lüftungs- und Kühlungsfunktionen | in ETS vorhanden |

Der erste ETS-Screenshot vom 29.08.2026 zeigte 12 Hauptgruppen: `0` bis `10` sowie `13`. Nach dem anschließenden Import ist zusätzlich Hauptgruppe `11` sichtbar; darunter werden die drei Mittelgruppen `11/0 Objekte 1–230`, `11/1 Objekte 292–499` und `11/3 PV und Batterie` angezeigt. Damit ist die Wärmepumpen-Struktur angelegt. Ob alle 43 Einzeladressen und DPTs vollständig übernommen wurden, muss noch durch Aufklappen der Mittelgruppen oder einen neuen ETS-Export bestätigt werden. Die Hauptgruppen 12, 14 und 15 bleiben als Reserve für allgemeine Störungen, Außenanlagen und spätere Erweiterungen frei.

## Abgleichstand der Dateien

| Datenbestand | Gruppenadressen | Bedeutung |
|---|---:|---|
| `export.xml` | 144 | älterer ETS-XML-Export der Grundstruktur |
| `gruppenadressen-ETS6-4-1.csv` | 145 | älterer ETS-CSV-Export; enthält zusätzlich die Altplanung `0/0/0 Zentral Aus` |
| `gruppenadressen-komplett.xml` | 164 | vorgesehene Basisstruktur einschließlich Abstellkammer-Licht, Zentralfunktionen, Zeit/Datum, Sicherheit und RaumController |
| `gruppenadressen-abstellkammer.xml` | 2 | einmaliger Zusatzimport für bereits mit der älteren Komplettdatei angelegte ETS-Projekte |
| `gruppenadressen-waermepumpe.xml` | 43 | separater Zusatzimport für die IDM-KNX-Bridge |
| geplanter Gesamtstand | 207 | aktuelle Basis-Komplettdatei plus Wärmepumpen-Datei; ohne die nicht importierte Altplanung `0/0/0` |

Der erste Gruppenadress-Screenshot vom 29.08.2026 bestätigt die damaligen Hauptgruppen und zeigt im Suchordner 117 Einträge „Addresses not assigned“. Diese Zahl beschreibt den Suchordner, nicht die Gesamtzahl aller Gruppenadressen. Der spätere Screenshot bestätigt zusätzlich Hauptgruppe `11` und ihre drei Mittelgruppen, zeigt aber weiterhin keine einzelnen Wärmepumpen-Adressen, DPTs oder Objektverknüpfungen. Der Geräte-Screenshot desselben Tages zeigt zusätzlich physikalische Teilnehmer und ETS-Statussymbole, aber ebenfalls keine Gruppenadressverknüpfungen.

Nach dem Import und der Verknüpfung der Kommunikationsobjekte ist deshalb ein neuer Gruppenadress-Export aus dem ETS-Projekt erforderlich; erst dieser ersetzt die beiden älteren Export-Snapshots als vollständigen Ist-Stand.

Die neu angelegten Glastaster `1.1.32` und `1.1.33` erhalten keine eigenen, gerätebezogenen Adressbereiche. Nach Festlegung von Raum und Bedienfunktion werden ihre Kommunikationsobjekte mit den bereits raum- und funktionsbezogen aufgebauten Gruppenadressen verbunden. Bis dahin bleiben diese Verknüpfungen offen.

## Abstellkammer

Die Abstellkammer, früher als Dusche bezeichnet, ist ein eigener neunter Raum und nicht das Badezimmer. Sie besitzt nur eine Lichtfunktion. Da beim 3-Ebenen-Stil die acht Mittelgruppen `0` bis `7` bereits verwendet werden, nutzt sie innerhalb von `1/7 Bad vorne` den freien Untergruppenblock `10–19`:

| Gruppenadresse | Name | DPT |
|---:|---|---:|
| `1/7/10` | Abstellkammer Licht Schalten | 1.001 |
| `1/7/11` | Abstellkammer Licht Status | 1.001 |

Die bestehenden Adressen des Badezimmers und von Bad vorne bleiben unverändert. Für ein ETS-Projekt, in das bereits die ältere Komplettdatei importiert wurde, wird nur [gruppenadressen-abstellkammer.xml](../ets-import/gruppenadressen-abstellkammer.xml) zusätzlich importiert. Die aktuelle `gruppenadressen-komplett.xml` enthält die beiden Adressen bereits und darf dann nicht nochmals zusätzlich importiert werden.

## IDM Wärmepumpe

Die 43 vorgesehenen Wärmepumpen-Adressen liegen unter `11/0/x`, `11/1/x` und `11/3/x`. Ihre Namen, DPTs und Schreibrichtungen sind in [25 – IDM Wärmepumpe über Home Assistant](25_idm_waermepumpe_knx.md) und [gruppenadressen-waermepumpe.csv](../ets-import/gruppenadressen-waermepumpe.csv) dokumentiert. Die Wärmepumpen-Datei wurde zusätzlich zur Basisstruktur importiert; beide Adressmengen sind kollisionsfrei. Der aktuelle Screenshot bestätigt Hauptgruppe `11` und ihre drei Mittelgruppen, aber noch nicht jede einzelne Adresse oder Verknüpfung.

## Raumklima / OpenKNX RaumController

| Gruppenadresse | Name | DPT | Quelle |
|---:|---|---:|---|
| 13/0/0 | RaumController Temperatur | 9.001 | `1.1.29`, Objekt 45 |
| 13/0/1 | RaumController Luftfeuchte | 9.007 | `1.1.29`, Objekt 48 |
| 13/0/2 | RaumController Luftdruck | 9.006 | `1.1.29`, Objekt 51 |
| 13/0/3 | RaumController VOC | 9 | `1.1.29`, Objekt 54 |
| 13/0/4 | RaumController CO2 | 9.008 | `1.1.29`, Objekt 57 |
| 13/0/5 | RaumController CO2-VOC berechnet | 9.008 | `1.1.29`, Objekt 58 |
| 13/0/6 | RaumController Helligkeit | 9.004 | `1.1.29`, Objekt 61 |
| 13/0/20 | RaumController Sensorwerte anfordern | 1.016 | optional an `1.1.29`, Objekt 43 |

Die Messwertadressen sind nicht Home-Assistant-spezifisch. Home Assistant liest sie zunächst zur Visualisierung und Statistik; spätere KNX-Teilnehmer dürfen dieselben Werte konsumieren. Nur der RaumController schreibt die Messwerte.

## Zentral Licht

| Gruppenadresse | Name | DPT | Verwendung |
|---:|---|---|---|
| 0/4/0 | Alle Lichter schalten | 1.001 | `1` schaltet die ausgewählten Lichtkanäle ein, `0` schaltet sie aus |

Für Ein und Aus wird bewusst dieselbe Gruppenadresse verwendet. Der Taster sendet abhängig von der gedrückten Taste den Wert 1 oder 0. Der Schaltaktor empfängt diese Adresse über sein Zentralobjekt.

## Zeit und Datum

| Gruppenadresse | Name | DPT | Verwendung |
|---:|---|---|---|
| 0/5/0 | Uhrzeit | 10.001 | Tageszeit als 3-Byte-Wert |
| 0/5/1 | Datum | 11.001 | Datum als 3-Byte-Wert |
| 0/5/2 | Datum/Uhrzeit | 19.001 | kombinierter 8-Byte-Wert |

Für den MDT Glastaster II Smart wird bevorzugt `0/5/2` mit seinem kombinierten Empfangsobjekt verwendet. Die Einzeladressen bleiben für Geräte bestehen, die nur DPT 10.001 oder DPT 11.001 unterstützen.

Die in ETS sichtbare Adresse `0/5/3 Aktuelle Werte empfangen` besitzt derzeit keine eindeutig definierte Funktion. Sie wird nicht in die Importdatei übernommen. Vor dem Löschen muss geprüft werden, ob sie mit einem Objekt verbunden ist.

## Sicherheit / Rauchwarnmelder

```text
10/0/0  Rauchalarm
10/0/1  Rauchwarnmelder Störung
10/0/2  Rauchwarnmelder Batterie schwach
10/0/4  Rauchwarnmelder Testalarm auslösen
10/0/5  Rauchwarnmelder Testalarm Status
10/0/6  Rauchwarnmelder Störung Rauchkammer
```

Die Gira-Applikation besitzt kein separates Objekt nur für Verschmutzung. Dieser Zustand ist Bestandteil der allgemeinen Störung an Objekt 12; Objekt 16 liefert zusätzlich die allgemeinere Rauchkammerstörung. `10/0/3` bleibt wegen des wiederholten ETS-Importkonflikts frei. Die tatsächliche Verknüpfung erfolgt anhand der in der Produktdatenbank sichtbaren Kommunikationsobjekte.

## Konventionen

| Art | Benennung | Beispiel |
|---|---|---|
| Befehl | `… Schalten`, `… Soll`, `… Freigabe` | `Wohnzimmer Licht Schalten` |
| Rückmeldung | `… Status`, `… Ist` | `Wohnzimmer Licht Status` |
| Position | `… Position Soll` / `… Position Status` | `Markise Position Status` |
| Messwert | eindeutige physikalische Größe | `Gang Isttemperatur` |
| Schutz | eindeutiger Auslöser und Status | `Markise Einfahren Schutz` / `Wetterschutz Aktiv Status` |

- Eine Gruppenadresse hat genau eine Bedeutung und wird nicht erneut vergeben.
- Kommunikationsobjekt-Namen wie „Aktuelle Werte empfangen“ werden nicht als Gruppenadressnamen übernommen.
- Taster, Aktor und Visualisierung verwenden für dieselbe Funktion dieselbe Befehlsadresse.
- Rückmeldungen werden nur vom zuständigen Gerät beziehungsweise der zuständigen Logik geschrieben.
- Der DPT muss zum Kommunikationsobjekt der importierten Produktdatenbank passen.
- Befehle unterschiedlicher Länge oder Bedeutung dürfen nicht auf dieselbe Gruppenadresse gelegt werden.
- Die XML-Dateien importieren Gruppenadressstrukturen, aber keine Geräte, physikalischen Adressen oder Objektverknüpfungen.

## Zentralfunktionen

Zentrale Befehle sind konfliktfrei angelegt:

- Licht: ein gemeinsamer 1-Bit-Befehl für Ein und Aus über `0/4/0`.
- Beschattungsautomatik: eine **Freigabe** und eine **Status**-Rückmeldung.
- Heizung: eine zentrale **Betriebsart Soll** und eine **Betriebsart Status** mit DPT 20.102.
- Rollläden: ein zentraler Auf-/Ab-Befehl sowie ein separater Stop-/Schritt-Befehl.

Die vollständigen Objektverknüpfungen stehen in [12 – Zentralfunktionen](12_zentralfunktionen.md) und [19 – Zeit, Datum, Temperatur und Display](19_zeit_datum_temperatur.md).
