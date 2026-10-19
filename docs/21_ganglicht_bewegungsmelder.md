# 21 – Ganglicht und Bewegungsmelder

Stand: 19.10.2026. Der folgende Diagnoseabschnitt hat Vorrang vor den älteren Inbetriebnahmeangaben.

**Aktueller Prüfstand:** Nach erneuter Störungsmeldung nach 20 Uhr ist die Auslöseempfindlichkeit nachts auf **6** angeglichen (tagsüber weiterhin 6), die Präsenzempfindlichkeit auf **5 (mittel)** und zyklisches EIN wieder auf **10 s** gesetzt. Applikationsdownload ausschließlich auf `1.1.30` erfolgreich abgeschlossen. KO 6 bleibt frei; Tag/Nacht-Polarität bleibt Tag 0 / Nacht 1. Die Aktorkanäle E/F verwenden weiterhin 180-s-Treppenlicht. Das zuvor deaktivierte zyklische EIN passte nicht zu diesen Aktorzeiten. **Zwei echte Durchgänge mit anschließender Abwesenheit haben nun jeweils EIN und selbständiges Melder-AUS einschließlich beider Aktorstatus bestätigt.** Der Nutzer bestätigt das erneute Einschalten beider Lichter nach der ersten Abschaltung. Die nachfolgenden Teststufen dokumentieren auch inzwischen zurückgenommene Einstellungen.

### Erneute Störung nach der Heizmodus-Programmierung

Der Nutzer meldet nach der separaten Heizungsprogrammierung, dass der Gangmelder nicht reagiert. Der Gruppenmonitor zeigt zuletzt **19:58:55,112** einen als **EIN** dekodierten Befehl von `1.1.30` auf `1/4/4`, gefolgt von Aktor-/Sammelstatus. Um **20:01:54,669 / ,739 / ,756** folgen die beiden Aktorstatus und der Sammelstatus, ungefähr 180 s später. Bis zur Prüfung nach 20:15 Uhr kein weiterer Schaltbefehl des Melders auf dieser Adresse.

Der Zeitablauf passt zur bekannten Inkonsistenz aus Treppenlicht und deaktiviertem Nachtriggern; er beweist weder einen Hardwaredefekt noch einen Einfluss der Heizungsprogrammierung. Zusätzlich war nachts nur Auslöseempfindlichkeit 3 eingestellt. Die ETS-Parameterprüfung bestätigt Lichtkanal 1 aktiv, alle vier Sensorbereiche aktiv, Vollautomat, EIN und AUS, Nachlauf Tag 3 min / Nacht 1 min und KO 6 frei.

Als gezielte nächste Korrekturstufe wurden Nacht-Auslösung 6, Präsenz 5 und zyklisches EIN 10 s geladen (ETS: „Programmieren (Appl.): Abgeschlossen“). Damit wird der Timer während aktiver Melderautomatik nachgetriggert; die mittlere Präsenzempfindlichkeit prüft das frühere unerwünschte Festhalten. Der Download startet den Melder neu und ist allein kein Beweis für eine dauerhafte Behebung. Die nächtliche Auslöseempfindlichkeit ist eine begründete Hypothese, keine bewiesene alleinige Ursache; allein die Uhrzeit nach 20 Uhr bestätigt noch nicht den Zustand der Melderadresse `0/0/2`.

Erneuter physischer Durchgang, Nutzer meldet anschließend „draußen“:

