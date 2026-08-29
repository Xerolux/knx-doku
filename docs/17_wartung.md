# 17 – Abnahme, Wartung und offene Punkte

Stand: 29.08.2026

## Vor der Inbetriebnahme

- Stromkreiszuordnung mit der tatsächlichen Verdrahtung abgleichen
- Neutralleiter jeder RCD-Gruppe eindeutig zuordnen
- Phasenverteilung und RCD-Bemessungsstrom prüfen
- Leiterquerschnitte, Verlegearten und Absicherung dokumentieren
- Einspeisegruppen und Kontaktbelastungen der Aktoren kontrollieren
- Klemmen, Leitungen und Geräte dauerhaft beschriften
- physikalische KNX-Adressen mit der ETS-Dokumentation abgleichen
- Funktion des zweiten IP-Routers festlegen
- Heizungsaktor 2 vollständig zuordnen oder als Reserve kennzeichnen
- Reservekanäle gegen unbeabsichtigte Nutzung sperren

## MDT SCN-SAFE.01 und „Verbindung verweigert“

Das Sicherheitsmodul `1.1.9` blockiert im aktiven Schutzbetrieb verbindungsorientierte ETS-Zugriffe wie Programmieren und Entladen. Meldet ETS **Verbindung verweigert**, ist zuerst das MDT SCN-SAFE.01 zu prüfen.

Vorgehen bei einer geplanten Programmierung:

1. Am Sicherheitsmodul die zeitlich begrenzte Freigabe über die Taste **2h** aktivieren.
2. Alarmanzeige bei Bedarf mit **Clear** quittieren.
3. ETS-Verbindung erneut aufbauen und Geräte programmieren.
4. Nach Abschluss kontrollieren, dass die Schutzfunktion wieder aktiv ist.

Die Freigabe darf nur für geplante Arbeiten genutzt werden. Ein dauerhaft deaktivierter Schutz widerspricht dem Zweck des Sicherheitsmoduls.

Die Gruppenadressen des Sicherheitsmoduls liegen ausschließlich unter `10/0`; Rauchwarnmelder-Planung liegt unter `10/1`. Vor jedem Gruppenadressimport wird `scripts/validate-group-addresses.ps1` ausgeführt. Der dokumentierte Vorfall, die wiederhergestellten Objekte 227 bis 231 und die ETS-Nacharbeit stehen in [26 – SCN-SAFE-Adressreparatur](26_scn_safe_adressreparatur.md).

## Zentrale Lichtfunktion prüfen

- Taster `1.1.20`: linke Taste sendet auf `0/4/0` den Wert `1`
- Taster `1.1.20`: rechte Taste sendet auf `0/4/0` den Wert `0`
- Schaltaktor `1.1.3`: Objekt 289 ist mit `0/4/0` verbunden
- nur Lichtkanäle nehmen an der Zentralfunktion teil
- Steckdosen, technische Verbraucher und Reservekanäle reagieren nicht
- Einzelbedienung der Lichtkreise funktioniert weiterhin
- individuelle Schalt- und Statusobjekte des Schaltaktors sind mit den tatsächlichen Raumadressen verbunden
- Terrassenlicht am Taster `1.1.27` besitzt eine geprüfte Gruppenadresse

## Rollladen-Inbetriebnahme prüfen

### Zentrale Objekte des JAL

```text
Objekt 0 Rollladen Auf/Ab          -> 0/1/0
Objekt 1 Lamellenverstellung/Stopp -> frei
Objekt 2 Stopp                     -> 0/1/1
```

Bei A, B, C, D, G und H muss `Zentrale Objekte = nur Auf/Ab` eingestellt sein. Kanal E und F werden erst nach bestätigter realer Funktion freigegeben.

### Einzelne Fahr- und Statusadressen

| Kanal | Funktion | Auf/Ab | Stopp | Position Status |
|---|---|---:|---:|---:|
| A | Schlafzimmer links | `2/2/0` | `2/2/1` | `2/2/3` |
| B | Schlafzimmer rechts | `2/2/10` | `2/2/11` | `2/2/13` |
| C | Arbeitszimmer | `2/1/0` | `2/1/1` | `2/1/3` |
| D | Wohnzimmer links | `2/0/0` | `2/0/1` | `2/0/3` |
| G | Markise | `2/4/0` | `2/4/1` | `2/4/3` |
| H | Wohnzimmer rechts | `2/0/10` | `2/0/11` | `2/0/13` |

Prüfpunkte:

- `Status aktuelle Position = aktiv`
- `Status senden = nach Fahrende`
- JAL-Statusobjekt und Glastaster-Statusobjekt besitzen dieselbe 1-Byte-Gruppenadresse
- JAL und betroffene Glastaster vollständig programmiert
- Fahrzeitmessung je Kanal durchgeführt
- lokale Handbedienung Auf, Ab und Stopp funktioniert
- langer Tastendruck fährt, kurzer Tastendruck stoppt
- obere Endlage zeigt ungefähr `0 %`
- untere Endlage zeigt ungefähr `100 %`
- Zentral Auf/Ab über `0/1/0` funktioniert
- Zentral Stopp über `0/1/1` funktioniert
- Telegramme sind im ETS-Gruppenmonitor sichtbar
- keine unerwartete Sperre, Alarm- oder Fensterfunktion ist aktiv

