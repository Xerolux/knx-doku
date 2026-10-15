# 08 – MDT KNX-RF-Fenstergriffe

Stand: 15.10.2026

## Bestand und Kopplung

Elf MDT KNX RF+ Fenstergriffe, Secure (Produktfamilie RF-FGxS.01S; Farbvariante nicht bestätigt) sind im **RF Segment 1** unter der TP-Linie 1.1 angelegt. Der **Gira 5114 00 RF Multi/TP Medienkoppler 1.1.2** verbindet das Segment mit TP. Eine separate RF-Linie 1.2 ist nicht erforderlich.

Die Tabelle beschreibt die heute im offenen ETS-Projekt gesetzten Objektverknüpfungen. Ihr Download und ihre physische Funktion sind noch nicht bestätigt.

| Adresse | Fenstergriff | Objekt 2: Fensterstellung | Objekt 3: Kippstellung | HA-Stellungsanzeige |
|---|---|---|---|---|
| 1.1.11 | Küche links klein | 5/1/0 | 5/1/20 | `sensor.eg_fenster_kuche_links_klein_stellung` |
| 1.1.12 | Küche rechts groß | 5/1/1 | 5/1/21 | `sensor.eg_fenster_kuche_rechts_gross_stellung` |
| 1.1.13 | Wohnzimmer links klein | 5/0/0 | 5/0/20 | `sensor.eg_fenster_wohnzimmer_links_klein_stellung` |
| 1.1.14 | Wohnzimmer rechts groß | 5/0/1 | 5/0/21 | `sensor.eg_fenster_wohnzimmer_rechts_gross_stellung` |
| 1.1.15 | Arbeitszimmer links klein | 5/3/0 | 5/3/20 | `sensor.eg_fenster_arbeitszimmer_links_klein_stellung` |
| 1.1.16 | Arbeitszimmer rechts groß | 5/3/1 | 5/3/21 | `sensor.eg_fenster_arbeitszimmer_rechts_gross_stellung` |
| 1.1.17 | Schlafzimmer rechts groß | 5/4/0 | 5/4/20 | `sensor.eg_fenster_schlafzimmer_rechts_gross_stellung` |
| 1.1.18 | Schlafzimmer Tür | 5/4/1 | 5/4/21 | `sensor.eg_fenster_schlafzimmer_tur_stellung` |
| 1.1.19 | Wohnzimmer Tür | 5/0/2 | 5/0/22 | `sensor.eg_fenster_wohnzimmer_tur_stellung` |
| 1.1.39 | Bad links | 5/5/0 | 5/5/20 | `sensor.eg_fenster_bad_links_stellung` |
| 1.1.42 | Bad rechts | 5/5/1 | 5/5/21 | `sensor.eg_fenster_bad_rechts_stellung` |

Die vorhandenen Statusadressen `5/x/0…2` bleiben erhalten; die Kippadressen `5/x/20…22` wurden neu angelegt. Die frühere Planung für Bad vorne und Raum-Sammeladressen `5/x/10` ist kein Nachweis zusätzlicher realer Griffe. Diese Adressen werden hier nicht in HA eingebunden.

## Kommunikationsobjekte

Alle elf Geräte zeigen derzeit fünf Objekte:

| Objekt | Funktion | Länge | Verwendung |
|---|---|---|---|
| 2 | Fensterstellung geschlossen/geöffnet | 1 Bit | eigene Statusadresse je Griff |
| 3 | Fensterkippstellung nicht gekippt/gekippt | 1 Bit | eigene Kippadresse je Griff |
| 5 | Erschütterungsalarm | 1 Bit | nicht verknüpft |
| 7 | Batterie Status | 1 Byte | nicht verknüpft |
| 8 | Batterie Warnung | 1 Bit | nicht verknüpft |

Es werden keine Batterie- oder Alarmwerte erfunden. MDT erlaubt eine parametrierbare Polarität. Die HA-Auswertung erwartet **1 = geöffnet** und **1 = gekippt**; dies muss bei der Inbetriebnahme je Griff geprüft werden. Die Griffstellung ist kein unabhängiger Nachweis für den tatsächlichen Sitz des Fensterflügels.

## Home Assistant

Das Paket [knx_fenstergriffe_eg.yaml](../home-assistant/knx_fenstergriffe_eg.yaml) ist live unter `packages/knx_fenstergriffe_eg.yaml` gespeichert und über die bestehende Paket-Einbindung geladen. Es enthält 22 empfangende KNX-Binärsensoren, elf Telegramm-Empfangssensoren und elf Stellungsanzeigen. KNX und Template-Entitäten wurden ohne Core-Neustart neu geladen. Die HA-Konfigurationsprüfung war erfolgreich.

