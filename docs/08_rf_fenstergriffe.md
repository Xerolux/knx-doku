# 08 – KNX-RF-Fenstergriffe

## RF-Kopplung

Der **Gira 5114 00 RF Multi/TP Medienkoppler** verbindet die TP-Hauptlinie 1.1 mit KNX RF. ETS erzeugt dafür automatisch **RF Segment 1** unterhalb der Linie 1.1.

Eine separate manuelle KNX-RF-Linie 1.2 wird in diesem Projekt nicht verwendet.

## Vorgesehene RF-Geräte

Die Fenstergriffe werden erst dann in ETS angelegt, wenn die konkreten Geräte vorhanden sind:

| Raum | Gerät |
|---|---|
| Wohnzimmer | Fenstergriff 1 |
| Wohnzimmer | Fenstergriff 2 |
| Wohnzimmer | Fenstergriff 3 |
| Küche | Fenstergriff 1 |
| Küche | Fenstergriff 2 |
| Bad vorne | Fenstergriff 1 |
| Arbeitszimmer | Fenstergriff 1 |
| Arbeitszimmer | Fenstergriff 2 |
| Schlafzimmer | Fenstergriff 1 |
| Schlafzimmer | Fenstergriff 2 |
| Badezimmer | Fenstergriff 1 |
| Badezimmer | Fenstergriff 2 |

Die physikalischen Adressen werden nicht vorab fest eingetragen. Sie werden beim Hinzufügen und Einlernen der Geräte direkt in ETS innerhalb von **RF Segment 1** vergeben.

## Gruppenadressen

```text
5/0/0  Wohnzimmer Fenstergriff 1 Status
5/0/1  Wohnzimmer Fenstergriff 2 Status
5/0/2  Wohnzimmer Fenstergriff 3 Status
5/1/0  Küche Fenstergriff 1 Status
5/1/1  Küche Fenstergriff 2 Status
5/2/0  Bad vorne Fenstergriff Status
5/3/0  Arbeitszimmer Fenstergriff 1 Status
5/3/1  Arbeitszimmer Fenstergriff 2 Status
5/4/0  Schlafzimmer Fenstergriff 1 Status
5/4/1  Schlafzimmer Fenstergriff 2 Status
5/5/0  Badezimmer Fenstergriff 1 Status
5/5/1  Badezimmer Fenstergriff 2 Status
```

Die Gruppenadressen sind medienunabhängig. TP-, RF- und IP-Teilnehmer können dieselbe Gruppenadresse verwenden, wenn Kommunikationsobjekte und Filtertabellen passend parametriert sind.

## Inbetriebnahme

1. Den passenden RF-Fenstergriff aus dem ETS-Katalog in **RF Segment 1** einfügen.
2. Gerätezertifikat beziehungsweise FDSK einlesen, falls das Gerät KNX Secure verwendet.
3. Immer nur ein Gerät gleichzeitig in den Programmier- oder Einlernmodus setzen.
4. Physikalische Adresse und Applikation laden.
5. Kommunikationsobjekte mit den vorgesehenen Gruppenadressen verbinden.
6. Statusänderungen anschließend im Gruppenmonitor prüfen.

Die Geräte sollten unmittelbar nach dem Einlernen eindeutig nach Raum und Fenster beschriftet werden.
