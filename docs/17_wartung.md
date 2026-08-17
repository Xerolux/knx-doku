# 17 – Abnahme, Wartung und offene Punkte

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

Das Sicherheitsmodul `1.1.9` blockiert im aktiven Schutzbetrieb verbindungsorientierte ETS-Zugriffe wie Programmieren und Entladen. Meldet ETS **„Verbindung verweigert“**, ist deshalb zuerst das MDT SCN-SAFE.01 zu prüfen.

Vorgehen bei einer geplanten Programmierung:

1. Am Sicherheitsmodul die zeitlich begrenzte Freigabe über die Taste **2h** aktivieren.
2. Alarmanzeige bei Bedarf mit **Clear** quittieren.
3. ETS-Verbindung erneut aufbauen und Geräte programmieren.
4. Nach Abschluss kontrollieren, dass die Schutzfunktion wieder aktiv ist.

Die Freigabe darf nur für geplante Arbeiten genutzt werden. Ein dauerhaft deaktivierter Schutz widerspricht dem Zweck des Sicherheitsmoduls.

## Zentrale Lichtfunktion prüfen

- Taster `1.1.20`: linke Taste sendet auf `0/4/0` den Wert 1
- Taster `1.1.20`: rechte Taste sendet auf `0/4/0` den Wert 0
- Schaltaktor `1.1.3`: Objekt 289 ist mit `0/4/0` verbunden
- nur Lichtkanäle nehmen an der Zentralfunktion teil
- Steckdosen, technische Verbraucher und Reservekanäle reagieren nicht
- Einzelbedienung der Lichtkreise funktioniert weiterhin

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
- Zentral Licht, Hauszustände, Frost-, Wind- und Markisenschutz testen
- Programmierstatus von `1.1.29` und `1.1.40` kontrollieren
- ungenutzte Gruppenadresse `0/5/3 Aktuelle Werte empfangen` prüfen und gegebenenfalls löschen

## Datensicherung

Mindestens folgende Dateien werden gemeinsam archiviert:

```text
ETS-Projektdatei
Gruppenadress-Export
physikalische Adressliste
Stromkreis- und Klemmenplan
Mess- und Abnahmeprotokoll
Geräte- und Firmwareliste
Home-Assistant-Konfiguration
```

Nach jeder größeren Änderung wird ein neuer datierter Sicherungsstand erstellt. Persönliche ETS-Projektdateien und Schlüsselbunddateien werden nicht in das öffentliche GitHub-Repository eingecheckt.

## Regelmäßige Kontrolle

- RCD-Prüftasten nach Herstellerangaben betätigen
- Schaltschrank auf ungewöhnliche Erwärmung und Verfärbungen prüfen
- Busspannung und Diagnosedaten kontrollieren
- NTP-Synchronisierung und Zeittelegramme kontrollieren
- Markisen- und Wetterschutz vor der Sturmsaison testen
- ETS-Projekt und Dokumentation nach Umbauten aktualisieren
- lockere Beschriftungen oder provisorische Markierungen ersetzen

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
- 24-V-Verbraucher am EARU-Netzteil
- genaue KNX-Versorgung der Router, Visualisierung und Logikgeräte
- Herstellerunterlagen und aktuelle Firmwarestände
- fertiges Mess- und Abnahmeprotokoll
