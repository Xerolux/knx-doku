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
- Zentral-Aus, Panik-, Frost-, Wind- und Markisenschutz testen

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

Nach jeder größeren Änderung wird ein neuer datierter Sicherungsstand erstellt.

## Regelmäßige Kontrolle

- RCD-Prüftasten nach Herstellerangaben betätigen
- Schaltschrank auf ungewöhnliche Erwärmung und Verfärbungen prüfen
- Busspannung und Diagnosedaten kontrollieren
- Markisen- und Wetterschutz vor der Sturmsaison testen
- ETS-Projekt und Dokumentation nach Umbauten aktualisieren
- lockere Beschriftungen oder provisorische Markierungen ersetzen

## Noch offene Projektdaten

- exakte Typen und Bemessungswerte der beiden RCDs
- Typ, Charakteristik und Bemessungsstrom aller LS-Schalter
- vollständige Leitungs- und Klemmenzuordnung
- Funktion und physikalische Adresse des zweiten MDT IP-Routers
- tatsächliche Belegung des zweiten Heizungsaktors
- Zuordnung der weiteren Kanäle I bis X des Schaltaktors
- 24-V-Verbraucher am EARU-Netzteil
- genaue KNX-Versorgung der Router, Visualisierung und Logikgeräte
- Herstellerunterlagen und aktuelle Firmwarestände
- fertiges Mess- und Abnahmeprotokoll
