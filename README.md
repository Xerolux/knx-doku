# KNX-Dokumentation Xerolux

Planungs- und Inbetriebnahmedokumentation für die KNX-Installation des Wohnhauses. Der Schwerpunkt liegt auf einer autarken KNX-Grundfunktion; Home Assistant ergänzt Visualisierung, Auswertungen und Komfortautomationen.

## Schnellstart für ETS 6

Die Gruppenadressen können im nativen XML-Format in ein ETS-Projekt mit **3-Ebenen-Gruppenadressstil** importiert werden:

1. Projekt in ETS anlegen oder öffnen.
2. In **Gruppenadressen** den obersten Eintrag rechtsklicken und **Gruppenadressen importieren** wählen.
3. Bei einem neuen Projekt [ets-import/gruppenadressen-komplett.xml](ets-import/gruppenadressen-komplett.xml) importieren. Ist eine ältere Komplettdatei bereits im Projekt, nur die benötigte, vorher geprüfte Ergänzungs- oder Reparaturdatei importieren.
4. Erst bei Inbetriebnahme der KNX-Bridge für die IDM-Wärmepumpe zusätzlich [ets-import/gruppenadressen-waermepumpe.xml](ets-import/gruppenadressen-waermepumpe.xml) importieren.
5. Die jeweiligen Importberichte und vorhandenen Adressen prüfen.
6. Anschließend Produktdatenbanken einfügen, Geräte anlegen und Kommunikationsobjekte verbinden.

Die Wärmepumpe liegt in einer eigenen Datei: [ets-import/gruppenadressen-waermepumpe.xml](ets-import/gruppenadressen-waermepumpe.xml) mit 43 Adressen auf Hauptgruppe `11`. Die Struktur wurde inzwischen zusätzlich zur Basisstruktur in ETS importiert; Einzeladressen, DPTs und Verknüpfungen müssen noch per Detailansicht oder ETS-Export bestätigt werden. Siehe [docs/25_idm_waermepumpe_knx.md](docs/25_idm_waermepumpe_knx.md).

Die Komplettdatei enthält 176 vorgesehene Basis-Gruppenadressen einschließlich der sechs Gang-Adressen, der zwei Abstellkammer-Lichtadressen, der sechs SCN-SAFE-Adressen und der getrennten Rauchwarnmelder-Planung. Zusammen mit den 43 separat gepflegten Wärmepumpen-Adressen umfasst der geplante Importstand 219 Gruppenadressen. Die bisherigen Basis-Einzeldateien dienen nur der modularen Pflege und werden nicht zusätzlich importiert. Einzelheiten stehen in [ets-import/ETS_IMPORT.md](ets-import/ETS_IMPORT.md).

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
| [docs/26_scn_safe_adressreparatur.md](docs/26_scn_safe_adressreparatur.md) | SCN-SAFE-Zuordnung, Adresskollision vom 29.08.2026 und Reparaturverfahren |
| [docs/27_fbh_mdt_raumregelung.md](docs/27_fbh_mdt_raumregelung.md) | live eingerichtete MDT-FBH-Bedienung, HA-Regler und offene Pumpenfrage |
| [docs/28_ets_bad_vorne_pm_2026-10-14.md](docs/28_ets_bad_vorne_pm_2026-10-14.md) | ETS-Protokoll Lichtverknüpfung Bad vorne und reduzierte HF-Reichweiten Küche/Bad |
| [docs/29_google_assistant_etagensteuerung.md](docs/29_google_assistant_etagensteuerung.md) | Google-Etagenziele für Licht/Rollläden und separate Einzelbefehle für Sondergeräte |
| [docs/30_google_knx_pruefung_2026-10-16.md](docs/30_google_knx_pruefung_2026-10-16.md) | ETS-Downloads, KNX-Verbindung und Diagnose der Google-Sprachstörung |
| [docs/31_glastaster_display_nacht.md](docs/31_glastaster_display_nacht.md) | KNX-Displayumschaltung aller elf MDT-Glastaster um 20:00/07:30 Uhr |
| [docs/32_wetter_fenster_inbetriebnahme_2026-10-16.md](docs/32_wetter_fenster_inbetriebnahme_2026-10-16.md) | Sitzungsprotokoll Wetter-Dashboard, Fensterdiagnose, Secure-Tunnel und offene Abnahme |
| [docs/33_markise_eg_wetterschutz.md](docs/33_markise_eg_wetterschutz.md) | Direkter KNX-Wind-/Regenschutz ausschließlich der EG-Markise |
| [docs/34_abstellkammer_zentral_bad_2026-10-18.md](docs/34_abstellkammer_zentral_bad_2026-10-18.md) | Abstellkammer, Zentralfunktionen und Badrollladen |
| [docs/35_raumzuordnung_ets_2026-10-18.md](docs/35_raumzuordnung_ets_2026-10-18.md) | Gerätezuordnung zu Räumen und Bereichen in ETS |
| [docs/36_ha_vollstaendigkeit_2026-10-18.md](docs/36_ha_vollstaendigkeit_2026-10-18.md) | Badlicht, Badrollladen und Vollständigkeit des EG-Dashboards |
| [docs/37_knx_sollwert_http_warnungen_2026-10-19.md](docs/37_knx_sollwert_http_warnungen_2026-10-19.md) | AKH-Leseantworten korrigiert und HTTP-Filterprüfung dokumentiert |
| [docs/38_mdt_glas_heizmodi_2026-10-19.md](docs/38_mdt_glas_heizmodi_2026-10-19.md) | Heizmodi an sechs Glastastern geladen, Aktorrückmeldungen und Frostschutz am Bus geprüft |

