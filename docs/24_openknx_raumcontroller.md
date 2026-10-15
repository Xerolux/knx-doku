# 24 – OpenKNX RaumController

## Änderung vom 14.10.2026: HF-Erfassungsbereich

Die maximale HF-Reichweite wurde im ETS-Projekt für Küche (`1.1.34`) von 5,95 auf 3,15 m und für Bad (`1.1.35`) von 5,95 auf 2,45 m reduziert. Anlass ist die vom Nutzer gemeldete Erfassung von Bewegungen im Vorgarten. Downloadnachweise und offene Funktionstests stehen im [ETS-Protokoll vom 14.10.2026](28_ets_bad_vorne_pm_2026-10-14.md). Die frühere Aussage, die Reichweiten seien unverändert, beschreibt den Stand vom 11.10.2026.

## Änderung vom 11.10.2026: Küche, Bad und Präsenzmelder

Die folgenden Änderungen wurden direkt im geöffneten ETS-Projekt vorgenommen und anhand der Kommunikationsobjekte und Gruppenadressansicht geprüft. Ein Gerätedownload und eine Gruppenmonitorprüfung sind noch nicht erfolgt. Die nachfolgenden älteren Abschnitte dokumentieren den bisherigen Stand mit Quelle `1.1.29`; sie sind keine aktuelle Zuordnung der Küchenmesswerte.

| Quelle | Messwertadressen | Aktueller Stand im ETS-Projekt |
|---|---|---|
| `1.1.34` Raumcontroller Küche | `13/0/0` bis `13/0/6` | Sensorobjekte verbunden; Anforderung KO 43 auf `13/0/20` |
| `1.1.35` Raumcontroller Bad | `13/1/0` bis `13/1/6` | Eigene Mittelgruppe angelegt und Sensorobjekte verbunden |
| `1.1.29` PM Treppenhaus | `13/2/0` bis `13/2/6` | Eigene Mittelgruppe angelegt; alte Küchenmesswertverknüpfungen und `13/0/20` entfernt |

In jeder Mittelgruppe gilt dieselbe Reihenfolge: Temperatur (KO 45, Unteradresse 0), Luftfeuchte (KO 48, 1), Luftdruck (KO 51, 2), rohes VOC (KO 54, 3), echtes CO2 (KO 57, 4), berechnetes CO2-VOC (KO 58, 5) und Helligkeit (KO 61, 6). Die Mittelgruppe `13/0` heißt jetzt `Küche Raumcontroller 1.1.34`.

Am Küchen-MDT `1.1.22` wurden die vorhandenen Empfangsverknüpfungen bestätigt: KO 122 auf `13/0/1`, KO 123 auf `13/0/5`, KO 124 auf `13/0/4`.

Am Bad-MDT `1.1.32` wurden drei Statuswerte aktiviert und verbunden:

| MDT-Objekt | Anzeige | Gruppenadresse | DPT |
|---:|---|---|---|
| 122 | Feuchte, % | `13/1/1` | 9.007 |
| 123 | CO2-VOC, ppm | `13/1/5` | 9.008 |
| 124 | CO2, ppm | `13/1/4` | 9.008 |

Die Bad-Infoanzeige wechselt zwischen Uhrzeit und diesen drei Statuswerten. Die bestehende Temperaturverknüpfung KO 108 auf `3/6/1` wurde beibehalten. Rohes VOC bleibt ein eigener generischer DPT-9-Messwert und wurde nicht als CO2 oder anderer unpassender Datentyp auf die MDT-Anzeige gelegt.

