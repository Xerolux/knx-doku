# 08 – KNX RF Fenstergriffe

## RF-Kopplung

Der MDT RF-LK001.02 verbindet die KNX-TP-Linie **1.1** mit der KNX-RF-Linie **1.2**. Die RF-Fenstergriffe sind deshalb als Teilnehmer der Linie 1.2 angelegt.

## Zuordnung

| Physikalische Adresse | Raum | Gerät |
|---|---|---|
| 1.2.1 | Wohnzimmer | Fenstergriff 1 |
| 1.2.2 | Wohnzimmer | Fenstergriff 2 |
| 1.2.3 | Wohnzimmer | Fenstergriff 3 |
| 1.2.4 | Küche | Fenstergriff 1 |
| 1.2.5 | Küche | Fenstergriff 2 |
| 1.2.6 | Bad vorne | Fenstergriff 1 |
| 1.2.7 | Arbeitszimmer | Fenstergriff 1 |
| 1.2.8 | Arbeitszimmer | Fenstergriff 2 |
| 1.2.9 | Schlafzimmer | Fenstergriff 1 |
| 1.2.10 | Schlafzimmer | Fenstergriff 2 |
| 1.2.11 | Badezimmer | Fenstergriff 1 |
| 1.2.12 | Badezimmer | Fenstergriff 2 |

## Gruppenadressen

```text
5/0/0 Wohnzimmer Fenstergriff 1 Status
5/0/1 Wohnzimmer Fenstergriff 2 Status
5/0/2 Wohnzimmer Fenstergriff 3 Status
5/1/0 Küche Fenstergriff 1 Status
5/1/1 Küche Fenstergriff 2 Status
5/2/0 Bad vorne Fenstergriff Status
5/3/0 Arbeitszimmer Fenstergriff 1 Status
5/3/1 Arbeitszimmer Fenstergriff 2 Status
5/4/0 Schlafzimmer Fenstergriff 1 Status
5/4/1 Schlafzimmer Fenstergriff 2 Status
5/5/0 Badezimmer Fenstergriff 1 Status
5/5/1 Badezimmer Fenstergriff 2 Status
```

Die Gruppenadressen bleiben medienunabhängig. TP-, RF- und IP-Teilnehmer können dieselbe Gruppenadresse verwenden, wenn die Filtertabellen und Kommunikationsobjekte passend parametriert sind.

## Inbetriebnahmehinweis

Die RF-Geräte nacheinander einlernen, sofort eindeutig beschriften und anschließend Reichweite, Batteriestatus und Telegrammweiterleitung über den Medienkoppler prüfen.