## Home Assistant

Die aktuelle Lovelace-Konfiguration liegt unter:

```text
home-assistant/lovelace_knx_eg.yaml
```

Sie verwendet `custom:button-card` und enthält fünf Reiter:

- Licht
- Rollläden
- Heizung
- Raumklima
- Fenster

Dokumentiert sind sechs einzelne Rollläden und eine Markise, neun einzelne Lichtkreise sowie die gemeinsame Ganglichtfunktion. Das Heizungsdashboard enthält sechs MDT-Raumregler, sechs AKH-Sollwertsensoren und drei vorhandene Klimaentitäten aus dem Altbestand. Die Rollladenkarten zeigen Position und Zustand; die eigentliche Bedienung erfolgt nach dem Anklicken im Dialog **Mehr Informationen**. Die lokale Dashboardvorlage und der live geprüfte Stand sind in [Dokument 36](docs/36_ha_vollstaendigkeit_2026-10-18.md) abgeglichen.

## Aktueller Stand

- Heizungsaktoren `1.1.5` und `1.1.6`: sechs MDT-Raumregelzonen und HA-Regler eingerichtet; [Raumregelung](docs/27_fbh_mdt_raumregelung.md). Basis-Sollwert-Leseantworten am 19.10.2026 korrigiert und für alle sechs Räume bestätigt; [Prüfung 37](docs/37_knx_sollwert_http_warnungen_2026-10-19.md). Anschließend Heizmodus-Bedienung an sechs Glastastern und beide Aktoren erfolgreich geladen, Frostschutz mit 7 °C am Bus geprüft; [Prüfung 38](docs/38_mdt_glas_heizmodi_2026-10-19.md). Physische Heizmodus-Tastenbedienung und Pumpenabstimmung bleiben offen.

