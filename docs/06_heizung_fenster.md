# 06 – Heizung und Fenster

Stand: 04.10.2026

## Räume mit Fußbodenheizung

- Wohnzimmer
- Esszimmer
- Küche
- Arbeitszimmer
- Gang
- Schlafzimmer
- Badezimmer
- Bad vorne

Die Abstellkammer ist ein eigener neunter Raum, gehört aber nicht zu den KNX-Heizungs- oder Fensterfunktionen. Die Home-Assistant-Altentität `climate.heizkorper_omaopa_dusche_1` bleibt als Altbestand dokumentiert und erzeugt keine neue KNX-Heizungsadresse.

## Fenstergriffe KNX RF

| Raum | Anzahl |
|---|---:|
| Wohnzimmer | 3 |
| Küche | 2 |
| Bad vorne | 1 |
| Arbeitszimmer | 2 |
| Schlafzimmer | 2 |
| Badezimmer | 2 |

## Grundlogik

Fensterstatus wird je Raum zusammengeführt.

```text
Fenster im Raum geschlossen → Heizung normal
Fenster im Raum offen/gekippt → Heizung abgesenkt
```

## Gruppenadressen je Raum

```text
3/x/0 Solltemperatur
3/x/1 Isttemperatur
3/x/2 Betriebsmodus
3/x/3 Ventilstellung
3/x/4 Fensterstatus Raum
```

## Empfehlung

Die Heizungslogik sollte direkt in KNX laufen. Home Assistant darf den Status anzeigen, sollte aber nicht die Grundfunktion ersetzen.

## Heizungsaktor 1.1.5: Screenshotstand vom 03.10.2026

Gerät: MDT `AKH-0800.02`, Heizungsaktor 8-fach, 24/230 VAC. Die Screenshots zeigen das ETS-Projekt, nicht den laufenden Zustand der Ausgänge.

### Allgemeine Einstellung

| Parameter | Sichtbarer Wert |
|---|---|
| Geräteanlaufzeit | 2 s |
| „In Betrieb“ zyklisch senden | nicht aktiv |
| Thermischer Antrieb | 230 V |
| Festsitzschutz (alle 6 Tage für 5 min Ventil auf/zu) | nicht aktiv |
| Auswahl Heizsystem | 2 Rohr System (Heizen oder Kühlen) |
| Auswahl Betriebsart | Heizen |
| Heizen Stellwerte bei Sommerbetrieb auf 0 % setzen | Nein |
| Objekt für Anforderung Heizen/Kühlen | nicht aktiv |
| Polarität für Objekt Sommer/Winter | Sommer = 1 / Winter = 0 |
| Objekt max. Stellwert | nicht aktiv |
| Stell-/Temperaturwerte nach Busspannungswiederkehr abfragen | nicht aktiv |
| Sollwert Frostbetrieb | 7 °C |
| Verhalten nach Busspannungswiederkehr | Keine Werte abfragen |
| Betriebsarten und Sollwerte nach Busspannungswiederkehr wiederherstellen | nicht aktiv |
| Betriebsart nach Busspannungswiederkehr | Komfort |
| Sprache für Diagnosetext | Deutsch |

Die Auswahl 230 V ist eine ETS-Einstellung und kein Nachweis der tatsächlichen Stellantriebsspannung. Spannung und reale Ausgangsbelegung sind vor Inbetriebnahme anhand von Typenschild und Verdrahtung zu prüfen. Die Neustarteinstellungen sind erst zusammen mit der gewählten Kanalregelung und den sendenden Geräten zu bewerten. Auch die Angabe Frostbetrieb 7 °C allein belegt keine funktionierende Frostschutzregelung.

### Kanal A: historischer Stand, noch deaktiviert

Objektbeschreibung ist leer; Betriebsart steht auf **Kanal nicht aktiv**. Das geöffnete Dropdown bietet:

| Auswahl in ETS | Vorgesehener Regelungsweg |
|---|---|
| Kanal nicht aktiv | keine Heizungsfunktion für diesen Kanal projektiert |
| schaltend (1Bit) | externer Regler liefert einen binären Schaltstellwert |
| stetig (1Byte) | externer Regler liefert einen prozentualen Stellwert |
| integrierter Regler | Temperaturregelung im Heizungsaktor; passende Temperatur- und Sollwertobjekte anschließend prüfen |

