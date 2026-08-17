# 04 – Gruppenadressen

## Gruppenadressstil

Das Projekt verwendet den ETS-Stil **3 Ebenen**:

`Hauptgruppe / Mittelgruppe / Untergruppe`

Die Datei [../ets-import/gruppenadressen.xml](../ets-import/gruppenadressen.xml) enthält die Grundstruktur. Ergänzungen werden getrennt gepflegt:

- [../ets-import/gruppenadressen-zentral-zeit.xml](../ets-import/gruppenadressen-zentral-zeit.xml) für Zentral Licht sowie Zeit und Datum
- [../ets-import/gruppenadressen-sicherheit.xml](../ets-import/gruppenadressen-sicherheit.xml) für den Gira-Rauchwarnmelder
- [../ets-import/gruppenadressen-raumcontroller.xml](../ets-import/gruppenadressen-raumcontroller.xml) für die Messwerte des OpenKNX RaumControllers

Gruppenadressen sind unabhängig von der physikalischen Linie. Geräte auf KNX TP, KNX RF und IP können dieselben Gruppenadressen verwenden, sofern ihre Kommunikationsobjekte und DPTs zueinander passen.

## Hauptgruppen

| Nr. | Bereich | Inhalt |
|---:|---|---|
| 0 | Zentral | Hauszustände, zentrale Funktionen, Zeit und Datum |
| 1 | Licht | Schalten und Status je Raum |
| 2 | Beschattung | Rollläden und Markise |
| 3 | Heizung | Raumregelung und Fensterstatus |
| 4 | Wetter | Messwerte, Alarme und Automatikfreigaben |
| 5 | Fenster | einzelne RF-Fenstergriffe und Raumstatus |
| 6 | Präsenz | Präsenz, Bewegung und Helligkeit |
| 7 | Szenen | Szenenaufrufe |
| 8 | Status | hausweite Sammelmeldungen |
| 9 | Home Assistant | optionale Diagnose- und Anzeigeobjekte |
| 10 | Sicherheit | Rauchalarm und Zustände des Gira KNX-Rauchwarnmoduls |
| 13 | Raumklima | Raumklimawerte sowie spätere Lüftungs- und Kühlungsfunktionen |

Die Hauptgruppen 11, 12, 14 und 15 bleiben als Reserve für Energie, allgemeine Störungen, Außenanlagen und spätere Erweiterungen frei. Hauptgruppe 13 wird für die Raumklimawerte des OpenKNX RaumControllers und spätere Lüftungs- oder Kühlungsfunktionen verwendet.

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
