# 01 – KNX-Topologie

## Aktueller Aufbau

Das ETS-Projekt verwendet aktuell eine aktive TP-Linie mit einem automatisch angelegten RF-Segment. Eine zusätzliche TP-Außenlinie bleibt als Zukunftsreserve bestehen.

```text
0.0 IP Backbone
└── 1.0 IP Hauptlinie
    ├── 1.1 TP Hauptlinie
    │   └── 1.1 RF Segment 1
    └── 1.3 TP Außen (Reserve)
```

Die Linie **1.1** enthält die aktuell vorhandenen REG-Geräte, Sensoren und Bedienstellen. Der Gira RF Multi/TP Medienkoppler erzeugt in ETS automatisch das RF-Segment unterhalb der TP-Linie. Eine separate Linie 1.2 wird deshalb nicht verwendet.

Die Linie **1.3** bleibt vorerst leer. Wetterstation und andere bereits vorhandene Außengeräte liegen bis zu einem späteren Ausbau weiterhin auf Linie 1.1.

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
1.1.40  Gira 2074 00 Wetterstation Plus
```

Weitere Geräte werden erst ergänzt, wenn sie tatsächlich vorhanden oder eindeutig festgelegt sind.

## KNX RF

Der Gira 5114 00 verbindet KNX TP und KNX RF. ETS legt dafür automatisch **RF Segment 1** unterhalb der Linie 1.1 an.

RF-Geräte werden später direkt in dieses RF-Segment eingefügt. Ihre konkrete physikalische Adresse wird erst bei der Inbetriebnahme in ETS festgelegt. Eine eigene manuelle Linie 1.2 ist nicht erforderlich.

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

- `1.1.0`: Koppler-/Routeradresse des MDT IP-Routers.
- `1.1.1–1.1.19`: Infrastruktur, REG-Geräte, Aktoren und Systemmodule.
- `1.1.20–1.1.39`: Reserve für weitere Innenraumsensoren und Bedienstellen.
- `1.1.40–1.1.59`: Wetter- und Außengeräte, solange keine eigene Außenlinie verwendet wird.
- `1.3.x`: ausschließlich für den späteren Ausbau der TP-Außenlinie.
- Physikalische Adressen werden nicht doppelt vergeben.
- Das ETS-Projekt ist die verbindliche Quelle für die tatsächlich programmierten Adressen.