| Zeit | Quelle und Telegramm | Ergebnis |
|---|---|---|
| 20:25:54,999 | 1.1.30 → 1/4/4 | Neustart nach Download, kein Bewegungsnachweis |
| 20:27:02,454 | 1.1.30 → 1/4/4, EIN | Echter Bewegungszyklus nach angefragtem Durchgang |
| 20:27:02,517 / ,546 / ,581 | 1.1.3 → 1/4/1, 1.1.8 → 1/4/5, 1.1.3 → 1/4/3 | Beide Lichtkreise eingeschaltet |
| 20:27:12,493 bis 20:30:02,505 | 1.1.30 → 1/4/4, jeweils EIN alle ca. 10 s | Aktorzeiten werden während aktiver Melderautomatik nachgetriggert |
| **20:30:12,032** | **1.1.30 → 1/4/4, als AUS dekodiert** | **Melder beendet den Zyklus selbständig** |
| 20:30:12,032 | 1.1.3 → 1/4/1 und 1/4/3, 1.1.8 → 1/4/5 | Aktor-/Sammelstatus folgen dem AUS |
| 20:33:44,911 | 1.1.30 → 1/4/4, EIN | Wiederanlauf nach erster Abschaltung; Nutzer bestätigt beide Lichter EIN |
| 20:33:44,973 / 20:33:45,023 / ,032 | 1.1.3 → 1/4/1, 1.1.8 → 1/4/5, 1.1.3 → 1/4/3 | Beide Aktorkanäle und Sammelstatus EIN |
| 20:33:54,938 bis 20:36:55,052 | 1.1.30 → 1/4/4, zyklisch EIN | Nachtriggerung auch im zweiten Zyklus |
| **20:36:56,691** | **1.1.30 → 1/4/4, AUS** | **Zweiter Zyklus selbständig beendet** |
| 20:36:56,892 / ,892 / ,929 | 1.1.3 → 1/4/1 und 1/4/3, 1.1.8 → 1/4/5, jeweils als AUS dekodiert | Beide Lichtkreise abschließend AUS |

Die beiden Melder-AUS-Nachweise unterscheiden diese erfolgreichen Zyklen vom früheren bloßen Ablaufen der Aktorzeit. Einschalten, Nachtriggerung, selbständiges Abschalten und Wiederanlauf sind nun zweimal nacheinander am Bus geprüft; das erneute Einschalten beider Lampen ist zusätzlich vor Ort bestätigt. Die zuvor geprüfte unabhängige manuelle 180-s-Abschaltung der unveränderten Aktorkanäle bleibt bestehen. Ein erneutes manuelles AUS während aktiver Automatik kann weiterhin durch das nächste zyklische EIN aufgehoben werden.

Räumliche Abdeckung, expliziter Nachtzustand und langfristige Störfreiheit sind damit noch nicht vollständig abgenommen. Im Verlauf auf `0/0/2` sind nach dem Neustart nur Leseanfragen von 1.1.30 (20:25:44,338 / 20:25:45,111 / 20:25:55,023) sichtbar, keine bestätigte externe Nacht-Rückmeldung. Deshalb wird die angeglichene Nachtempfindlichkeit nicht als bewiesene Ursache der aktuellen Besserung bezeichnet. Die Laufzeiten der beiden Zyklen entsprechen ungefähr der Tag-Nachlaufzeit von drei Minuten.

## Diagnose vom 19.10.2026 – manuelle Bedienung und Automatik

Gemeldetes Fehlerbild: Nach gemischter manueller Bedienung der beiden Ganglichtkreise bleibt Licht eingeschaltet oder die Automatik reagiert nicht wie erwartet.

Im geöffneten ETS-Projekt direkt festgestellt:

- `1.1.30 Gang Bewegung`, Applikation **Präsenzmelder 360° KLR 4S**: KO 0 sendet auf `1/4/4`; KO 3 (externer Taster kurz), KO 4 (externer Taster lang) und KO 6 (Status Aktorkanal) waren unverbunden.
- Vollautomat, Nachlaufzeit Tag 3 min / Nacht 1 min, alle vier Sensorbereiche aktiv; kein zyklisches EIN. Handbetrieb fällt nach Präsenz und Nachlaufzeit zurück.
- KO 90 war bereits mit `0/0/2 Nachtmodus` verbunden, jedoch mit **Tag = 1 / Nacht = 0** parametriert. Dies widerspricht der vorgesehenen Hauspolarität `1 = Nacht`.

Im ETS-Projekt geändert:

1. Tag/Nacht-Polarität auf **Tag = 0 / Nacht = 1** korrigiert. ETS entfernt beim Wechsel die Zuordnung des bisherigen Objekttyps; anschließend KO 90 gezielt erneut mit der bestehenden Adresse `0/0/2` verbunden.
2. **KO 6 Status Aktorkanal → `1/4/5 Gang beide Lichter Status`** verbunden. Die beiden Einzelstatusadressen werden weiterhin ausschließlich über den ODER-Sammelstatus zusammengeführt.