Am 03.10.2026 war noch keine aktive Betriebsart bestätigt. Dieser historische Stand wird durch die nachstehenden Screenshots vom 04.10.2026 ergänzt. Der Glastaster-Temperaturmesswert allein belegt keinen externen Raumregler. Die Entscheidung zwischen integriertem Regler und externem Stellwert bleibt offen.

Die Eigenschaften zeigen physikalische Adresse `1.1.5` und Status `Unbekannt`. Ein historischer Eintrag zur letzten Programmierung bestätigt keinen Download der aktuellen Einstellungen und keinen aktuellen Funktionstest. Der zweite Heizungsaktor `1.1.6` und die Kanäle B–H sind durch diese Screenshots nicht geprüft.

### Nächste Schritte

1. Reale Zuordnung des Ausgangs A zum Heizkreis feststellen. Die Raumliste in [05 – Kanalbelegung](05_kanalbelegung.md#heizung) ist keine durch diesen Screenshot bestätigte Ausgangsbelegung.
2. Prüfen, ob bereits ein externer KNX-Raumregler vorhanden ist und welches Stellwertformat er sendet.
3. Ohne externen Regler, bei gewünschter Regelung im Aktor, `integrierter Regler` auswählen und die eingeblendeten Parameter sowie Kommunikationsobjekte prüfen. Bei externem Regler die Betriebsart nach dessen Stellwertformat wählen.
4. Erst danach Isttemperatur, Solltemperatur, Betriebsmodus, Fensterstatus und Ventilstatus mit den passenden vorhandenen Raumadressen verbinden. `3/x/3 Ventilstellung` nicht ungeprüft als Stellwertbefehl verwenden; Befehls- und Rückmelderichtung getrennt prüfen.
5. Stellantriebstyp, Reglerparameter, Temperaturüberwachung, Festsitzschutz und Verhalten nach Busspannungswiederkehr anhand des vollständigen Kanalaufbaus festlegen.
6. Nach abgeschlossener Projektierung die tatsächlich geänderten Geräte programmieren und Temperaturregelung, Ventilreaktion, Fensterabsenkung sowie Wiederanlauf prüfen.

**Historischer Status vom 03.10.2026:** Kanalregelung und Verknüpfungen waren noch offen. Aktueller Projektierungsstand siehe unten; ein Download oder Eingriff am realen Gerät wurde durch diese Dokumentationsarbeit nicht ausgeführt.

## FBH-Projektierung vom 04.10.2026

### Stellantriebe und Regelparameter

Laut Nutzer werden COSMO **CTS230N** verwendet. COSMO beschreibt genau diesen Typ als **230 V, stromlos geschlossen (NC)**: [Herstellerproduktseite](https://www.cosmo-info.de/profi/heizung/fussbodenheizung/stellantriebe-und-zubehoer/standard-stellantrieb-230v-cts230n). Dazu passen die Auswahl 230 V und Ventilart spannungslos geschlossen. Die genaue Stellzeit ist noch nicht bestätigt; die manuelle Offen-Arretierung darf den automatischen Regelbetrieb nicht übersteuern.

Die Parameter-Screenshots von `1.1.6`, Kanal A `Wohnzimmer Fenster`, zeigen:

| Parameter | Sichtbarer Wert |
|---|---|
| Betriebsart / Heizbetrieb | integrierter Regler / Heizen |
| Ventilart / PWM-Zyklus | spannungslos geschlossen / 10 min |
| Stellwertbegrenzung | 0–100 % |
| Sperrobjekt / Zwangsstellung | nicht aktiv / nicht aktiv |
| Status Stellwert senden / Diagnosetext | nicht aktiv / nicht aktiv |
| Berücksichtigung in Heiz-/Kühlanforderung und max. Stellwert | Ja |
| Zusätzlicher Vorlauftemperaturfühler | nicht aktiv |
| Frostalarm / Hitzealarm | unter 8 °C / über 35 °C |
| Notbetrieb | aktiv, nach 30 min ohne Temperaturmesswert |
| Notbetrieb Winter / Sommer | 50 % / 0 % |
| Regler-Heizsystem | Fußbodenheizung (6 K / 150 min) |
| Basis Komfortsollwert | 21 °C |
| Absenkung Standby / Nacht | 2 K / 3 K, entsprechend 19 °C / 18 °C |
| Priorität | Frost / Komfort / Nacht / Standby |
| Komfortsollwert zyklisch senden / Sollwertänderungen senden | 5 min / Nein |
| Maximale Sollwertverschiebung | 3 K |
| Sollwertverschiebung über 1-/2-Byte bzw. 1-Bit | nicht aktiv |
| Verschiebung gilt für / löschen bei Betriebsartenwechsel | Komfort / Nein |
| Präsenz bzw. Komfortverlängerung bei Nacht | nicht aktiv |
| Status auf Betriebsartvorwahl senden | Nein |
| HVAC-Statusformat / zyklisch senden | HVAC Status / nicht aktiv |

Bewertung: FBH-Reglerprofil und PWM 10 min sind plausible Startwerte, keine bestätigte Anlagenoptimierung. Eine geringere Absenkung von 0–1 K wurde als Startempfehlung besprochen, ist aber **nicht als eingestellt bestätigt**. Hitzealarm 35 °C ist kein Nachweis einer Boden- oder Vorlauftemperaturbegrenzung. Beim integrierten Regler überwacht der Notbetrieb den Eingang der Isttemperatur; das zyklische Senden des Komfortsollwerts ersetzt die Temperaturtelegramme nicht. Siehe [MDT-Handbuch AKH .02](https://www.mdt.de/download/MDT_THB_Heizungsaktor_02.pdf), Abschnitte Notbetrieb und PWM-Zyklus.

### Aktuelle Kanalnamen und Objektverknüpfungen

Die Objektlisten vom 04.10.2026 bestätigen die nachstehenden Kanalnamen und Objektnummern. Sie zeigten zunächst noch leere Verknüpfungen. Der Nutzer meldete anschließend, alle besprochenen Verknüpfungen gesetzt zu haben; ausdrücklich gezeigter Tabellenbeleg: `1.1.5` Objekt 130 → `3/0/2`. Die übrigen Aktorverknüpfungen sind Nutzerbestätigung, noch kein neuer vollständiger Screenshot-/Exportnachweis.

Wohnzimmer und Küche werden auf Nutzerwunsch **getrennt** geregelt. Kanal G `Wohnzimmer Küche Mitte` ist mit der gemeldeten Verknüpfung dem Wohnzimmer zugeordnet; der tatsächliche Verlauf des Heizkreises bleibt vor Ort zu prüfen.

| Aktor | Kanal / ETS-Name | Temperaturmesswert | Sollwert Komfort | Betriebsartvorwahl |
|---|---|---|---|---|
| `1.1.5` | A Badezimmer | 0 → `3/6/1` | 7 → `3/6/0` | 10 → `3/6/2` |
| `1.1.5` | B Schlafzimmer Fenster | 20 → `3/5/1` | 27 → `3/5/0` | 30 → `3/5/2` |
| `1.1.5` | C Schlafzimmer Wand | 40 → `3/5/1` | 47 → `3/5/0` | 50 → `3/5/2` |
| `1.1.5` | D Gang | 60 → `3/4/1` | 67 → `3/4/0` | 70 → `3/4/2` |
| `1.1.5` | E Arbeitszimmer Wand | 80 → `3/3/1` | 87 → `3/3/0` | 90 → `3/3/2` |
| `1.1.5` | F Arbeitszimmer Fenster | 100 → `3/3/1` | 107 → `3/3/0` | 110 → `3/3/2` |
| `1.1.5` | G Wohnzimmer Küche Mitte | 120 → `3/0/1` | 127 → `3/0/0` | 130 → `3/0/2` |
| `1.1.5` | H Wohnzimmer Mitte | 140 → `3/0/1` | 147 → `3/0/0` | 150 → `3/0/2` |
| `1.1.6` | A Wohnzimmer Fenster | 0 → `3/0/1` | 7 → `3/0/0` | 10 → `3/0/2` |
| `1.1.6` | B Küche | 20 → `3/2/1` | 27 → `3/2/0` | 30 → `3/2/2` |

Ist- und Solltemperatur verwenden DPT 9.001, Betriebsartvorwahl DPT 20.102. Vorhandene Adressen werden wiederverwendet; keine neuen Importadressen erforderlich. Die Kanalnamen belegen nicht die reale Verdrahtung. Weitere Kanäle von `1.1.6` sind nicht durch die gezeigte Objektliste bestätigt.

### Temperaturgeber: bestätigt und noch auszuführen

| Raum | Temperaturgeber / Objekt | Isttemperatur | Nachweis |
|---|---|---|---|
| Wohnzimmer | zugeordnet zu `1.1.23`, Objekt 108 | `3/0/1` | Verknüpfung im Screenshot bestätigt; Geräteadresse im Ausschnitt nicht sichtbar |
| Küche | zugeordnet zu `1.1.22`, Objekt 108 | `3/2/1` | Verknüpfung im Screenshot bestätigt; Geräteadresse im Ausschnitt nicht sichtbar |
| Badezimmer | passender Bad-Taster, Objekt 108 | `3/6/1` | Anleitung; noch nicht bestätigt |
| Schlafzimmer | ein ausgewählter Raum-Taster, Objekt 108 | `3/5/1` | Anleitung; noch nicht bestätigt |
| Gang | `1.1.21`, Objekt 108 | `3/4/1` | ältere Verknüpfung vom 25.09.2026 bestätigt; aktuelles Sendeintervall offen |
| Arbeitszimmer | passender Raum-Taster, Objekt 108 | `3/3/1` | Anleitung; noch nicht bestätigt |

Je Raum genau **einen** Temperaturgeber auf die jeweilige Isttemperaturadresse senden lassen. Alle Heizkreise desselben Raums empfangen diesen Wert. Unter Temperaturmessung das zyklische Senden beispielsweise auf **5 min** einstellen. Die aktuellen Objekt-Screenshots belegen keine Sendeintervalle. Das Intervall muss deutlich kürzer als die konfigurierte Notbetriebsfrist sein.

### Noch erforderliche Inbetriebnahme

1. Aktorverknüpfungen anhand der Tabelle kontrollieren; reale Heizkreiszuordnung, insbesondere Kanal G, prüfen.
2. Fehlende Raumtemperaturgeber verbinden; zyklisches Senden bei allen verwendeten Gebern prüfen und einstellen.
3. Gewünschte Komforttemperaturen, Absenkung, NC-Ventilart und passende Reglerparameter je Kanal kontrollieren. Die vollständigen Parameter sind nur für `1.1.6` A gezeigt.
4. Sollwert-/Betriebsmodusbedienung separat einrichten, falls benötigt. Eine Gruppenadressverknüpfung allein erzeugt keine Bedienbefehle. Home-Assistant-Entitäten entstehen nicht automatisch.
5. HVAC-Statusobjekte mit aktueller Einstellung nicht ungeprüft auf DPT-20.102-Befehlsadressen legen. Ventilstatus mehrerer Kanäle nicht gemeinsam auf eine einzelne Raumstatusadresse senden lassen; getrennte Rückmeldungen beziehungsweise eine definierte Zusammenführung planen.
6. Geänderte Aktoren `1.1.5`, `1.1.6` und tatsächlich geänderte Temperaturgeber mit dem Applikationsprogramm laden.
7. Im Gruppenmonitor die zyklischen Raumtemperaturen, Sollwert-/Modusbefehle und Ventilreaktion prüfen. Raumtemperaturregelung, Wiederanlauf und Notbetrieb anschließend verifizieren; ETS-Projekt und Export sichern.

**Aktueller Status:** Kanalnamen und Reglerobjekte sichtbar; Aktorverknüpfungen laut Nutzer gesetzt, Objekt 130 ausdrücklich belegt. Küche und Wohnzimmer als getrennte Zonen projektiert, deren Temperaturgeber-Verknüpfungen per Screenshot bestätigt. Weitere Temperaturgeber, Sendeintervalle, Downloads und physische Funktionstests bleiben offen.