- Schaltaktor `1.1.3`: bestätigte Lichtkanäle A bis F dokumentiert.
- Gang: zwei getrennte Lichtkreise mit Einzeladressen und gemeinsamer Adresse `1/4/4`.
- Bewegungsmelder `1.1.30`: schaltet beide Ganglichter über `1/4/4`.
- Gemeinsamer Ganglichtstatus `1/4/5`: ODER-Logik in Funktion F1 des Logikmoduls `1.1.8`; Leseantwort und Statuswechsel am 19.10.2026 am Bus bestätigt. Ganglichtkorrektur mit zeitgesteuerten Aktorkanälen und Melder-Nachtriggerung: zwei echte EIN-/AUS-Zyklen einschließlich Wiederanlauf nach abschließender Korrektur bestanden. [Diagnose und Prüfstand](docs/21_ganglicht_bewegungsmelder.md).
- Jalousieaktor `1.1.4`, Kanal E Bad: Einzeladressen `2/3/0`, `2/3/1`, `2/3/3`, Zentralteilnahme nur Auf/Ab und Applikationsdownload am 18.10.2026 bestätigt. Automatische Fahrzeitmessung ergab 23 s aufwärts / 26 s abwärts mit beiden Endlagenrückmeldungen; absolute Positions-Sendeadresse bleibt frei. [Messprotokoll 34](docs/34_abstellkammer_zentral_bad_2026-10-18.md), [HA-Ergänzung 36](docs/36_ha_vollstaendigkeit_2026-10-18.md). Physische Sichtprüfung und Zwischenposition bleiben offen.
- Zentral Rollladen: `0/1/0` für Auf/Ab und `0/1/1` für Stopp.
- Home Assistant: Licht-, Rollladen- und Markisenentitäten angelegt; Live-Dashboard `Übersicht → IOT` zeigt jetzt die sieben Raumklimawerte der Küche. Live-IDs und geprüfte Momentwerte stehen in Dokument 23.
- OpenKNX RaumController `1.1.29`: sieben Raumklimaobjekte verbunden und am 17.08.2026 erfolgreich im Gruppenmonitor geprüft; VOC und Helligkeit lieferten beim Test noch `0`.
- Küchen-Glastaster `1.1.22`: Anzeige-Parameter und Gruppenadressverknüpfungen für Feuchte (`13/0/1`), berechnetes CO2-VOC (`13/0/5`) und echtes CO2 (`13/0/4`) sind projektiert. Der rohe VOC-DPT passt zu keinem auswählbaren numerischen MDT-Statuswert. Applikation zuletzt am 19.10.2026 für die Heizmodus-Bedienung geladen, vorhandene Raumklimaobjekte erhalten; deren Anzeige am physischen Taster bleibt offen.
- Glastaster `1.1.21 Eingang Gang`: Objekt 108 `Temperaturmesswert` → `3/4/1 Gang Isttemperatur` (DPT 9.001). Temperaturquelle und Raumregelung live geprüft, Applikation zuletzt am 19.10.2026 für die Heizmodus-Bedienung geladen. [Raumregelung](docs/27_fbh_mdt_raumregelung.md), [Heizmodi](docs/38_mdt_glas_heizmodi_2026-10-19.md).
- ETS-Gebäudezuordnung am 18.10.2026: 45 Geräte in 14 Räumen/Bereichen; alle Geräte zugeordnet, `1.1.32` Bad und `1.1.33` Bad Gang. Enertex und Rauchmelder-Eintrag im Technikraum, Gira-Medienkoppler im EG Gang und Wetterstation unter Dach / Außenbereich; siehe [35 – Raumzuordnung](docs/35_raumzuordnung_ets_2026-10-18.md).
- Wetterstation `1.1.40`: am 16.10.2026 mit B00D29 programmiert, 33 Mess-/Diagnoseausgänge in HA und eigenem Wetter-Dashboard eingebunden. Interne Beschattungssteuerung deaktiviert; später ausschließlich EG-Markise mit direktem Wind-/Regenschutz verbunden, Alarmrichtung Ab und keine Fahrt bei Alarmende. Stand in [33 – EG-Markise](docs/33_markise_eg_wetterschutz.md); Details und Nachweisgrenzen in [11 – Wetterstation](docs/11_wetterstation_gira.md).
- Gruppenadress-Iststand vom 29.08.2026 nach dem Zusatzimport: Hauptgruppen `0` bis `11` sowie `13`; unter `11 Wärmepumpe` sind die Mittelgruppen `11/0`, `11/1` und `11/3` sichtbar. Die 43 Einzeladressen und DPTs sind noch durch einen ETS-Export zu bestätigen.
- Sicherheitsbereich: MDT SCN-SAFE liegt ausschließlich unter `10/0`; die noch nicht in Betrieb genommene Rauchwarnmelder-Planung liegt ausschließlich unter `10/1`. Die versehentliche Namenskollision wurde repariert und als Vorfall dokumentiert.
- Raumstand: neun getrennte Räume. Die Abstellkammer ist weder Badezimmer noch Bad vorne und erhält ausschließlich `12/0/0` und `12/0/1` unter `12 Licht Erweiterung`.
- Der ETS-Suchordner zeigt 117 Einträge unter „Addresses not assigned“. Diese Zahl ist kein Gesamtzähler aller angelegten Gruppenadressen.
- Positionsstatus und Fahrzeitmessung müssen für zuverlässige Prozentwerte vollständig funktionieren.
- ETS zeigt für geänderte Geräte **Programmieren notwendig**; die betroffenen Geräte sind in Dokument 22 aufgeführt.

## ETS-Importdateien