Diese Rückmeldung und die Polaritätskorrektur waren zunächst eine Korrekturstufe, kein Nachweis, dass jedes manuelle EIN bereits eine Nachlaufzeit startet. Der folgende Test zeigte, dass zusätzlich die zeitgesteuerten Aktorkanäle erforderlich waren. Die Eingänge „externer Taster kurz/lang“ bleiben frei, um die Einzelbedienung zu erhalten und keine Rückkopplung der eigenen Melderausgabe zu erzeugen.

Der erste Applikationsdownload um **17:08:35–17:08:39 Uhr** scheiterte mit **„Verbindung verweigert von 1.1.30“**. Nach angefragter Programmierfreigabe wurde ein erneuter Download in der ETS-Historie als **„Programmieren(Appl.): Abgeschlossen“** bestätigt. Die Änderungen sind damit geladen; die vollständige Funktionsabnahme ist davon getrennt.

Busnachweise vom 19.10.2026 (Ortszeit):

| Uhrzeit | Nachweis |
|---|---|
| 17:10:55,941 / 17:10:55,955 | Leseanfrage auf `1/4/5`; `1.1.8` antwortet mit **0 / Aus**. Der ODER-Sammelstatus ist somit tatsächlich am Bus verfügbar. |
| 17:11:43,109 | Gezieltes manuelles **EIN** nur auf `1/4/0`, Quelle ETS. |
| 17:11:43,198 / 17:11:43,230 | Aktor `1.1.3` meldet auf `1/4/1`; Logikmodul `1.1.8` sendet den Sammelstatus auf `1/4/5`. |

Der Einzel-EIN-Test blieb auch nach mehr als drei Minuten ohne AUS-Telegramm des Melders. Damit reicht die neue Verbindung zu KO 6 für den geforderten Schutz gegen dauerhaftes manuelles EIN **nicht** aus.

Zweite Korrekturstufe erfolgreich auf `1.1.3` und `1.1.30` programmiert (jeweils **„Programmieren(Appl.): Abgeschlossen“** in ETS): Beide Gang-Aktorkanäle schalten selbst nach **180 Sekunden ohne erneutes EIN** ab (Treppenlicht, Zeit neu starten, manuelles AUS aktiv, keine Vorwarnung). Der Melder sendet während aktiver Automatik zyklisches EIN alle **10 Sekunden**, damit seine aktive Automatik die Aktorzeiten nachtriggert. Ein normales AUS des Melders schaltet über das Treppenlichtobjekt unmittelbar ab. Die bisherige Helligkeitsschwelle bleibt bestehen. Ein manuelles AUS während noch aktiver Melderautomatik kann durch das nächste zyklische EIN wieder aufgehoben werden; es ist keine dauerhafte Automatiksperre. Die vom Benutzer gewünschte Einzelbedienung bleibt erhalten, mit automatischer Abschaltung auch nach manuellem EIN. Parametrierung, Download und echte PIR-Auslösung einschließlich zyklischer Telegramme sind bestätigt; Nachweise siehe unten.

| Gerät / Kanal | Objekt | Gruppenadressen nach Umstellung |
|---|---|---|
| `1.1.3`, E Licht Gang | KO **50**, Treppenlicht | `1/4/0`, `1/4/4`, `0/4/0` |
| `1.1.3`, E Licht Gang | KO 56, Status | `1/4/1` |
| `1.1.3`, F Licht Neubau | KO **62**, Treppenlicht | `1/4/2`, `1/4/4`, `0/4/0` |
| `1.1.3`, F Licht Neubau | KO 68, Status | `1/4/3` |

Das zusätzliche Dauer-Schaltobjekt bleibt in beiden Kanälen deaktiviert. Die bisherige Zentralteilnahme ist in E/F deaktiviert; stattdessen liegt derselbe Befehl `0/4/0` direkt an den Treppenlichtobjekten, damit auch Zentral-EIN die Abschaltzeit startet. Die Zentralteilnahme der übrigen Kanäle wurde nicht verändert. Bei Busspannungswiederkehr starten E/F mit AUS, bei Busspannungsausfall keine Änderung. Sperren: keine Änderung; Entsperren: AUS. Die ursprünglichen Bezeichnungen wurden nach dem Funktionswechsel wiederhergestellt. ETS entfernt beim Funktionswechsel die bisherigen Kanalverknüpfungen; die sechs Befehls- und zwei Statusverbindungen wurden gezielt neu angelegt.

### Bustests der ersten Korrekturstufe

