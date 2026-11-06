# EG-Rollläden: Dämmerungsautomatik vom 06.11.2026

Auftrag: nur EG, bei Helligkeit öffnen und bei Dunkelheit schließen;
Schlafzimmer ausnehmen. Direkte KNX-Auswertung in Gira Wetterstation Plus
`1.1.40`, ohne Abhängigkeit von Home Assistant.

## Parameter

Unter Dämmerungssensor ist Grenzwert 1 aktiviert:

- Grenzwert 50 Lux, Hysterese 50 Lux.
- Unterschreitung des Grenzwerts: EIN = 1 = Ab.
- Überschreitung Grenzwert + Hysterese (100 Lux): AUS = 0 = Auf.
- Ein- und Ausschaltverzögerung jeweils 5 Minuten.
- Senden bei Wertänderung: Ja; zyklisches Senden: 0 (aus).
- Externer Grenzwert: Nein.

Damit werden manuelle Fahrten zwischen den Helligkeitswechseln nicht durch
zyklische Automatikbefehle überschrieben. Es gibt keine zusätzliche Uhrzeitsperre.

## Verbindungen

Neue separate Gruppenadresse `0/1/2`, Name
`EG Rolllaeden ohne Schlafzimmer Daemmerung Auf Ab`.
Sender: Gira KO 36, Grenzwert 1 Dämmerung.

Empfänger am MDT JAL-0810M.02 `1.1.4`, jeweils zusätzlich zur Einzeladresse:

| Kanal | Raum | KO Auf/Ab | Bestehende Einzeladresse |
|---|---|---:|---|
| C | Arbeitszimmer | 81 | 2/1/0 |
| D | Wohnzimmer Fenster | 110 | 2/0/0 |
| E | Bad | 139 | 2/3/0 |
| H | Wohnzimmer Türe | 226 | 2/0/10 |

Schlafzimmer A/B, Markise G und Zentralobjekt 0 erhalten keine Verbindung
zu 0/1/2. OG erhält keine Verbindung. Kanal F Küche bleibt ohne neue
Verbindung, weil reale Motorzuordnung und Einzeladressen unbestätigt sind.
Nutzer wurde nach dem Küchenrollladen gefragt.

## Prüfung und Grenzen

Alle vier zusätzlichen Aktorverbindungen sowie der Gira-Sender wurden in
ETS geprüft. Die ETS-Historie bestätigt für `1.1.4` und `1.1.40` jeweils
mit grünem Pfeil `Programmieren(Appl.): Abgeschlossen`.
Die natürliche Dämmerungsreaktion und physische Fahrten sind noch zu bestätigen;
es wurden keine künstlichen Helligkeitswerte oder Testfahrbefehle gesendet.

Kein zusätzlicher Aussperrschutz wurde eingerichtet. Insbesondere der
Wohnzimmer-Türrollladen folgt der Dämmerungsautomatik. Die Schwellen sind
Startwerte; eine physische Vor-Ort-Abnahme steht aus.

Grundlage: [Gira Produkthandbuch, Dämmerungssensor und Grenzwerte](https://partner.gira.de/data3/20743510.pdf).
