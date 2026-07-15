# 15 – Stromkreise, RCD- und LS-Zuordnung

> Planungsstand: Die Schutzorgane sind mit 40 A / 30 mA für die RCDs und B16 A für die nachgeschalteten Leitungsschutzschalter festgelegt. Die tatsächliche Zuordnung ist bei der Verdrahtung und Messung vor Ort zu bestätigen.

## RCD 1 – Beleuchtung

**RCD 1: 4-polig, 40 A, 30 mA**

| Kennzeichnung | Schutz | Phase | Funktion | Aktor / Kanal | Bemerkung |
|---|---|---|---|---|---|
| LS01 | B16 A | L1 | Licht Wohnzimmer | MDT AKS-2416.03 / A | eigener Endstromkreis |
| LS02 | B16 A | L2 | Licht Esszimmer | MDT AKS-2416.03 / B | eigener Endstromkreis |
| LS03 | B16 A | L3 | Licht Küche | MDT AKS-2416.03 / C | eigener Endstromkreis |
| LS04 | B16 A | L1 | Licht Arbeitszimmer | MDT AKS-2416.03 / D | eigener Endstromkreis |
| LS05 | B16 A | L2 | Licht Gang | MDT AKS-2416.03 / E | eigener Endstromkreis |
| LS06 | B16 A | L3 | Licht Schlafzimmer | MDT AKS-2416.03 / F | eigener Endstromkreis |
| LS07 | B16 A | L1 | Licht Badezimmer | MDT AKS-2416.03 / G | eigener Endstromkreis |
| LS08 | B16 A | L2 | Licht Bad vorne | MDT AKS-2416.03 / H | eigener Endstromkreis |

## RCD 2 – Beschattung, Heizung und Technik

**RCD 2: 4-polig, 40 A, 30 mA**

| Kennzeichnung | Schutz | Phase | Funktion | Aktor / Kanal | Bemerkung |
|---|---|---|---|---|---|
| LS09 | B16 A | L1 | Rollläden Wohnbereich | MDT JAL-0810M.02 / A–C | endgültige Einspeisegruppe prüfen |
| LS10 | B16 A | L2 | Rollläden Schlafbereich | MDT JAL-0810M.02 / D–F | endgültige Einspeisegruppe prüfen |
| LS11 | B16 A | L3 | Markise | MDT JAL-0810M.02 / G | separater Stromkreis |
| LS12 | B16 A | L1 | Heizungsaktor 1 | MDT AKH-0800.02 / 1–8 | Ventilspannung und Last prüfen |
| LS13 | B16 A | L2 | Heizungsaktor 2 | MDT AKH-0800.02 / 1–8 | zweite Heizkreisgruppe |
| LS14 | B16 A | L3 | KNX-Infrastruktur | Enertex, Router, Visu, Logik, Uhr | gemeinsame Versorgung prüfen |
| LS15 | B16 A | L1 | 24-V-Netzteil Wetterstation | EARU DR-30-24 / Gira Wetterstation | Sekundärkreis dokumentieren |
| LS16 | B16 A | L2 | Reserve | noch nicht belegt | frei lassen und abdecken |

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
| A | Wohnzimmer | LS01 B16 A |
| B | Esszimmer | LS02 B16 A |
| C | Küche | LS03 B16 A |
| D | Arbeitszimmer | LS04 B16 A |
| E | Gang | LS05 B16 A |
| F | Schlafzimmer | LS06 B16 A |
| G | Badezimmer | LS07 B16 A |
| H | Bad vorne | LS08 B16 A |
| I–X | Reserve / spätere Lichtgruppen | noch festzulegen |

## Technische Prüfung

Die B16-A-Absicherung setzt voraus, dass Leitung, Querschnitt, Verlegeart, Spannungsfall, Abschaltbedingungen und die angeschlossenen Aktoren dafür geeignet sind. Ebenso ist sicherzustellen, dass die 40-A-RCDs durch die vorgeschaltete Absicherung beziehungsweise durch die Anlagenauslegung nicht überlastet werden.

## Vor Ort zu ergänzende Daten

Für jeden Stromkreis sind nach Abschluss einzutragen:

- Leitungstyp und Querschnitt
- Leitungslänge
- Verlegeart
- gemessene Schleifenimpedanz
- Isolationswiderstand
- RCD-Auslösezeit und Auslösestrom
- verwendete Aktoreinspeisung
- Klemmen- und Kabelnummer
