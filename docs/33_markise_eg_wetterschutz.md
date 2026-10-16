# 33 – KNX-Wetterschutz der EG-Markise

Stand: 16.10.2026, korrigierte Alarmanbindung erneut eingerichtet und nach manuellem Nutzerdownload in ETS als abgeschlossen bestätigt. Physische Alarmabnahme noch offen.

Der Nutzer hat die einzige in KNX geführte Markise als untere EG-Markise bestätigt und die Umsetzung direkt in KNX beauftragt. Hersteller HEIM & HAUS; Modell, Abmessungen und Windfreigabe der Befestigung sind unbekannt. Die OG-Markise bleibt unverändert. Die vorherige Beschränkung auf Wetteranzeige wurde für genau diese EG-Markise erweitert.

## Maßgeblicher Abschlussstand

- Nach ausdrücklich gewünschter Wiederaufnahme wurden Wind- und Regenalarm ausschließlich an **1.1.4 Kanal G** wieder aktiviert und verbunden: KO 216 → 4/2/1, KO 217 → 4/0/2.
- Beide Alarmaktionen stehen auf **Nach unten fahren**. Der Nutzer hatte zuvor die physische Einfahrt nach einem normalen Ab-Befehl bestätigt. Die bestehende Kanalparametrierung **Motor Auf/Ab vertauschen = Auf/Ab vertauscht** wurde bei der Schlussprüfung sichtbar festgestellt und unverändert belassen.
- Bei Rücknahme beider Alarme jeweils **keine Aktion**; keine automatische Ausfahrt. Telegrammüberwachung jeweils drei Minuten.
- Der erste erneute Downloadversuch des Assistenten scheiterte. Danach stoppte der Nutzer Computer Use und meldete anschließend, die Applikation selbst in den JAL geschrieben zu haben. Die nachfolgende read-only ETS-Prüfung zeigte einen neueren erfolgreichen Applikationsdownload **Abgeschlossen** oberhalb des fehlgeschlagenen Versuchs.
- Die abschließende Prüfung bestätigte die Projektparameter und den Downloadverlauf. Sie enthielt keine Fahrbefehle, keinen erneuten Download und keine simulierten Wettertelegramme.
- Die Wetterstation wurde bei dieser Wiederaufnahme nicht erneut programmiert; Windgrenzwert 5 m/s = 18 km/h und vorhandener Regenausgang bleiben wie unten dokumentiert. Die Windgrenze ist weiterhin keine bestätigte Herstellerfreigabe für Modell/Befestigung.
- Die vorherige Einfahrt ist vom Nutzer bestätigt; tatsächliche Alarmreaktion, Sperrwirkung, Alarmrücknahme und Telegrammausfall sind nach dem finalen Download noch nicht physisch abgenommen. Stillstand nach dem finalen Nutzerdownload wurde nicht separat bestätigt.
- OG-Markise unverändert; Auswertung direkt in KNX, ohne HA-Automation.

Die folgenden Abschnitte protokollieren auch den Vorfall und verworfene Zwischenstände. Maßgeblich für den aktuellen Stand ist dieser Abschnitt.

## ETS-Konfiguration (Zuordnungen und endgültige Alarmrichtung)

| Funktion | Einstellung |
|---|---|
| Ziel | MDT JAL-0810M.02, 1.1.4, ausschließlich Kanal G Markise |
| Vorhandene Bedienung | 2/4/0 Auf/Ab, 2/4/1 Stopp, 2/4/3 Position |
| Windalarm | Gira 1.1.40 KO 30 → 4/2/1 → JAL KO 216 |
| Regenalarm | vorhandenes Gira KO 38 → 4/0/2 → JAL KO 217 |
| Alarmfahrt | jeweils Nach unten fahren; normale Ab-Einfahrt zuvor physisch bestätigt, Alarmfahrt noch nicht separat getestet |
| Alarmende | jeweils keine Aktion; kein automatisches Wieder-Ausfahren |
| Telegrammüberwachung | Wind und Regen jeweils 3 Minuten |
| Priorität | Windalarm vor Regenalarm, Frostalarm, Sperrfunktion |
| Frostalarm | unverändert nicht aktiv |

