# 27 – Fußbodenheizung: MDT-Raumregelung

Live eingerichtet und geprüft am 11.10.2026. Dieser Stand ergänzt die historische Heizungsdokumentation vom 04.10.2026.

Die integrierten Regler der Heizungsaktoren 1.1.5 und 1.1.6 regeln die einzelnen Räume. MDT-Glastaster und Home Assistant geben die Basis-Komforttemperatur vor. IDM regelt weiterhin Heizkreis D mit Vorlauf, Mischer und Pumpe. Die OpenKNX-Raumcontroller sind separate Sensorquellen und wurden nicht als neue Temperaturquelle der AKH-Regler eingesetzt.

## Bedienung und Adressen

| Raum | MDT-Bedienung | Komfort schreiben / zurückmelden | Isttemperatur | Aktueller AKH-Sollwert | Status-Sender |
|---|---|---|---|---|---|
| Wohnzimmer | 1.1.23, T3/4 | 3/0/0 | 3/0/1 | 3/0/5 | 1.1.5 G, KO 129 |
| Küche | 1.1.22, T3/4 | 3/2/0 | 3/2/1 | 3/2/5 | 1.1.6 B, KO 29 |
| Arbeitszimmer | 1.1.24, T5/6 | 3/3/0 | 3/3/1 | 3/3/5 | 1.1.5 E, KO 89 |
| Gang | 1.1.21, T3/4 | 3/4/0 | 3/4/1 | 3/4/5 | 1.1.5 D, KO 69 |
| Schlafzimmer | 1.1.25 „Schlafzimmer“, Ebene 2 T7/8 | 3/5/0 | 3/5/1 | 3/5/5 | 1.1.5 B, KO 29 |
| Bad | 1.1.32, T5/6 | 3/6/0 | 3/6/1 | 3/6/5 | 1.1.5 A, KO 9 |

Die Tasten verwenden „2Byte Verschiebung des Basis Komfort Sollwertes“, Schritte von 0,5 K, Grenzen 19–23 °C und Statusrückmeldung. Links senkt, rechts erhöht. Wiederholtes Senden bei gehaltener Taste ist deaktiviert. T3/4 verwendet KO 10 (Schreiben), 12 (aktueller Sollwert), 13 (Basisrückmeldung); T5/6 entsprechend KO 20, 22 und 23.

Am Schlafzimmer-Haupttaster 1.1.25 bleiben Licht und beide Rollläden auf Ebene 1 erhalten. Die Heizung liegt auf Ebene 2, oberes Tastenpaar T7/8: KO 30 schreibt 3/5/0, KO 33 erhält die Basisrückmeldung 3/5/0 und KO 32 den aktuellen AKH-Sollwert 3/5/5. Der interne Messwert stammt weiterhin von 1.1.25 / KO 108 / 3/5/1. Ebenenwechsel ist über die versteckten unteren Tasten eingestellt, Rückkehr zur Startebene nach 10 Sekunden ohne Berührung. Die zunächst eingerichtete Schlafzimmer-Heizung am Taster 1.1.26 wurde auf Nutzerkorrektur deaktiviert. Auch die übrigen Bediengeräte verwenden ihren internen Temperaturwert. Vorhandene Licht- und Rollladenverknüpfungen wurden erhalten.

Pro Raum sendet genau der oben genannte AKH-Kanal den aktuellen Sollwert bei Änderung und alle fünf Minuten. Dieser Status ist getrennt vom Basis-Komfortwert, damit Nacht-/Standby-Absenkungen den Basiswert nicht überschreiben. Vorhandene Absenkungen bleiben erhalten: Küche und Bad Standby 2 K / Nacht 1 K; übrige Räume Standby 1 K / Nacht 3 K.

## Home Assistant

Zusätzlich wurde am 19.10.2026 die direkte Betriebsartenwahl „Heizmodus“ für sechs Glastaster eingerichtet. Nach erneuter Programmierfreigabe wurden alle sechs Taster und beide AKH erfolgreich geladen. Je Raum besteht ein Modus-Antwortgeber; Wiederherstellung von Betriebsart und Sollwert nach Buswiederkehr ist aktiviert. Bad: Standby → Frostschutz mit bestätigten 7 °C → zurück zu Standby am Bus geprüft. Physischer Tastentest steht noch aus. Tasten, Modusadressen und Prüfprotokoll: [38 – MDT Glas Heizmodi](38_mdt_glas_heizmodi_2026-10-19.md).

