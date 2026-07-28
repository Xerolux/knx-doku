# 01 – KNX-Topologie

## Aktueller Aufbau

Das ETS-Projekt verwendet aktuell eine aktive TP-Linie mit einem automatisch angelegten RF-Segment. Eine zusätzliche TP-Außenlinie bleibt als Zukunftsreserve bestehen.

```text
0.0 IP Backbone
└── 1.0 IP Hauptlinie
    ├── 1.1 TP Hauptlinie
    │   └── RF Segment 1
    └── 1.3 TP Außen (Reserve)
```

Die Linie **1.1** enthält die vorhandenen REG-Geräte, Sensoren und Bedienstellen. Der Gira RF Multi/TP Medienkoppler erzeugt in ETS automatisch das RF-Segment unterhalb der TP-Linie. Eine separate Linie 1.2 wird deshalb nicht verwendet.

Die Linie **1.3** bleibt vorerst leer. Wetterstation, Rauchwarnmelder-KNX-Modul und andere bereits vorhandene Geräte liegen bis zu einem späteren Ausbau weiterhin auf Linie 1.1.

## Aktuell angelegte Geräte

```text
1.1.0   MDT SCN-IP100.03 IP Router Secure
1.1.1   Enertex KNX PowerSupply 960
1.1.2   Gira 5114 00 RF Multi/TP Medienkoppler
1.1.3   MDT AKS-2416.03 Schaltaktor 24-fach
1.1.4   MDT JAL-0810M.02 Jalousieaktor 8-fach
1.1.5   MDT AKH-0800.02 Heizungsaktor 8-fach – Gerät 1
1.1.6   MDT AKH-0800.02 Heizungsaktor 8-fach – Gerät 2
1.1.7   MDT SCN-RTC20.01 Schaltuhr
1.1.8   MDT SCN-LOG1.02 Logikmodul
1.1.9   MDT SCN-SAFE.01 Sicherheitsmodul
1.1.10  MDT VC-EASY.02 VisuControl Easy II
1.1.20  MDT Glastaster II Smart mit Temperatursensor – Eingang
1.1.21–1.1.28  weitere MDT Glastaster II Smart mit Temperatursensor
1.1.29  MDT Glastaster II Smart – Programmierstand prüfen
1.1.30  MDT Präsenzmelder 360° KLR 4S
1.1.31  MDT SCN-IP100.03 E-Mail- und Zeitserver-Applikation
1.1.40  Gira Wetterstation Plus – ETS-Applikation B00D21
1.1.41  Gira KNX Rauchwarnmelder – ETS-Applikation C01602
```

Die Adresse `1.1.31` gehört zur zusätzlichen E-Mail- und Zeitserver-Applikation eines vorhandenen MDT SCN-IP100.03. Diese Applikation besitzt eine eigene physikalische Adresse, obwohl sie auf demselben realen Gerät wie die Router-Applikation laufen kann.

## KNX RF

Der Gira 5114 00 verbindet KNX TP und KNX RF. ETS legt dafür automatisch **RF Segment 1** unterhalb der Linie 1.1 an.

RF-Geräte werden direkt in dieses RF-Segment eingefügt. Ihre konkrete physikalische Adresse wird bei der Inbetriebnahme in ETS festgelegt. Eine eigene manuelle Linie 1.2 ist nicht erforderlich.

## Linie 1.3 – Außenbereich / Reserve

Die Außenlinie wird aktuell nicht bestückt. Sie ist für einen späteren Ausbau vorgesehen, etwa für:

```text
- separate Außenaktoren
- Garage oder Gartenhaus
- Tor- und Türsteuerung
- Außenmelder
- zusätzliche Wetter- oder Umweltsensorik
```

Bei tatsächlichem Ausbau benötigt die Linie einen passenden Linienkoppler und eine eigene KNX-Busspannungsversorgung. Außenleitungen müssen zusätzlich hinsichtlich Überspannungsschutz, Leitungsführung und Potentialausgleich geplant werden.

## Adresskonventionen

- `1.1.0`: Router-Applikation des MDT IP-Routers.
- `1.1.1–1.1.19`: Infrastruktur, REG-Geräte, Aktoren und Systemmodule.
- `1.1.20–1.1.30`: Innenraumsensoren und Bedienstellen.
- `1.1.31`: festgelegte Zusatzapplikation für E-Mail und NTP-Zeitserver.
- `1.1.32–1.1.39`: Reserve für weitere Innenraumsensoren und Bedienstellen.
- `1.1.40–1.1.59`: Wetter-, Sicherheits- und Außengeräte, solange keine eigene Außenlinie verwendet wird.
- `1.3.x`: ausschließlich für den späteren Ausbau der TP-Außenlinie.
- Physikalische Adressen werden nicht doppelt vergeben.
- Das ETS-Projekt ist die verbindliche Quelle für die tatsächlich programmierten Adressen.
