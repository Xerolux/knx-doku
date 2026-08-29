# 22 – Aktueller ETS-Programmierstand

Stand: 29.08.2026

## Bedeutung „Programmieren notwendig“

ETS zeigt ein Gerät unter **Programmieren notwendig**, wenn seit dem letzten Download Parameter, Kommunikationsobjekte, Verknüpfungen oder relevante Applikationsdaten geändert wurden. Die Anzeige bedeutet nicht automatisch einen Gerätefehler.

## Sichtbarer Stand im ETS-Screenshot

| Physikalische Adresse | Sichtbarer Status am 29.08.2026 | Folgerung |
|---:|---|---|
| `1.1.10`, `1.1.20–1.1.31`, `1.1.41` | in allen fünf sichtbaren Statusspalten grüne Häkchen | kein pauschaler Download allein aufgrund des Screenshots; Funktionen und Telegramme trotzdem prüfen |
| `1.1.32`, `1.1.33` | in den fünf sichtbaren Statusspalten Striche | Raum, Bedienfunktion, Parameter und Gruppenadressverknüpfungen festlegen, danach vollständig programmieren |
| `1.1.40` | in den fünf sichtbaren Statusspalten Striche | Applikation, Parameter, Wetter-Gruppenadressen und Programmierstand prüfen |

Der Screenshot enthält keine Spaltenüberschriften und keine Kommunikationsobjekte. Die Symbole werden deshalb nur als sichtbarer ETS-Status dokumentiert, nicht als Nachweis einer vollständigen oder funktionierenden Gruppenadressverknüpfung.

## Sichtbarer Gruppenadressstand

Der erste Gruppenadress-Screenshot vom 29.08.2026 zeigt 12 Hauptgruppen: `0` bis `10` sowie `13`. Nach dem Import ist zusätzlich Hauptgruppe `11 Wärmepumpe` sichtbar. Der aufgeklappte Bereich zeigt die Mittelgruppen `11/0 Objekte 1–230`, `11/1 Objekte 292–499` und `11/3 PV und Batterie`. Damit ist die Struktur der Wärmepumpen-Importdatei vorhanden. Einzeladressen, DPTs und konkrete Objektverknüpfungen sind in dieser Ansicht nicht nachprüfbar und müssen durch Aufklappen oder einen neuen ETS-Export bestätigt werden. Der ältere Suchordnerstand zeigte 117 Einträge unter „Addresses not assigned“; diese Zahl ist kein Gesamtzähler.

Die Abstellkammer ist ein eigener neunter Raum und weder das Badezimmer noch Bad vorne. Für sie sind ausschließlich `12/0/0 Abstellkammer Licht Schalten` und `12/0/1 Abstellkammer Licht Status` vorgesehen. Die beiden Adressen müssen noch über `gruppenadressen-abstellkammer.xml` importiert und anschließend mit dem bestätigten Taster- und Aktorkanal verknüpft werden.

## Nach den nächsten Gruppenadressänderungen programmieren

| Physikalische Adresse | Gerät | Grund |
|---:|---|---|
| `1.1.32`, `1.1.33` | MDT Glastaster | nach Festlegung von Raum, Bedienfunktion und den dazugehörigen Gruppenadressen |
| `1.1.40` | Gira Wetterstation Plus | nach Prüfung beziehungsweise Zuordnung der Wetterobjekte und Gruppenadressen |
| jeweils betroffene Taster `1.1.20–1.1.33` | MDT Glastaster | nur wenn Parameter, Licht-, Rollladen-, Status-, Display- oder Wärmepumpen-Verknüpfungen tatsächlich geändert werden |
| jeweils betroffene Aktoren und Sensoren | KNX-Teilnehmer | nur wenn deren Parameter oder Kommunikationsobjektverknüpfungen geändert werden |
| `1.1.8` | MDT Logikmodul | erst nach Umsetzung des gemeinsamen Ganglichtstatus `1/4/5` |

Geräte, an denen keine Parameter oder Verknüpfungen geändert wurden, müssen nicht allein wegen ihrer Position in einer Geräteübersicht erneut programmiert werden.

## RF-Fenstergriffe

Die RF+-Fenstergriffe `1.1.11` bis `1.1.19` werden nur programmiert, wenn deren Parameter, Gruppenadressen oder Secure-Zuordnung tatsächlich geändert wurden. Batteriebetriebene RF-Geräte müssen für eine Übertragung gegebenenfalls aufgeweckt beziehungsweise in den Programmiermodus versetzt werden.

## Sicherheitsmodul

Blockiert das MDT SCN-SAFE.01 den ETS-Zugriff, wird für geplante Arbeiten die zeitlich begrenzte Programmierfreigabe am Gerät aktiviert. Nach Abschluss ist zu kontrollieren, dass der Schutzbetrieb wieder aktiv ist.

## Empfohlene Reihenfolge

1. Raum und Bedienfunktion der Glastaster `1.1.32` und `1.1.33` festlegen.
2. Kommunikationsobjekte mit den bestehenden raum- und funktionsbezogenen Gruppenadressen verbinden.
3. Wärmepumpen-Adressen nur an passende Anzeige- oder Bedienobjekte mit identischem DPT anbinden.
4. Die betroffenen Glastaster und weitere tatsächlich geänderte Teilnehmer vollständig programmieren.
5. Wetterstation `1.1.40` nach Prüfung von Applikation, Parametern und Verknüpfungen programmieren.
6. Nach Einrichtung des Sammelstatus das Logikmodul `1.1.8` programmieren.
7. Im Gruppenmonitor alle Befehle und Rückmeldungen prüfen.
8. Gruppenadressen neu aus ETS exportieren und die älteren Repository-Snapshots ersetzen.
9. ETS-Projekt anschließend lokal mit Datum sichern.

## Funktionsprüfung

- Einzellicht je Raum
- beide Ganglichter über `1/4/4`
- Bewegungsmelder mit 3 Minuten Nachlaufzeit am Tag und 1 Minute in der Nacht
- Zentral Licht über `0/4/0`
- Einzelbedienung aller Rollladen
- Zentral Auf/Ab über `0/1/0`
- Zentral Stopp über `0/1/1`
- Positionsanzeige der Rollladen
- Datum, Uhrzeit und interne Temperatur der Glastaster

Dieses öffentliche Dokument enthält keine Bilder, Passwörter, PINs, Schlüssel oder privaten ETS-Projektdateien.
