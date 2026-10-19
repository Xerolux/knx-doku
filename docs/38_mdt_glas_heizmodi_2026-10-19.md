# 38 – Heizmodi an den MDT-Glastastern, 19.10.2026

Nutzerauftrag: Die Raum-Betriebsart direkt am MDT-Glastaster wählen und beibehalten können. Bestehende Temperatur-, Licht- und Rollladenfunktionen bleiben erhalten.

## Bedienung und Projektierung

Neue Funktion „Heizmodus“ als Zwei-Tasten-Betriebsartenumschaltung mit Komfort, Standby, Nacht und Frostschutz. Statusanzeige: HVAC Mode; Umschaltung berücksichtigt das Statusobjekt. Umschaltung mit Anschlag, ohne Überlauf; keine zusätzliche Langdruckfunktion.

| Raum | Glastaster | Tasten / Ebene | Modus senden / Status-KO | Gruppenadresse, DPT 20.102 |
|---|---|---|---|---|
| Gang | 1.1.21 | T5/6, Ebene 1 | 20 / 21 | 3/4/2 |
| Küche | 1.1.22 | T5/6, Ebene 1 | 20 / 21 | 3/2/2 |
| Wohnzimmer | 1.1.23 | T5/6, Ebene 1 | 20 / 21 | 3/0/2 |
| Arbeitszimmer | 1.1.24 | T7/8, Ebene 2 oben | 30 / 31 | 3/3/2 |
| Schlafzimmer | 1.1.25 | T9/10, Ebene 2 Mitte | 40 / 41 | 3/5/2 |
| Bad | 1.1.32 | T7/8, Ebene 2 oben | 30 / 31 | 3/6/2 |

Arbeitszimmer und Bad erhalten dafür eine zweite Ebene. Ebenenwechsel über die versteckten unteren Tasten; Rückkehr zur Startebene nach zehn Sekunden ohne Berührung. Die bestehende zweite Ebene im Schlafzimmer und deren Temperaturfunktion T7/8 bleiben erhalten.

HVAC-Werte: 1 = Komfort, 2 = Standby, 3 = Nacht, 4 = Frostschutz. Frostschutz ist der verfügbare reduzierte Raumbetrieb mit weiterhin aktivem Frostschutz; am AKH sind 7 °C eingestellt. Er bedeutet keine vollständige elektrische Abschaltung. Wert 0 wird nicht als „Aus“ angeboten.

## Heizungsaktoren

Die vorhandenen raumbezogenen Betriebsartadressen sind an sämtlichen zugehörigen Ventilreglern verknüpft: Wohnzimmer 1.1.5 G/H und 1.1.6 A, Schlafzimmer 1.1.5 B/C, Arbeitszimmer 1.1.5 E/F, Gang 1.1.5 D, Bad 1.1.5 A und Küche 1.1.6 B. Die acht Betriebsartobjekte von 1.1.5 und beide aktiven von 1.1.6 wurden im gefilterten ETS-Objektverzeichnis abgeglichen.

In beiden AKH ist „Betriebsarten und Sollwerte nach Busspannungswiederkehr wiederherstellen“ aktiviert und erfolgreich geladen. Ein physischer Busspannungs-Ausfalltest wurde nicht durchgeführt. Andere Busbefehle können die Betriebsart weiterhin ändern; eine Sperre gegen andere Bediengeräte ist nicht vorgesehen.

„Status auf Betriebsartvorwahl senden“ ist je Raum an genau einem Kanal aktiviert. ETS ersetzt dabei das bisherige Betriebsartobjekt und entfernt dessen Gruppenverknüpfung. Nach ausdrücklicher Nutzerbestätigung wurden die sechs betroffenen Adressen identisch wiederhergestellt. Diese Objekte besitzen nun Kommunikation, Lesen, Schreiben und Übertragen. Die übrigen Kanäle desselben Raums empfangen weiter den Modus, antworten aber nicht zusätzlich. Zyklisches Modussenden bleibt deaktiviert. Das separate rohe HVAC-Statusobjekt ist nicht auf die Modusadresse gelegt.

| Raum | Modus-Rückmeldung und Leseantwort |
|---|---|
| Bad | 1.1.5 A, KO 10 → 3/6/2 |
| Schlafzimmer | 1.1.5 B, KO 30 → 3/5/2 |
| Gang | 1.1.5 D, KO 70 → 3/4/2 |
| Arbeitszimmer | 1.1.5 E, KO 90 → 3/3/2 |
| Wohnzimmer | 1.1.5 G, KO 130 → 3/0/2 |
| Küche | 1.1.6 B, KO 30 → 3/2/2 |

## Lieferung und Prüfung

- Alle sechs Tasterfunktionen einschließlich beider Objektverknüpfungen im ETS-Projekt eingerichtet.
- Erster Downloadversuch gegen 19:29 Uhr wegen verweigerter Verbindung fehlgeschlagen. Nach erneuter Programmierfreigabe des Nutzers wurden alle sechs Glastaster erfolgreich mit „Programmieren (Appl.): Abgeschlossen“ geladen. Die ETS-Historie bestätigt anschließend auch für 1.1.5 und 1.1.6 abgeschlossene Applikationsdownloads; keine aktive Operation mehr.
- Nach dem Download sendete 1.1.5 gegen 20:05:42–20:05:45 Uhr Modusrückmeldungen für Bad, Arbeitszimmer, Schlafzimmer, Wohnzimmer und Gang. 1.1.6 sendete die Küchenrückmeldung um 20:08:25 Uhr.
- Bad: Leseantwort auf 3/6/2 um 20:09:32 Uhr von 1.1.5 mit Wert 2 / Standby. Testweise Wert 4 / Frostschutz um 20:10:32 Uhr geschrieben. 1.1.5 meldete auf 3/6/5 um 20:10:33 Uhr **7 °C** aktuellen Sollwert. Leseantwort um 20:10:46 Uhr bestätigte Wert 4. Anschließend um 20:11:53 Uhr den zuvor gelesenen Modus 2 / Standby wiederhergestellt; erneute Leseantwort um 20:12:07 Uhr bestätigte Standby. Die Adresse 3/6/0 blieb davon als Basis-Komfortwert getrennt.
- Küche: Leseantwort auf 3/2/2 um 20:14:07 Uhr von 1.1.6 mit Wert 2 / Standby bestätigt.
- Physischer Tastentest am Gang (Nacht, anschließend zurück zu Standby) angefragt, noch nicht bestätigt. Displaydarstellung, tatsächliche Tastentelegramme und mechanische Ventilstellung sind damit noch nicht physisch abgenommen.
- Kein Test mit sämtlichen geschlossenen Ventilen. Offene Frage zur Pumpenabstimmung bleibt gemäß [Raumregelung](27_fbh_mdt_raumregelung.md) bestehen.
- Die separate Gang-Bewegungsmelderdiagnose wurde anschließend fortgesetzt: Nach Korrektur des Melders zwei echte EIN-/AUS-Zyklen mit Wiederanlauf bestanden; expliziter Nachtzustand und Langzeitbeobachtung bleiben offen. [Prüfprotokoll](21_ganglicht_bewegungsmelder.md).

Quellen: [MDT Glastaster II Smart .01 ab R2.0, Abschnitt 4.4.9](https://www.mdt.de/download/MDT_THB_Smart_Taster_01_R20.pdf), [MDT Heizungsaktor .02](https://www.mdt.de/download/MDT_THB_Heizungsaktor_02.pdf).
