# KNX-Dokumentation Xerolux

Planungs- und Inbetriebnahmedokumentation für die KNX-Installation des Wohnhauses. Der Schwerpunkt liegt auf einer autarken KNX-Grundfunktion; Home Assistant ergänzt Visualisierung, Auswertungen und Komfortautomationen.

## Schnellstart für ETS 6

Die Gruppenadressen können im nativen XML-Format in ein ETS-Projekt mit **3-Ebenen-Gruppenadressstil** importiert werden:

1. Projekt in ETS anlegen oder öffnen.
2. In **Gruppenadressen** den obersten Eintrag rechtsklicken und **Gruppenadressen importieren** wählen.
3. Bei einem neuen Projekt [ets-import/gruppenadressen-komplett.xml](ets-import/gruppenadressen-komplett.xml) importieren. Ist die ältere Komplettdatei bereits im Projekt, für die Abstellkammer nur [ets-import/gruppenadressen-abstellkammer.xml](ets-import/gruppenadressen-abstellkammer.xml) ergänzen.
4. Erst bei Inbetriebnahme der KNX-Bridge für die IDM-Wärmepumpe zusätzlich [ets-import/gruppenadressen-waermepumpe.xml](ets-import/gruppenadressen-waermepumpe.xml) importieren.
5. Die jeweiligen Importberichte und vorhandenen Adressen prüfen.
6. Anschließend Produktdatenbanken einfügen, Geräte anlegen und Kommunikationsobjekte verbinden.

Die Wärmepumpe liegt in einer eigenen Datei: [ets-import/gruppenadressen-waermepumpe.xml](ets-import/gruppenadressen-waermepumpe.xml) mit 43 Adressen auf Hauptgruppe `11`. Die Struktur wurde inzwischen zusätzlich zur Basisstruktur in ETS importiert; Einzeladressen, DPTs und Verknüpfungen müssen noch per Detailansicht oder ETS-Export bestätigt werden. Siehe [docs/25_idm_waermepumpe_knx.md](docs/25_idm_waermepumpe_knx.md).

Die Komplettdatei enthält 164 vorgesehene Basis-Gruppenadressen einschließlich der zwei Abstellkammer-Lichtadressen und der geplanten DPTs. Zusammen mit den 43 separat gepflegten Wärmepumpen-Adressen umfasst der geplante Importstand 207 Gruppenadressen. Die bisherigen Basis-Einzeldateien dienen nur der modularen Pflege und werden nicht zusätzlich importiert. Einzelheiten stehen in [ets-import/ETS_IMPORT.md](ets-import/ETS_IMPORT.md).

> Die Komplettdatei enthält Gruppenadressstrukturen und geplante DPTs, aber keine physikalischen Adressen, Geräte oder Objektverknüpfungen.

## Topologie

```text
0.0 IP Backbone
└── 1.0 IP Hauptlinie
    ├── 1.1 TP Hauptlinie
    │   └── RF Segment 1
    └── 1.3 TP Außen (Reserve)
```

## Dokumentation

