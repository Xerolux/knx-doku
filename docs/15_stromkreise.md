# 15 – Stromkreise, RCD- und LS-Zuordnung

> Planungsstand: Vorschlag. Die tatsächliche Zuordnung ist bei der Verdrahtung und Messung vor Ort zu bestätigen.

## RCD 1 – Beleuchtung

| Kennzeichnung | Phase | Funktion | Aktor / Kanal | Bemerkung |
|---|---|---|---|---|
| LS01 | L1 | Licht Wohnzimmer | MDT AKS-2416.03 / A | eigener Endstromkreis |
| LS02 | L2 | Licht Esszimmer | MDT AKS-2416.03 / B | eigener Endstromkreis |
| LS03 | L3 | Licht Küche | MDT AKS-2416.03 / C | eigener Endstromkreis |
| LS04 | L1 | Licht Arbeitszimmer | MDT AKS-2416.03 / D | eigener Endstromkreis |
| LS05 | L2 | Licht Gang | MDT AKS-2416.03 / E | eigener Endstromkreis |
| LS06 | L3 | Licht Schlafzimmer | MDT AKS-2416.03 / F | eigener Endstromkreis |
| LS07 | L1 | Licht Badezimmer | MDT AKS-2416.03 / G | eigener Endstromkreis |
| LS08 | L2 | Licht Bad vorne | MDT AKS-2416.03 / H | eigener Endstromkreis |

## RCD 2 – Beschattung, Heizung und Technik

| Kennzeichnung | Phase | Funktion | Aktor / Kanal | Bemerkung |
|---|---|---|---|---|
| LS09 | L1 | Rollläden Wohnbereich | MDT JAL-0810M.02 / A–C | endgültige Einspeisegruppe prüfen |
| LS10 | L2 | Rollläden Schlafbereich | MDT JAL-0810M.02 / D–F | endgültige Einspeisegruppe prüfen |
| LS11 | L3 | Markise | MDT JAL-0810M.02 / G | separater Stromkreis empfohlen |
| LS12 | L1 | Heizungsaktor 1 | MDT AKH-0800.02 / 1–8 | Ventilspannung und Last prüfen |
| LS13 | L2 | Heizungsaktor 2 | MDT AKH-0800.02 / 1–8 | Reserve bzw. zweite Heizkreisgruppe |
| LS14 | L3 | KNX-Infrastruktur | Enertex, Router, Visu, Logik, Uhr | Versorgungskonzept prüfen |
| LS15 | L1 | 24-V-Netzteil | EARU DR-30-24 | Sekundärkreise getrennt dokumentieren |
| LS16 | L2 | Reserve | noch nicht belegt | frei lassen und abdecken |

## Phasenverteilung

Die tabellarische Phasenfolge ist ein Startvorschlag. Vor Inbetriebnahme sind die tatsächlichen Leistungen zu erfassen und die Phasen möglichst gleichmäßig zu verteilen.

```text
L1: LS01, LS04, LS07, LS09, LS12, LS15
L2: LS02, LS05, LS08, LS10, LS13, LS16
L3: LS03, LS06, LS11, LS14
```

## Zuordnung zu Aktorkanälen

Die Kanalbelegung des Schaltaktors ist zunächst auf die acht dokumentierten Räume begrenzt. Die Kanäle I bis X bleiben bis zur endgültigen Leitungszuordnung Reserve.

| Kanal | Funktion | Schutzorgan |
|---|---|---|
| A | Wohnzimmer | LS01 |
| B | Esszimmer | LS02 |
| C | Küche | LS03 |
| D | Arbeitszimmer | LS04 |
| E | Gang | LS05 |
| F | Schlafzimmer | LS06 |
| G | Badezimmer | LS07 |
| H | Bad vorne | LS08 |
| I–X | Reserve / spätere Lichtgruppen | noch festzulegen |

## Vor Ort zu ergänzende Daten

Für jeden Stromkreis sind nach Abschluss einzutragen:

- Leitungstyp und Querschnitt
- Leitungslänge
- Verlegeart
- Bemessungsstrom und Charakteristik des LS
- Bemessungsstrom, Typ und Auslösestrom des RCD
- gemessene Schleifenimpedanz
- Isolationswiderstand
- RCD-Auslösezeit und Auslösestrom
- verwendete Aktoreinspeisung
- Klemmen- und Kabelnummer
