# 14 – Schaltschrank und Schutzkonzept

## Aufbau

Die KNX-Komponenten sind in einem separaten Verteilfeld mit ausreichender Platzreserve angeordnet. Die Installation wird in Funktionsgruppen gegliedert:

1. KNX-Infrastruktur und Reihenklemmen
2. Logik, Schaltuhr und Heizungsaktoren
3. Schalt- und Jalousieaktoren
4. Fehlerstromschutz und Leitungsschutz
5. KNX- und 24-V-Spannungsversorgungen
6. Reserve für DALI, RGBW und spätere Erweiterungen

## Schutzkonzept

Für die Endstromkreise sind zwei getrennte RCD-Gruppen vorgesehen. Jede Gruppe besteht aus einem vierpoligen Fehlerstrom-Schutzschalter mit **40 A Bemessungsstrom und 30 mA Bemessungsdifferenzstrom** sowie bis zu acht nachgeschalteten Leitungsschutzschaltern mit **B-Charakteristik und 16 A Bemessungsstrom**.

```text
RCD 1: 4-polig, 40 A, 30 mA
├── LS01 B16 A
├── LS02 B16 A
├── LS03 B16 A
├── LS04 B16 A
├── LS05 B16 A
├── LS06 B16 A
├── LS07 B16 A
└── LS08 B16 A

RCD 2: 4-polig, 40 A, 30 mA
├── LS09 B16 A
├── LS10 B16 A
├── LS11 B16 A
├── LS12 B16 A
├── LS13 B16 A
├── LS14 B16 A
├── LS15 B16 A
└── LS16 B16 A
```

Die B16-A-Absicherung ist der dokumentierte Planungsstand. Vor Inbetriebnahme müssen Leitungstyp, Leiterquerschnitt, Verlegeart, Leitungslänge, Spannungsfall, Schleifenimpedanz, Kurzschlussstrom und die zulässige Belastung der angeschlossenen Aktoren geprüft werden. Die 40-A-RCDs müssen durch die vorgeschaltete Absicherung beziehungsweise durch die Auslegung der Anlage gegen Überlast geschützt sein.

## Wichtige Verdrahtungsregeln

- Jeder RCD erhält eine eigene Neutralleiterschiene.
- Neutralleiter verschiedener RCD-Gruppen dürfen hinter den RCDs nicht verbunden werden.
- Außenleiter und zugehöriger Neutralleiter müssen immer derselben RCD-Gruppe zugeordnet sein.
- Die Phasen L1, L2 und L3 werden möglichst gleichmäßig belastet.
- Ein Aktorkanal ist nicht automatisch ein eigener Stromkreis.
- Mehrere Aktorkanäle dürfen nur gemeinsam abgesichert werden, wenn sie tatsächlich zum selben Endstromkreis gehören.
- Die maximale Kontaktbelastung und zulässige Einspeisegruppe des jeweiligen Aktors ist zu beachten.
- KNX-Busleitung, 24-V-Leitungen und 230-V-Leitungen werden entsprechend den geltenden Trennungs- und Installationsregeln geführt.

## Funktionsgruppen im Schaltschrank

### KNX-Infrastruktur

- Enertex KNX PowerSupply 960³
- MDT SCN-IP100.03 IP Router für die Wohnhauslinie
- zweiter MDT SCN-IP100.03 als Reserve für eine spätere Außenlinie
- MDT VC-EASY.02 VisuControl Easy
- MDT SCN-SAFE.01 Sicherheitsmodul
- MDT SCN-LOG1.02 Logikmodul
- MDT SCN-RTC20.01 Zeitschaltuhr

### Aktoren

- MDT AKS-2416.03 Schaltaktor 24-fach
- MDT JAL-0810M.02 Jalousieaktor 8-fach
- zwei MDT AKH-0800.02 Heizungsaktoren 8-fach

### Hilfsspannungen

- KNX-Busspannungsversorgung
- EARU DR-30-24, 24 V DC, als Zusatzversorgung der Gira Wetterstation vorgesehen

## Reserve

Freie Teilungseinheiten und mindestens zwei unbenutzte Leitungsschutzschalter bleiben für spätere Erweiterungen vorgesehen. Reservekanäle werden nicht mit einer konkreten Funktion beschriftet, bevor die zugehörige Leitung festgelegt und geprüft wurde.