| Bereich | Inhalt |
|---|---|
| [docs/01_topologie.md](docs/01_topologie.md) | aktive TP-Linie, RF-Segment, Außenreserve und physikalische Adressen |
| [docs/02_geraeteliste.md](docs/02_geraeteliste.md) | vorhandene KNX-Hardware und aktueller ETS-Stand |
| [docs/03_raeume_funktionen.md](docs/03_raeume_funktionen.md) | Räume und Ausbaustufen |
| [docs/04_gruppenadressen.md](docs/04_gruppenadressen.md) | Adresskonzept und Benennungsregeln |
| [docs/05_kanalbelegung.md](docs/05_kanalbelegung.md) | aktuelle Licht- und Rollladenkanäle |
| [docs/06_heizung_fenster.md](docs/06_heizung_fenster.md) | Heizung und Fensterstatus |
| [docs/07_beschattung_wetter.md](docs/07_beschattung_wetter.md) | Beschattung, Rollladen und Wetterschutz |
| [docs/08_rf_fenstergriffe.md](docs/08_rf_fenstergriffe.md) | RF-Fenstergriffe |
| [docs/09_home_assistant.md](docs/09_home_assistant.md) | Rolle, Projektimport und Verbindung von Home Assistant |
| [docs/10_glastaster_bedienkonzept.md](docs/10_glastaster_bedienkonzept.md) | Bedienkonzept, Beschriftung, Temperatur und Positionsanzeige |
| [docs/11_wetterstation_gira.md](docs/11_wetterstation_gira.md) | Wetterstation |
| [docs/12_zentralfunktionen.md](docs/12_zentralfunktionen.md) | Zentral Licht und Zentral Rollladen |
| [docs/13_logikmodul.md](docs/13_logikmodul.md) | KNX-Logiken |
| [docs/14_schaltschrank.md](docs/14_schaltschrank.md) | Schaltschrankaufbau und Schutzkonzept |
| [docs/15_stromkreise.md](docs/15_stromkreise.md) | RCD-, LS- und Aktorzuordnung |
| [docs/16_beschriftung.md](docs/16_beschriftung.md) | Beschriftungsstandard |
| [docs/17_wartung.md](docs/17_wartung.md) | Abnahme, Wartung, MDT SAFE und offene Punkte |
| [docs/18_rauchwarnmelder_gira.md](docs/18_rauchwarnmelder_gira.md) | Rauchwarnmelder und Alarmadressen |
| [docs/19_zeit_datum_temperatur.md](docs/19_zeit_datum_temperatur.md) | Zeitserver, Datum, Uhrzeit, Temperatur und Display |
| [docs/20_rollladen_inbetriebnahme.md](docs/20_rollladen_inbetriebnahme.md) | JAL-Zuordnung, Namenskonvention, Fahrzeitmessung und Status |
| [docs/21_ganglicht_bewegungsmelder.md](docs/21_ganglicht_bewegungsmelder.md) | beide Ganglichter, Bewegungsmelder und Sammelstatus |
| [docs/22_programmierstand_ets.md](docs/22_programmierstand_ets.md) | Bedeutung von „Programmieren notwendig“ und Download-Reihenfolge |
| [docs/23_home_assistant_knx_entities_dashboard.md](docs/23_home_assistant_knx_entities_dashboard.md) | KNX-Entitäten, Gruppenadressen und Lovelace-Dashboard |
| [docs/24_openknx_raumcontroller.md](docs/24_openknx_raumcontroller.md) | OpenKNX-Sensorobjekte, ETS-Verknüpfung und Home-Assistant-Konfiguration |
| [docs/25_idm_waermepumpe_knx.md](docs/25_idm_waermepumpe_knx.md) | IDM Wärmepumpe auf KNX über Home Assistant, Hauptgruppe 11 |

## Home Assistant

Die aktuelle Lovelace-Konfiguration liegt unter:

```text
home-assistant/lovelace_knx_eg.yaml
```

Sie verwendet `custom:button-card` und enthält genau drei Reiter:

- Licht
- Rollläden
- Heizung

Dokumentiert sind sechs Rollladen-/Markisenentitäten, sieben Lichtentitäten und drei vorhandene Klimaentitäten. Die Rollladenkarten zeigen Position und Zustand; die eigentliche Bedienung erfolgt nach dem Anklicken im Dialog **Mehr Informationen**.

## Aktueller Stand

- Schaltaktor `1.1.3`: bestätigte Lichtkanäle A bis F dokumentiert.
- Gang: zwei getrennte Lichtkreise mit Einzeladressen und gemeinsamer Adresse `1/4/4`.
- Bewegungsmelder `1.1.30`: schaltet beide Ganglichter über `1/4/4`.
- Gemeinsamer Ganglichtstatus `1/4/5`: noch per eindeutiger ODER- oder UND-Logik zu erzeugen.
- Jalousieaktor `1.1.4`: Kanäle A, B, C, D, G und H dokumentiert.
- Zentral Rollladen: `0/1/0` für Auf/Ab und `0/1/1` für Stopp.
- Home Assistant: Licht-, Rollladen- und Markisenentitäten angelegt und Dashboard erstellt.
- OpenKNX RaumController `1.1.29`: sieben Raumklimaobjekte verbunden und am 17.08.2026 erfolgreich im Gruppenmonitor geprüft; VOC und Helligkeit lieferten beim Test noch `0`.
- Glastaster `1.1.32` und `1.1.33`: im ETS-Projekt angelegt; Raum, Funktion und Gruppenadressverknüpfungen sind noch festzulegen.
- Wetterstation `1.1.40`: im ETS-Screenshot vom 29.08.2026 ohne grüne Statushäkchen; Applikation, Parameter und Gruppenadressverknüpfungen prüfen.
- Gruppenadress-Iststand vom 29.08.2026 nach dem Zusatzimport: Hauptgruppen `0` bis `11` sowie `13`; unter `11 Wärmepumpe` sind die Mittelgruppen `11/0`, `11/1` und `11/3` sichtbar. Die 43 Einzeladressen und DPTs sind noch durch einen ETS-Export zu bestätigen.
- Raumstand: neun getrennte Räume. Die Abstellkammer ist weder Badezimmer noch Bad vorne und erhält ausschließlich `12/0/0` und `12/0/1` unter `12 Licht Erweiterung`.
- Der ETS-Suchordner zeigt 117 Einträge unter „Addresses not assigned“. Diese Zahl ist kein Gesamtzähler aller angelegten Gruppenadressen.
- Positionsstatus und Fahrzeitmessung müssen für zuverlässige Prozentwerte vollständig funktionieren.
- ETS zeigt für geänderte Geräte **Programmieren notwendig**; die betroffenen Geräte sind in Dokument 22 aufgeführt.

