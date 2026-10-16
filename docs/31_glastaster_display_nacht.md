# Glastaster: Display-Zeitsteuerung

Stand: 16.10.2026. Nutzerauftrag: täglich ab 20:00 Uhr dunkle Displays, ab 07:30 Uhr bisheriges Tagesverhalten.

## KNX-Verknüpfung

Die eigene Gruppenadresse `0/5/4 Displays Tag/Nacht (Tag=1)` verbindet ausschließlich die Schaltuhr mit den elf MDT Glastastern II Smart. Sie ist getrennt von `0/0/2 Nachtmodus`, damit keine Heizungs- oder Präsenzmelderfunktionen mit umgeschaltet werden.

| Teilnehmer | Kommunikationsobjekt | Wert |
|---|---|---|
| `1.1.7` Schaltuhr 20-Kanal | 3, Kanal 1, Schalten EIN/AUS | sendet |
| `1.1.20–1.1.28`, `1.1.32`, `1.1.33` | jeweils 106, Tag/Nacht | Tag = 1, Nacht = 0 |

ETS zeigt zwölf Assoziationen: einen Sender und elf Empfänger. Die Objektverknüpfungen waren vor der Änderung frei.

## Zeitprogramm

Der zuvor inaktive Kanal 1 wurde aktiviert, Funktion 1-Bit-Wert senden. Die Gerätebeschriftung ist auf „Displays Tag/Na“ begrenzt.

| Tage | Zeit | Schaltwert |
|---|---|---|
| Montag bis Sonntag | 20:00 | Taste C = AUS = 0, Nacht |
| Montag bis Sonntag | 07:30 | Taste D = EIN = 1, Tag |

Nachholen bei Neustart und Zeitänderung ist aktiviert. Andere Zeitkanäle wurden nicht aktiviert.

Bei der ersten Busprüfung antwortete `1.1.7` tagsüber auf `0/5/4` mit `0/Aus`. Die Schaltuhr war als Master eingerichtet, ihre Zeitobjekte waren unverknüpft. Daher wurde sie auf **Slave** umgestellt, Objekt 2 `Datum und Zeit – Status empfangen` mit der bestehenden Adresse `0/5/2` verbunden und die Uhrzeitabfrage nach Reset aktiviert. Sommer-/Winterzeitberücksichtigung bleibt aktiv. Im Monitor war bereits eine Datumzeitantwort vom vorhandenen Router `1.1.31` auf `0/5/2` sichtbar. Das falsche Ausgangsergebnis wird nicht als erfolgreicher Funktionstest gewertet; die korrigierte Zeitversorgung wird erneut heruntergeladen und geprüft.

Der Router bestätigte auf dem Bus die gültige Datumzeit `2026-10-16 Fr 10:57:17` als `GroupValue_Response`. Am Empfangsobjekt 2 war das Flag „Aktualisieren“ zunächst ausgeschaltet. Es wurde eingeschaltet, damit auch Antworten auf die Reset-Zeitabfrage übernommen werden; anschließend partieller Download nur der Schaltuhr.

Zusätzlich wurde der Modus von „Handeingabe und über Datenbank“ auf **„fest über Datenbank“** gesetzt. Laut [MDT-Handbuch SCN-RTC20.01, Abschnitt 4.5](https://www.mdt.de/download/Archiv/MDT_THB_Zeitschaltuhr_01.pdf) erfordert der bisherige Mischmodus nach jedem Download eine Bestätigung der Schaltzeiten am Gerät. Die feste ETS-Vorgabe vermeidet diesen offenen Handschritt. Alle anderen Zeitkanäle waren im Projekt inaktiv.

## Displayverhalten

Die bestehenden Tagesparameter bleiben unverändert. An Eingang, Schlafzimmer, Bad und Bad Gang wurden die vorhandenen Displayparameter kontrolliert: Tag weiß/Nacht schwarz, Umgebungsanpassung aktiv, Helligkeitsstufe 8, minimale Helligkeit Tag 10 %, Nacht 3 %, Nachtabschaltung im Standby bei Schwelle 2 (dunkel). Es wurde keine dauerhafte zusätzliche Orientierungs-LED eingeschaltet.

Die 3 % sind bei aktiver Umgebungsanpassung eine Mindesthelligkeit und kein jederzeit fester Wert. Bei Dunkelheit kann die vorhandene Standby-Nachtabschaltung das Display ausschalten. Das genaue Verhalten beschreibt das [MDT-Handbuch der Serie .01](https://www.mdt.de/download/MDT_THB_Smart_Taster_01_R20.pdf). Ein physischer Sichttest ist zusätzlich erforderlich.

## Inbetriebnahme und Nachweise

- Gruppenadresse und alle zwölf Verknüpfungen in ETS angelegt und geprüft.
- ETS bestätigt `Programmieren(Appl.): Abgeschlossen` für alle elf Glastaster `1.1.20–1.1.28`, `1.1.32`, `1.1.33` sowie die Schaltuhr `1.1.7`. Auch der anschließende Download der Zeitempfangsparameter und der partielle Flag-Download waren erfolgreich.
- Auch der abschließende Applikationsdownload der Schaltuhr mit fester ETS-Zeitvorgabe ist in der Historie erfolgreich abgeschlossen.
- Nach dem abschließenden Download: Reset-Zeitabfrage auf `0/5/2`, Datumzeitantworten der vorhandenen Teilnehmer und anschließend selbstständiges `GroupValue_Write` von **`1.1.7` auf `0/5/4` mit Wert `1/Ein`** gegen 11:01 Uhr. Dies bestätigt die aktuelle Tagesumschaltung durch die Schaltuhr, ohne manuell einen Tagwert zu schreiben.
- Noch offen: Sichtprüfung der Nacht-/Taganzeige am realen Taster und Beobachtung der regulären Umschaltzeitpunkte 20:00/07:30 Uhr. Der aktuelle Busnachweis ersetzt diese Prüfung nicht.

Keine Licht-, Rollladen-, Tor- oder Heizungsbefehle wurden für diese Displayeinrichtung ausgelöst.