| Datei | Verwendung |
|---|---|
| [ets-import/gruppenadressen-komplett.xml](ets-import/gruppenadressen-komplett.xml) | empfohlener Ein-Datei-Import aller 176 Basis-Gruppenadressen mit DPTs |
| [ets-import/gruppenadressen.xml](ets-import/gruppenadressen.xml) | Grundstruktur für ETS 6 |
| [ets-import/gruppenadressen-abstellkammer.xml](ets-import/gruppenadressen-abstellkammer.xml) | einmaliger Zusatzimport für `12 Licht Erweiterung / 12/0 Abstellkammer` |
| [ets-import/gruppenadressen-zentral-zeit.xml](ets-import/gruppenadressen-zentral-zeit.xml) | Ergänzung für `0/4/0` und `0/5/0` bis `0/5/2` |
| [ets-import/gruppenadressen-sicherheit.xml](ets-import/gruppenadressen-sicherheit.xml) | SCN-SAFE auf `10/0` und getrennte Rauchwarnmelder-Planung auf `10/1` |
| [ets-import/gruppenadressen-reparatur-safe-rauchwarnmelder.xml](ets-import/gruppenadressen-reparatur-safe-rauchwarnmelder.xml) | einmalige Reparaturdatei nach der Adresskollision vom 29.08.2026 |
| [ets-import/gruppenadressen-raumcontroller.xml](ets-import/gruppenadressen-raumcontroller.xml) | Ergänzung für die Messwerte des OpenKNX RaumControllers `1.1.29` |
| [ets-import/gruppenadressen-waermepumpe.xml](ets-import/gruppenadressen-waermepumpe.xml) | zusätzlicher Import von 43 IDM-Wärmepumpen-Adressen in Hauptgruppe `11` |
| [ets-import/gruppenadressen-planung.csv](ets-import/gruppenadressen-planung.csv) | DPT- und Planungsreferenz der Grundstruktur |
| [ets-import/gruppenadressen-zentral-zeit-planung.csv](ets-import/gruppenadressen-zentral-zeit-planung.csv) | DPT-Referenz für Zentral Licht sowie Zeit und Datum |
| [ets-import/gruppenadressen-sicherheit-planung.csv](ets-import/gruppenadressen-sicherheit-planung.csv) | DPT-Referenz für Rauchwarnmelder und Sicherheitsmeldungen |
| [ets-import/gruppenadressen-raumcontroller-planung.csv](ets-import/gruppenadressen-raumcontroller-planung.csv) | DPT- und Objektzuordnung des OpenKNX RaumControllers |
| [ets-import/gruppenadressen-waermepumpe.csv](ets-import/gruppenadressen-waermepumpe.csv) | DPT-, Objekt- und Richtungsreferenz der IDM-Wärmepumpen-Adressen |
| [ets-import/physikalische-adressen.csv](ets-import/physikalische-adressen.csv) | Geräte- und Adresscheckliste |
| [ets-import/ETS_IMPORT.md](ets-import/ETS_IMPORT.md) | Importanleitung, Topologie und Regeln |

Die Importdateien werden lokal und bei jedem relevanten GitHub-Push mit [scripts/validate-group-addresses.ps1](scripts/validate-group-addresses.ps1) auf doppelte Adressen, Namens-/DPT-Konflikte und die feste Trennung von SCN-SAFE und Rauchwarnmelder geprüft.

Aktuelle Änderungen vom 18.10.2026: [Abstellkammer, Zentralfunktionen und Badrollladen](docs/34_abstellkammer_zentral_bad_2026-10-18.md).

HA-Vollständigkeitsprüfung vom 18.10.2026: [Badlicht und Badrollladen live ergänzt; Licht, Rollläden und Heizung abgeglichen](docs/36_ha_vollstaendigkeit_2026-10-18.md). Offene Zuordnungen und die noch ausstehende Live-Übernahme der korrigierten Etagen-Sammellisten sind dort getrennt aufgeführt.

## Home-Assistant-Dateien

| Datei | Verwendung |
|---|---|
| [home-assistant/lovelace_knx_eg.yaml](home-assistant/lovelace_knx_eg.yaml) | Lovelace-Dashboard für Licht, Rollläden, Heizung, Raumklima und Fenster |
| [home-assistant/knx_fenstergriffe_eg.yaml](home-assistant/knx_fenstergriffe_eg.yaml) | Live geladenes Paket für zwölf MDT-Fenstergriffe; Bad vorne noch ohne abgeschlossene Inbetriebnahme |
| [home-assistant/lovelace_fenster_eg_view.yaml](home-assistant/lovelace_fenster_eg_view.yaml) | Ergänzender EG-Fensterreiter mit bestätigten Stellungsanzeigen |
| [home-assistant/knx_abstellkammer_licht.yaml](home-assistant/knx_abstellkammer_licht.yaml) | YAML-Alternative zur live angelegten Abstellkammer-Leuchte; nicht doppelt laden |
| [home-assistant/knx_raumcontroller.yaml](home-assistant/knx_raumcontroller.yaml) | einbindbare KNX-Sensorliste für den OpenKNX RaumController |

## Planungsprinzip

- Grundfunktionen bleiben auf KNX.
- Befehle und Rückmeldungen erhalten getrennte Gruppenadressen.
- Ein gemeinsamer Status mehrerer Verbraucher wird durch genau eine Logik erzeugt.
- Gerätebezeichnungen, Gruppenadressennamen und reale Verdrahtung werden miteinander abgeglichen.
- Home Assistant ist keine Voraussetzung für Licht, Beschattung oder Schutzfunktionen.

## Datenschutz und Geheimnisse

Dieses öffentliche Repository enthält keine Passwörter, PINs, Tokens, Schlüsselbunddateien, privaten ETS-Projektdateien, Fotos oder Screenshots der Anlage.