Details stehen in [20 – Rollladen: ETS-Zuordnung, Inbetriebnahme und Prüfung](20_rollladen_inbetriebnahme.md).

## Zeitserver prüfen

- E-Mail- und Zeitserver-Applikation `1.1.31` ist programmiert
- NTP-Server, Gateway, DNS, Zeitzone und Sommer-/Winterzeit sind korrekt eingestellt
- nur ein Gerät sendet als Zeitmaster
- Telegramme auf `0/5/0`, `0/5/1` oder bevorzugt `0/5/2` sind im Gruppenmonitor sichtbar
- bei Störungen Objekt 53 **NTP-Zeitserver – Fehler** prüfen
- Uhrzeit, Datum und Temperaturanzeige am Taster `1.1.20` kontrollieren

## Elektrische Prüfwerte

Die Prüf- und Messwerte gehören in das Abnahmeprotokoll:

| Prüfung | Ergebnis / Ablage |
|---|---|
| Durchgängigkeit des Schutzleiters | offen |
| Isolationswiderstand | offen |
| Schleifenimpedanz / Abschaltbedingungen | offen |
| RCD-Auslösezeit | offen |
| RCD-Auslösestrom | offen |
| Drehfeld | offen |
| Funktionsprüfung aller Stromkreise | offen |
| Beschriftung geprüft | offen |

## KNX-Abnahme

- ETS-Projekt vollständig sichern
- physikalische Adressen dokumentieren
- Gruppenadressen exportieren
- Applikationsprogramme und Parameterstände sichern
- Gerätebezeichnungen in ETS und Schaltschrank angleichen
- Diagnose der Busspannungsversorgung prüfen
- Telegrammverkehr und Linienstatus kontrollieren
- Ausfall von Home Assistant testen: Grundfunktionen müssen weiterhin funktionieren
- Zentral Licht, Zentral Rollladen, Hauszustände, Frost-, Wind- und Markisenschutz testen
- Programmierstatus von `1.1.29` und `1.1.40` kontrollieren
- ungenutzte Gruppenadresse `0/5/3 Aktuelle Werte empfangen` prüfen und gegebenenfalls löschen

## Datensicherung und öffentliche Dokumentation

Mindestens folgende Dateien werden intern gemeinsam archiviert:

```text
ETS-Projektdatei
Gruppenadress-Export
physikalische Adressliste
Stromkreis- und Klemmenplan
Mess- und Abnahmeprotokoll
Geräte- und Firmwareliste
Home-Assistant-Konfiguration
```

Nach jeder größeren Änderung wird ein neuer datierter Sicherungsstand erstellt.

Nicht in das öffentliche GitHub-Repository gehören:

- ETS-Projektdateien mit privaten Anlagendaten
- Schlüsselbund- oder Zertifikatsdateien
- Passwörter, PINs, Tokens oder Zugangsdaten
- private IP-Konfigurationen, sofern sie nicht zwingend für die öffentliche Dokumentation benötigt werden
- Fotos oder Screenshots aus ETS, Schaltschrank oder Wohnhaus
- personenbezogene Dokumente

## Regelmäßige Kontrolle

- RCD-Prüftasten nach Herstellerangaben betätigen
- Schaltschrank auf ungewöhnliche Erwärmung und Verfärbungen prüfen
- Busspannung und Diagnosedaten kontrollieren
- NTP-Synchronisierung und Zeittelegramme kontrollieren
- Markisen- und Wetterschutz vor der Sturmsaison testen
- ETS-Projekt und Dokumentation nach Umbauten aktualisieren
- lockere Beschriftungen oder provisorische Markierungen ersetzen
- Rollladen-Endlagen, Fahrzeiten und Positionsanzeige nach Motor- oder Behangänderungen erneut prüfen

## Noch offene Projektdaten

- exakte Typen und Bemessungswerte der beiden RCDs
- Typ, Charakteristik und Bemessungsstrom aller LS-Schalter
- vollständige Leitungs- und Klemmenzuordnung
- Funktion und physikalische Adresse des zweiten MDT IP-Routers
- tatsächliche Belegung des zweiten Heizungsaktors
- Raumzuordnung der Glastaster `1.1.21` bis `1.1.28`
- Einbauort und genaue Hardwarevariante des OpenKNX RaumControllers `1.1.29`
- genaue Bestellnummer und Raumzuordnung des Präsenzmelders `1.1.30`
- Zuordnung der weiteren Kanäle I bis X des Schaltaktors
- individuelle Lichtkanäle des Schaltaktors vollständig verbinden
- Terrassenlicht am Glastaster `1.1.27` zuordnen
- reale Funktion der JAL-Kanäle E und F klären
- Statusverknüpfungen der JAL-Kanäle C, D, G und H abschließend prüfen
- 24-V-Verbraucher am EARU-Netzteil
- genaue KNX-Versorgung der Router, Visualisierung und Logikgeräte
- Herstellerunterlagen und aktuelle Firmwarestände
- fertiges Mess- und Abnahmeprotokoll
