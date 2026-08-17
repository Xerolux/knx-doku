# 20 – OpenKNX RaumController

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

Die Sensorliste liegt zusätzlich als direkt einbindbare Datei unter [knx_raumcontroller.yaml](../home-assistant/knx_raumcontroller.yaml). Sie wird beispielsweise nach `/config/knx_raumcontroller.yaml` kopiert und im vorhandenen KNX-Block eingebunden:

```yaml
knx:
  sensor: !include knx_raumcontroller.yaml
```

Existieren bereits KNX-Sensoren, müssen die neuen Listeneinträge mit der vorhandenen Sensorliste zusammengeführt werden; ein zweiter `knx:`-Schlüssel darf nicht angelegt werden.

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
