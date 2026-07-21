# KNX-Dokumentation Xerolux

Planungs- und Inbetriebnahmedokumentation für die KNX-Installation des Wohnhauses. Der Schwerpunkt liegt auf einer autarken KNX-Grundfunktion; Home Assistant ergänzt Visualisierung, Auswertungen und Komfortautomationen.

## Schnellstart für ETS 6

Die Gruppenadressen können direkt im nativen XML-Format in ein ETS-Projekt mit **3-Ebenen-Gruppenadressstil** importiert werden:

1. Projekt in ETS anlegen oder öffnen.
2. In **Gruppenadressen** den obersten Eintrag rechtsklicken und **Gruppenadressen importieren** wählen.
3. Zuerst [ets-import/gruppenadressen.xml](ets-import/gruppenadressen.xml) auswählen.
4. Für den Gira-Rauchwarnmelder zusätzlich [ets-import/gruppenadressen-sicherheit.xml](ets-import/gruppenadressen-sicherheit.xml) importieren.
5. Danach Produktdatenbanken importieren, Linien und Geräte anlegen und Kommunikationsobjekte verbinden.

Die vollständige Importreihenfolge steht in [ets-import/ETS_IMPORT.md](ets-import/ETS_IMPORT.md).

> Die XML-Dateien enthalten ausschließlich Gruppenadressstrukturen. DPTs, physikalische Adressen, Geräte und Objektverknüpfungen werden getrennt gepflegt.

## Topologie

```text
0.0 IP Backbone
└── 1.0 IP Hauptlinie
    ├── 1.1 TP Hauptlinie
    │   └── RF Segment 1
    └── 1.3 TP Außen (Reserve)
```

Der Gira 5114 00 erzeugt in ETS automatisch das RF-Segment unter Linie 1.1. Die Linie 1.3 bleibt für Außenbereich, Garage, Gartenhaus, Torsteuerung und spätere Erweiterungen reserviert.

## Dokumentation

| Bereich | Inhalt |
|---|---|
| [docs/01_topologie.md](docs/01_topologie.md) | aktive TP-Linie, RF-Segment, Außenreserve und physikalische Adressen |
| [docs/02_geraeteliste.md](docs/02_geraeteliste.md) | vorhandene KNX-Hardware |
| [docs/03_raeume_funktionen.md](docs/03_raeume_funktionen.md) | Räume und Ausbaustufen |
| [docs/04_gruppenadressen.md](docs/04_gruppenadressen.md) | Adresskonzept und Benennungsregeln |
| [docs/05_kanalbelegung.md](docs/05_kanalbelegung.md) | Aktorkanäle |
| [docs/06_heizung_fenster.md](docs/06_heizung_fenster.md) | Heizung und Fensterstatus |
| [docs/07_beschattung_wetter.md](docs/07_beschattung_wetter.md) | Beschattung und Wetterschutz |
| [docs/08_rf_fenstergriffe.md](docs/08_rf_fenstergriffe.md) | RF-Fenstergriffe |
| [docs/09_home_assistant.md](docs/09_home_assistant.md) | Rolle von Home Assistant |
| [docs/10_glastaster_bedienkonzept.md](docs/10_glastaster_bedienkonzept.md) | Bedienkonzept |
| [docs/11_wetterstation_gira.md](docs/11_wetterstation_gira.md) | Wetterstation |
| [docs/12_zentralfunktionen.md](docs/12_zentralfunktionen.md) | zentrale Funktionen |
| [docs/13_logikmodul.md](docs/13_logikmodul.md) | KNX-Logiken |
| [docs/14_schaltschrank.md](docs/14_schaltschrank.md) | Schaltschrankaufbau und Schutzkonzept |
| [docs/15_stromkreise.md](docs/15_stromkreise.md) | RCD-, LS- und Aktorzuordnung |
| [docs/16_beschriftung.md](docs/16_beschriftung.md) | Beschriftungsstandard für Geräte, Klemmen und Leitungen |
| [docs/17_wartung.md](docs/17_wartung.md) | Abnahme, Wartung und offene Punkte |
| [docs/18_rauchwarnmelder_gira.md](docs/18_rauchwarnmelder_gira.md) | Gira 2343 00 und Rauchalarm-Gruppenadressen |

## ETS-Importdateien

| Datei | Verwendung |
|---|---|
| [ets-import/gruppenadressen.xml](ets-import/gruppenadressen.xml) | Grundstruktur für ETS 6 |
| [ets-import/gruppenadressen-sicherheit.xml](ets-import/gruppenadressen-sicherheit.xml) | Ergänzung für Rauchalarm und Rauchwarnmelderzustände |
| [ets-import/gruppenadressen-planung.csv](ets-import/gruppenadressen-planung.csv) | DPT- und Planungsreferenz |
| [ets-import/physikalische-adressen.csv](ets-import/physikalische-adressen.csv) | Geräte- und Adresscheckliste |
| [ets-import/ETS_IMPORT.md](ets-import/ETS_IMPORT.md) | Importanleitung, Topologie und Regeln |

## Schutzkonzept

Die geplante Verteilung besteht aus zwei getrennten RCD-Gruppen mit jeweils bis zu acht nachgeschalteten Leitungsschutzschaltern. Beleuchtung, Beschattung, Heizung und technische Versorgungen werden eindeutig den Schutzorganen und Aktorkanälen zugeordnet. Die endgültigen Bemessungswerte und Messergebnisse sind vor Ort durch die Elektrofachkraft zu bestätigen.

## Planungsprinzip

- Grundfunktionen bleiben auf KNX: Licht, Beschattung, Heizung, Fenster-, Wetter- und Sicherheitsmeldungen.
- Befehle und Rückmeldungen haben getrennte Gruppenadressen.
- Die Geräteobjekte und deren DPTs aus der jeweiligen Produktdatenbank sind verbindlich.
- Home Assistant darf ergänzen, aber keine Schutz- oder Grundfunktion voraussetzen.
- Jedes Betriebsmittel, jede Leitung und jeder Aktorkanal erhält eine eindeutige Kennzeichnung.
- Planungswerte werden nach Abschluss durch die tatsächliche Verdrahtung und die elektrischen Messwerte ersetzt.

## Aktueller Status

Die Dokumentation enthält einen belastbaren Planungsstand. Noch zu bestätigen sind insbesondere die tatsächlichen RCD- und LS-Daten, die vollständige Klemmenbelegung, die Belegung des zweiten Heizungsaktors sowie das Mess- und Abnahmeprotokoll.
