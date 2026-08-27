# ETS-Import – Gruppenadressen

## Zweck

Die XML-Dateien sind direkte Importdateien für ETS 6 mit **3-Ebenen-Gruppenadressstil**:

| Datei | Inhalt |
|---|---|
| `gruppenadressen-komplett.xml` | empfohlener Ein-Datei-Import aller 162 Gruppenadressen mit geplanten DPTs |
| `gruppenadressen.xml` | Grundstruktur der Anlage |
| `gruppenadressen-zentral-zeit.xml` | Zentral Licht sowie Zeit und Datum |
| `gruppenadressen-sicherheit.xml` | Gira Rauchwarnmelder und Sicherheitsmeldungen |
| `gruppenadressen-raumcontroller.xml` | Messwerte und Anforderung des OpenKNX RaumControllers `1.1.29` |
| `gruppenadressen-waermepumpe.xml` | IDM Wärmepumpe über die KNX-Bridge von Home Assistant, Hauptgruppe `11` |

Die CSV-Dateien bleiben technische Referenzen mit den vorgesehenen DPTs. Sie sind **keine** ETS-Importdateien. Die DPTs sind zusätzlich in `gruppenadressen-komplett.xml` hinterlegt.

## Import in ETS 6

1. ETS-Projekt öffnen und den Gruppenadressstil **3 Ebenen** verwenden.
2. Vor dem Import eine Sicherung des ETS-Projekts erstellen.
3. In der Ansicht **Gruppenadressen** den obersten Eintrag rechtsklicken.
4. **Gruppenadressen importieren** wählen.
5. `gruppenadressen-komplett.xml` importieren.
6. Importbericht und Behandlung bereits vorhandener Adressen prüfen.
7. Produktdatenbanken einfügen, Geräte anlegen und Kommunikationsobjekte verknüpfen.

Für XML muss beim Import keine CSV-Zeichenkodierung und kein Trennzeichen ausgewählt werden.

> Bereits vorhandene Gruppenadressen mit identischen Adressen dürfen nicht versehentlich dupliziert oder umbenannt werden. Im Importdialog ist die vorhandene ETS-Struktur mit der Importdatei abzugleichen.

## Alternative: modularer Import

Nur wenn bewusst einzelne Bereiche importiert werden sollen, können stattdessen nacheinander `gruppenadressen.xml`, `gruppenadressen-zentral-zeit.xml`, `gruppenadressen-sicherheit.xml` und `gruppenadressen-raumcontroller.xml` verwendet werden. Komplettdatei und Einzeldateien werden nicht im selben Importlauf kombiniert.

## Ergänzung Zentral Licht sowie Zeit und Datum

Die Ergänzungsdatei enthält:

```text
0/4/0  Alle Lichter schalten  DPT 1.001
0/5/0  Uhrzeit               DPT 10.001
0/5/1  Datum                 DPT 11.001
0/5/2  Datum/Uhrzeit         DPT 19.001
```

Die in ETS sichtbare Adresse `0/5/3 Aktuelle Werte empfangen` wird bewusst nicht importiert. Ihre Funktion ist nicht eindeutig definiert und muss im bestehenden Projekt geprüft werden.

## Ergänzung OpenKNX RaumController

Die Ergänzungsdatei enthält die sieben Messwerte von `1.1.29` unter `13/0/0` bis `13/0/6` sowie den optionalen Anforderungstrigger `13/0/20`. DPTs und Objektnummern stehen in [gruppenadressen-raumcontroller-planung.csv](gruppenadressen-raumcontroller-planung.csv) und in [24 – OpenKNX RaumController](../docs/24_openknx_raumcontroller.md).

## Ergänzung IDM Wärmepumpe

