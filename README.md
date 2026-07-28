# KNX-Dokumentation Xerolux

Planungs- und Inbetriebnahmedokumentation für die KNX-Installation des Wohnhauses. Der Schwerpunkt liegt auf einer autarken KNX-Grundfunktion; Home Assistant ergänzt Visualisierung, Auswertungen und Komfortautomationen.

## Schnellstart für ETS 6

Die Gruppenadressen können im nativen XML-Format in ein ETS-Projekt mit **3-Ebenen-Gruppenadressstil** importiert werden:

1. Projekt in ETS anlegen oder öffnen.
2. In **Gruppenadressen** den obersten Eintrag rechtsklicken und **Gruppenadressen importieren** wählen.
3. Zuerst [ets-import/gruppenadressen.xml](ets-import/gruppenadressen.xml) importieren.
4. Danach [ets-import/gruppenadressen-zentral-zeit.xml](ets-import/gruppenadressen-zentral-zeit.xml) für Zentral Licht sowie Zeit und Datum importieren.
5. Für den Gira-Rauchwarnmelder zusätzlich [ets-import/gruppenadressen-sicherheit.xml](ets-import/gruppenadressen-sicherheit.xml) importieren.
6. Anschließend Produktdatenbanken einfügen, Geräte anlegen und Kommunikationsobjekte verbinden.

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

Der Gira 5114 00 erzeugt in ETS automatisch das RF-Segment unter Linie 1.1. Eine separate Linie 1.2 wird nicht verwendet. Die Linie 1.3 bleibt für Außenbereich, Garage, Gartenhaus, Torsteuerung und spätere Erweiterungen reserviert.

## Dokumentation

| Bereich | Inhalt |
|---|---|
| [docs/01_topologie.md](docs/01_topologie.md) | aktive TP-Linie, RF-Segment, Außenreserve und physikalische Adressen |
| [docs/02_geraeteliste.md](docs/02_geraeteliste.md) | vorhandene KNX-Hardware und aktueller ETS-Stand |
| [docs/03_raeume_funktionen.md](docs/03_raeume_funktionen.md) | Räume und Ausbaustufen |
| [docs/04_gruppenadressen.md](docs/04_gruppenadressen.md) | Adresskonzept und Benennungsregeln |
| [docs/05_kanalbelegung.md](docs/05_kanalbelegung.md) | Aktorkanäle |
| [docs/06_heizung_fenster.md](docs/06_heizung_fenster.md) | Heizung und Fensterstatus |
| [docs/07_beschattung_wetter.md](docs/07_beschattung_wetter.md) | Beschattung und Wetterschutz |
| [docs/08_rf_fenstergriffe.md](docs/08_rf_fenstergriffe.md) | RF-Fenstergriffe |
| [docs/09_home_assistant.md](docs/09_home_assistant.md) | Rolle von Home Assistant |
| [docs/10_glastaster_bedienkonzept.md](docs/10_glastaster_bedienkonzept.md) | Bedienkonzept und aktueller Taster 1.1.20 |
| [docs/11_wetterstation_gira.md](docs/11_wetterstation_gira.md) | Wetterstation |
| [docs/12_zentralfunktionen.md](docs/12_zentralfunktionen.md) | zentrale Funktionen einschließlich Zentral Licht |
| [docs/13_logikmodul.md](docs/13_logikmodul.md) | KNX-Logiken |
| [docs/14_schaltschrank.md](docs/14_schaltschrank.md) | Schaltschrankaufbau und Schutzkonzept |
| [docs/15_stromkreise.md](docs/15_stromkreise.md) | RCD-, LS- und Aktorzuordnung |
| [docs/16_beschriftung.md](docs/16_beschriftung.md) | Beschriftungsstandard für Geräte, Klemmen und Leitungen |
| [docs/17_wartung.md](docs/17_wartung.md) | Abnahme, Wartung, MDT SAFE und offene Punkte |
| [docs/18_rauchwarnmelder_gira.md](docs/18_rauchwarnmelder_gira.md) | Gira KNX-Rauchwarnmelder und Alarmadressen |
| [docs/19_zeit_datum_temperatur.md](docs/19_zeit_datum_temperatur.md) | KNX-Zeitserver, Datum, Uhrzeit, Temperatur und Display |

## ETS-Importdateien

| Datei | Verwendung |
|---|---|
| [ets-import/gruppenadressen.xml](ets-import/gruppenadressen.xml) | Grundstruktur für ETS 6 |
| [ets-import/gruppenadressen-zentral-zeit.xml](ets-import/gruppenadressen-zentral-zeit.xml) | Ergänzung für `0/4/0` und `0/5/0` bis `0/5/2` |
| [ets-import/gruppenadressen-sicherheit.xml](ets-import/gruppenadressen-sicherheit.xml) | Ergänzung für Rauchalarm und Rauchwarnmelderzustände |
| [ets-import/gruppenadressen-planung.csv](ets-import/gruppenadressen-planung.csv) | DPT- und Planungsreferenz der Grundstruktur |
| [ets-import/gruppenadressen-zentral-zeit-planung.csv](ets-import/gruppenadressen-zentral-zeit-planung.csv) | DPT-Referenz für Zentral Licht sowie Zeit und Datum |
| [ets-import/physikalische-adressen.csv](ets-import/physikalische-adressen.csv) | Geräte- und Adresscheckliste |
| [ets-import/ETS_IMPORT.md](ets-import/ETS_IMPORT.md) | Importanleitung, Topologie und Regeln |

## Planungsprinzip

- Grundfunktionen bleiben auf KNX: Licht, Beschattung, Heizung, Fenster-, Wetter- und Sicherheitsmeldungen.
- Befehle und Rückmeldungen haben getrennte Gruppenadressen.
- Die Geräteobjekte und deren DPTs aus der jeweiligen Produktdatenbank sind verbindlich.
- Home Assistant darf ergänzen, aber keine Schutz- oder Grundfunktion voraussetzen.
- Jedes Betriebsmittel, jede Leitung und jeder Aktorkanal erhält eine eindeutige Kennzeichnung.
- Planungswerte werden nach Abschluss durch die tatsächliche Verdrahtung und die elektrischen Messwerte ersetzt.

## Aktueller Status

Die zentrale Lichtsteuerung ist unter `0/4/0 Alle Lichter schalten` angelegt. Der Taster `1.1.20 Eingang` sendet als Zwei-Tastenfunktion Ein und Aus auf diese Adresse; der MDT AKS-2416.03 empfängt sie über sein Zentralobjekt. Die E-Mail- und Zeitserver-Applikation des MDT SCN-IP100.03 ist unter `1.1.31` angelegt und versorgt den Bus über `0/5/0`, `0/5/1` und bevorzugt `0/5/2`. Die MDT Glastaster `1.1.20` bis `1.1.28` sind im ETS-Projekt vorhanden, `1.1.29` und einzelne Gira-Geräte müssen hinsichtlich ihres vollständigen Programmierstands noch geprüft werden.