| Uhrzeit | Befehl / Rückmeldung | Ergebnis |
|---|---|---|
| 17:24:36,579 | EIN auf `1/4/0`; Status `1/4/1` um 17:24:36,698 | Altbau einzeln eingeschaltet |
| 17:25:06,654 | EIN auf `1/4/2`; Status `1/4/3` um 17:25:06,783 | Neubau einzeln eingeschaltet |
| 17:26:05,516 | erneut EIN auf `1/4/0`, während E bereits EIN | Nachtriggern ohne zusätzliche Statusänderung |
| 17:28:06,347 | Aktor `1.1.3` sendet **AUS** auf `1/4/3` | Neubau schaltet nach rund 180 s selbst ab; Altbau läuft unabhängig weiter |
| 17:29:05,264 / 17:29:05,285 | Status `1/4/1`, anschließend Sammelstatus `1/4/5` | Altbau schaltet rund 180 s nach erneutem EIN ab; beide Kreise wieder AUS. Kein vorzeitiges Ausschalten zur ursprünglichen Frist um 17:27:36. |
| 17:29:46,374 | gemeinsames EIN auf `1/4/4`; Status E um ,458, Sammelstatus um ,494, Status F um ,521 | beide Kreise gemeinsam eingeschaltet |
| 17:30:39,010 / 17:30:39,141 | Einzel-AUS auf `1/4/0`, Status E | Altbau sofort AUS; Neubau bleibt EIN, kein falscher AUS-Sammelstatus |
| 17:31:09,097 / 17:31:09,212 / 17:31:09,346 | gemeinsames AUS auf `1/4/4`, Status F, Sammelstatus | Neubau ebenfalls sofort AUS, abschließend beide AUS |

Damit sind Einzelbedienung, Gruppenbedienung, unabhängige automatische Abschaltung und Neustart der Abschaltzeit direkt mit KNX-Telegrammen geprüft. Die Befehle wurden gezielt über ETS an dieselben Gruppenadressen wie Taster/HA gesendet. Zentralbefehle wurden zur Vermeidung von Auswirkungen auf andere Räume nicht ausgelöst.

### Bewegungstest mit Rückmeldung des Benutzers

Der Benutzer bestätigte, dass jemand durch den Gang gelaufen ist. Im laufenden Gruppenmonitor ist die echte Quelle **`1.1.30 Gang Bewegung`** eindeutig von den vorherigen ETS-Testbefehlen zu unterscheiden:

- **17:33:40,578:** Melder sendet EIN auf `1/4/4`.
- **17:33:40,703 / ,731 / ,766:** Rückmeldungen von Aktor E, Logik-Sammelstatus und Aktor F.
- **17:33:50,658; 17:34:00,592; 17:34:10,588; 17:34:20,594; 17:34:30,698** und weitere: Melder sendet zyklisch EIN im eingestellten Abstand von rund 10 Sekunden. Ein solches Telegramm wurde in den ETS-Details als **1 / Ein** dekodiert.
- **17:35:27,110 / ,164:** Gezieltes Einzel-AUS über ETS auf `1/4/0`, Aktor E meldet AUS; Aktor F bleibt eingeschaltet. **17:35:30,609 / ,757:** Nächstes zyklisches EIN von `1.1.30` auf `1/4/4`, Aktor E meldet wieder EIN. Damit ist die automatische Wiederübernahme nach manueller Einzelbedienung während eines echten Melderzyklus am Bus bestätigt.

Der Melder sendete bis mindestens **18:21:11,292** weiterhin zyklisch EIN. Der Benutzer bestätigte ausdrücklich, dass der Gang seit mindestens drei Minuten vollständig leer war, einschließlich Bewegung vor offenen angrenzenden Türen. Damit war dieser Bewegungstest **fehlgeschlagen**: Die wiederholten EIN-Befehle starteten die Aktorzeiten ständig neu. Diese damalige Korrekturstufe war **nicht abgenommen**; die späteren erfolgreichen Tests nach 20 Uhr stehen am Dokumentanfang.

Als isolierter Diagnoseversuch wurde anschließend ausschließlich die zuvor hinzugefügte Verbindung **KO 6 → `1/4/5` wieder entfernt**. Applikationsdownload auf `1.1.30`: ETS meldet **abgeschlossen**. Beim Neustart sendet der Melder um **18:21:35,561** auf `1/4/4`; anschließend folgen die beiden Aktorstatus und der Sammelstatus bis **18:21:35,688**. Ein Neustart ist kein Nachweis für behobenes automatisches Abschalten. Ein neuer echter Bewegungszyklus mit anschließender Abwesenheit wurde angefragt. Die Empfindlichkeit wurde nicht verändert; eine Rückkopplung oder ein Sensordefekt ist bislang nicht als Ursache bewiesen.