Gira-Windgrenzwert 1: 5 m/s = **18 km/h**, Hysterese 1 m/s; EIN bei Überschreitung, AUS nach Unterschreitung von GW minus Hysterese, also 4 m/s = 14,4 km/h. Keine Einschaltverzögerung; Ausschaltverzögerung 15 Minuten. Versand bei Änderung und zyklisch alle 60 Sekunden (6 × 10 s).

Die feste Auswahl bietet 5 oder 8 m/s, aber keinen Wert entsprechend 25 km/h. Deshalb wurde der frühere Wert 5 m/s gewählt. Er ist eine vorläufige Betriebswahl und **kein Nachweis einer zulässigen Windbelastung**. Die dokumentierte Herstellervorgabe hängt auch von der Befestigung ab.

Das vorhandene Regensignal meldet Regen EIN ohne Einschaltverzögerung, zehn Minuten Ausschaltverzögerung und sendet bei Änderung sowie alle 60 Sekunden. Es wurde direkt verwendet; 4/2/2 wurde nicht zusätzlich benötigt. Andere Kanäle erhielten keine neuen Wetterverknüpfungen. Keine HA-Automation übernimmt den Schutz.

## Nachweise und offene Prüfung

Parameter und Verknüpfungen wurden in ETS gesetzt. Applikationsdownloads für Wetterstation 1.1.40 und Aktor 1.1.4 wurden jeweils als Abgeschlossen bestätigt. Alarmfahrt, Sperre während Alarm, Freigabe ohne Fahrt und Reaktion bei Telegrammausfall sind physisch noch nicht abgenommen. Kein Wetterereignis wurde durch gefälschte Telegramme simuliert.

## Quellen

