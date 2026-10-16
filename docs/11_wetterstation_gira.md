# 11 – Gira Wetterstation: Messwerte und Anzeige

> Späterer Folgeauftrag vom 16.10.: Der Nutzer hat anschließend den direkten KNX-Wetterschutz ausschließlich für die EG-Markise freigegeben. Umsetzung und tatsächlicher Download-/Prüfstand stehen in [Dokument 33](33_markise_eg_wetterschutz.md). Die unten beschriebene reine Anzeige war der davor abgeschlossene Arbeitsstand; OG bleibt unverändert.


## Inbetriebnahme am 16.10.2026

Die offene ETS zeigt **Wetterstation Plus 1.1.40, Applikation B00D29**. Die frühere Projektangabe B00D21 ist damit überholt. Alle 33 aktivierten Mess-/Diagnoseausgänge sind zugeordnet. Der Applikationsdownload wurde in ETS als **Abgeschlossen** bestätigt, einschließlich der Umstellung der absoluten Feuchte auf DPT 9.029. Das Eingangsobjekt 23 für eine GPS-Sendeanforderung bleibt unverbunden.

**Auf Nutzerwunsch ausschließlich Anzeige:** Die interne Beschattungssteuerung ist deaktiviert, es wurden keine Verknüpfungen zu Rollläden, Markisen, Alarm- oder Freigabeadressen angelegt. Die Abschnitte zu späterem Wetterschutz weiter unten beschreiben nur eine ältere Planung und sind keine aktive Schutzfunktion.

### Tatsächlich verbundene Ausgänge

| GA | KO | Messwert | DPT / Format |
|---|---:|---|---|
| 4/0/0 | 12 | Außentemperatur | 9.001 °C |
| 4/0/1 | 1 | Windgeschwindigkeit | 9.005 m/s; HA zeigt km/h |
| 4/0/2 | 38 | Regen, Grenzwert 1 | 1.001 |
| 4/0/4 | 13 | Relative Luftfeuchte | 9.007 % |
| 4/0/5 | 14 | Luftdruck | 9.006 Pa |
| 4/0/6 | 26 | Absolute Luftfeuchte | 9.029 g/m³ |
| 4/0/7 | 27 | Gefühlte Temperatur | 9.001 °C |
| 4/0/8 | 10 | Globalstrahlung | 9.022 W/m² |
| 4/0/9 | 9 | Dämmerungshelligkeit | 9.004 lx |
| 4/0/10 | 2 | Windrichtung | 5.003 Grad |
| 4/0/11 | 3 | Windorientierung | 16.000 Text |
| 4/0/12 | 4 | Windbereichsmeldung | 1 Bit |
| 4/0/13 | 28 | Schwüle | 1 Bit |
| 4/0/14 | 29 | Behaglichkeit | 1 Bit |
| 4/0/15 | 15 | GPS-Uhrzeit | 10.001 |
| 4/0/16 | 16 | GPS-Datum | 11.001 |
| 4/0/17 | 17 | GPS-Länge | 14.007 |
| 4/0/18 | 18 | GPS-Breite | 14.007 |
| 4/0/19 | 19 | Sonnenazimut | 5.003 |
| 4/0/20 | 20 | Sonnenelevation | 5.003 |
| 4/0/21 | 21 | GPS-Höhe | 14.039 m |
| 4/0/22 | 262 | Windsensor unverändert | 1 Bit |
| 4/0/23 | 263 | Windrichtung unverändert | 1 Bit |
| 4/0/24 | 264 | Kein Windsignal | 1 Bit |
| 4/0/25 | 265 | Versorgung OK | 1 Bit |
| 4/0/26 | 266 | GPS-Statuscode | 1 Byte |
| 4/0/27 | 267 | Sensorstatus | 2 Byte unsigned |
| 4/1/3–6 | 5–8 | Helligkeit Sensor 1–4 | 9.004 lx |
| 4/1/7 | 24 | Maximale Helligkeit | 9.004 lx |
| 4/1/8 | 25 | Maximale Helligkeit + Dämmerung | 9.004 lx |

4/0/3 und 4/1/0–2 wurden nicht verwendet. Die reale Ausrichtung der vier Helligkeitssensoren ist nicht vor Ort bestätigt; deshalb werden sie neutral als Sensor 1–4 angezeigt. GPS-Datum/-Zeit sind von der bestehenden KNX-Masterzeit getrennt.