Der angefragte neue Durchgang wurde vom Benutzer bestätigt: **18:26:32,444** EIN von `1.1.30` auf `1/4/4`, danach Status E um **,576**, Sammelstatus um **,611**, Status F um **,642**. Trotzdem weiterhin zyklische EIN-Befehle bis mindestens **18:30:22,502**, ohne abschließendes AUS. Das Entfernen der Statusrückführung allein hat den Fehler somit nicht behoben.

Die Nachlaufparameter wurden erneut direkt geprüft: Tag **3 min**, Nacht **1 min**, Vollautomat. Als nächster Diagnoseversuch wurde die **Präsenzempfindlichkeit von 8 (hoch) auf 5 (mittel)** reduziert und erfolgreich als Applikation geladen (ETS: **abgeschlossen**). Neustarttelegramm um **18:32:20,407**, anschließend Aktorstatus E/F und Sammelstatus bis **18:32:20,646**. Die Auslöseempfindlichkeiten für das erste Einschalten bleiben Tag 6 / Nacht 3. Dies prüft die Hypothese, dass nach der ersten Erkennung kleine Störungen den Präsenzzustand aufrechterhalten; eine Ursache ist dadurch noch nicht bewiesen. Die Funktionsabnahme dieser Änderung steht aus.

Die Richtung vorne/hinten wurde vom Benutzer nicht einzeln benannt; eine vollständige Prüfung der räumlichen Sensorabdeckung und der nächtliche Betrieb bleiben getrennte Vor-Ort-Abnahmen.

