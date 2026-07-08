# 12 – Zentralfunktionen

## Ziel

Zentralfunktionen bündeln wichtige Hauszustände. Sie werden von Glastastern, Logikmodul, Schaltuhr und optional Home Assistant verwendet.

## Hauszustände

| Funktion | Gruppenadresse | Zweck |
|---|---:|---|
| Zentral Aus | 0/0/0 | alle normalen Lichtkreise aus |
| Haus verlassen | 0/0/1 | Abwesenheitsmodus |
| Nachtmodus | 0/0/2 | reduzierte Beleuchtung / Nachtbetrieb |
| Urlaub | 0/0/3 | längere Abwesenheit |
| Panik | 0/0/4 | Notfunktion, Licht an |
| Anwesenheit | 0/0/5 | Haus bewohnt / normal |

## Rollladen zentral

| Funktion | Gruppenadresse | Zweck |
|---|---:|---|
| Alle Rollläden Hoch | 0/1/0 | zentrale Fahrt hoch |
| Alle Rollläden Runter | 0/1/1 | zentrale Fahrt runter |
| Alle Rollläden Stop | 0/1/2 | zentrale Stop-Funktion |

## Beschattung zentral

| Funktion | Gruppenadresse | Zweck |
|---|---:|---|
| Beschattungsautomatik Ein | 0/2/0 | Automatik freigeben |
| Beschattungsautomatik Aus | 0/2/1 | Automatik sperren |
| Markise Einfahren Zentral | 0/2/2 | Schutz- und Zentralbefehl |
| Wetterschutz Aktiv | 0/2/3 | Status für Anzeige und Sperren |

## Heizungsmodi zentral

| Funktion | Gruppenadresse | Zweck |
|---|---:|---|
| Heizung Komfort | 0/3/0 | normale Nutzung |
| Heizung Nacht | 0/3/1 | Nachtabsenkung |
| Heizung Eco | 0/3/2 | Abwesenheit |
| Heizung Frostschutz | 0/3/3 | Minimalbetrieb |

## Anzeige auf Glastastern

Sinnvolle Statusanzeigen:

- Haus verlassen aktiv
- Nachtmodus aktiv
- Urlaub aktiv
- Wetterschutz aktiv
- Fenster offen
- Markise gesperrt

## Empfehlung

Zentralfunktionen sollen sparsam, aber eindeutig aufgebaut werden. Jeder Zentralzustand muss klar sagen, was im Haus passieren soll.