### Parameter und Home Assistant

- Wind: Senden bei 3 % Änderung und zyklisch alle 60 Sekunden.
- Regen: bei Regen EIN, keine Einschaltverzögerung, vorhandene Ausschaltverzögerung 10 Minuten, bei Änderung und zyklisch alle 60 Sekunden senden.
- Zeit: interne GPS-Uhr, UTC+1 mit europäischer Sommerzeit, zyklisch einmal pro Minute.
- Weitere Messwerte: bestehende Änderungsschwellen beibehalten; HA liest nach fünf Minuten ohne Aktualisierung nach (`expire 5`).
- Absolute Feuchte: Die neu angelegte Zuordnung 4/0/6 wurde nach ausdrücklicher Nutzerfreigabe gelöst, KO 26 und GA auf 9.029 umgestellt, dieselbe Adresse wieder verbunden und die Applikation erneut geladen.

Das live gespeicherte [HA-Paket](../home-assistant/knx_wetterstation_gira.yaml) enthält 31 native KNX-Sensoren, zwei empfangende GPS-Templates und zwei abgeleitete Anzeigen (Wind gültig, Luftdruck hPa). Die historische Entity-ID `absolute_feuchte_rohwert` bleibt zur Registry-Stabilität bestehen, enthält aber **g/m³**, keinen Rohwert mehr. Eine Automation führt ausschließlich Leseanfragen für GPS-Zeit/-Datum aus. Keine Aktion steuert einen Aktor. KNX und Templates wurden ohne Core-Neustart neu geladen; die HA-Konfigurationsprüfung war erfolgreich.

Das neue Live-Dashboard **Wetter** hat drei Reiter: Wetter, Sonne & Helligkeit, Diagnose & GPS. Alle 33 Stationsausgänge sowie beide abgeleiteten Anzeigen sind in der [Lovelace-Kopie](../home-assistant/lovelace_wetter_gira.yaml) enthalten. Es nutzt native Karten und 24-Stunden-Verläufe.

Bei der visuellen Schlussprüfung wurde eine Reihenfolge-Randbedingung erkannt: Der Wind-Ersatzwert kann vor dem Fehlerstatus eintreffen. Die gültige Windanzeige verwirft deshalb zusätzlich Werte ab 50 m/s beziehungsweise 180 km/h unabhängig vom Statuswort. Der Windverlauf wurde aus der Hauptansicht entfernt, weil vor dieser Korrektur bereits ein falscher Startwert gespeichert worden war. Historische Daten wurden nicht gelöscht. Temperatur- und Helligkeitsverläufe bleiben enthalten. Regressionstests rendern den tatsächlichen Verfügbarkeitsausdruck auch für diese Telegrammreihenfolge sowie für Ausfall der Versorgung und interne Fehler.

### Messwertqualität und Nachweisgrenzen

Nach dem Download wurden zunächst ungültige Initialwerte beobachtet. Die Station sendet bei ungültigem Windsensor unter anderem den Ersatzwert **50 m/s = 180 km/h**. Die Hauptanzeige verwendet deshalb einen Sensor, der bei fehlender Versorgung, ungültigem Wind (Bit 12) oder internem Systemfehler (Bit 15) nicht verfügbar ist. Rohwerte und die vollständigen Statusbits bleiben in der Diagnose sichtbar. Statusbit 0 bedeutet Betauungsschutz, Bit 1 Trocknung; diese sind allein keine Messwertfehler. GPS-Code 252 bedeutet, dass die beiden Fehlerbits 0 und 1 nicht gesetzt sind.

Nach der Anlaufphase live bestätigt: Außentemperatur etwa 13 °C, relative Feuchte etwa 88 %, absolute Feuchte **9,0 g/m³**, Luftdruck etwa **954,4 hPa**, Wind etwa **1,4 km/h**, Versorgung EIN und Sensorstatus 1. Das sind Momentaufnahmen, keine kalibrierten Referenzmessungen. GPS-Position, Höhe und Sonnenazimut wurden nach einer gezielten Leseanfrage mit aktuellen Werten empfangen; die anfänglichen Nullwerte waren noch nicht aktualisiert. Koordinaten bleiben privat. Physischer Regen- und Ausrichtungstest wurde nicht durchgeführt.