## ETS-Importdateien

| Datei | Verwendung |
|---|---|
| [ets-import/gruppenadressen-komplett.xml](ets-import/gruppenadressen-komplett.xml) | empfohlener Ein-Datei-Import aller 164 Basis-Gruppenadressen mit DPTs |
| [ets-import/gruppenadressen.xml](ets-import/gruppenadressen.xml) | Grundstruktur für ETS 6 |
| [ets-import/gruppenadressen-abstellkammer.xml](ets-import/gruppenadressen-abstellkammer.xml) | einmaliger Zusatzimport für `12 Licht Erweiterung / 12/0 Abstellkammer` |
| [ets-import/gruppenadressen-zentral-zeit.xml](ets-import/gruppenadressen-zentral-zeit.xml) | Ergänzung für `0/4/0` und `0/5/0` bis `0/5/2` |
| [ets-import/gruppenadressen-sicherheit.xml](ets-import/gruppenadressen-sicherheit.xml) | Ergänzung für Rauchalarm und Rauchwarnmelderzustände |
| [ets-import/gruppenadressen-raumcontroller.xml](ets-import/gruppenadressen-raumcontroller.xml) | Ergänzung für die Messwerte des OpenKNX RaumControllers `1.1.29` |
| [ets-import/gruppenadressen-waermepumpe.xml](ets-import/gruppenadressen-waermepumpe.xml) | zusätzlicher Import von 43 IDM-Wärmepumpen-Adressen in Hauptgruppe `11` |
| [ets-import/gruppenadressen-planung.csv](ets-import/gruppenadressen-planung.csv) | DPT- und Planungsreferenz der Grundstruktur |
| [ets-import/gruppenadressen-zentral-zeit-planung.csv](ets-import/gruppenadressen-zentral-zeit-planung.csv) | DPT-Referenz für Zentral Licht sowie Zeit und Datum |
| [ets-import/gruppenadressen-sicherheit-planung.csv](ets-import/gruppenadressen-sicherheit-planung.csv) | DPT-Referenz für Rauchwarnmelder und Sicherheitsmeldungen |
| [ets-import/gruppenadressen-raumcontroller-planung.csv](ets-import/gruppenadressen-raumcontroller-planung.csv) | DPT- und Objektzuordnung des OpenKNX RaumControllers |
| [ets-import/gruppenadressen-waermepumpe.csv](ets-import/gruppenadressen-waermepumpe.csv) | DPT-, Objekt- und Richtungsreferenz der IDM-Wärmepumpen-Adressen |
| [ets-import/physikalische-adressen.csv](ets-import/physikalische-adressen.csv) | Geräte- und Adresscheckliste |
| [ets-import/ETS_IMPORT.md](ets-import/ETS_IMPORT.md) | Importanleitung, Topologie und Regeln |

## Home-Assistant-Dateien

| Datei | Verwendung |
|---|---|
| [home-assistant/lovelace_knx_eg.yaml](home-assistant/lovelace_knx_eg.yaml) | Lovelace-Dashboard für Licht, Rollläden und Heizung |
| [home-assistant/knx_raumcontroller.yaml](home-assistant/knx_raumcontroller.yaml) | einbindbare KNX-Sensorliste für den OpenKNX RaumController |

## Planungsprinzip

- Grundfunktionen bleiben auf KNX.
- Befehle und Rückmeldungen erhalten getrennte Gruppenadressen.
- Ein gemeinsamer Status mehrerer Verbraucher wird durch genau eine Logik erzeugt.
- Gerätebezeichnungen, Gruppenadressennamen und reale Verdrahtung werden miteinander abgeglichen.
- Home Assistant ist keine Voraussetzung für Licht, Beschattung oder Schutzfunktionen.

## Datenschutz und Geheimnisse

Dieses öffentliche Repository enthält keine Passwörter, PINs, Tokens, Schlüsselbunddateien, privaten ETS-Projektdateien, Fotos oder Screenshots der Anlage.