Die Ergänzungsdatei enthält 43 Adressen auf der freien Hauptgruppe `11`. Sie werden nicht von einem KNX-Gerät bedient, sondern von der KNX-Bridge der Integration [idm-heatpump-hass](https://github.com/Xerolux/idm-heatpump-hass) über die KNX-Integration von Home Assistant.

Anders als die übrigen Dateien beschreibt sie deshalb kein Gerät, das in ETS programmiert wird. In ETS werden nur die Adressen angelegt und mit den Anzeige- oder Bedienobjekten der vorhandenen Geräte verbunden.

Die Adressen leiten sich aus `Basisadresse + IDM-Objektnummer` ab. Basis ist `11/0/0`, weil die Vorgabe der Integration `8/0/0` in dieser Anlage mit `Allgemein` belegt ist. Der Wert muss in Home Assistant identisch eingetragen sein.

Einzelheiten, Schreibrichtungen und die Einschränkung bei Leseanfragen stehen in [25 – IDM Wärmepumpe](../docs/25_idm_waermepumpe_knx.md).

Die Datei wurde mit `scripts/generate_knx_group_addresses.py` aus dem Integrations-Repository erzeugt:

```bash
python scripts/generate_knx_group_addresses.py \
  --base 11/0/0 --profile compact \
  --output ets-import --basename gruppenadressen-waermepumpe
```

## Topologie

```text
0.0 IP Backbone
└── 1.0 IP Hauptlinie
    ├── 1.1 TP Hauptlinie
    │   └── RF Segment 1
    └── 1.3 TP Außen (Reserve)
```

Der Gira 5114 00 RF Multi/TP Medienkoppler erzeugt in ETS automatisch das RF-Segment unterhalb der Linie 1.1. Eine separate Linie 1.2 wird nicht manuell angelegt. Die Linie 1.3 wird erst bei tatsächlichem Ausbau mit TP-Linienkoppler und eigener Busspannungsversorgung bestückt.

## Was die XML bewusst nicht erledigt

- **DPT-Prüfung:** Die Komplettdatei enthält die vorgesehenen DPTs. Sie müssen trotzdem zu den Kommunikationsobjekten der tatsächlich geladenen Produktdatenbank passen.
- **Physikalische Adressen und Geräte:** Diese werden nach dem Einfügen der konkreten Produktdatenbanken in ETS vergeben.
- **Verknüpfungen:** Aktor-, Taster- und Sensorobjekte müssen gezielt mit den Gruppenadressen verbunden werden.
- **Topologieerstellung:** Backbone, Hauptlinie, TP-Linie, RF-Segment und Außenreserve werden in ETS angelegt; die XML-Dateien importieren nur Gruppenadressen.
- **KNX Secure:** Schlüsselbund, Zertifikate und persönliche ETS-Projektdateien werden nicht im öffentlichen Repository gespeichert.

## Wichtige Objektverknüpfungen

```text
1.1.20 Objekt 0   T1/2 Alle Lichter Schalten
    -> 0/4/0
    -> 1.1.3 Objekt 289 Zentralfunktion Schalten EIN/AUS

1.1.31 Objekt 4   Datum/Uhrzeit senden
    -> 0/5/2
    -> 1.1.20 Objekt 114 Uhrzeit/Datum empfangen
    -> 1.1.29 Objekt 4 Uhrzeit/Datum empfangen

1.1.29 Objekte 45/48/51/54/57/58/61 Sensorwerte
    -> 13/0/0 bis 13/0/6
    -> Home Assistant sowie spätere KNX-Verbraucher
```

Bei allen gewünschten Lichtkanälen des MDT AKS-2416.03 muss die Teilnahme an der Zentralfunktion in den Parametern aktiviert sein.

## Wichtige Konventionen

- Adressen werden nicht wiederverwendet.
- Eine Gruppenadresse hat genau eine Funktion und einen passenden DPT.
- Befehle und Rückmeldungen sind getrennt.
- Gruppenadressen sind medienunabhängig und können von TP-, RF- und IP-Geräten gemeinsam verwendet werden.
- Schutz- und Grundfunktionen bleiben auch ohne Home Assistant funktionsfähig.
- Es gibt nur einen aktiven Zeitmaster.
- Die endgültigen DPTs richten sich immer nach den tatsächlich verwendeten Kommunikationsobjekten.
