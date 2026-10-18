# 35 – ETS-Gebäude- und Raumzuordnung

Stand: 18.10.2026. Direkt im geöffneten ETS6-Projekt Home bearbeitet und kontrolliert.

## Auftrag und Abgrenzung

Die Anzeige „45 Keinem Raum zugewiesen“ war der Gerätezähler des ETS-Suchordners. Geräte hatten bereits Namen, aber noch keine formale Gebäudezuordnung. Nach Nutzerangabe befinden sich die MDT-Technikbauteile im Keller / Technikraum; Taster, Fenstergriffe, Bewegungsmelder und Raumfühler werden nach den vorhandenen Gerätenamen den Räumen zugeordnet.

Unter Home wurden 14 Räume/Bereiche angelegt und alle 45 ETS-Geräte zugeordnet. Nach der ergänzenden Ortsangabe des Nutzers wurden auch die vier verbleibenden Geräte zugeordnet. Der ETS-Suchordner „Keinem Raum zugewiesen“ zeigt anschließend 0 Geräte. Der Suchordner „Programmieren notwendig“ bleibt bei 0. Es wurden keine Applikationen geladen und keine Schalt-, Fahr- oder Heizbefehle gesendet.

## Zuordnung

| ETS-Raum | Physikalische Adressen |
|---|---|
| Abstellkammer | `1.1.43` |
| Arbeitszimmer | `1.1.15`, `1.1.16`, `1.1.24` |
| Bad | `1.1.32`, `1.1.35`, `1.1.39`, `1.1.42` |
| Bad Gang | `1.1.33` |
| Bad vorne | `1.1.38`, `1.1.44` |
| Dach / Außenbereich | `1.1.40` |
| Eingang | `1.1.20` |
| Gang | `1.1.2`, `1.1.21`, `1.1.26`, `1.1.28`, `1.1.30` |
| Keller / Technikraum | `1.1.0`, `1.1.1`, `1.1.3`, `1.1.4`, `1.1.5`, `1.1.6`, `1.1.7`, `1.1.8`, `1.1.9`, `1.1.10`, `1.1.31`, `1.1.36`, `1.1.37`, `1.1.41` |
| Küche | `1.1.11`, `1.1.12`, `1.1.22`, `1.1.34` |
| Schlafzimmer | `1.1.17`, `1.1.18`, `1.1.25` |
| Terrasse | `1.1.27` |
| Treppenhaus | `1.1.29` |
| Wohnzimmer | `1.1.13`, `1.1.14`, `1.1.19`, `1.1.23` |

Die Taster `1.1.21 Eingang Gang`, `1.1.26 Schlafzimmer Gang` und `1.1.28 Gang Wohnzimmer` sind dem gemeinsamen Raum Gang zugeordnet. `1.1.33 Bad Gang` hat einen eigenen Raum. Diese Zusammenfassung folgt den vorhandenen Namen; eine feinere Unterteilung der Gangabschnitte kann später erfolgen.

Bei den Unterputzaktoren `1.1.36 Bad vorne` und `1.1.37 Abstellkammer` gilt Keller / Technikraum als Geräteort gemäß Nutzerangabe. Bad vorne und Abstellkammer bleiben ihre Lichtfunktionen. Eine Raumzuordnung verändert keine Gruppenadresse und keinen bedienten Verbraucher.

## Ergänzende Ortsangaben des Nutzers

- Enertex-Spannungsversorgung `1.1.1`: Keller / Technikraum.
- Gira RF Multi/TP Medienkoppler `1.1.2`: EG Gang, im ETS-Raum Gang.
- Gira Wetterstation Plus `1.1.40`: auf dem Dach, eigener ETS-Bereich Dach / Außenbereich.
- Gira Rauchwarnmelder-Eintrag `1.1.41`: Keller / Technikraum. Die Ortsangabe und formale Zuordnung bestätigen allein noch keine KNX-Inbetriebnahme; der bisherige Status als ETS-Platzhalter bleibt bis zu einem gesonderten Gerätenachweis bestehen.

Es bleiben keine Geräte ohne ETS-Raum.

Die Zuordnung ist ein Nachweis der ETS-Projektpflege, kein neuer Nachweis für Montage, Verdrahtung oder Gerätefunktion. Vorhandene Inbetriebnahmegrenzen, insbesondere beim Fenstergriff Bad vorne, gelten weiter.
