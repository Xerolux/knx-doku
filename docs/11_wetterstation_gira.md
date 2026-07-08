# 11 – Gira Wetterstation und Beschattung

## Ziel

Die Wetterstation ist ein zentrales Schutzgerät. Wetter- und Schutzfunktionen sollen direkt in KNX laufen und nicht von Home Assistant abhängig sein.

## Grundwerte

| Funktion | Gruppenadresse | Datentyp | Nutzung |
|---|---:|---|---|
| Außentemperatur | 4/0/0 | 9.001 | Anzeige, Frost, Heizung |
| Windgeschwindigkeit | 4/0/1 | 9.005 | Markisenschutz |
| Regen | 4/0/2 | 1.001 | Markisenschutz |
| Dämmerung | 4/0/3 | 1.001 | Nacht / Außenlicht |
| Helligkeit Ost | 4/1/0 | 9.004 | Beschattung Ost |
| Helligkeit Süd | 4/1/1 | 9.004 | Beschattung Süd |
| Helligkeit West | 4/1/2 | 9.004 | Beschattung West |

## Wetteralarme

| Funktion | Gruppenadresse | Zweck |
|---|---:|---|
| Windwarnung | 4/2/0 | Vorwarnung, noch keine harte Sperre |
| Windalarm | 4/2/1 | Markise sofort einfahren |
| Regenalarm | 4/2/2 | Markise einfahren |
| Frostalarm | 4/2/3 | Schutz- und Infofunktion |

## Beschattungsfreigaben

| Funktion | Gruppenadresse | Zweck |
|---|---:|---|
| Sonne Ost aktiv | 4/3/0 | spätere Automatik |
| Sonne Süd aktiv | 4/3/1 | spätere Automatik |
| Sonne West aktiv | 4/3/2 | spätere Automatik |
| Beschattung Automatik aktiv | 4/3/3 | globale Freigabe |

## Markisenschutz

Empfohlene Logik:

```text
Windalarm = 1 -> Markise einfahren
Regenalarm = 1 -> Markise einfahren
Frostalarm = 1 -> Markise sperren
```

Empfohlene Startwerte:

| Schwelle | Startwert | Hinweis |
|---|---:|---|
| Windwarnung | 25 km/h | nur Meldung / Vorwarnung |
| Windalarm | 35 km/h | Markise fährt ein |
| Frostalarm | 3 °C | Schutzfunktion |

Die Werte sind Startwerte und müssen an die reale Markise und den Montageort angepasst werden.

## ETS-Hinweis

Die Ausgänge der Wetterstation werden mit Logikmodul und Jalousieaktor verknüpft. Der Wetterschutz muss auch dann funktionieren, wenn Home Assistant ausgeschaltet ist.
