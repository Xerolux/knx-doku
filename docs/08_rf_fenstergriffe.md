# 08 – MDT KNX-RF-Fenstergriffe

Stand: 16.10.2026

## Spook-Reparaturen und Paketumbau am 16.10.2026 (zweite Sitzung)

Nach der ersten Korrektur blieben in HA elf aktive Spook-Reparaturen der Art `template_unknown_attribute_references` für alle elf Stellungsanzeigen bestehen. Ursache: Die Stellungsanzeigen lasen `offen`/`gekippt` per `state_attr()` von den Empfangssensoren; diese Attribute existieren erst nach dem ersten bestätigten Grifftelegramm, sodass Spook die Referenzen zu Recht als ungültig meldete.

Umbau des Live-Pakets `packages/knx_fenstergriffe_eg.yaml` (Repository-Kopie synchron):

- Die elf Stellungsanzeigen sind jetzt selbst trigger-basiert (`trigger: knx.telegram` auf beide Adressen des Griffs, Quelle und Nutzdaten gefiltert wie bisher). Sie führen `offen`/`gekippt` als eigene Attribute mit `-1`-Vorelegung und referenzieren keine anderen Entitäten mehr.
- Die elf separaten Telegramm-Empfangssensoren entfallen; keine Karte, Automation oder derivate Anzeige verwendete sie. Ihre Entitäten wurden aus der Entity-Registry entfernt. Zuletzt empfangenes Telegramm steht jetzt als Attribut `letzte_meldung` der Stellungsanzeige.
- Zusätzlicher Latenzfehler beseitigt: `knx.telegram` stellt kein `trigger.timestamp` bereit; das alte Zustands-Template der Empfangssensoren hätte beim ersten echten Telegramm einen Template-Fehler erzeugt. Die Zeitmarke verwendet jetzt `now()`.
- Die 22 KNX-Binärsensoren sind unverändert (bytengleich zur vorherigen Version; `sync_state: false`).

Verifikation: `ha core check` erfolgreich; `template/reload` und `knx/reload` ohne Core-Neustart; elf Stellungsanzeigen live mit Zustand **Unbekannt**; null `_empfang`-Entitäten; Reparatur-Registry von 310 auf 299 aktive Issues gesunken, keine fenstergriffbezogene Reparatur mehr vorhanden. `scripts/validate-fenstergriffe.py` prüft zusätzlich 444 Zustandskombinationen und lehnt `state_attr(`-Querverweise sowie `trigger.timestamp` in den Templates ab; `scripts/generate_fenstergriffe.py` erzeugt das Paket aus der Grifftabelle.

## Grifftest am Abend des 16.10.2026: Telegramm kam nicht an

Der Nutzer öffnete nach der Korrektur eine Tür; keine Anzeige reagierte. Auswertung des HA-Telegrammprotokolls (`.storage/knx/telegrams.db`, 167 154 Einträge):

- **Null** Telegramme auf irgendeine Griffadresse `5/x/*` und **null** von einer Griff-Quelladresse (1.1.11–1.1.19, 1.1.39, 1.1.42) – jemals, nicht nur heute.
- Der HA-Tunnel 1.1.255 ist gesund: Wetterstation 1.1.40 liefert fortlaufend, und Data-Secure-Empfang funktioniert nachweislich (Zeitserver 1.1.31 → 0/5/0+0/5/1, 288 secure Telegramme/24 h, entschlüsselt).
- Damit scheidet die HA-Seite (Tunnel, Schlüsselbund, Trigger, Anzeige) als Fehlerort aus. Der Bruch liegt zwischen Griff und TP-Linie 1.1.

**Hauptverdacht: Filtertabelle des Gira Medienkopplers 1.1.2.** RF→TP-Gruppentelegramme werden nur für Adressen der Koppler-Filtertabelle weitergeleitet; ein aktualisierter Koppler-Download steht bereits seit der Wetter-/Fenstersitzung aus („nicht durchgeführt oder nachgewiesen“). Die erfolgreichen ETS-Griffdownloads belegen nur die individualadressierte Programmierung über den Tunnel, nicht die Gruppenweiterschaltung. Nächster Schritt: vollständiger Download der Koppleranwendung 1.1.2 in ETS, danach Grifftest.

Nebenbefund: `knx.reload` stoppt die Telegrammprotokollierung in `telegrams.db` (letzter Eintrag exakt beim Reload; Busverkehr läuft weiter). Ein Core-Neustart reaktiviert sie; für den Grifftest sind die 22 KNX-Roh-Binärsensoren der zuverlässige Indikator.

## Diagnose und HA-Korrektur am 16.10.2026

