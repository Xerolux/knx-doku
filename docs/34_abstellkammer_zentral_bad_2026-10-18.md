# 34 – Abstellkammer, Zentralfunktionen und Badrollladen

Stand: 18.10.2026. Änderungen im geöffneten ETS-Projekt, erfolgreiche Applikationsdownloads und die unten genannten HA-/Bustests wurden direkt geprüft.

## Abstellkammerlicht

| Teilnehmer | Objekt / Einstellung | Gruppenadresse |
|---|---|---|
| `1.1.43 Licht Abstellkammer` | KO 0, Ausgang A1 schalten, Wippe A+B Objekt 1 | `12/0/0` |
| `1.1.37 Abstellkammer`, MDT AKK-01UP.03 | KO 0, Kanal A Schalten | `12/0/0` |
| `1.1.37` | KO 7, Kanal A Status | `12/0/1` |
| `1.1.37` | KO 12, Zentralfunktion Schalten; Teilnahme im Kanal aktiviert | `0/4/0` |

Der fehlerhaft als Abstellkammer angelegte **AKS-Kanal H auf `1.1.3` ist nicht aktiv**. Die zugehörigen Gruppenadressverknüpfungen wurden beim Deaktivieren entfernt. Das Gerät selbst bleibt erhalten.

Die frühere MDT-Touch-Funktion wurde eindeutig über die Assoziationen von `12/0/0` identifiziert: **`1.1.33 Bad Gang`, T5/6 Abstellkammer, KO 20**. Nur dieses Tastenpaar wurde auf **nicht aktiv** gesetzt; ETS entfernte die zugehörigen Verknüpfungen. T1/2 Gang und T3/4 Bad bleiben bestehen. Danach enthält `12/0/0` nur noch den UP-Aktor und den neuen Taster.

## Alle Lichter am Eingang / Treppenhaus

Der bestehende Glastaster **`1.1.20 Eingang`** sendet mit KO 0, T1/2 Alle Lichter, auf **`0/4/0`**. Der AKS empfängt diese Adresse auf KO 289. Bei allen sieben belegten Lichtkanälen A–G wurde **Zentralfunktion aktiv** kontrolliert:

- A Wohnzimmer, B Arbeitszimmer, C Küche, D Schlafzimmer;
- E Gang Altbau, F Gang Neubau, G Bad.

Zusätzlich wurden die beiden UP-Aktoren **`1.1.36 Bad vorne`** und **`1.1.37 Abstellkammer`** jeweils mit KO 12 auf `0/4/0` verbunden und die Zentralteilnahme im jeweiligen Kanal aktiviert. Reservekanäle erhalten keine neue Freigabe. AKS-Kanal H ist deaktiviert.

## Alle Rollläden, ohne Markise

Am Taster `1.1.20` bestätigt: KO 10, T3/4 Auf/Ab → **`0/1/0`**; KO 11, Stopp → **`0/1/1`**. Am JAL `1.1.4` sind diese Adressen mit Zentralobjekt 0 beziehungsweise 2 verbunden. Die Zentralobjekte 1, 3 und 4 bleiben unverknüpft.

| JAL-Kanal | Bezeichnung | Zentrale Objekte, live geprüft |
|---|---|---|
| A | Schlafzimmer Türe | absolute Position und Auf/Ab |
| B | Schlafzimmer Fenster | absolute Position und Auf/Ab |
| C | Arbeitszimmer | nur Auf/Ab |
| D | Wohnzimmer Fenster | nur Auf/Ab |
| E | Bad | nur Auf/Ab |
| F | Küche | nur Auf/Ab; Einzeladressen weiterhin unverbunden, reale Motorzuordnung offen |
| G | Markise | **nicht aktiv**, heute korrigiert |
| H | Wohnzimmer Türe | nur Auf/Ab |

Die Markise war entgegen der älteren Dokumentation tatsächlich für **absolute Position und Auf/Ab** freigegeben. Diese Freigabe wurde entfernt. Der bereits vorhandene Wind-/Regenschutz und die individuellen Markisenadressen wurden dabei nicht verändert. Die erweiterte Zentralfreigabe bei A/B bleibt bestehen; mangels Verbindung am Zentralobjekt 3 wird keine zentrale Prozentposition gesendet.

## Badrollladen: automatische Fahrzeitmessung

Kanal E ist als Rollladen mit automatischer Fahrzeitmessung, laufender Fahrzeitkorrektur und Relaisabschaltung über Motorstrom eingerichtet. Fahrzeitverlängerung 5 %, Positionsstatus aktiv, Senden nach Fahrende. Die vorhandene Statusverbindung KO 148 → **`2/3/3`** ist bestätigt; Auf/Ab KO 139 → `2/3/0`, Stopp KO 141 → `2/3/1`. KO 146 für absolute Position bleibt unverknüpft.

Für den gezielten Messstart und dessen Nachweis wurden zwei bisher freie Serviceadressen angelegt:

| Adresse | Funktion | JAL Kanal E |
|---|---|---|
| `2/3/9` | Badezimmer Rollladen Fahrzeitmessung starten, DPT 1.010 | KO 151, 1 Bit |
| `2/3/10` | Badezimmer Rollladen Diagnosetext, 14-Byte-Text | KO 167 |

Nach erfolgreichem JAL-Applikationsdownload wurde über das HA-KNX-Panel genau ein **Startwert 1 auf `2/3/9`** geschrieben. Der Gruppenmonitor bestätigt das ausgehende Telegramm und die folgenden eingehenden Antworten von **`1.1.4`**, jeweils am 18.10.2026 in Ortszeit:

| Uhrzeit | Adresse | Nachweis |
|---|---|---|
| 14:30:53,376 | `2/3/9` | Start, Quelle HA `1.1.255` |
| 14:30:56,437 | `2/3/10` | `Cur: 0253   Dn` |
| 14:31:21,766 | `2/3/3` | `0xff`, 100 % |
| 14:31:21,846 | `2/3/10` | `Saved: 026  Dn` |
| 14:31:23,503 | `2/3/10` | `Cur: 0248   Up` |
| 14:31:45,961 | `2/3/10` | `Saved: 023  Up` |
| 14:31:46,029 | `2/3/3` | `0x00`, 0 % |

Damit sind **26 Sekunden abwärts**, **23 Sekunden aufwärts** und beide Endlagenrückmeldungen nachgewiesen. Die Messfahrt endet oben. KNX zeigt dort 0 % geschlossen; HA verwendet bei Cover-Entitäten den umgekehrten Öffnungsgrad. Eine physische Sichtprüfung des Behanges, der Tasteranzeige und einer Zwischenposition wurde nicht durchgeführt.

Das Verfahren entspricht dem [MDT-Handbuch, Abschnitt 4.3.1](https://www.mdt.de/fileadmin/user_upload/MDT_THB_JAL_02_Jalousieaktor_Fahrzeitmessung_V11.pdf): Messung beider Richtungen über das Startobjekt und Ausgabe der gemessenen Zeiten über das Diagnoseobjekt. Die Serviceadressen sind ausschließlich für Inbetriebnahme und Diagnose vorgesehen.

## Home Assistant und Lovelace

Live angelegt: **`light.eg_abstellkammer_licht`**, Name EG Abstellkammer Licht, Schaltadresse `12/0/0`, Zustandsadresse `12/0/1`, reine Schaltleuchte ohne Dimmung/Farbe. Die eingeblendete Meldung Unbekannte Gruppenadresse bezieht sich auf den älteren in HA importierten ETS-Projektstand; sie verhinderte die Speicherung nicht. Die Verbindung und Rückmeldungen wurden anschließend geprüft.

In **EG → Licht** wurde im vorhandenen Kartenraster die Karte **Abstellkammer** mit `template: card_light` ergänzt und gespeichert. Die lokale Dashboardvorlage enthält dieselbe Karte. Die Datei [knx_abstellkammer_licht.yaml](../home-assistant/knx_abstellkammer_licht.yaml) ist eine YAML-Alternative, kein zusätzlich zu ladendes Paket.

Kurzer Schalt-/Rückmeldetest über die Dashboardkarte:

- 14:32:20,582: HA schreibt Ein auf `12/0/0`; um 14:32:20,611 meldet **`1.1.37`** den Status 1 auf `12/0/1`.
- 14:32:25,976: HA schreibt Aus; um 14:32:26,003 meldet **`1.1.37`** den Status 0.
- Der abschließende Dashboardzustand ist **Aus**, wie vor dem Test. Die physische Lichtwirkung wurde nicht per Sichtkontrolle abgenommen.

## Downloadnachweise und verbleibende Abnahme

Die ETS-Historie zeigt für alle sechs geänderten Geräte **Programmieren(Appl.): Abgeschlossen**:

`1.1.43`, `1.1.37`, `1.1.36`, `1.1.3`, `1.1.33` und `1.1.4`.

Der unveränderte Zentral-Taster `1.1.20` musste nicht erneut programmiert werden. Es wurde kein zentraler Ein-/Aus- oder Auf-/Ab-Befehl für sämtliche Verbraucher ausgelöst. Die Parametrierung und Downloads sind geprüft; die gemeinsame physische Reaktion und die Bedienung am neuen Taster `1.1.43` bleiben als Vor-Ort-Abnahme offen. Batterie-Fenstergriffe wurden bei diesen Arbeiten weder programmiert noch geweckt.

ETS-Projektdateien, Schlüsselbund, Zugangsdaten und Screenshots bleiben außerhalb des öffentlichen Repositorys. Die vorhandenen Änderungen zur Fenstergriff-Erweiterung vom 17.10. wurden nicht verworfen; ihr weiterhin offener Inbetriebnahmestand bleibt dokumentiert.
