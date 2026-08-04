# 05 – Kanalbelegung

Stand: 04.08.2026

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
| G–X | noch nicht vollständig dokumentiert | – | – | reale Belegung und Zentralteilnahme prüfen |

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
| `1/4/5` | geplanter Sammelstatus aus einer Logik |

Die Statusobjekte der Kanäle E und F werden nicht direkt auf dieselbe Statusadresse gelegt. Der Sammelstatus `1/4/5` wird durch genau eine ODER- oder UND-Logik erzeugt. Details stehen in [21 – Ganglicht und Bewegungsmelder](21_ganglicht_bewegungsmelder.md).

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
| E | noch ungeklärt | – | – | – | reale Belegung feststellen |
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