**PM vorerst ohne Lichtsteuerung:** Der Nutzer hat bestätigt, dass das Treppenhauslicht noch nicht existiert und der PM zunächst nichts schalten soll. Bei `1.1.29` wurden deshalb KO 133 von `1/2/0 Küche Licht Schalten` und KO 125 von `1/2/1 Küche Licht Status` getrennt. Die ETS-Objektansicht bestätigt leere Lichtverknüpfungen; Datum/Uhrzeit und die eigenen Messwertadressen `13/2/0–6` bleiben verbunden. Die bestehenden Lichtzuordnungen der Küche und des Bads wurden nicht umgestellt. Diese Änderung ist noch nicht in das physische Gerät geladen.

### Präsenzsteuerung Küche und Bad

Auf ausdrücklichen Nutzerwunsch wurde PM-Kanal 1 in beiden Raumcontrollern aktiviert. Die eingebauten Helligkeitssensoren werden verwendet; Präsenz und Bewegung werden ausgewertet (HF-Sensor und PIR). Die vorhandene Hardwarekonfiguration ist HLK LD2420, analoger PIR und VEML7700 für Helligkeit.

| Raumcontroller | KO 133 Schalten 1 | KO 125 Aktorstatus |
|---|---|---|
| `1.1.34` Küche | `1/2/0 Küche Licht Schalten` | `1/2/1 Küche Licht Status` |
| `1.1.35` Bad | `1/6/0 Badezimmer Licht Schalten` | `1/6/1 Badezimmer Licht Status` |

Die Tagesphase verwendet automatisches Ein- und Ausschalten, eine Einschaltschwelle von 50 Lux und eine Nachlaufzeit von 1 Minute. Ausgang 1 sendet EIN (1) und AUS (0); Ausgang 2 ist inaktiv. Die vorhandenen Werte für HF-Reichweite und Empfindlichkeit wurden nicht geändert. Messwertverknüpfungen bleiben bestehen.

Die Applikationsdownloads für Küche und Bad wurden versucht, beide von ETS als fehlgeschlagen gemeldet. Für Küche lautet der Detailfehler `Verbindung verweigert von 1.1.34`. Deshalb ist die neue Lichtsteuerung bislang nur im ETS-Projekt bestätigt; ein erfolgreicher Gerätedownload und ein realer Präsenz-/Lichttest fehlen.
### Home Assistant live eingebunden und geprüft

Am 11.10.2026 wurden die vorhandenen sieben Küchen-Sensoren auf `13/0/0–6` beibehalten und dem Bereich Küche zugeordnet. Ihre Entitäts-IDs und damit Dashboard- und Historienreferenzen bleiben bestehen. Je sieben neue Sensoren wurden über die KNX-Integration für Bad (`13/1/0–6`) und Treppenhaus (`13/2/0–6`) angelegt und ihren Bereichen zugeordnet. Die Raumklima-Ansicht im EG-Dashboard enthält nun alle drei Räume. Es gibt pro Messwertadresse genau eine KNX-Sensorentität.

| Raum | Entitäts-IDs | Live-Nachweis |
|---|---|---|
| Küche | `sensor.eg_kuche_raumsensor_temperatur` und die vorhandenen `sensor.eg_kuche_raumcontroller_*` | Alle sieben Sensoren haben Werte; Quelle ist ausdrücklich `1.1.34` |
| Bad | `sensor.eg_bad_raumcontroller_*` | Alle sieben Sensoren haben Werte; Quelle ist ausdrücklich `1.1.35` |
| Treppenhaus | `sensor.treppenhaus_pm_*` | Alle sieben Sensoren angelegt; bislang `unknown`, keine Antwort auf den neuen Adressen |

Der Live-Test hat ausschließlich Messwertadressen gelesen (`knx.read`); keine Licht-, Heizungs- oder Rollladen-Schalttelegramme wurden gesendet. Beispiele der Prüfung: Küche ungefähr 25,7 °C und 47,6 %; Bad ungefähr 24,8 °C und 50,2 %. Werte ändern sich mit der Messung. Roh-VOC bleibt ohne erfundene Einheit; echtes CO2 und berechnetes CO2-VOC bleiben getrennt. Neue Sensoren sind als Messwerte eingerichtet, echtes CO2 zusätzlich mit Geräteklasse `carbon_dioxide`.

