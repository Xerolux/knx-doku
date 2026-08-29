# ETS-Import – Gruppenadressen

## Zweck

Die XML-Dateien sind direkte Importdateien für ETS 6 mit **3-Ebenen-Gruppenadressstil**:

| Datei | Inhalt |
|---|---|
| `gruppenadressen-komplett.xml` | empfohlener Ein-Datei-Import der 174 Basis-Gruppenadressen mit geplanten DPTs |
| `gruppenadressen.xml` | Grundstruktur der Anlage |
| `gruppenadressen-abstellkammer.xml` | Hauptgruppe `12 Licht Erweiterung` mit zwei Lichtadressen für die Abstellkammer |
| `gruppenadressen-zentral-zeit.xml` | Zentral Licht sowie Zeit und Datum |
| `gruppenadressen-sicherheit.xml` | MDT SCN-SAFE auf `10/0` und getrennte Rauchwarnmelder-Planung auf `10/1` |
| `gruppenadressen-reparatur-safe-rauchwarnmelder.xml` | einmalige Reparaturdatei für den Adresskonflikt vom 29.08.2026 |
| `gruppenadressen-raumcontroller.xml` | Messwerte und Anforderung des OpenKNX RaumControllers `1.1.29` |
| `gruppenadressen-waermepumpe.xml` | separater Zusatzimport von 43 IDM-Wärmepumpen-Adressen über die KNX-Bridge von Home Assistant, Hauptgruppe `11` |

Die aktuelle Basis-Komplettdatei enthält 174 Gruppenadressen. Die zusätzliche Wärmepumpen-Datei enthält 43 kollisionsfreie Adressen; zusammen umfasst der vorgesehene Importstand 217 Gruppenadressen. Die CSV-Dateien bleiben technische Referenzen mit den vorgesehenen DPTs. Sie sind **keine** ETS-Importdateien. Die DPTs sind in den jeweiligen XML-Dateien hinterlegt.

## Aktueller ETS-Stand

Der erste ETS-Screenshot vom 29.08.2026 zeigt 12 vorhandene Hauptgruppen: `0` bis `10` sowie `13`. Nach dem anschließenden Import ist auch Hauptgruppe `11 Wärmepumpe` mit den Mittelgruppen `11/0`, `11/1` und `11/3` sichtbar. Damit ist die Struktur aus `gruppenadressen-waermepumpe.xml` vorhanden. Die 43 Einzeladressen und DPTs sind im Screenshot nicht aufgeklappt; ein neuer ETS-Export bleibt für den vollständigen Ist-Abgleich erforderlich. Der ältere Suchordner „Addresses not assigned“ zeigt 117 Einträge. Diese Zahl ist kein Gesamtzähler aller Gruppenadressen.

## Import in ETS 6

1. ETS-Projekt öffnen und den Gruppenadressstil **3 Ebenen** verwenden.
2. Vor dem Import eine Sicherung des ETS-Projekts erstellen.
3. In der Ansicht **Gruppenadressen** den obersten Eintrag rechtsklicken.
4. **Gruppenadressen importieren** wählen.
5. Bei einem neuen Projekt `gruppenadressen-komplett.xml` importieren. Bei einem bestehenden Projekt nur die konkret benötigte, vorher gegen den ETS-Iststand geprüfte Ergänzungs- oder Reparaturdatei importieren.
6. Nur bei Inbetriebnahme der IDM-KNX-Bridge zusätzlich `gruppenadressen-waermepumpe.xml` importieren.
7. Die jeweiligen Importberichte und die Behandlung bereits vorhandener Adressen prüfen.
8. Produktdatenbanken einfügen, Geräte anlegen und Kommunikationsobjekte verknüpfen.

Für XML muss beim Import keine CSV-Zeichenkodierung und kein Trennzeichen ausgewählt werden.

> Bereits vorhandene Gruppenadressen mit identischen Adressen dürfen nicht versehentlich dupliziert oder umbenannt werden. Im Importdialog ist die vorhandene ETS-Struktur mit der Importdatei abzugleichen.

Vor jedem Import wird zusätzlich `powershell -File scripts/validate-group-addresses.ps1` ausgeführt. Der Prüflauf bricht bei doppelten Adressen, widersprüchlichen Namen/DPTs oder einer Vermischung von SCN-SAFE (`10/0`) und Rauchwarnmelder (`10/1`) ab.