Sechs KNX-Klimaentitäten wurden über die KNX-Integration angelegt: `climate.eg_<raum>_mdt_komforttemperatur` mit den Raumteilen `kuche`, `bad`, `wohnzimmer`, `arbeitszimmer`, `gang`, `schlafzimmer`. Sie lesen die jeweilige Istadresse und schreiben/lesen die Basisadresse. Grenzen: 19–23 °C, Schritt 0,5 °C. Die sechs Statussensoren heißen `sensor.eg_<raum>_akh_aktuelle_solltemperatur`, lesen die jeweilige Adresse 3/x/5 mit DPT 9.001 und sind ihren Räumen zugeordnet.

Diese Entitäten sind bereits in HA gespeichert; keine zusätzlichen YAML-Duplikate importieren. Auf `/dashboard-eg/heizung` wurden sechs Thermostatkarten und eine Liste der tatsächlich verwendeten AKH-Sollwerte ergänzt. Die vorhandenen Karten bleiben erhalten. „Heizbetrieb“ bezeichnet bei diesen Klimaentitäten den konfigurierten Heizmodus; eine gemessene Ventilöffnung wird damit nicht bestätigt.

Am 19.10.2026 wurde das fehlende Leseflag der Basis-Komfortobjekte korrigiert: je Raum genau ein AKH-Antwortgeber, partielle Downloads für beide AKH und anschließend sechs bestätigte Leseantworten mit 21 °C. Zuordnung und Busnachweis stehen in [37 – KNX-Sollwertabfrage und HTTP-Sicherheitswarnung](37_knx_sollwert_http_warnungen_2026-10-19.md). Die Basisadressen bleiben von den aktuellen AKH-Sollwerten getrennt.

## Prüfung und Grenzen

- ETS meldet abgeschlossene partielle Downloads für beide AKH und die sechs Bediengeräte 1.1.21, 1.1.22, 1.1.23, 1.1.24, 1.1.25 und 1.1.32; zusätzlich wurde die Korrektur an 1.1.26 heruntergeladen.
- Alle sechs HA-Regler zeigen einen aktuellen Raumwert und Basiswert 21 °C; alle sechs AKH-Statussensoren melden 21 °C.
- Küchenprüfung: HA-Basiswert 21 → 21,5 °C; der getrennte AKH-Sensor bestätigte 21,5 °C. Anschließend zurück auf 21 °C, mit bestätigter AKH-Rückmeldung.
- Physische Tastendrücke und tatsächliche Stellmotorbewegungen wurden nicht geprüft. Es wurde kein Test durchgeführt, der alle Ventile schließt.
- HA/IDM ist für die Übermittlung des Gang-MDT-Werts an den externen Raumwert von Heizkreis D konfiguriert; der Datenweg wurde live geprüft. Die hydraulische Eignung dieses Referenzraums ist damit nicht bewiesen.

## Noch offen: FBH-Pumpe bei geschlossenen Ventilen

Nutzerangabe vom 11.10.2026: Die separate FBH-Pumpe ist eine Grundfos ALPHA3 und wird von IDM geschaltet. Es gibt keinen Überströmweg. In HA wurde keine eindeutig Heizkreis D zugeordnete externe Pumpenanforderung gefunden. Deshalb wurde keine AKH-Sammelanforderung auf einen globalen IDM-Eingang gelegt und keine Pumpenabschaltung eingerichtet. Die hydraulische Weiche und der Speicher allein belegen keinen Durchflussweg auf der Sekundärseite bei geschlossenen FBH-Ventilen.

Vor einer entsprechenden Anpassung sind die unterstützte IDM-Anforderung für D, Pumpennachlauf und die zeitliche Abstimmung mit den thermischen Ventilen zu klären. Eine pauschale Mindestöffnung wurde nicht gesetzt. Die vorhandene IDM-Pumpenregelung bleibt bestehen; der Schutz bei vollständig geschlossenen Raumkreisen ist weiterhin ungeklärt.

### Prüfung der IDM-Schnittstellen am 11.10.2026

