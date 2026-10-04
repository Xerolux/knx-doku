# 05 – Kanalbelegung

Stand: 03.10.2026

Die Tabellen bilden den aktuell in ETS sichtbaren Stand ab. Vor der endgültigen Abnahme ist jede Zuordnung mit der realen Verdrahtung im Schaltschrank und am Verbraucher abzugleichen.

## Licht – aktueller ETS-Stand

Gerät: MDT Schaltaktor `1.1.3` mit den Kanälen A bis X.

| Kanal | ETS-Bezeichnung | Schalten | Status | zusätzliche Gruppenfunktion |
|---|---|---:|---:|---|
| A | Licht Wohnzimmer | `1/0/0` | `1/0/1` | Zentral Licht über `0/4/0` |
| B | Licht Arbeitszimmer | `1/3/0` | `1/3/1` | Zentral Licht über `0/4/0` |
| C | Licht Küche | `1/2/0` | `1/2/1` | Zentral Licht über `0/4/0` |
| D | Licht Schlafzimmer | `1/5/0` | `1/5/1` | Zentral Licht über `0/4/0` |
| E | Licht Gang | `1/4/0` | `1/4/1` | zusätzlich `1/4/4 Gang beide Lichter schalten` |
| F | Licht Gang Neubau | `1/4/2` | `1/4/3` | zusätzlich `1/4/4 Gang beide Lichter schalten` |
| G | Licht Bad | `1/6/0` | `1/6/1` | Badezimmer |
| H | Licht Abstellkammer | `12/0/0` | `12/0/1` | eigener Raum; nicht Bad vorne |
| I–X | noch nicht vollständig dokumentiert | – | – | reale Belegung und Zentralteilnahme prüfen |

### Objektzuordnung der bestätigten Kanäle

```text
Kanal A:
  Objekt 1 Schalten EIN/AUS -> 1/0/0
  Objekt 8 Status          -> 1/0/1

Kanal B:
  Objekt 13 Schalten EIN/AUS -> 1/3/0
  Objekt 20 Status           -> 1/3/1

Kanal C:
  Objekt 25 Schalten EIN/AUS -> 1/2/0
  Objekt 32 Status           -> 1/2/1

Kanal D:
  Objekt 37 Schalten EIN/AUS -> 1/5/0
  Objekt 44 Status           -> 1/5/1

Kanal E:
  Objekt 49 Schalten EIN/AUS -> 1/4/0 und 1/4/4
  Objekt 56 Status           -> 1/4/1

Kanal F:
  Objekt 61 Schalten EIN/AUS -> 1/4/2 und 1/4/4
  Objekt 68 Status           -> 1/4/3

Kanal G:
  Objekt 73 Schalten EIN/AUS -> 1/6/0
  Objekt 80 Status           -> 1/6/1

Kanal H:
  Objekt 85 Schalten EIN/AUS -> 12/0/0
  Objekt 92 Status           -> 12/0/1
```

Die Sperrobjekte der Lichtkanäle bleiben frei, solange keine dokumentierte Sperrfunktion vorgesehen ist.

### Gang mit zwei Lichtkreisen

| Gruppenadresse | Funktion |
|---:|---|
| `1/4/0` | Ganglicht Kanal E einzeln schalten |
| `1/4/1` | Status Kanal E |
| `1/4/2` | Gang Neubau Kanal F einzeln schalten |
| `1/4/3` | Status Kanal F |
| `1/4/4` | beide Ganglichter gemeinsam schalten |
| `1/4/5` | ODER-Sammelstatus aus Funktion F1 des Logikmoduls `1.1.8` |

Die Statusobjekte der Kanäle E und F werden nicht direkt auf dieselbe Statusadresse gelegt. Der Sammelstatus `1/4/5` wird durch eine ODER-Logik aus `1/4/1` und `1/4/3` erzeugt. Die Parametrierung und die ETS-Objektverknüpfungen sind angelegt; Download und Busprüfung stehen noch aus. Details stehen in [21 – Ganglicht und Bewegungsmelder](21_ganglicht_bewegungsmelder.md).

### Zentral Licht

```text
Schaltaktor Objekt 289 Zentralfunktion – Schalten EIN/AUS
    -> 0/4/0 Alle Lichter schalten
```

