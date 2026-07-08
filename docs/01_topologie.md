# 01 – KNX Topologie

## Linie

Für das Projekt wird zunächst eine einfache Hauptlinie verwendet.

```text
Bereich 1
└── Linie 1.1 Hauptlinie Wohnhaus
```

## Vorgeschlagene physikalische Adressen

```text
1.1.1   MDT STR-0640.01 Busspannungsversorgung Diagnose
1.1.2   MDT SCN-IP100.03 IP Router Data Secure
1.1.3   MDT RF-LK001.02 KNX RF+ Linienkoppler

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

1.1.70  RF Fenstergriff Wohnzimmer 1
1.1.71  RF Fenstergriff Wohnzimmer 2
1.1.72  RF Fenstergriff Wohnzimmer 3
1.1.73  RF Fenstergriff Küche 1
1.1.74  RF Fenstergriff Küche 2
1.1.75  RF Fenstergriff Bad vorne
1.1.76  RF Fenstergriff Arbeitszimmer 1
1.1.77  RF Fenstergriff Arbeitszimmer 2
1.1.78  RF Fenstergriff Schlafzimmer 1
1.1.79  RF Fenstergriff Schlafzimmer 2
1.1.80  RF Fenstergriff Badezimmer 1
1.1.81  RF Fenstergriff Badezimmer 2
```

## Hinweise

- Geräte im Schaltschrank bekommen niedrige Adressen.
- Bedienstellen und Sensoren bekommen mittlere Adressen.
- RF-Geräte bekommen einen eigenen Adressbereich.
- Reservebereiche bleiben bewusst frei.