- [HEIM & HAUS Bedienungsanleitung Markise](https://www.heimhaus.de/fileadmin/user_upload/Bedienungsanleitung_Markise_060307_23_screen.pdf): Befestigungsnachweis und Windnutzung; nass eingefahrenes Tuch später trocknen lassen.
- [HEIM & HAUS FAQ](https://www.heimhaus.de/kundenservice/hilfe-infos/produkt-faqs/markise/): bei jedem Regenschauer einfahren.
- [MDT Lösungsvorschlag Wetteralarm](https://www.mdt.de/fileadmin/user_upload/user_upload/download/MDT_LSG_Wie%20realisiert%20man%20einen%20Wetteralarm.pdf): kanalbezogener Windalarm und Überwachungszeit etwa dreimal so lang wie das Sendeintervall.
- [Gira Wetterstation Plus](https://partner.gira.de/data3/20743510.pdf).

## Vorfall: unerwartete Ausfahrt nach Aktivierung

Der Nutzer meldete unmittelbar danach, die Markise sei ausgefahren. Im ETS-Gruppenmonitor wurde ein echtes GroupValue_Write von 1.1.40 nach 4/2/1 mit Wert EIN bestätigt. Die Alarmaktion war Nach oben fahren. Die reale Einfahrrichtung war vor dem Laden nicht physisch geprüft worden; die Annahme Nach oben = Einfahren war deshalb unzulässig. Der genaue kausale Ablauf der beobachteten Fahrt ist noch nicht vollständig nachgewiesen. Ein Start-/Ersatzwert der Wetterstation ist als Alarmauslöser möglich; ein echter Windgrenzwertübertritt wurde nicht nachgewiesen.

Als sofortige Begrenzung wurden **beide Alarm-Fahraktionen auf keine Aktion** gesetzt, die Aktionen bei Alarmende bleiben ebenfalls keine Aktion. Die Gruppenverknüpfungen bleiben bestehen. Der erneute Aktordownload wurde in ETS als Abgeschlossen bestätigt; beide Alarmaktionen stehen sichtbar auf keine Aktion. Ein erfolgreicher Stopp oder eine sichere physische Position wurde nicht behauptet. Der Nutzer wurde um lokalen Stopp bei fortdauernder Bewegung und Angabe der realen Auf-/Ab-Richtung gebeten.

**Die obige Tabelle beschreibt die ursprüngliche Einrichtung, nicht den abschließenden freigegebenen Schutzstand.** Bis zur Richtungsprüfung und erneuten Funktionsabnahme besteht kein bestätigter automatischer Einfahrschutz. Alarmfunktionen/Überwachungen bleiben vorerst aktiv und können die normale Bedienung sperren, obwohl keine Fahraktion mehr vorgesehen ist.

## Ausdrücklicher Einfahrauftrag nach dem Vorfall

Auf die Meldung, dass die Markise weiter ausgefahren steht, wurde ein einzelnes GroupValue_Write an **2/4/0 mit Wert 1 / Ab** gesendet (ETS-Monitor etwa 20:34). Der Sendebefund ist bestätigt; tatsächliche Einfahrt und Endlage wurden zur physischen Bestätigung beim Nutzer abgefragt. Die Alarmfahraktionen bleiben keine Aktion. Keine OG-Ansteuerung.

Der Nutzer bestätigte anschließend: Auf den normalen Ab-Befehl keine Bewegung. Wegen weiterhin aktivem Windalarm wurde die Windalarmaktion von keine Aktion auf **Nach unten fahren** geändert; Regenalarm bleibt keine Aktion, beide Alarmende-Aktionen keine Aktion. Ein erneuter Applikationsdownload wurde gestartet, um die Gegenrichtung über den aktiven Alarm auszuführen. Physische Richtungsbestätigung bleibt erforderlich.

## Freigegebene vollständige Rücknahme am Aktor

Auch nach erfolgreich geladenem Windalarm mit Gegenrichtung meldete der Nutzer keine Bewegung. Anschließend gab er ausdrücklich die Entfernung beider neuen Alarmzuordnungen frei. Windalarm und Regenalarm an Kanal G wurden deaktiviert; ETS bestätigte das Entfernen der Zuordnungen. Die Objektzahl sank von 55 auf 53. Der Applikationsdownload für den ursprünglichen Zustand ohne beide Alarme wurde gestartet. Die Wetterstation sendet weiterhin ihre Werte und den neuen Windgrenzwert, aber der Markisenkanal soll diese nach Download nicht mehr auswerten. Keine Rücknahme anderer Kanäle oder Änderung der OG-Markise.

Der abschließende Download ohne beide Alarmfunktionen war erfolgreich. Nach erneutem Ab-Einzelbefehl bestätigte der Nutzer die Einfahrt. Die Bestätigung erfolgte erst nach vollständiger Rücknahme der Alarmfunktionen; die vorherigen Versuche hatten keine Bewegung ausgelöst. Die Alarmanbindung bleibt deaktiviert.

## Wiederaufnahme nach bestätigter Einfahrt

Der Nutzer verlangte die Wiederaufnahme bei bereits eingefahrener Markise. Beide Alarmaktionen wurden auf Nach unten fahren geprüft, beide Rücknahmeaktionen auf keine Aktion; die zwei Zuordnungen wurden erneut angelegt. Der erneute Assistenten-Download scheiterte. Nach Nutzerstopp mit Escape erfolgten keine weiteren UI-Aktionen in diesem Turn. Auf die anschließende Mitteilung des Nutzers über seinen eigenen JAL-Download wurde ausschließlich lesend geprüft: neuester JAL-Applikationsdownload abgeschlossen, darunter der fehlgeschlagene Versuch; Alarmparameter wie im maßgeblichen Abschlussstand. Keine erneute Fahrt durch den Assistenten bei dieser Schlussprüfung.
