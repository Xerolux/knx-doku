# Bad: HF-Einschaltschwellen am 06.11.2026

Nutzer meldet Auslösung durch den fahrenden Rollladen; Raumbreite etwa 2–3 m.
Geprüft in ETS: `1.1.35 Raumkontroller Bad`, Präsenzmodul 3.10,
HF-Sensor `HLK LD2420`.

Die drei aktiven Trigger-Schwellen wurden moderat erhöht:

| Entfernungsbereich | Vorher | Neu |
|---|---:|---:|
| 0,35–1,05 m | 4477 | 5600 |
| 1,05–1,75 m | 3477 | 4350 |
| 1,75–2,45 m | 3101 | 3900 |

Halteschwellen 4301 / 2602 / 2177, Haltedauer 30 s und Reichweite
0,35–2,45 m unverändert. Keine Kalibrierung oder Rollladenfahrt ausgelöst.
Applikationsdownload ausschließlich für 1.1.35 durchgeführt; ETS-Historie
bestätigt mit grünem Pfeil `Programmieren(Appl.): Abgeschlossen`.

Physisch offen: leerer Raum bei Rollladenfahrt sowie Erkennung beim Betreten
und ruhigen Aufenthalt. Die höheren Schwellen sind ein Startwert und kein
Nachweis einer sicheren Unterdrückung der Rollladenbewegung.