Die neuen Messwerttelegramme von `1.1.34` und `1.1.35` sind damit live bestätigt, obwohl die zuvor hier dokumentierten eigenen ETS-Downloadversuche fehlgeschlagen waren. Das beweist die aktuellen Sensorquellen, aber noch nicht die Funktion der Präsenz-Lichtsteuerung oder die Anzeige am physischen MDT-Taster. Treppenhaus benötigt weiterhin die wirksame Umstellung des Geräts auf `13/2/0–6`.

Vorherige Konfiguration, neue Sensorzuordnungen und Live-Ergebnis wurden außerhalb des Git-Repositories lokal gesichert. Zugangstoken und private Sicherungsdateien werden nicht veröffentlicht.

**Noch offen:** Treppenhaus-Messwerttelegramme, Funktion der Präsenz-Lichtsteuerung und Anzeigen am Gerät sowie Aktualisierung der ETS-Exportdateien. Die vorhandenen Importdateien bilden weiterhin den früheren Stand ab. Bereits per HA-Oberfläche angelegte Sensoren nicht zusätzlich über YAML importieren.
## Ziel

Der OpenKNX RaumController `1.1.29` stellt seine Raumklimawerte zuerst für Home Assistant bereit. Die Werte liegen auf allgemeinen KNX-Gruppenadressen und können später ohne Doppelbelegung auch von Anzeige-, Logik- oder Lüftungsgeräten verwendet werden.

Die Adressen liegen deshalb in `13 Raumklima` und nicht in `9 Home Assistant`. Home Assistant ist Verbraucher der Messwerte, aber nicht deren Eigentümer oder Voraussetzung.

Der Einbauort von `1.1.29` ist noch zu bestätigen. Bis dahin bleibt die Benennung gerätebezogen; nach der Raumzuordnung können Mittelgruppe und Namen geändert werden, die Adressen selbst bleiben bestehen.

## Gruppenadressen und Objekte

Die im ETS-Screenshot sichtbaren Sensorobjekte entsprechen der OpenKNX-Nummerierung ab RaumController-Applikation 5.1.

| Objekt | Kommunikationsobjekt | Gruppenadresse | DPT | Einheit | Verwendung |
|---:|---|---:|---:|---|---|
| 45 | Temperatur | `13/0/0` | 9.001 | °C | Home Assistant und spätere Raumregelung/Anzeige |
| 48 | Luftfeuchte | `13/0/1` | 9.007 | % | Home Assistant und spätere Lüftungslogik |
| 51 | Luftdruck | `13/0/2` | 9.006 | Pa | Home Assistant/Statistik |
| 54 | VOC | `13/0/3` | 9 | einheitenlos | Home Assistant/Statistik |
| 57 | CO2 | `13/0/4` | 9.008 | ppm | Home Assistant und spätere Lüftungslogik |
| 58 | CO2-VOC | `13/0/5` | 9.008 | ppm | aus VOC berechneter Vergleichswert |
| 61 | Helligkeit | `13/0/6` | 9.004 | lx | Home Assistant und spätere Lichtlogik |
| 43 | Sensorwerte anfordern | `13/0/20` | 1.016 | Trigger | optional: Wert `1` fordert alle Messwerte an |

`CO2-VOC` ist ein aus dem VOC-Signal berechneter Wert. Er darf nicht mit dem echten CO2-Messwert von Objekt 57 gleichgesetzt werden.

