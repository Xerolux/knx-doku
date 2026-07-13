# 12 – Zentralfunktionen

## Hauszustände

| Gruppenadresse | Funktion | DPT | Zweck |
|---:|---|---|---|
| 0/0/0 | Zentral Aus | 1.001 | alle normalen Lichtkreise ausschalten |
| 0/0/1 | Haus verlassen | 1.001 | Abwesenheitsmodus auslösen |
| 0/0/2 | Nachtmodus | 1.001 | Nachtbetrieb aktiv |
| 0/0/3 | Urlaub | 1.001 | längere Abwesenheit |
| 0/0/4 | Panik | 1.001 | definierte Notfunktion |

## Rollladen zentral

| Gruppenadresse | Funktion | DPT | Zweck |
|---:|---|---|---|
| 0/1/0 | Alle Rollladen Auf / Ab | 1.008 | gemeinsame Fahrtrichtung |
| 0/1/1 | Alle Rollladen Stop / Schritt | 1.007 | Fahrt stoppen oder Schritt fahren |

## Beschattung zentral

| Gruppenadresse | Funktion | DPT | Richtung |
|---:|---|---|---|
| 0/2/0 | Beschattungsautomatik Freigabe | 1.001 | Befehl |
| 0/2/1 | Beschattungsautomatik Status | 1.001 | Rückmeldung |
| 0/2/2 | Markise Einfahren Schutz | 1.008 | Schutzbefehl |
| 0/2/3 | Wetterschutz Aktiv Status | 1.001 | Rückmeldung |

## Heizung zentral

| Gruppenadresse | Funktion | DPT | Richtung |
|---:|---|---|---|
| 0/3/0 | Heizung Zentral Betriebsart Soll | 20.102 | Befehl |
| 0/3/1 | Heizung Zentral Betriebsart Status | 20.102 | Rückmeldung |

Eine zentrale Betriebsart verhindert widersprüchliche Parallelbefehle wie gleichzeitig „Komfort“ und „Eco“. Welcher Wert welcher Betriebsart entspricht, wird anhand der Kommunikationsobjekte des verwendeten Heizungsaktors und der Raumregler festgelegt.

## Anzeige auf Glastastern

Sinnvolle Statusanzeigen sind Haus verlassen, Nachtmodus, Urlaub, Wetterschutz, Fenster offen und Markise gesperrt.
