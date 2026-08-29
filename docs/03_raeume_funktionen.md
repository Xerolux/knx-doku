# 03 – Räume und Funktionen

## Räume

| Raum | Licht | Rollladen | Fenstergriffe RF | Heizung |
|---|---:|---:|---:|---:|
| Wohnzimmer | ja | 2 | 3 | ja |
| Esszimmer | ja | 0 | 0 | ja |
| Küche | ja | 0 | 2 | ja |
| Arbeitszimmer | ja | 1 | 2 | ja |
| Gang | ja | 0 | 0 | ja |
| Schlafzimmer | ja | 2 | 2 | ja |
| Badezimmer | ja | 1 | 2 | ja |
| Bad vorne | ja | 0 | 1 | ja |
| Abstellkammer (ehemals Dusche) | offen | offen | offen | Zuordnung offen |

Damit umfasst die Anlage **neun getrennte Räume**. Badezimmer und Abstellkammer sind nicht identisch. Die Abstellkammer fehlt bislang in der raumbezogenen Gruppenadressplanung und darf deshalb nicht mit den Adressen des Badezimmers verknüpft werden. Die vorhandene Home-Assistant-Altentität `climate.heizkorper_omaopa_dusche_1` gehört zur Abstellkammer; ihre endgültige KNX-Zuordnung ist noch zu prüfen.

## Erste Ausbaustufe

Die erste Ausbaustufe bleibt bewusst einfach:

- Licht nur ein/aus
- Rollläden auf/ab, Stop und Position
- Markise mit Wetterschutz
- Fußbodenheizung je Raum
- Fensterstatus je Raum
- Präsenzmelder für automatische Grundfunktionen

## Spätere Ausbaustufen

Vorbereitet durch vorhandene 5-adrige Leitungen und vorhandene Hardware:

- DALI Beleuchtung
- RGBW LED-Stripes
- Tunable White
- zweite Lichtgruppen je Raum
- erweiterte Szenen
- Home Assistant Visualisierung