Wichtig bei der Aktorumstellung: Das zusätzliche Dauer-Schaltobjekt der Treppenlichtfunktion darf die bestehenden Gangbefehle nicht weiterhin empfangen. Die Einzel- und Gruppenbefehle müssen am zeitgesteuerten Treppenlichtobjekt liegen. Herstellerreferenz: [MDT-Handbuch AKI/AKS, Version 1.6, Abschnitt 4.5](https://www.mdt.de/fileadmin/user_upload/user_upload/download/MDT_THB_AKI_03_04_AKS_03_Schaltaktor_V16.pdf).

Kein Zentralbefehl und keine Betätigung von Rollläden, Markise oder anderen Verbrauchern. Private Freigabewerte und Telegrammaufzeichnungen mit Sicherheitsdaten werden nicht in das Repository übernommen.

Herstellerreferenz: [MDT-Handbuch SCN-x360xx.03, Version 1.7](https://www.mdt.de/fileadmin/user_upload/user_upload/download/SCN-x360xx-03_MDT_TM_V17_DE.pdf), insbesondere Kommunikationsobjekte sowie Abschnitte 4.2.5–4.2.8. „Statusinformation“ ist dort ein Ausgang für Automatik-/Handbetrieb und nicht die Rückmeldung des Schaltaktors an KO 6.

## Ziel

Im Gang sind zwei getrennte Lichtkreise vorhanden. Beide bleiben einzeln bedienbar und erhalten zusätzlich einen gemeinsamen Schaltbefehl. Der Präsenz-/Bewegungsmelder `1.1.30 Gang Bewegung` schaltet über diesen gemeinsamen Befehl beide Lichtkreise.

## Beteiligte Geräte

| Gerät | Funktion |
|---|---|
| MDT Schaltaktor `1.1.3` | schaltet die beiden Gang-Lichtkreise auf Kanal E und F |
| Präsenz-/Bewegungsmelder `1.1.30` | Automatik für beide Ganglichter |
| MDT Glastaster im Gang | manuelle Einzel- oder Gruppenbedienung |
| MDT Logikmodul `1.1.8` | erzeugt in Funktion F1 den gemeinsamen ODER-Status |

Die genaue Bestellnummer des Präsenzmelders wird noch anhand des eingebauten Geräts bestätigt. In ETS sind vier aktive Sensorbereiche und bis zu vier Lichtkanäle sichtbar.

## Gruppenadressen im Gang

| Gruppenadresse | Name | DPT | Verwendung |
|---:|---|---|---|
| `1/4/0` | Gang Licht Schalten | 1.001 | einzelner Lichtkreis auf Aktorkanal E |
| `1/4/1` | Gang Licht Status | 1.001 | Rückmeldung von Aktorkanal E |
| `1/4/2` | Licht Gang Neubau Schalten | 1.001 | einzelner Lichtkreis auf Aktorkanal F |
| `1/4/3` | Licht Gang Neubau Status | 1.001 | Rückmeldung von Aktorkanal F |
| `1/4/4` | Gang beide Lichter schalten | 1.001 | gemeinsamer Schaltbefehl für E und F |
| `1/4/5` | Gang beide Lichter Status | 1.001 | ODER-Sammelstatus aus `1/4/1` und `1/4/3` |

Die Adressen `1/4/4` und `1/4/5` liegen innerhalb der bereits vorhandenen Mittelgruppe `1/4 Gang`. Eine zusätzliche Mittelgruppe ist nicht erforderlich und wegen des Limits von acht Mittelgruppen unter der Hauptgruppe `1 Licht` auch nicht möglich.

## Schaltaktor `1.1.3`

### Kanal E – Licht Gang

```text
Objekt 50 Treppenlicht (180 s, seit 19.10.2026)
    -> 1/4/0 Gang Licht Schalten
    -> 1/4/4 Gang beide Lichter schalten
    -> 0/4/0 Alle Lichter schalten

Objekt 56 Status
    -> 1/4/1 Gang Licht Status
```

### Kanal F – Licht Neubau / Gang Neubau

```text
Objekt 62 Treppenlicht (180 s, seit 19.10.2026)
    -> 1/4/2 Licht Gang Neubau Schalten
    -> 1/4/4 Gang beide Lichter schalten
    -> 0/4/0 Alle Lichter schalten

Objekt 68 Status
    -> 1/4/3 Licht Gang Neubau Status
```

Ein Schaltobjekt darf mehrere Gruppenadressen besitzen. Dadurch können beide Lichtkreise weiterhin einzeln und zusätzlich gemeinsam geschaltet werden.

## Gemeinsamer Status

Die beiden Statusobjekte `1/4/1` und `1/4/3` werden **nicht direkt gemeinsam** auf dieselbe Statusadresse gelegt. Zwei Aktorkanäle würden sonst unabhängig auf dieselbe Gruppenadresse schreiben und der angezeigte Zustand wäre nicht eindeutig.

Der Sammelstatus `1/4/5` wird durch genau eine ODER-Logik erzeugt:

```text
1/4/1 ODER 1/4/3
    -> 1/4/5 Gang beide Lichter Status
```

Damit bedeutet `1` auf `1/4/5`: Mindestens eines der beiden Ganglichter ist eingeschaltet.

Die Umsetzung ist in Funktion F1 des MDT Logikmoduls `1.1.8` angelegt:

```text
Objekt 0  Logik Eingang 1 -> 1/4/1
Objekt 1  Logik Eingang 2 -> 1/4/3
Objekt 9  Logik Ausgang   -> 1/4/5
```

F1 verwendet `Logikgatter / Inverter`, `Logikgatter, 8 Eingänge mit Sperre`, Logikfunktion `ODER`, zwei normale externe Eingänge und einen normalen Ausgang vom Typ `Ein/Aus`. Eingänge 3–8, Sperre, Filter, Verzögerung und zyklisches Senden sind deaktiviert. Gesendet wird bei Änderung des Ausgangs. Beide Eingänge werden nach Reset abgefragt; der Ausgang sendet erst, wenn beide Eingänge gültig sind.

Am Ausgangsobjekt 9 sind **Kommunikation, Lesen und Übertragen** aktiv; Schreiben und Aktualisieren sind aus. Der Datentyp ist `1.001 Schalten`. Damit beantwortet ausschließlich das Logikmodul Leseanfragen auf `1/4/5`.

Der gemeinsame Status ist seit 19.10.2026 am Bus bestätigt. Die versuchsweise Verbindung mit KO 6 des Präsenzmelders wurde im weiteren Diagnoseverlauf wieder entfernt; KO 6 ist aktuell frei. Der Sammelstatus kann weiterhin die Statusanzeige eines Glastasters versorgen.

## Präsenz-/Bewegungsmelder `1.1.30`

### Kommunikationsobjekte

| Objekt | Funktion | Verbindung / Stand |
|---:|---|---|
| 0 | Lichtkanal 1 – Ausgang 1, Schalten | `1/4/4 Gang beide Lichter schalten` |
| 3 | Externer Taster kurz | derzeit frei |
| 4 | Externer Taster lang | derzeit frei |
| 5 | Externe Bewegung / Slave | derzeit frei |
| 6 | Status Aktorkanal | aktuell frei; versuchsweise Verbindung mit `1/4/5` am 19.10.2026 wieder entfernt |
| 7 | Bewegungserkennung sperren | derzeit frei |
| 8 | Zwangsführung | derzeit frei |
| 11 | Dunkel schalten | derzeit frei |
| 13 | Nachlaufzeit über Objekt | derzeit frei |
| 90 | Tag/Nacht | `0/0/2`, seit 19.10.2026 passende Polarität Nacht = 1 |
| 92 | LED Rot blinken | derzeit frei; deaktivieren, wenn ungenutzt |
| 97 | Helligkeit Messwert | derzeit frei |
| 98 | Einschaltschwelle einstellen | derzeit frei |
| 99 | Teach-In starten | derzeit frei |

### Allgemeine Einstellungen – aktueller ETS-Stand

```text
„In Betrieb“ zyklisch senden: nicht aktiv
Tag/Nacht-Objekt: abfragen nach Reset
Wert für Tag/Nacht: Tag = 0 / Nacht = 1 (korrigiert am 19.10.2026)
Umschaltung Tag/Nacht: bei nächster Präsenz

Auslöseempfindlichkeit Tag: 6
Auslöseempfindlichkeit Nacht: 6 (nach erneuter Störung nach 20 Uhr angeglichen)
Präsenzempfindlichkeit: 5 (mittel), zwei Abwesenheitszyklen mit Wiederanlauf am Bus bestanden
Empfindlichkeit für Sensoren reduzieren: nicht aktiv

Einschaltschwelle Tag: 400 Lux
Einschaltschwelle Nacht: 400 Lux
Ausschalten beim Überschreiten: nicht aktiv

Rückfall Zwangsführung/Sperre: nicht aktiv
Rückfall externer Taster lang: nach Präsenz und Nachlaufzeit
Handbetrieb-Nachlaufzeiten EIN/AUS Tag/Nacht: jeweils 3 min
```

### Lichtkanal 1 – aktueller ETS-Stand

```text
Aktive Sensoren: 1, 2, 3 und 4
Empfindlichkeit: Grundeinstellung
Helligkeit: Grundeinstellung oder Objekt „Dunkel schalten“
Betriebsart: Vollautomat
Bewegungsfilter: nicht aktiv
Verkürzung der Nachlaufzeit: nicht aktiv
Nachlaufzeit Tag: 3 min
Nachlaufzeit Nacht: 1 min

Zwangsführungsobjekt: 2 Bit
Rückfall Zwangsführung/Sperre: aktiv
Objekttyp Ausgang Licht: Schalten
Tag/Nacht: ein gemeinsames Ausgangsobjekt
Ausgangsobjekt 1 sendet: EIN und AUS
Zyklisches EIN: 10 s (seit 19.10.2026)
Zusätzlicher Ausgang 2: nicht aktiv
Statusinformation: nicht aktiv
```

Verhalten externer Taster im aktuellen Stand:

```text
Taster kurz reagiert auf: EIN und AUS
Totzeit nach Taster kurz AUS: 5 s
Taster lang reagiert auf: EIN und AUS
Totzeit nach Ausschalten: 1 s
Bei aktivem Nachtlicht: auf Taglicht schalten
Wenn Ausgang Tag bereits EIN: auf Handbetrieb schalten
```

### Helligkeitsmessung – aktueller ETS-Stand

```text
Lichtkanäle beeinflussen die Helligkeitsmessung: ja
Helligkeit senden bei Änderung: 10 %
Messwert zyklisch senden: nicht aktiv
Korrektur Luxwert: 0 %
Raum-Reflektionsfaktor: 0,4 Mittel
Schwellwertschalter: nicht aktiv
Teach-In-Wert: 450 Lux
Teach-In-Wert beim Laden: halten
```

Die Einschaltschwelle von `400 Lux` ist für die erste Inbetriebnahme und einen Funktionstest geeignet. Nach einigen Tagen Betrieb wird sie anhand der realen Beleuchtung angepasst. Für einen Gang ist häufig ein niedrigerer Wert sinnvoll; die endgültige Einstellung richtet sich nach Tageslicht, Montageort und gewünschtem Komfort.

### LED – aktueller ETS-Stand

```text
LED Grün: aktiv bei Bewegung
Lichtkanal 1: aktiv
Lichtkanal 2–4: nicht aktiv
LED Rot / Objekt „LED Rot blinken“: aktiv, aber Objekt nicht verbunden
LED Weiß / Nachtlicht: nicht aktiv
```

Das rote Blinkobjekt wird deaktiviert, wenn keine Diagnose- oder Alarmfunktion dafür vorgesehen ist.

## Tag/Nacht-Anbindung

Das vorhandene Hausobjekt `0/0/2 Nachtmodus` verwendet `1 = Nacht`. Am 19.10.2026 wurde die bereits bestehende, aber falsch gepolte Verbindung korrigiert.

Bestätigte Einstellung seit 19.10.2026:

```text
Tag = 0 / Nacht = 1
```

Bestätigte Verbindung:

```text
0/0/2 Nachtmodus
    -> Objekt 90 Tag/Nacht des Präsenzmelders
```

Alternativ wäre eine eigene invertierte Tag/Nacht-Gruppenadresse mit vorgeschalteter Logik möglich. Die direkte Anpassung der Polarität im Präsenzmelder ist einfacher.

## Glastaster im Gang

Für eine Taste, die beide Ganglichter gemeinsam schaltet:

```text
Tasterobjekt Schalten
    -> 1/4/4 Gang beide Lichter schalten
```

Nach erfolgreicher Programmierung und Busprüfung kann die Statusanzeige verbunden werden:

```text
1/4/5 Gang beide Lichter Status
    -> Status für Anzeige am Glastaster
```

## Programmierung

Nach Abschluss der Verknüpfungen vollständig programmieren:

1. Schaltaktor `1.1.3`
2. Präsenz-/Bewegungsmelder `1.1.30`
3. betroffene Glastaster
4. Logikmodul `1.1.8`

Bei blockiertem ETS-Zugriff wird am MDT SCN-SAFE.01 vorübergehend die zeitlich begrenzte Programmierfreigabe aktiviert. Passwörter, Schlüssel und private ETS-Projektdateien gehören nicht in dieses Repository.

## Funktionstest

1. Über `1/4/0` nur Kanal E schalten.
2. Über `1/4/2` nur Kanal F schalten.
3. Über `1/4/4` beide Kanäle gleichzeitig ein- und ausschalten.
4. Im Gruppenmonitor prüfen, dass der Bewegungsmelder bei erkannter Bewegung `1` auf `1/4/4` sendet.
5. Ohne weitere Bewegung muss nach 3 Minuten am Tag beziehungsweise 1 Minute in der Nacht `0` gesendet werden.
6. Helligkeitsabhängigkeit zunächst bei ausreichend dunkler Umgebung prüfen; für einen reinen Funktionstest vorübergehend helligkeitsunabhängig parametrieren.
7. Manuelle Bedienung und Rückfall aus dem Handbetrieb testen.
8. Prüfen, dass `1/4/5` bei mindestens einem eingeschalteten Ganglicht `1` und nur bei beiden ausgeschalteten Ganglichtern `0` liefert.
9. Eine `GroupValueRead`-Anfrage auf `1/4/5` senden und die Antwort des Logikmoduls `1.1.8` kontrollieren.
10. Nach Busspannungswiederkehr Tag/Nacht, Status und Automatik erneut prüfen.

## Offene Punkte

- genaue Bestellnummer des Präsenzmelders bestätigen
- räumliche Sensorabdeckung in beiden Richtungen, gemischte physische Tasterbedienung und expliziten Nachtbetrieb ergänzend abnehmen; zwei Bewegung-/Abwesenheitszyklen mit Wiederanlauf sind am 19.10.2026 bestätigt, siehe Prüfstand am Dokumentanfang
- rote Blink-LED deaktivieren, sofern nicht benötigt
- Luxschwelle im realen Betrieb optimieren
- Bezeichnung `Licht Neubau` beziehungsweise `Licht Gang Neubau` vereinheitlichen
