# 22 – Aktueller ETS-Programmierstand

Stand: 04.08.2026

## Bedeutung „Programmieren notwendig“

ETS zeigt ein Gerät unter **Programmieren notwendig**, wenn seit dem letzten Download Parameter, Kommunikationsobjekte, Verknüpfungen oder relevante Applikationsdaten geändert wurden. Die Anzeige bedeutet nicht automatisch einen Gerätefehler.

## Nach den aktuellen Änderungen vollständig programmieren

| Physikalische Adresse | Gerät | Grund |
|---:|---|---|
| `1.1.3` | MDT Schaltaktor | Einzeladressen der Lichtkanäle, beide Ganglichter und Zentral Licht |
| `1.1.4` | MDT JAL-0810M.02 | Rollladenstatus, Zentralobjekte und Kanalparameter |
| `1.1.20` | MDT Glastaster Eingang | Zentral Licht und Zentral Rollladen |
| betroffene Taster `1.1.21–1.1.28` | MDT Glastaster | Licht-, Rollladen-, Status- und Displayänderungen |
| `1.1.30` | Gang Bewegungsmelder | Ausgang `1/4/4`, Nachlaufzeiten und Helligkeitssteuerung |
| `1.1.8` | MDT Logikmodul | erst nach Umsetzung des gemeinsamen Ganglichtstatus `1/4/5` |

Geräte, an denen keine Parameter oder Verknüpfungen geändert wurden, müssen nicht allein wegen ihrer Position in einer Geräteübersicht erneut programmiert werden.

## RF-Fenstergriffe

Die RF+-Fenstergriffe `1.1.11` bis `1.1.19` werden nur programmiert, wenn deren Parameter, Gruppenadressen oder Secure-Zuordnung tatsächlich geändert wurden. Batteriebetriebene RF-Geräte müssen für eine Übertragung gegebenenfalls aufgeweckt beziehungsweise in den Programmiermodus versetzt werden.

## Sicherheitsmodul

Blockiert das MDT SCN-SAFE.01 den ETS-Zugriff, wird für geplante Arbeiten die zeitlich begrenzte Programmierfreigabe am Gerät aktiviert. Nach Abschluss ist zu kontrollieren, dass der Schutzbetrieb wieder aktiv ist.

## Empfohlene Reihenfolge

1. Schaltaktor `1.1.3` vollständig programmieren.
2. Jalousieaktor `1.1.4` vollständig programmieren.
3. Bewegungsmelder `1.1.30` vollständig programmieren.
4. Betroffene Glastaster vollständig programmieren.
5. Nach Einrichtung des Sammelstatus das Logikmodul `1.1.8` programmieren.
6. Im Gruppenmonitor alle Befehle und Rückmeldungen prüfen.
7. Fahrzeitmessung der verwendeten Rollladenkanäle starten.
8. ETS-Projekt anschließend lokal mit Datum sichern.

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
