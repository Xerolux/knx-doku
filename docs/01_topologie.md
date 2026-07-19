# 01 – KNX-Topologie

## Vorgesehene Linienstruktur

Für das Wohnhaus wird Bereich 1 mit drei logisch getrennten Linien vorgesehen:

```text
Bereich 1
├── Linie 1.1 KNX TP – Innenbereich und Hauptverteilung
├── Linie 1.2 KNX RF – Funkgeräte
└── Linie 1.3 KNX TP – Außenbereich / Reserve
```

Die Linie **1.1** enthält die zentralen REG-Geräte, Innenraumsensoren und Bedienstellen. Die Linie **1.2** ist die KNX-RF-Linie für Fenstergriffe und spätere Funkgeräte. Die Linie **1.3** ist für Außenanlagen, Garage, Gartenhaus, Tor, Außenbeleuchtung oder spätere Erweiterungen reserviert.

## Linienkoppler und Infrastruktur

```text
1.1.1   MDT STR-0640.01 Busspannungsversorgung Diagnose
1.1.2   MDT SCN-IP100.03 IP Router Data Secure
1.1.3   MDT RF-LK001.02 KNX RF+ Medien-/Linienkoppler zur Linie 1.2

1.3.1   KNX TP Linienkoppler für Außenlinie (bei Ausbau)
1.3.2   separate KNX Busspannungsversorgung Außenlinie (bei Ausbau)
```

Die Außenlinie wird erst bei tatsächlichem Ausbau bestückt. Eine eigene Linie bietet galvanische und telegrammtechnische Trennung und begrenzt Fehler im Außenbereich auf diesen Abschnitt.

## Linie 1.1 – Innenbereich und Hauptverteilung

```text
1.1.10  MDT SCN-LOG1.02 Logikmodul
1.1.11  MDT SCN-SAFE.01 Sicherheitsmodul
1.1.12  MDT SCN-RTC20.01 Schaltuhr

1.1.20  MDT AKS-2416.03 Schaltaktor 24-fach
1.1.21  MDT AMI-1216.02 Schaltaktor 12-fach mit Strommessung
1.1.22  MDT AZI-0616.01 Schaltaktor 6-fach mit Wirkleistungsmessung
1.1.23  MDT JAL-0810M.02 Jalousieaktor 8-fach
1.1.24  MDT AKH-0800.02 Heizungsaktor 8-fach

1.1.30  MDT AKD-0424V.02 RGBW LED Controller 4 Kanal
1.1.31  MDT AKD-0424R.02 RGBW LED Controller 4 Kanal REG
1.1.32  MDT SCN-DALI64.03 DALI Control IP

1.1.40  Gira Wetterstation Pro / Wetterstation
1.1.41  MDT SCN-P360D4.03 Präsenzmelder Decke

1.1.50  MDT Glastaster Smart II Wohnzimmer
1.1.51  MDT Glastaster Smart II Esszimmer
1.1.52  MDT Glastaster Smart II Küche
1.1.53  MDT Glastaster Smart II Arbeitszimmer
1.1.54  MDT Glastaster Smart II Gang 1
1.1.55  MDT Glastaster Smart II Gang 2
1.1.56  MDT Glastaster Smart II Gang 3
1.1.57  MDT Glastaster Smart II Schlafzimmer
1.1.58  MDT Glastaster Smart II Badezimmer
1.1.59  MDT Glastaster Smart II Bad vorne
```

## Linie 1.2 – KNX RF

```text
1.2.1   RF Fenstergriff Wohnzimmer 1
1.2.2   RF Fenstergriff Wohnzimmer 2
1.2.3   RF Fenstergriff Wohnzimmer 3
1.2.4   RF Fenstergriff Küche 1
1.2.5   RF Fenstergriff Küche 2
1.2.6   RF Fenstergriff Bad vorne
1.2.7   RF Fenstergriff Arbeitszimmer 1
1.2.8   RF Fenstergriff Arbeitszimmer 2
1.2.9   RF Fenstergriff Schlafzimmer 1
1.2.10  RF Fenstergriff Schlafzimmer 2
1.2.11  RF Fenstergriff Badezimmer 1
1.2.12  RF Fenstergriff Badezimmer 2
```

## Linie 1.3 – Außenbereich / Reserve

Vorgesehene mögliche Teilnehmer:

```text
1.3.10  Wetterstation außen, falls physikalisch auf Außenlinie umgesetzt
1.3.20  Außenbeleuchtung / Außenaktor
1.3.21  Garten- oder Garagenaktor
1.3.30  Tor- oder Türsteuerung
1.3.40  Außenbewegungs- oder Präsenzmelder
```

Die konkreten Adressen werden erst vergeben, wenn die Geräte feststehen. Außenleitungen müssen entsprechend Überspannungsschutz, Leitungsführung und Potentialausgleich geplant werden.

## Adresskonventionen

- `1.1.x`: Innenbereich, Hauptverteilung und fest verdrahtete TP-Geräte.
- `1.2.x`: ausschließlich KNX-RF-Teilnehmer.
- `1.3.x`: Außenbereich, Nebengebäude und spätere Erweiterungen.
- REG-Geräte erhalten niedrige Adressen, Sensoren und Bedienstellen getrennte Nummernbereiche.
- Reservebereiche bleiben bewusst frei.
- Jede TP-Linie benötigt bei tatsächlichem Ausbau eine passende Busspannungsversorgung; Koppler werden entsprechend der ETS-Topologie eingefügt und parametriert.
