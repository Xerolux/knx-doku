# 05 – Kanalbelegung

Stand: 04.08.2026

Die Tabellen unterscheiden zwischen geplanter Zuordnung und dem aktuell in ETS sichtbaren Stand. Vor der endgültigen Abnahme ist jede Zuordnung mit der realen Verdrahtung abzugleichen.

## Licht

Geplante Kanalzuordnung des Schaltaktors:

| Kanal | Funktion | Schalten | Status |
|---|---|---:|---:|
| A | Wohnzimmer | `1/0/0` | `1/0/1` |
| B | Esszimmer | `1/1/0` | `1/1/1` |
| C | Küche | `1/2/0` | `1/2/1` |
| D | Arbeitszimmer | `1/3/0` | `1/3/1` |
| E | Gang | `1/4/0` | `1/4/1` |
| F | Schlafzimmer | `1/5/0` | `1/5/1` |
| G | Badezimmer | `1/6/0` | `1/6/1` |
| H | Bad vorne | `1/7/0` | `1/7/1` |

Im aktuellen ETS-Stand ist am Schaltaktor das Zentralobjekt mit `0/4/0 Alle Lichter schalten` verbunden. Die individuellen Schalt- und Statusobjekte der Kanäle sind noch nicht vollständig mit den oben genannten Gruppenadressen verknüpft. Die Zuordnung darf erst nach Prüfung der tatsächlichen Ausgangsverdrahtung übernommen werden.

Das Terrassenlicht am Glastaster `1.1.27` besitzt derzeit noch keine Gruppenadresse und bleibt offen.

## Beschattung – aktueller ETS-Stand

Gerät: MDT `JAL-0810M.02` mit Fahrzeitmessung.

| Kanal | ETS-Bezeichnung | Auf/Ab | Stopp | Position Status | Bemerkung |
|---|---|---:|---:|---:|---|
| A | Schlafzimmer Tür / links | `2/2/0` | `2/2/1` | `2/2/3` | reale Zuordnung prüfen |
| B | Schlafzimmer Fenster / rechts | `2/2/10` | `2/2/11` | `2/2/13` | verbunden |
| C | Arbeitszimmer | `2/1/0` | `2/1/1` | `2/1/3` | Statusverknüpfung prüfen |
| D | Wohnzimmer Fenster / links | `2/0/0` | `2/0/1` | `2/0/3` | Statusverknüpfung prüfen |
| E | noch ungeklärt | – | – | – | reale Belegung feststellen |
| F | Küche | – | – | – | in ETS benannt, noch ohne Gruppenadressen |
| G | Markise | `2/4/0` | `2/4/1` | `2/4/3` | Statusverknüpfung prüfen |
| H | Wohnzimmer Tür / rechts | `2/0/10` | `2/0/11` | `2/0/13` | Statusverknüpfung prüfen |

Zentrale Beschattung:

```text
0/1/0 Alle Rollladen Auf / Ab
0/1/1 Alle Rollladen Stop / Schritt
```

Die zentrale Objektzuordnung am JAL lautet:

```text
Objekt 0 Rollladen Auf/Ab          -> 0/1/0
Objekt 1 Lamellenverstellung/Stopp -> frei
Objekt 2 Stopp                     -> 0/1/1
```

Bei den verwendeten Rollladenkanälen ist `Zentrale Objekte = nur Auf/Ab` eingestellt. Details zur Inbetriebnahme, Positionsrückmeldung und Fahrzeitmessung stehen in [20 – Rollladen: ETS-Zuordnung, Inbetriebnahme und Prüfung](20_rollladen_inbetriebnahme.md).

## Heizung

| Kanal | Raum |
|---|---|
| 1 | Wohnzimmer |
| 2 | Esszimmer |
| 3 | Küche |
| 4 | Arbeitszimmer |
| 5 | Gang |
| 6 | Schlafzimmer |
| 7 | Badezimmer |
| 8 | Bad vorne |