- Die KNX-Brücke der HA-Integration ist live aktiviert; Befehlempfang ist eingeschaltet, Senden und Antworten auf Leseanfragen sind ausgeschaltet. Das Einschalten des Sendens stellt keine Pumpenanforderung für D her.
- Der lokale KNX-Katalog bildet Objekt 380 auf `demand_heating` (Modbus 1710) ab. Laut IDM-Modbus-Anleitung, Abschnitt 4.3.3, dient dieser Eingang der externen Wärmeanforderung bei reiner Pufferbewirtschaftung. Eine gezielte Abschaltung der Sekundärpumpe von D ist damit nicht belegt.
- Die IDM-Montageanleitung für AERO ALM 2-8/4-12/6-15 beschreibt auf Seite 54 das **Summensignal Zonenventile**: Geschlossene Endschalterkontakte geöffneter Zonenventile erzeugen eine Anforderung; das Summensignal kann den Heiz-/Kühlkreis über die Thermostatfunktion ein-/ausschalten. Die Zeichnung zeigt den Raumgeräte-Eingang für Heizkreis A. Sie belegt weder die Klemmenzuordnung für D am Erweiterungsmodul noch einen entsprechenden KNX-/Modbus-Schreibpunkt im vorhandenen Add-on.
- Im geprüften Integrationscode wurde keine eigene schreibbare Summensignal- oder Pumpenanforderung für D gefunden. Der Raumtemperaturwert von D und dessen Betriebsart sind keine bestätigten Ersatzsignale für diesen Eingang.
- Nächster notwendiger Nachweis: Schaltplan des tatsächlich verbauten Heizkreiserweiterungsmoduls und Navigator-10-Konfiguration für den Thermostat-/Summensignaleingang von D. Erst danach lässt sich eine MDT-Sammelanforderung über einen geeigneten Kontakt mit korrekter Verzögerung und Ventilabstimmung umsetzen. Es wurde keine Verdrahtung oder Anlagenkonfiguration geändert.

