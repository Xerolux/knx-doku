# KNX-Dokumentation Xerolux

Planungs- und Inbetriebnahmedokumentation für die KNX-Installation des Wohnhauses. Der Schwerpunkt liegt auf einer autarken KNX-Grundfunktion; Home Assistant ergänzt Visualisierung, Auswertungen und Komfortautomationen.

## Schnellstart für ETS

Die Gruppenadressen können direkt in ein ETS-Projekt mit **3-Ebenen-Gruppenadressstil** importiert werden:

1. Projekt in ETS anlegen oder öffnen.
2. In **Gruppenadressen** den obersten Eintrag rechtsklicken und **Gruppenadressen importieren** wählen.
3. [ets-import/gruppenadressen.csv](ets-import/gruppenadressen.csv) auswählen.
4. Danach Produktdatenbanken importieren, Geräte einfügen und die Kommunikationsobjekte verbinden.

Die vollständige, sichere Importreihenfolge steht in [ets-import/ETS_IMPORT.md](ets-import/ETS_IMPORT.md).

> Die Importdatei enthält nur die ETS-Gruppenadressstruktur. DPTs, physikalische Adressen und die Verknüpfung der Geräteobjekte werden bewusst getrennt gepflegt.

## Dateien

| Bereich | Inhalt |
|---|---|
| [docs/01_topologie.md](docs/01_topologie.md) | Linie und vorgeschlagene physikalische Adressen |
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

## ETS-Importdateien

| Datei | Verwendung |
|---|---|
| [ets-import/gruppenadressen.csv](ets-import/gruppenadressen.csv) | direkt in ETS importieren |
| [ets-import/gruppenadressen-planung.csv](ets-import/gruppenadressen-planung.csv) | DPT- und Planungsreferenz |
| [ets-import/physikalische-adressen.csv](ets-import/physikalische-adressen.csv) | Geräte- und Adresscheckliste |
| [ets-import/ETS_IMPORT.md](ets-import/ETS_IMPORT.md) | Importanleitung und Regeln |

## Planungsprinzip

- Grundfunktionen bleiben auf KNX: Licht, Beschattung, Heizung, Fenster- und Wetterschutz.
- Befehle und Rückmeldungen haben getrennte Gruppenadressen.
- Die Geräteobjekte und deren DPTs aus der jeweiligen Produktdatenbank sind verbindlich.
- Home Assistant darf ergänzen, aber keine Schutz- oder Grundfunktion voraussetzen.
