# 16 – Beschriftungskonzept

## Ziel

Alle Betriebsmittel, Leitungen, Klemmen und Aktorkanäle erhalten eine eindeutige, dauerhafte und in der Dokumentation identische Kennzeichnung.

## Schutzorgane

```text
RCD1  Beleuchtung
LS01  Licht Wohnzimmer
LS02  Licht Esszimmer
LS03  Licht Küche
LS04  Licht Arbeitszimmer
LS05  Licht Gang
LS06  Licht Schlafzimmer
LS07  Licht Badezimmer
LS08  Licht Bad vorne

RCD2  Beschattung / Heizung / Technik
LS09  Rollläden Wohnbereich
LS10  Rollläden Schlafbereich
LS11  Markise
LS12  Heizungsaktor 1
LS13  Heizungsaktor 2
LS14  KNX-Infrastruktur
LS15  Netzteil 24 V DC
LS16  Reserve
```

## KNX-Gerätekennzeichnung

| Kürzel | Gerät |
|---|---|
| KNX-PS1 | Enertex KNX PowerSupply 960³ |
| KNX-IP1 | MDT SCN-IP100.03 IP Router 1 |
| KNX-IP2 | MDT SCN-IP100.03 IP Router 2, Funktion noch festzulegen |
| KNX-VC1 | MDT VC-EASY.02 VisuControl Easy |
| KNX-SAFE1 | MDT SCN-SAFE.01 Sicherheitsmodul |
| KNX-LOG1 | MDT SCN-LOG1.02 Logikmodul |
| KNX-RTC1 | MDT SCN-RTC20.01 Zeitschaltuhr |
| KNX-AKS1 | MDT AKS-2416.03 Schaltaktor |
| KNX-JAL1 | MDT JAL-0810M.02 Jalousieaktor |
| KNX-AKH1 | MDT AKH-0800.02 Heizungsaktor 1 |
| KNX-AKH2 | MDT AKH-0800.02 Heizungsaktor 2 |
| PS-24V1 | EARU DR-30-24 Netzteil |

## Aktorkanäle

Beschriftung direkt am Gerät und an der zugehörigen Abgangsklemme:

```text
KNX-AKS1-A   Licht Wohnzimmer
KNX-AKS1-B   Licht Esszimmer
KNX-AKS1-C   Licht Küche
KNX-AKS1-D   Licht Arbeitszimmer
KNX-AKS1-E   Licht Gang
KNX-AKS1-F   Licht Schlafzimmer
KNX-AKS1-G   Licht Badezimmer
KNX-AKS1-H   Licht Bad vorne
```

```text
KNX-JAL1-A   Rollladen Wohnzimmer links
KNX-JAL1-B   Rollladen Wohnzimmer rechts
KNX-JAL1-C   Rollladen Arbeitszimmer
KNX-JAL1-D   Rollladen Schlafzimmer links
KNX-JAL1-E   Rollladen Schlafzimmer rechts
KNX-JAL1-F   Rollladen Badezimmer
KNX-JAL1-G   Markise
KNX-JAL1-H   Reserve
```

## Heizkreise

```text
KNX-AKH1-01  Wohnzimmer
KNX-AKH1-02  Esszimmer
KNX-AKH1-03  Küche
KNX-AKH1-04  Arbeitszimmer
KNX-AKH1-05  Gang
KNX-AKH1-06  Schlafzimmer
KNX-AKH1-07  Badezimmer
KNX-AKH1-08  Bad vorne

KNX-AKH2-01 bis KNX-AKH2-08  Reserve / vor Ort zu erfassen
```

## Klemmen

Empfohlenes Schema:

```text
X1   Lichtabgänge
X2   Rollladen- und Markisenabgänge
X3   Heizungsabgänge
X4   KNX-Bus
X5   24 V DC
X6   Reserve
```

Einzelklemmen werden fortlaufend bezeichnet, beispielsweise `X1:01`, `X1:02` und `X1:03`. Die gleiche Kennzeichnung steht im Stromlaufplan, an der Klemme und am Leiter.

## Kabelkennzeichnung

Empfohlenes Format:

```text
Ziel-Funktion / Stromkreis / laufende Nummer
```

Beispiele:

```text
WO-LICHT / LS01 / 01
KUE-LICHT / LS03 / 01
WZ-ROLL-L / LS09 / 01
BAD-HK / LS12 / 07
```

Beide Leitungsenden sind zu kennzeichnen. Handschriftliche Provisorien werden vor der Abnahme durch dauerhafte Beschriftungen ersetzt.