Die elf Telegramm-Empfangssensoren waren live nicht angelegt. Ursache war der für Template-Sensoren unzulässige Schlüssel `entity_category: diagnostic`; dadurch fehlten die von den Stellungsanzeigen referenzierten Entitäten. Die elf Schlüssel wurden im Live-Paket und in der Repository-Kopie entfernt und Template-Entitäten neu geladen. Alle elf Empfangssensoren existieren nun. Die HA-Konfigurationsprüfung war erfolgreich; `scripts/validate-fenstergriffe.py` schützt zusätzlich vor einer erneuten Einführung dieses Schlüssels.

Zum Prüfzeitpunkt hatte noch keiner der elf Empfangssensoren ein bestätigtes Grifftelegramm gespeichert. Die Anzeigen bleiben daher korrekt **Unbekannt**. Keine Telegramme wurden simuliert und kein Zustand auf geschlossen gesetzt. Ein physischer Test offen/gekippt/geschlossen wurde beim Nutzer angefragt und ist noch nicht nachgewiesen.

Die aktuelle ETS-Geräteliste zeigt grüne Programmierkennzeichen für Koppler und die sichtbaren Griffe. Das ist gegenüber dem gestrigen offenen Downloadstand ein neuer Projektbefund, aber noch kein Funk-/Secure-Funktionsnachweis. HA ist live unter **1.1.255** verbunden, ETS verwendet **1.1.254**. Der ETS-Tunneling-Endpunkt **1.1.255 (Kanal 1)** zeigte zunächst **0 Assoziationen**. Nach ausdrücklicher Nutzerfreigabe wurden genau die 22 Status-/Kippadressen der Tabelle zugeordnet; die ETS bestätigt nun **22 Assoziationen**. Raum-Sammeladressen und der nicht verwendete Bereich 5/2 wurden ausgelassen. Der Nutzer hat den anschließenden Export und Import des neuen Schlüsselbunds in HA bestätigt. Danach zeigt die HA-KNX-Seite wieder Verbunden unter 1.1.255. Den physischen Griff-Test kann der Nutzer erst später durchführen; sichere Grifftelegramme sind deshalb noch nicht bestätigt. Passwörter und Schlüssel werden nicht in dieser Dokumentation gespeichert.

Die folgenden Abschnitte enthalten die vollständige Zuordnung und den historischen Vorbereitungsstand vom 15.10.; offene Punkte sind anhand dieses neuen Befunds fortzuführen.

### Nachprüfung der weiterhin unbekannten Stellungsentitäten

Die Nutzerbeanstandung betrifft ausdrücklich `sensor.eg_fenster_schlafzimmer_rechts_gross_stellung` und alle weiteren Stellungsentitäten. **Die funktionierende Zustandsanzeige ist noch nicht nachgewiesen und darf nicht als behoben gemeldet werden.** Live haben alle 22 Rohsensoren keine Absenderattribute; alle elf Empfangssensoren haben noch keine gespeicherten Zustandsbits. Die Rohwerte `off` sind daher weiterhin kein Beweis für geschlossene Fenster.

Am konkreten Beispiel `1.1.17` wurde in ETS zusätzlich geprüft: Objekt 2 ist mit `5/4/0`, Objekt 3 mit `5/4/20` verbunden. Beide Objekte haben K/Ü, aber kein L-Flag. Fensterstellung und Kippstellung stehen beide auf **zyklisch senden: nicht aktiv**. Die Polarität ist jeweils **Wert 1**. Auch „In Betrieb“ ist nicht zyklisch aktiv; Empfangsbereitschaft nach Neustart ist auf fünf Minuten begrenzt. Damit lässt sich für diesen Griff kein Anfangszustand über regelmäßige Meldungen oder eine normale Gruppenleseanfrage herbeiführen. Diese Parameterprüfung wurde nicht pauschal als Einzelprüfung aller elf Griffe ausgegeben.

Im HA-Core-Protokoll wurde der frühere ungültige Template-Schlüssel zuletzt um 19:10 gemeldet; die später korrigierten elf Empfangssensoren sind geladen. Die sichtbare Protokollübersicht enthält keinen neuen Fehler zur Entschlüsselung der Griffe. Das ist kein Beweis für eine funktionierende Secure-Strecke ohne tatsächliches Grifftelegramm.

