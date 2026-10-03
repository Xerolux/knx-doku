# 06 – Heizung und Fenster

Stand: 03.10.2026

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

### Kanal A: noch deaktiviert

Objektbeschreibung ist leer; Betriebsart steht auf **Kanal nicht aktiv**. Das geöffnete Dropdown bietet:

| Auswahl in ETS | Vorgesehener Regelungsweg |
|---|---|
| Kanal nicht aktiv | keine Heizungsfunktion für diesen Kanal projektiert |
| schaltend (1Bit) | externer Regler liefert einen binären Schaltstellwert |
| stetig (1Byte) | externer Regler liefert einen prozentualen Stellwert |
| integrierter Regler | Temperaturregelung im Heizungsaktor; passende Temperatur- und Sollwertobjekte anschließend prüfen |

Es wurde noch keine aktive Betriebsart ausgewählt oder durch einen weiteren Screenshot bestätigt. Der Glastaster-Temperaturmesswert allein belegt keinen externen Raumregler. Die Entscheidung zwischen integriertem Regler und externem Stellwert bleibt offen.

Die Eigenschaften zeigen physikalische Adresse `1.1.5` und Status `Unbekannt`. Ein historischer Eintrag zur letzten Programmierung bestätigt keinen Download der aktuellen Einstellungen und keinen aktuellen Funktionstest. Der zweite Heizungsaktor `1.1.6` und die Kanäle B–H sind durch diese Screenshots nicht geprüft.

### Nächste Schritte

1. Reale Zuordnung des Ausgangs A zum Heizkreis feststellen. Die Raumliste in [05 – Kanalbelegung](05_kanalbelegung.md#heizung) ist keine durch diesen Screenshot bestätigte Ausgangsbelegung.
2. Prüfen, ob bereits ein externer KNX-Raumregler vorhanden ist und welches Stellwertformat er sendet.
3. Ohne externen Regler, bei gewünschter Regelung im Aktor, `integrierter Regler` auswählen und die eingeblendeten Parameter sowie Kommunikationsobjekte prüfen. Bei externem Regler die Betriebsart nach dessen Stellwertformat wählen.
4. Erst danach Isttemperatur, Solltemperatur, Betriebsmodus, Fensterstatus und Ventilstatus mit den passenden vorhandenen Raumadressen verbinden. `3/x/3 Ventilstellung` nicht ungeprüft als Stellwertbefehl verwenden; Befehls- und Rückmelderichtung getrennt prüfen.
5. Stellantriebstyp, Reglerparameter, Temperaturüberwachung, Festsitzschutz und Verhalten nach Busspannungswiederkehr anhand des vollständigen Kanalaufbaus festlegen.
6. Nach abgeschlossener Projektierung die tatsächlich geänderten Geräte programmieren und Temperaturregelung, Ventilreaktion, Fensterabsenkung sowie Wiederanlauf prüfen.

**Status:** Sichtbare Einstellungen und Betriebsartauswahl dokumentiert. Regelungsentscheidung, aktive Kanalparameter, Gruppenadressverknüpfungen, Download und Funktionstest bleiben offen. Es wurden keine Heizungsparameter am realen Gerät geändert.
