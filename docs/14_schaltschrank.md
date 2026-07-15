# 14 – Schaltschrank und Schutzkonzept

## Aufbau

Die KNX-Komponenten sind in einem separaten Verteilfeld mit ausreichender Platzreserve angeordnet. Die Installation wird in Funktionsgruppen gegliedert:

1. KNX-Infrastruktur und Reihenklemmen
2. Logik, Schaltuhr und Heizungsaktoren
3. Schalt- und Jalousieaktoren
4. Fehlerstromschutz und Leitungsschutz
5. KNX- und 24-V-Spannungsversorgungen
6. Reserve für DALI, RGBW und spätere Erweiterungen

## Vorgesehenes Schutzkonzept

Für die Endstromkreise sind zwei getrennte RCD-Gruppen vorgesehen. Jede Gruppe besteht aus einem vierpoligen Fehlerstrom-Schutzschalter und bis zu acht nachgeschalteten Leitungsschutzschaltern.

```text
RCD 1
├── LS01
├── LS02
├── LS03
├── LS04
├── LS05
├── LS06
├── LS07
└── LS08

RCD 2
├── LS09
├── LS10
├── LS11
├── LS12
├── LS13
├── LS14
├── LS15
└── LS16
```

Die endgültigen Bemessungswerte, Auslösecharakteristiken und Leiterquerschnitte müssen anhand der vorhandenen Geräte, Leitungen, Verlegearten, Schleifenimpedanzen und Herstellerangaben geprüft werden.

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
- MDT SCN-IP100.03 IP Router
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
- EARU DR-30-24, 24 V DC

## Reserve

Freie Teilungseinheiten und mindestens zwei unbenutzte Leitungsschutzschalter bleiben für spätere Erweiterungen vorgesehen. Reservekanäle werden nicht mit einer konkreten Funktion beschriftet, bevor die zugehörige Leitung festgelegt und geprüft wurde.