Der nächste notwendige Nachweis bleibt ein echter Wechsel eines benannten Griffs mit gleichzeitigem Abgleich im ETS-/HA-Gruppenmonitor (Quelle, Ziel, Nutzdaten, Rohsensor, Empfangsattribute, Stellungsanzeige). Der Nutzer kann dies erst später durchführen. Bis dahin wurde keine geschlossene Stellung unterstellt. Eine spätere Aktivierung zyklischer Statusmeldungen erfordert eine bewusste Intervallwahl und einen Applikationsdownload am aufgeweckten Griff; sie wurde hier nicht unbemerkt vorbereitet oder geladen. Quelle für Sendeparameter und Empfangsbereitschaft: [MDT Handbuch, Abschnitte 3.2.1 und 3.2.2](https://www.mdt.de/fileadmin/user_upload/user_upload/download/RF-FGxS-01S_MDT_TM_V10_DE.pdf).

## Bestand und Kopplung

Elf MDT KNX RF+ Fenstergriffe, Secure (Produktfamilie RF-FGxS.01S; Farbvariante nicht bestätigt) sind im **RF Segment 1** unter der TP-Linie 1.1 angelegt. Der **Gira 5114 00 RF Multi/TP Medienkoppler 1.1.2** verbindet das Segment mit TP. Eine separate RF-Linie 1.2 ist nicht erforderlich.

Die Tabelle beschreibt die im ETS-Projekt gesetzten Objektverknüpfungen. Der am 16.10. dokumentierte ETS-Downloadverlauf bestätigt erfolgreiche Downloads der elf Griffe (siehe [Programmierstand](22_programmierstand_ets.md)). Der Empfang ihrer sicheren Telegramme und die physische Funktion sind weiterhin offen.

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

Das Paket [knx_fenstergriffe_eg.yaml](../home-assistant/knx_fenstergriffe_eg.yaml) ist live unter `packages/knx_fenstergriffe_eg.yaml` gespeichert und über die bestehende Paket-Einbindung geladen. Es enthält 22 empfangende KNX-Binärsensoren und elf trigger-basierte Stellungsanzeigen. KNX und Template-Entitäten wurden ohne Core-Neustart neu geladen. Die HA-Konfigurationsprüfung war erfolgreich.

Die KNX-Roh-Binärsensoren können bereits nach dem Start `off` anzeigen, ohne dass ein Telegramm empfangen wurde. Deshalb verwendet die sichtbare Stellungsanzeige ausschließlich die gespeicherten Nutzdaten tatsächlich eingehender Telegramme **von der jeweiligen Geräteadresse**. Ausgehende Telegramme, Leseanfragen und andere Absender bestätigen keinen Zustand.

- **Gekippt**: bestätigtes Kippbit 1.
- **Offen**: bestätigtes Öffnungsbit 1 ohne bestätigtes aktives Kippbit.
- **Geschlossen**: beide Bits tatsächlich als 0 empfangen.
- **Unbekannt**: noch nicht genügend bestätigte Daten vorhanden.

Die Stellungsanzeigen führen `offen` und `gekippt` als eigene Attribute (fehlend = noch kein Telegramm, dargestellt als `-1`) und stellen nach einem HA-Neustart den letzten bekannten Zustand wieder her. Das ist kein Beweis für aktuelle Funk-Erreichbarkeit. Es gibt keinen automatischen Reset auf geschlossen. `sync_state: false` vermeidet regelmäßige Leseanfragen an die schlafenden Batteriegeräte. Automationen sollten die bestätigten Stellungsanzeigen statt der initialen Rohwerte verwenden.

## Lovelace

Im bestehenden Live-Dashboard **EG → Fenster** sind elf Karten gespeichert. Die Darstellung greift die vorhandenen EG-/OG-Karten auf: dunkel = geschlossen, orange = gekippt, rot = offen, grau = unbekannt. Tippen öffnet nur „Mehr Informationen“. Das OG-Dashboard wurde nicht verändert; die vier bisherigen EG-Reiter bleiben erhalten.

Die ergänzende Ansicht liegt unter [lovelace_fenster_eg_view.yaml](../home-assistant/lovelace_fenster_eg_view.yaml); die vollständige [EG-Vorlage](../home-assistant/lovelace_knx_eg.yaml) erhält denselben Fenster-Reiter. Live geprüft wurden elf Karten mit **Unbekannt**, ohne simulierte Telegramme oder Aktorbetätigung.

## Programmierstand und verbleibende Inbetriebnahme

Der Vorbereitungsstand vom 15.10. ist durch die folgenden Befunde vom 16.10. ergänzt:

- Erfolgreiche Downloads der elf Griffe sind im [ETS-Programmierstand](22_programmierstand_ets.md) dokumentiert. Die dortige Downloadhistorie ist von der späteren HA-Empfangsprüfung zu unterscheiden.
- Die 22 Status-/Kippadressen sind dem tatsächlich verwendeten HA-Tunnel **1.1.255** zugeordnet; den erneuten Schlüsselbundexport und HA-Import hat der Nutzer bestätigt.
- Ein erneuter Download aktualisierter Router-/Kopplertabellen wurde in dieser Wetter-/Fensterdiagnose nicht durchgeführt oder nachgewiesen.
- Alle elf HA-Empfangssensoren sind nach der Template-Korrektur vorhanden, aber noch ohne bestätigte Zustandsbits. Die Stellungsanzeigen bleiben **Unbekannt**.

### Warum die Adressen am HA-Tunnel zugeordnet wurden

Die Zuordnung beschreibt in ETS, welche gesicherten Gruppenadressen der Tunneling-Endpunkt benötigt. Sie dient der passenden Bereitstellung der Gruppeninformationen und Schlüssel für den exportierten Schlüsselbund. HA benutzt **1.1.255**, der ETS-Monitor **1.1.254**; deshalb wurde der HA-Endpunkt ausgewählt. Die Zuordnung erzeugt weder Griffzustände noch Verbindungen zu Rollläden oder anderen Aktoren. Dass die zuvor fehlende Zuordnung die alleinige Ursache für „Unbekannt“ war, ist **nicht nachgewiesen**. Erst ein echtes eingehendes Grifftelegramm kann die Secure-Strecke und die Anzeige bestätigen.

### Besprochene Sendeparameter – Empfehlung, nicht heruntergeladen

Für **Fensterstellung und Fensterkippstellung jeweils zyklisch alle 1 Stunde** wurde ein Kompromiss zwischen Wiederholung des Zustands und Batteriebedarf empfohlen. Änderungen sollen weiterhin unmittelbar gesendet werden. MDT nennt eine Voreinstellung von fünf Stunden und weist auf den höheren Batteriebedarf kürzerer Intervalle hin. Die Stunde ist unsere besprochene Intervallwahl, keine Herstellervorgabe. Zyklische Meldungen ersetzen keinen Nachweis einer funktionierenden Funk-/Secure-Strecke.

Im anschließend vom Nutzer gezeigten Parameterbild waren folgende Werte sichtbar:

| Parameter | Sichtbarer Wert | Bedeutung |
|---|---|---|
| „In Betrieb“ zyklisch senden | nicht aktiv | optionales Lebenszeichen; enthält keine Fensterstellung |
| Empfangsbereitschaft nach Griffbewegung | aktiv, `00:03` mm:ss | drei Sekunden Empfangsfenster |
| Empfangsbereitschaft nach Neustart | aktiv, `05:00` mm:ss | fünf Minuten Empfangsfenster |

Die Empfangszeiten wurden als beizubehaltende Werte besprochen. Empfangsbereitschaft schaltet keinen zyklischen Versand von Stellungswerten ein. Für die reine Stellungsanzeige wurde kein zusätzliches „In Betrieb“-Lebenszeichen verlangt. Im Bild ist kein Gerät eindeutig identifiziert; es beweist weder diese Einstellung an allen elf Griffen noch einen Download. Bei der vorherigen Einzelprüfung von 1.1.17 war die Empfangsbereitschaft nach Griffbewegung noch nicht aktiv.

In dieser Sitzung wurden **keine neuen Griffparameter durch uns geladen**. Für eine spätere Änderung muss der jeweilige Griff entsprechend dem MDT-Verfahren wach sein und seine Applikation geladen werden. Der bereits dokumentierte vorherige Downloadstand bleibt davon getrennt.

### Verbleibender Funktionsnachweis

Je Griff geschlossen → geöffnet → gekippt → geschlossen prüfen und Quelle, Zieladresse, Nutzdaten sowie die HA-Stellungsanzeige samt ihrer Attribute `offen`, `gekippt` und `letzte_meldung` abgleichen. Insbesondere müssen beide Zustandsbits tatsächlich eingetroffen sein, bevor „Geschlossen“ bestätigt werden kann. Der Nutzer hat diesen Test auf später verschoben.

Die Spook-Reparaturen zu unbekannten Attributen sind mit dem Paketumbau der zweiten Sitzung vom 16.10. behoben und werden vom Validierungsskript gegen Regression geschützt.

**Die Fensterüberwachung ist noch nicht funktional abgenommen.** Vollständiges Sitzungsprotokoll: [Wetter und Fenster am 16.10.2026](32_wetter_fenster_inbetriebnahme_2026-10-16.md).

## Quellen

- [MDT Technisches Handbuch RF-FGxS.01S](https://www.mdt.de/fileadmin/user_upload/user_upload/download/RF-FGxS-01S_MDT_TM_V10_DE.pdf).
- [Gira Dokumentation 5114 00](https://partner.gira.de/data3/51143110.pdf).
- [Home Assistant KNX](https://www.home-assistant.io/integrations/knx/): Data Secure, Telegrammtrigger und Binärsensoren.