Die ETS-Screenshots vom 25.09.2026 belegen, dass der Küchen-Glastaster `1.1.22` alle drei geeigneten Werte anzeigt: Feuchte `13/0/1` auf Statuswert 1, berechnetes `CO2-VOC` `13/0/5` auf Statuswert 2 und echtes `CO2` `13/0/4` auf Statuswert 3. Der rohe VOC-Messwert `13/0/3` ist als generischer DPT 9 dokumentiert; der Taster bietet dafür keinen passenden Statuswert-DPT. `13/0/5` ist ein aus VOC berechnetes CO2-Äquivalent, kein echtes CO2 und kein Roh-VOC. Die vollständige Anleitung steht in [10 – MDT Glastaster Smart II Bedienkonzept](10_glastaster_bedienkonzept.md#küchen-raumklima-am-glastaster-1122). Der ETS-Screenshot belegt die Parametrierung, nicht aber den Download zum physischen Taster oder den Funktionstest dort.

## Weitere sichtbare Objekte

| Objekt | Kommunikationsobjekt | Behandlung |
|---:|---|---|
| 1 | In Betrieb | Noch nicht mit Home Assistant verbinden. Das Objekt kann je nach Parameter als einfacher 1-Bit-Heartbeat oder als erweiterter 1-Byte-Status arbeiten; DPT und Auswertung werden nach Festlegung des Modus geplant. |
| 4 | Uhrzeit/Datum | Mit `0/5/2` verbinden. Der RaumController empfängt damit DPT 19.001 vom KNX-Zeitmaster `1.1.31`; Home Assistant schreibt nicht auf diese Adresse. |
| 30 | IDs unbekannter Geräte | Nicht als normalen HA-Sensor verwenden. DPT 16.001 dient nur während der 1-Wire-Inbetriebnahme zur Ausgabe unbekannter Geräte-IDs; die Gerätesuche soll im Produktivbetrieb deaktiviert sein. |

## ETS-Verknüpfung

1. [gruppenadressen-komplett.xml](../ets-import/gruppenadressen-komplett.xml) in ETS importieren. Falls die Grundstruktur bereits vollständig vorhanden ist, kann alternativ nur [gruppenadressen-raumcontroller.xml](../ets-import/gruppenadressen-raumcontroller.xml) verwendet werden.
2. Beim Gerät `1.1.29` den Bereich **Sensoren** öffnen.
3. Die Objekte 45, 48, 51, 54, 57, 58 und 61 mit den Adressen aus der Tabelle verbinden.
4. Objekt 43 optional mit `13/0/20` verbinden.
5. Objekt 4 unter **OpenKNX** mit der vorhandenen Adresse `0/5/2` verbinden.
6. In den Sensorparametern sinnvolle Sendeintervalle und Wertänderungsschwellen aktivieren.
7. Applikation in das Gerät laden und die Telegramme im ETS-Gruppenmonitor prüfen.

Die Objekt-DPTs der geladenen Produktdatenbank sind verbindlich. Besonders bei älteren OpenKNX-Applikationen können sich Objektnummern unterscheiden; dann anhand von Name und DPT statt nur anhand der Nummer verknüpfen.

## Home Assistant

Die Einträge werden unter dem vorhandenen `knx:`-Block ergänzt. Wenn die KNX-Sensoren bereits per `!include` ausgelagert sind, nur die Listeneinträge übernehmen.

```yaml
knx:
  sensor:
    - name: "RaumController Temperatur"
      state_address: "13/0/0"
      type: temperature
      sync_state: "expire 60"
      state_class: measurement

    - name: "RaumController Luftfeuchte"
      state_address: "13/0/1"
      type: humidity
      sync_state: "expire 60"
      state_class: measurement

    - name: "RaumController Luftdruck"
      state_address: "13/0/2"
      type: pressure_2byte
      sync_state: "expire 60"
      state_class: measurement

    - name: "RaumController VOC"
      state_address: "13/0/3"
      type: 2byte_float
      sync_state: "expire 60"
      state_class: measurement

    - name: "RaumController CO2"
      state_address: "13/0/4"
      type: ppm
      sync_state: "expire 60"
      state_class: measurement
      device_class: carbon_dioxide

    - name: "RaumController CO2-VOC berechnet"
      state_address: "13/0/5"
      type: ppm
      sync_state: "expire 60"
      state_class: measurement

    - name: "RaumController Helligkeit"
      state_address: "13/0/6"
      type: illuminance
      sync_state: "expire 60"
      state_class: measurement
```

Home Assistant liest die Werte beim Start beziehungsweise nach längerer Funkstille aktiv. Der RaumController bleibt der einzige Schreiber auf den Messwertadressen.

Als alternative Konfiguration für eine HA-Instanz ohne bereits vorhandene RaumController-Sensoren liegt die Sensorliste unter [knx_raumcontroller.yaml](../home-assistant/knx_raumcontroller.yaml). Sie kann nach `/config/knx_raumcontroller.yaml` kopiert und im vorhandenen KNX-Block eingebunden werden:

```yaml
knx:
  sensor: !include knx_raumcontroller.yaml
```

Existieren bereits KNX-Sensoren, müssen die neuen Listeneinträge mit der vorhandenen Sensorliste zusammengeführt werden; ein zweiter `knx:`-Schlüssel darf nicht angelegt werden.

Die Live-Prüfung am 25.09.2026 zeigt, dass die Sensoren in Home Assistant bereits als KNX-Entitäten angelegt sind; die oben genannte Datei ist daher nur eine alternative Konfigurationsvorlage und soll nicht zusätzlich eingebunden werden, wenn dieselben Werte schon existieren. Die aktuellen Entity-IDs und Momentwerte stehen in [23 – Home Assistant Dashboard](23_home_assistant_knx_entities_dashboard.md#raumklima-openknx-raumcontroller).

Die Karte **Küche – Raumklima** wurde im bestehenden Dashboard **Übersicht → IOT** gespeichert. Sie liest alle sieben Werte ausschließlich aus Home Assistant; es wurden keine KNX-Schreibtelegramme oder Aktorsteuerungen ausgelöst. Für den Prüfzeitpunkt: Temperatur 25,4 °C, Feuchte 36,48 %, VOC roh 50,0 (generischer DPT 9 ohne Einheit), berechnetes CO2-VOC 500,16 ppm, echtes CO2 656,0 ppm, Luftdruck 95.928 Pa und Helligkeit 0,0 lx. Diese Momentwerte sind keine Sollwerte. Rohes VOC und Helligkeit sollten bei anhaltend 0 anhand der Sensorbestückung und realen Messbedingungen weiter beobachtet werden.

## Bustest vom 17.08.2026

Der Trigger auf `13/0/20` wurde im ETS-Gruppenmonitor erfolgreich gesendet. Der RaumController antwortete auf allen sieben Messwertadressen:

| Gruppenadresse | Beobachteter Wert |
|---:|---:|
| 13/0/0 | 25,74 °C |
| 13/0/1 | 51,6 % |
| 13/0/2 | 95.272,96 Pa |
| 13/0/3 | 0, einheitenlos |
| 13/0/4 | 400 ppm |
| 13/0/5 | 400 ppm |
| 13/0/6 | 0 lx |

Temperatur, Luftfeuchte, Luftdruck und CO2 waren plausibel. VOC und Helligkeit müssen beobachtet werden, weil sie beim Test jeweils `0` lieferten.

## Prüfung

- Im ETS-Gruppenmonitor erscheinen die sieben Messwerte mit plausiblen Einheiten. **Erfüllt am 17.08.2026.**
- Der Trigger auf `13/0/20` wird vom RaumController mit allen sieben Messwerten beantwortet. **Erfüllt am 17.08.2026.**
- In Home Assistant entstehen sieben Sensor-Entitäten ohne DPT-Fehler im Protokoll.
- CO2 und CO2-VOC werden als getrennte Entitäten geführt.
- Home Assistant sendet keine Messwerte auf `13/0/0` bis `13/0/6` zurück auf den Bus.
