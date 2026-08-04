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
| [docs/09_home_assistant.md](docs/09_home_assistant.md) | Rolle von Home Assistant |
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

## Aktueller Stand

- Schaltaktor `1.1.3`: bestätigte Lichtkanäle A bis F dokumentiert.
- Gang: zwei getrennte Lichtkreise mit Einzeladressen und gemeinsamer Adresse `1/4/4`.
- Bewegungsmelder `1.1.30`: schaltet beide Ganglichter über `1/4/4`.
- Gemeinsamer Ganglichtstatus `1/4/5`: noch per eindeutiger ODER- oder UND-Logik zu erzeugen.
- Jalousieaktor `1.1.4`: Kanäle A, B, C, D, G und H dokumentiert.
- Rollladen-Namenskonvention: Raum plus `Fenster` oder `Türe`; Adressen bleiben unverändert.
- Zentral Rollladen: `0/1/0` für Auf/Ab und `0/1/1` für Stopp.
- Positionsstatus und Fahrzeitmessung werden nach vollständiger Programmierung geprüft.
- ETS zeigt für geänderte Geräte **Programmieren notwendig**; die betroffenen Geräte sind in Dokument 22 aufgeführt.

## Planungsprinzip

- Grundfunktionen bleiben auf KNX.
- Befehle und Rückmeldungen erhalten getrennte Gruppenadressen.
- Ein gemeinsamer Status mehrerer Verbraucher wird durch genau eine Logik erzeugt.
- Gerätebezeichnungen, Gruppenadressennamen und reale Verdrahtung werden miteinander abgeglichen.
- Home Assistant ist keine Voraussetzung für Licht, Beschattung oder Schutzfunktionen.

## Datenschutz und Geheimnisse

Dieses öffentliche Repository enthält keine Passwörter, PINs, Tokens, Schlüsselbunddateien, privaten ETS-Projektdateien, Fotos oder Screenshots der Anlage.