Quellen: [IDM Modbus TCP, Abschnitt 4.3.3, Seite 33](https://api.library.loxone.com/downloader/file/1480/iDM%20Mobus%20TCP%20Navigator%202.0%20DE.pdf), [IDM AERO ALM Montageanleitung, Abschnitt 6.12, Seite 54](https://www.manualslib.de/manual/810257/Idm-Aero-Alm-2-8.html?page=54). Die Montageanleitung gilt auch für ALM 6-15, beschreibt jedoch Navigator 2.0; die konkrete Navigator-10-/Erweiterungsmodul-Zuordnung bleibt zu bestätigen.

### Nachgereichte Elektroschaltpläne: Zuordnung von D

Die fünf vom Nutzer nachgereichten Pläne wurden am 11.10.2026 geprüft. **E1069-00** (internes Erweiterungsmodul A3, I/O28.0EW, Navigator 2.0) enthält Heizkreis C und D. Damit ist die vorher offene Plan-Zuordnung geklärt:

| Funktion D | Betriebsmittel / Modul | Klemmen laut Plan | Planseite |
|---|---|---|---|
| Heizkreispumpe | M34 / A3 | 211, 211N, 211PE; Triacausgang, max. 1 A | 5 |
| Mischer auf | M44 / A3 | 202 | 5 |
| Mischer zu | M44 / A3 | 204; Neutralleiter 203N | 5 |
| Vorlauffühler | B54 / A3 | 222, 223 (M), PT1000 | 6 |
| Raumgerät | B64 / A3 | 226 (P), 227 (M/GND), Analogeingang 0–15 kΩ | 6 |

Der Plan verlangt bei Niedertemperaturheizkreisen einen bauseitigen Thermostat zur Vorlauftemperatur-Maximalbegrenzung in Serie zur Pumpe. Das ist eine Temperaturbegrenzung, keine Ventil-Sammelanforderung.

**E1005-01** zeigt das externe Modul A6 für E/F/G, nicht für D. **0002997 / E1121-00** und **0002998 / E1112-00** betreffen Warmwasserstationen. **E1088-01** zeigt die ALM-Inneneinheit und die Verbindung zum internen Erweiterungsmodul.

Die Pläne bestätigen Anschlussbezeichnungen, nicht die tatsächliche Verdrahtung oder die aktuelle Navigator-10-Parametrierung. Insbesondere ist B64 im E1069-00 als analoges Raumgerät eingezeichnet, nicht als expliziter Digitaleingang für eine Sammelanforderung. Die Verwendung von 226/227 als potentialfreier Thermostat-/Summensignaleingang und die Kombination mit der bereits aktiven GLT-Raumtemperatur müssen für die vorhandene Regelung bestätigt werden. Keine Brücke, Fremdspannung oder Anschlussänderung wurde vorgenommen. Eine reine Aktivierung der HA-KNX-Brücke kann diesen physischen Eingang nicht bedienen.

## Gemeinsame Raumwerte und getrennte Ventilregler

HA und MDT verwenden je Raum einen gemeinsamen Isttemperatur- und Basis-Sollwert. Wohnzimmer (1.1.5 G/H und 1.1.6 A), Schlafzimmer (1.1.5 B/C) und Arbeitszimmer (1.1.5 E/F) erhalten jeweils ihre gemeinsamen Raumwerte. Küche (1.1.6 B), Bad (1.1.5 A) und Gang (1.1.5 D) bleiben eigene Regelzonen. Diese Zuordnung beschreibt die ETS-Projektierung; der reale Verlauf jeder Heizschleife ist nicht durch einen hydraulischen Funktionstest bestätigt.

Jeder Aktorkanal behält seinen eigenen integrierten Regler. Gemeinsame Ist-/Sollwerte garantieren keine synchronen PWM-Ausgänge oder identische mechanische Ventilstellungen. Gleiche Ansteuerung bedeutet auch keinen gleichen Durchfluss: Dieser hängt vom hydraulischen Abgleich ab. Der HA-Sensor für den aktuellen Raum-Sollwert liest genau den oben angegebenen Status-Sender; er bildet weder einen Mittelwert noch eine Sammelrückmeldung aller Ventile.

## ALPHA3, Navigator Pro und verbleibende Entscheidung

Nachgereichte Fotos zeigen eine Grundfos ALPHA3 mit Funk-/Bluetooth-Bedienung. Vollständige Produktnummer, Förderhöhe und aktueller Regelmodus sind daraus nicht ablesbar. Die Fotos zeigen belegte Anschlüsse an 211/N/PE sowie am Mischer von D; Leitungsziel und die Raumgeräteklemmen 226/227 sind dadurch nicht vollständig bestätigt. Es handelt sich nicht um einen aktuellen Laufzustandsnachweis.

Für die ALPHA3 mit Bluetooth beschreibt Grundfos einen Fußbodenheizungsmodus mit AUTOADAPT, Proportionaldruck, Konstantdruck und konstante Kennlinie. Bei Druckregelung passt die Pumpe ihre Drehzahl an den Betriebspunkt an. Eine automatische Abschaltung allein wegen vollständig geschlossener Raumventile ist im geprüften Datenblatt nicht ausgewiesen; elektrischer/thermischer Motorschutz ist kein solcher Nachweis. Die zuvor betrachtete gemeinsame ALPHA2/3-Anleitung darf nicht ohne Prüfung der Gerätegeneration auf diese Ausführung übertragen werden. Quelle: [Grundfos ALPHA3 Bluetooth-Datenblatt](https://api.grundfos.com/literature/Grundfosliterature-6014678.pdf).

Ein Mindeststellwert von 10 % am thermischen AKH-Ausgang ist keine garantierte mechanische Öffnung von 10 %. Bei PWM bezeichnet der Wert ein zeitliches Einschaltverhältnis; daraus folgt kein gesicherter dauerhafter Wasserweg. Weder ein pauschaler Mindeststellwert noch ein Versuch mit allen geschlossenen Ventilen wurde eingerichtet.

Navigator Pro verwendet IDM-Raumsensoren und Zonenmodule für die Einzelraumregelung, verbunden mit dem Navigator; IDM beschreibt das Lernen des Aufheizverhaltens und die Integration mit der Heizkreisregelung. Die genaue Pumpenabschaltung, Öffnungsverzögerung und Nachlaufstrategie sind in den geprüften Unterlagen nicht ausreichend beschrieben. Diese Funktionen werden daher nicht als bestätigte Schutzlogik behauptet. Bei der bestehenden MDT-Regelung kennt IDM bisher den weitergeleiteten Gang-Raumwert, nicht nachweislich den Bedarf oder die Ventilzustände aller EG-Räume. Quellen: [IDM Navigator Pro / Planerforum](https://www.idm-energie.at/wp-content/uploads/2020/03/06_Navigator-2.0-Regelung_Reinhard-Gion.pdf), [IDM Regelung](https://www.idm-energie.at/regelung/).

Die lokale originale Navigator-10-Modbus-Anleitung 812663 Rev.0 bestätigt auf Seite 31 die Pufferanforderung 1710. Betriebsart D (1396, Seite 16) ist mit einem Stern als EEPROM-Parameter markiert; Seite 11 warnt vor permanenten Wertänderungen. Sie wurde deshalb nicht als zyklischer Ventil-/Pumpenschalter verwendet.

Aktuelle Entscheidung: MDT-Raumregelung und IDM-Pumpen-/Mischerregelung bleiben bestehen. Das bedeutet keine abschließende Bestätigung des Betriebs bei vollständig geschlossenen Ventilen. Offen sind die tatsächlich eingestellte ALPHA3-Regelungsart (über Grundfos GO ablesen), die Navigator-Konfiguration des Summensignaleingangs für D, dessen Zusammenspiel mit GLT-Raumtemperatur und die zeitliche Abstimmung mit den thermischen Stellantrieben. Private Originalpläne, Fotos, HA-Diagnosen und Zugangsdaten bleiben außerhalb der veröffentlichten Dateien.
