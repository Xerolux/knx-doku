# 02 – Geräteliste

## Vorhandene KNX-Komponenten

### Infrastruktur

- Enertex KNX PowerSupply 960³ – KNX-Busspannungsversorgung mit Diagnose
- 2 × MDT SCN-IP100.03 – KNX IP Router
- MDT SCN-IP100.03 Zusatzapplikation `1.1.31` – E-Mail- und Zeitserverfunktion auf einem vorhandenen Router
- Gira 5114 00 – RF Multi/TP Medienkoppler mit automatisch angelegtem RF-Segment unter Linie 1.1
- MDT SCN-LOG1.02 – Logikmodul, `1.1.8`
- MDT SCN-SAFE.01 – Sicherheitsmodul, `1.1.9`
- MDT SCN-RTC20.01 – 20-Kanal-Schaltuhr, `1.1.7`

### Aktoren

- MDT AKS-2416.03 – Schaltaktor 24-fach, `1.1.3`
- MDT AMI-1216.02 – Schaltaktor 12-fach mit Strommessung
- MDT AZI-0616.01 – Schaltaktor 6-fach mit Wirkleistungsmessung
- MDT JAL-0810M.02 – Jalousieaktor 8-fach, `1.1.4`
- 2 × MDT AKH-0800.02 – Heizungsaktor 8-fach, `1.1.5` und `1.1.6`
- MDT RF-AKK2UP.01 – KNX RF+ Schaltaktor 2-fach UP

### Lichtreserve

- MDT AKD-0424V.02 – RGBW LED Controller 4 Kanal
- MDT AKD-0424R.02 – RGBW LED Controller 4 Kanal REG
- MDT SCN-DALI64.03 – DALI Control IP
- Enertex LED PowerSupply 160-24 – 24-V-LED-Netzteil

### Sensoren und Bedienung

| Adresse | Gerät | Aktueller Stand |
|---:|---|---|
| 1.1.20 | MDT BE-GT2Tx.01 / Glastaster II Smart mit Temperatursensor | Eingang; Zentral Licht sowie Zeit-/Temperaturanzeige werden eingerichtet |
| 1.1.21–1.1.28 | MDT Glastaster II Smart mit Temperatursensor | im ETS-Projekt vorhanden und programmiert; Raumzuordnung noch dokumentieren |
| 1.1.29 | OpenKNX RaumController | Raumklimaobjekte verbunden und am 17.08.2026 erfolgreich im Gruppenmonitor geprüft; VOC und Helligkeit lieferten beim Test noch `0` |
| 1.1.30 | MDT Präsenzmelder 360° KLR 4S | im ETS-Projekt vorhanden; genaue Bestellnummer und Raumzuordnung prüfen |
| 1.1.40 | Gira Wetterstation Plus, ETS-Applikation B00D21 | im ETS-Projekt; vollständigen Programmierstand prüfen |
| 1.1.41 | Gira KNX Rauchwarnmelder, ETS-Applikation C01602 | Rauchalarm und Störmeldungen |

Zusätzlich sind MDT KNX RF Fenstergriffe vorgesehen beziehungsweise vorhanden.

### Visualisierung

- MDT VC-EASY.02 – VisuControl Easy II, `1.1.10`
- Home Assistant als bevorzugte Visualisierung

### Hilfsspannungen

- EARU DR-30-24 – Netzteil 24 V DC / 1,5 A

## Festgelegte Zeitquelle

Die E-Mail- und Zeitserver-Applikation `1.1.31` eines MDT SCN-IP100.03 ist der vorgesehene NTP-basierte KNX-Zeitmaster. Die Router-Applikation und die Zeitserver-Applikation können auf demselben realen Gerät laufen, besitzen in ETS aber getrennte physikalische Adressen.

Die MDT SCN-RTC20.01 wird für Datum und Uhrzeit als Slave betrieben. Home Assistant und ein zweiter IP-Router dürfen nicht parallel als weiterer Zeitmaster senden.

## Aktuell umgesetzte Funktion

- `0/4/0 Alle Lichter schalten` steuert die Zentralfunktion des MDT AKS-2416.03.
- Taster `1.1.20` sendet über Tasten 1/2 Ein und Aus auf dieselbe 1-Bit-Gruppenadresse.
- `0/5/0`, `0/5/1` und `0/5/2` sind für Uhrzeit, Datum und den kombinierten Datum-/Uhrzeitwert angelegt.
- Für den Glastaster wird bevorzugt der kombinierte DPT 19.001 über `0/5/2` verwendet.

## Noch zu bestätigen

- Aufgabe und physikalische Adresse des zweiten MDT IP-Routers
- Raumzuordnung der Glastaster `1.1.21` bis `1.1.28`
- Einbauort und genaue Hardwarevariante des OpenKNX RaumControllers `1.1.29`
- genaue Bestellnummer und Raumzuordnung des Präsenzmelders `1.1.30`
- vollständiger Programmierstand von `1.1.29` und `1.1.40`
- tatsächliche Belegung des zweiten Heizungsaktors
- Einbauort der noch nicht montierten Reservekomponenten
- Verbraucher und Absicherung der 24-V-Versorgung
- genaue Typ- und Seriennummern aller eingebauten Geräte

## Planungsentscheidung

Das Licht wird in der ersten Ausbaustufe nur ein- und ausgeschaltet. DALI und RGBW werden vorbereitet, aber nicht zwingend sofort in Betrieb genommen. Reservegeräte und Reservekanäle gelten erst nach dokumentierter Verdrahtung als betriebsbereit.