Bei jedem echten Lichtkanal wird die Teilnahme an der Zentralfunktion aktiviert. Steckdosen, technische Verbraucher und Reservekanäle dürfen nicht unbeabsichtigt teilnehmen.

### Terrassenlicht

Das Terrassenlicht am Glastaster `1.1.27` besitzt weiterhin noch keine bestätigte Gruppenadresse. Erst reale Verdrahtung und Aktorkanal ermitteln, anschließend eine eindeutige Schalt- und Statusadresse zuordnen.

## Beschattung – aktueller ETS-Stand

Gerät: MDT `JAL-0810M.02` mit Fahrzeitmessung.

Die Gruppenadressennamen wurden in ETS einheitlich auf **Fenster** und **Türe** umbenannt. Die Gruppenadressen bleiben unverändert.

| Kanal | ETS-Bezeichnung | Auf/Ab | Stopp | Position Status | Bemerkung |
|---|---|---:|---:|---:|---|
| A | Schlafzimmer Rollladen Türe | `2/2/0` | `2/2/1` | `2/2/3` | Statusobjekt aktiviert; Zuordnung prüfen |
| B | Schlafzimmer Rollladen Fenster | `2/2/10` | `2/2/11` | `2/2/13` | Statusobjekt aktiviert und verbunden |
| C | Arbeitszimmer Rollladen | `2/1/0` | `2/1/1` | `2/1/3` | Statusverknüpfung prüfen |
| D | Wohnzimmer Rollladen Fenster | `2/0/0` | `2/0/1` | `2/0/3` | Statusverknüpfung prüfen |
| E | Badezimmer Rollladen | `2/3/0` | `2/3/1` | `2/3/3` | ETS-Bezeichnung und Verknüpfungen am 03.10.2026 bestätigt; Download und Test offen |
| F | Küche | – | – | – | in ETS benannt, noch ohne Gruppenadressen |
| G | Markise | `2/4/0` | `2/4/1` | `2/4/3` | Statusverknüpfung prüfen |
| H | Wohnzimmer Rollladen Türe | `2/0/10` | `2/0/11` | `2/0/13` | Statusverknüpfung prüfen |

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

Für A, B, C, D, E und H ist `Zentrale Objekte = nur Auf/Ab` vorgesehen; G (Markise) bleibt `nicht aktiv`. Die Einzelverknüpfungen von E sind bestätigt; die Zentralteilnahme bleibt zu prüfen. Details zur Inbetriebnahme, Positionsrückmeldung und Fahrzeitmessung stehen in [20 – Rollladen: ETS-Zuordnung, Inbetriebnahme und Prüfung](20_rollladen_inbetriebnahme.md).

## Heizung

Stand: 04.10.2026. Die neue ETS-Kanalbenennung ersetzt die frühere pauschale Raumfolge 1–8. Reale Ausgangsverdrahtung und Funktion bleiben zu prüfen.

| Aktor | Kanal | ETS-Bezeichnung | Regelzone |
|---|---|---|---|
| `1.1.5` | A | Badezimmer | Badezimmer |
| `1.1.5` | B | Schlafzimmer Fenster | Schlafzimmer |
| `1.1.5` | C | Schlafzimmer Wand | Schlafzimmer |
| `1.1.5` | D | Gang | Gang |
| `1.1.5` | E | Arbeitszimmer Wand | Arbeitszimmer |
| `1.1.5` | F | Arbeitszimmer Fenster | Arbeitszimmer |
| `1.1.5` | G | Wohnzimmer Küche Mitte | Wohnzimmer laut gemeldeter Verknüpfung; Heizkreisverlauf prüfen |
| `1.1.5` | H | Wohnzimmer Mitte | Wohnzimmer |
| `1.1.6` | A | Wohnzimmer Fenster | Wohnzimmer |
| `1.1.6` | B | Küche | Küche, getrennt vom Wohnzimmer |
| `1.1.6` | C–H | nicht bestätigt | vor Ort erfassen |

Objektnummern, Gruppenadressen, COSMO CTS230N und Nachweisstatus stehen in [06 – Heizung und Fenster](06_heizung_fenster.md#fbh-projektierung-vom-04102026). Für Esszimmer und Bad vorne ist in diesen Screenshots kein eigener Ausgang bestätigt. Die Abstellkammer besitzt keine geplante KNX-Heizungsfunktion.