### Reparatur SCN-SAFE / Rauchwarnmelder

Die frühere Rauchwarnmelder-Datei verwendete irrtümlich `10/0/x` und benannte dadurch vorhandene SCN-SAFE-Gruppen um. Die Objektverknüpfungen des Sicherheitsmoduls blieben numerisch erhalten, zeigten aber falsche Rauchwarnmelder-Namen. Die Datei `gruppenadressen-reparatur-safe-rauchwarnmelder.xml` stellt die Trennung wieder her:

- `10/0/0` bis `10/0/5`: MDT SCN-SAFE
- `10/1/0` bis `10/1/6`: noch nicht in Betrieb genommene Rauchwarnmelder-Planung
- Objekt 227 `Aktivieren`: `10/0/5`, Verbindung in ETS noch prüfen
- Objekt 228 `Alarm quittieren`: `10/0/4`
- Objekt 229 `Befehl/Passwort`: `10/0/3`, DPT 16.000, 14 Byte
- Objekt 230 `Status`: `10/0/0`
- Objekt 231 `Alarm`: `10/0/1`

ETS-Imports sind additiv. Nicht mehr gewünschte Altadressen werden dadurch nicht automatisch entfernt. Im sichtbaren Zwischenstand waren `10/0/5 Rauchwarnmelder Testalarm Status` und `10/0/6 Rauchwarnmelder Störung Rauchkammer` noch vorhanden. Die Reparaturdatei weist `10/0/5` wieder dem SCN-SAFE-Objekt 227 zu; `10/0/6` entfällt. Beide dürfen erst umbenannt beziehungsweise gelöscht werden, nachdem in ETS bestätigt wurde, dass keine Rauchwarnmelder-Kommunikationsobjekte mehr mit ihnen verbunden sind. Der vollständige Ablauf steht in [26 – SCN-SAFE-Adressreparatur](../docs/26_scn_safe_adressreparatur.md).

### Zusatzimport Abstellkammer

Die Datei `gruppenadressen-abstellkammer.xml` ergänzt eine vollständig getrennte Licht-Erweiterung:

```text
12 Licht Erweiterung
└── 12/0 Abstellkammer
    ├── 12/0/0  Abstellkammer Licht Schalten  DPT 1.001
    └── 12/0/1  Abstellkammer Licht Status    DPT 1.001
```

Eine Mittelgruppe `1/8` ist im 3-Ebenen-Stil nicht zulässig. Die bestehenden Gruppen `1/6 Badezimmer` und `1/7 Bad vorne` werden weder verändert noch gelöscht.

## Alternative: modularer Import

Nur wenn bewusst einzelne Basisbereiche importiert werden sollen, können statt `gruppenadressen-komplett.xml` nacheinander `gruppenadressen.xml`, `gruppenadressen-zentral-zeit.xml`, `gruppenadressen-sicherheit.xml` und `gruppenadressen-raumcontroller.xml` verwendet werden. Komplettdatei und Basis-Einzeldateien werden nicht im selben Importlauf kombiniert. Die Wärmepumpen-Datei bleibt davon unabhängig und wird bei Nutzung der KNX-Bridge zusätzlich importiert.

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

Einzelheiten, Schreibrichtungen und das Verhalten bei Leseanfragen stehen in [25 – IDM Wärmepumpe](../docs/25_idm_waermepumpe_knx.md).

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

1.1.3 Objekt 49 Schalten Kanal E
    -> 1/4/0 und 1/4/4
1.1.3 Objekt 56 Status Kanal E
    -> 1/4/1

1.1.3 Objekt 61 Schalten Kanal F
    -> 1/4/2 und 1/4/4
1.1.3 Objekt 68 Status Kanal F
    -> 1/4/3

1.1.8 F1 Objekt 0 / Objekt 1 / Objekt 9
    -> 1/4/1 ODER 1/4/3
    -> 1/4/5 Gang beide Lichter Status

1.1.3 Objekt 85 Schalten Kanal H
    -> 12/0/0
1.1.3 Objekt 92 Status Kanal H
    -> 12/0/1
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