Validierung: `python scripts/validate-wetterstation.py` prüft vollständige Anzeigeabdeckung, eindeutige GAs, DPT 9.029, Windfehlerfälle und ausschließlich lesende Automationen. Grundlage: [Gira Wetterstation Plus Handbuch](https://partner.gira.de/data3/20743510.pdf) und [HA KNX](https://www.home-assistant.io/integrations/knx/).

### Offene Punkte nach der Inbetriebnahme

- HA meldet für `sensor.gira_wetter_absolute_feuchte_rohwert` einen Wechsel der Statistik-Einheit von zuvor ohne Einheit auf g/m³. Die Reparaturmeldung wurde beobachtet; die Bereinigung der bisherigen Statistik ist **noch nicht erfolgt**. Die aktuelle Messwertanzeige und die Langzeitstatistik sind getrennt zu beurteilen.
- Das Textobjekt Windorientierung war bei der Prüfung noch leer; die numerische Windrichtung ist separat eingebunden.
- Regenfunktion und Himmelsrichtung der Helligkeitssensoren sind vor Ort noch zu prüfen. Alle Ausgänge sind eingebunden, aber damit nicht sämtliche Messungen physisch abgenommen.
- Rollladen-/Markisenanbindung, Alarmgrenzen und Freigaben bleiben einem späteren Auftrag vorbehalten.

Sitzungsprotokoll einschließlich Fensterdiagnose: [16.10.2026](32_wetter_fenster_inbetriebnahme_2026-10-16.md).

## Ältere Planung für einen späteren Ausbau (nicht umgesetzt)

### Historische Planungsgrundlage

Die ältere Planung verwendete B00D21. Maßgeblich für die oben dokumentierte Inbetriebnahme ist die tatsächlich beobachtete Applikation **B00D29**. Die folgenden Adressen und Schwellen sind Planungsreserve und keine bestätigte aktive Schutzkonfiguration.

### Ziel

Die Wetterstation ist ein zentrales Schutzgerät. Wetter- und Schutzfunktionen sollen direkt in KNX laufen und nicht von Home Assistant abhängig sein.

### Grundwerte

| Funktion | Gruppenadresse | Datentyp | Nutzung |
|---|---:|---|---|
| Außentemperatur | 4/0/0 | 9.001 | Anzeige, Frost, Heizung |
| Windgeschwindigkeit | 4/0/1 | 9.005 | Markisenschutz |
| Regen | 4/0/2 | 1.001 | Markisenschutz |
| Dämmerung | 4/0/3 | 1.001 | Nacht / Außenlicht |
| Helligkeit Ost | 4/1/0 | 9.004 | Beschattung Ost |
| Helligkeit Süd | 4/1/1 | 9.004 | Beschattung Süd |
| Helligkeit West | 4/1/2 | 9.004 | Beschattung West |

### Wetteralarme

| Funktion | Gruppenadresse | Zweck |
|---|---:|---|
| Windwarnung | 4/2/0 | Vorwarnung, noch keine harte Sperre |
| Windalarm | 4/2/1 | Markise sofort einfahren |
| Regenalarm | 4/2/2 | Markise einfahren |
| Frostalarm | 4/2/3 | Schutz- und Infofunktion |

### Beschattungsfreigaben

| Funktion | Gruppenadresse | Zweck |
|---|---:|---|
| Sonne Ost aktiv | 4/3/0 | spätere Automatik |
| Sonne Süd aktiv | 4/3/1 | spätere Automatik |
| Sonne West aktiv | 4/3/2 | spätere Automatik |
| Beschattung Automatik aktiv | 4/3/3 | globale Freigabe |

### Markisenschutz

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

Diese alten Planungswerte wurden nicht freigegeben oder parametriert. Vor einer späteren Umsetzung müssen Herstellergrenzen der konkreten Markise und der Montageort geprüft werden.

### ETS-Hinweis

Bei einem später beauftragten Wetterschutz wäre eine direkte KNX-Verknüpfung zu planen, die auch ohne Home Assistant funktioniert. Dazu sind die tatsächlichen Objekte der Applikation B00D29, die Aktorparameter und die erforderlichen Schutzgrenzen erneut zu prüfen. Solche Verknüpfungen wurden am 16.10. nicht eingerichtet.