Die KNX-Roh-Binärsensoren können bereits nach dem Start `off` anzeigen, ohne dass ein Telegramm empfangen wurde. Deshalb verwendet die sichtbare Stellungsanzeige ausschließlich die gespeicherten Nutzdaten tatsächlich eingehender Telegramme **von der jeweiligen Geräteadresse**. Ausgehende Telegramme, Leseanfragen und andere Absender bestätigen keinen Zustand.

- **Gekippt**: bestätigtes Kippbit 1.
- **Offen**: bestätigtes Öffnungsbit 1 ohne bestätigtes aktives Kippbit.
- **Geschlossen**: beide Bits tatsächlich als 0 empfangen.
- **Unbekannt**: noch nicht genügend bestätigte Daten vorhanden.

Die Empfangssensoren stellen nach einem HA-Neustart den letzten bekannten Zustand wieder her. Das ist kein Beweis für aktuelle Funk-Erreichbarkeit. Es gibt keinen automatischen Reset auf geschlossen. `sync_state: false` vermeidet regelmäßige Leseanfragen an die schlafenden Batteriegeräte. Automationen sollten die bestätigten Stellungsanzeigen statt der initialen Rohwerte verwenden.

## Lovelace

Im bestehenden Live-Dashboard **EG → Fenster** sind elf Karten gespeichert. Die Darstellung greift die vorhandenen EG-/OG-Karten auf: dunkel = geschlossen, orange = gekippt, rot = offen, grau = unbekannt. Tippen öffnet nur „Mehr Informationen“. Das OG-Dashboard wurde nicht verändert; die vier bisherigen EG-Reiter bleiben erhalten.

Die ergänzende Ansicht liegt unter [lovelace_fenster_eg_view.yaml](../home-assistant/lovelace_fenster_eg_view.yaml); die vollständige [EG-Vorlage](../home-assistant/lovelace_knx_eg.yaml) erhält denselben Fenster-Reiter. Live geprüft wurden elf Karten mit **Unbekannt**, ohne simulierte Telegramme oder Aktorbetätigung.

## Programmierstand und verbleibende Inbetriebnahme

Vor dieser Erweiterung zeigte die ETS-Historie erfolgreiche vollständige Downloads für Koppler 1.1.2 und Badgriffe 1.1.39/1.1.42. Sie bestätigen nicht den Download der danach neu angelegten Verknüpfungen. Die vorherige Kopplerdiagnose zeigte nur Teilnehmer 11–19 im Subsegment und einen gespeicherten Secure-Sequenzfehler von 1.1.39. Der Nutzer meldete nach Koppler-/Badgriffprogrammierung Erfolg; die ETS-Historie bestätigte die Downloads.

Für diese neue Erweiterung sind noch erforderlich:

1. Die 22 gesicherten Gruppenadressen am tatsächlich von HA verwendeten Tunnel-Endpunkt prüfen bzw. zuordnen. Den HA-Tunnel nicht mit dem ETS-Tunnel verwechseln.
2. Betroffenen Router und Medienkoppler mit aktuellen Tabellen laden.
3. Aktuellen ETS-Schlüsselbund exportieren und in HA importieren. Schlüssel und Passwörter bleiben privat; KNX Data Secure bleibt aktiviert.
4. Jeden Griff unmittelbar vor seinem Applikationsdownload mit kurzem Druck auf die Programmiertaste aufwecken. MDT empfiehlt das gegen Deep Sleep. Jeweils nur ein Griff im Programmiermodus.
5. Geschlossen, geöffnet und gekippt je Griff vor Ort prüfen; Quelle, Zieladresse, Nutzdaten und HA-Anzeige abgleichen. Danach Programmiermodus beenden.

Der Nutzer hat am 15.10.2026 den Import der aktuellen Keys in HA bestätigt. Der Applikationsdownload ist für den Folgetag vorgesehen. Der Schlüsselimport wurde nicht unabhängig erneut geprüft; die sichere Kommunikation ist erst nach den Downloads und empfangenen Telegrammen bestätigt.

**Download der neuen Verknüpfungen, Prüfung der sicheren Kommunikation und physischer Zustandstest sind noch offen.** Die gespeicherten Karten sind daher noch kein Nachweis einer funktionierenden Fensterüberwachung.

## Quellen

- [MDT Technisches Handbuch RF-FGxS.01S](https://www.mdt.de/fileadmin/user_upload/user_upload/download/RF-FGxS-01S_MDT_TM_V10_DE.pdf).
- [Gira Dokumentation 5114 00](https://partner.gira.de/data3/51143110.pdf).
- [Home Assistant KNX](https://www.home-assistant.io/integrations/knx/): Data Secure, Telegrammtrigger und Binärsensoren.
