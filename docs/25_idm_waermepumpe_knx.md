# 25 – IDM Wärmepumpe über Home Assistant

## Ziel

Die IDM Navigator Wärmepumpe wird über Modbus TCP von Home Assistant gelesen. Die KNX-Bridge der Integration [idm-heatpump-hass](https://github.com/Xerolux/idm-heatpump-hass) legt diese Werte zusätzlich auf den KNX-Bus, damit Glastaster, Visualisierung und Logikmodul sie ohne Home-Assistant-Umweg anzeigen und teilweise auch setzen können.

IDM verkauft die KNX-Anbindung des Navigators sonst als **Weinzierl KNX IP BAOS 774**. Die Bridge bildet dessen Kommunikationsobjekte nach — gleiche Objektnummern, gleiche DPTs, gleiche Schreibrichtung —, sodass das Modul nicht beschafft werden muss.

> **Experimentell.** Die Bridge ist bislang nur durch Tests abgesichert und war noch nie an einem echten KNX-Bus. Diese Anlage ist damit der erste Praxistest. Was dabei auffällt, gehört zurück ins Integrations-Repository.
>
> Besonders zu prüfen: ob die gesendeten Werte auf dem Taster korrekt dekodiert werden, ob eine Leseanfrage nach einem Neustart tatsächlich beantwortet wird, und ob ein erster Vollexport den Bus stört.

## Abgrenzung

Die Bridge ist **kein KNX-Gerät**. Sie hat keine Applikation, wird nicht mit ETS programmiert und bekommt keine physikalische Adresse. Sie sendet über die KNX-Integration von Home Assistant, die ihrerseits über das vorhandene IP-Interface am Bus hängt. KNX Secure, Tunneling und Routing bleiben Sache der KNX-Integration.

In ETS ist deshalb nur zweierlei zu tun: die Gruppenadressen anlegen und die Kommunikationsobjekte der **echten** Geräte damit verbinden.

## Adressbereich

Hauptgruppe `11` ist in dieser Anlage frei und wird für die Wärmepumpe verwendet. Die Bridge leitet jede Adresse aus `Basisadresse + IDM-Objektnummer` ab; bei Basis `11/0/0` liegt Objekt 1 auf `11/0/1` und Objekt 222 auf `11/0/222`.

Die Vorgabe der Integration ist `8/0/0`. Diese Hauptgruppe ist hier bereits mit `Allgemein` belegt, deshalb weicht die Anlage bewusst auf `11/0/0` ab. Der Wert wird in Home Assistant unter **Einstellungen → Geräte & Dienste → IDM Heatpump → Konfigurieren → KNX-Bridge** als Basis-Gruppenadresse eingetragen.

## Aktueller ETS-Stand

Im ersten ETS-Screenshot vom 29.08.2026 war Hauptgruppe `11` noch nicht vorhanden. Nach dem anschließenden Import ist `11 Wärmepumpe` mit den Mittelgruppen `11/0 Objekte 1–230`, `11/1 Objekte 292–499` und `11/3 PV und Batterie` sichtbar. Damit ist die Gruppenadressstruktur importiert. Der Screenshot zeigt jedoch nicht die 43 Einzeladressen, ihre DPTs oder Verknüpfungen; diese Punkte benötigen einen neuen ETS-Export beziehungsweise eine Detailprüfung. Aus dem Screenshot lässt sich außerdem nicht ableiten, ob die KNX-Bridge in Home Assistant bereits aktiviert oder konfiguriert wurde.

## Gruppenadressen

Importdatei: [gruppenadressen-waermepumpe.xml](../ets-import/gruppenadressen-waermepumpe.xml), technische Referenz: [gruppenadressen-waermepumpe.csv](../ets-import/gruppenadressen-waermepumpe.csv).

Die Auswahl umfasst 43 Adressen: was ein Taster oder eine Visualisierung sinnvoll anzeigt, dazu die Werte, die KNX in die Wärmepumpe zurückschreiben kann. Der vollständige Katalog hat 654 Objekte und lässt sich bei Bedarf mit dem Generator im Integrations-Repository erzeugen.

### System

| Objekt | Name | Gruppenadresse | DPT | Richtung |
|---:|---|---:|---:|---|
| 1 | Außentemperatur | `11/0/1` | 9.001 | lesen |
| 2 | Gemittelte Außentemperatur | `11/0/2` | 9.001 | lesen |
| 3 | Interne Meldung | `11/0/3` | 7.001 | lesen |
| 4 | Systembetriebsart | `11/0/4` | 5.010 | lesen/schreiben |
| 6 | Wärmespeichertemperatur | `11/0/6` | 9.001 | lesen |
| 499 | Fehlerquittierung | `11/1/243` | 7.001 | lesen/schreiben |

### Warmwasser

| Objekt | Name | Gruppenadresse | DPT | Richtung |
|---:|---|---:|---:|---|
| 8 | Trinkwassererwärmer unten | `11/0/8` | 9.001 | lesen |
| 9 | Trinkwassererwärmer oben | `11/0/9` | 9.001 | lesen |
| 20 | Warmwasser Zapftemperatur | `11/0/20` | 9.001 | lesen |
| 21 | Warmwasser Sollwert | `11/0/21` | 9.001 | lesen/schreiben |

### Wärmepumpe

| Objekt | Name | Gruppenadresse | DPT | Richtung |
|---:|---|---:|---:|---|
| 30 | Wärmepumpen Vorlauftemperatur | `11/0/30` | 9.001 | lesen |
| 31 | Wärmepumpen Rücklauftemperatur | `11/0/31` | 9.001 | lesen |
| 33 | Wärmequelleneintritt | `11/0/33` | 9.001 | lesen |
| 34 | Wärmequellenaustritt | `11/0/34` | 9.001 | lesen |
| 50 | Wärmepumpen Betriebsart | `11/0/50` | 7.001 | lesen |
| 51 | Heizanforderung | `11/0/51` | 7.001 | lesen |
| 52 | Kühlanforderung | `11/0/52` | 7.001 | lesen |
| 53 | Warmwasseranforderung | `11/0/53` | 7.001 | lesen |
| 60 | Verdichter 1 | `11/0/60` | 7.001 | lesen |

### Heizkreise

| Objekt | Name | Gruppenadresse | DPT | Richtung |
|---:|---|---:|---:|---|
| 200 | Vorlauftemperatur HK A | `11/0/200` | 9.001 | lesen |
| 201 | Vorlauftemperatur HK B | `11/0/201` | 9.001 | lesen |
| 207 | Raumtemperatur HK A | `11/0/207` | 9.001 | lesen |
| 208 | Raumtemperatur HK B | `11/0/208` | 9.001 | lesen |
| 214 | Sollvorlauftemperatur HK A | `11/0/214` | 9.001 | lesen |
| 215 | Sollvorlauftemperatur HK B | `11/0/215` | 9.001 | lesen |
| 222 | Betriebsart HK A | `11/0/222` | 7.001 | lesen/schreiben |
| 223 | Betriebsart HK B | `11/0/223` | 7.001 | lesen/schreiben |
| 229 | Raumsoll Heizen Normal HK A | `11/0/229` | 9.001 | lesen/schreiben |
| 230 | Raumsoll Heizen Normal HK B | `11/0/230` | 9.001 | lesen/schreiben |
| 292 | Aktive Betriebsart HK A | `11/1/36` | 7.001 | lesen |
| 293 | Aktive Betriebsart HK B | `11/1/37` | 7.001 | lesen |
| 350 | Externe Raumtemperatur HK A | `11/1/94` | 9.001 | lesen/schreiben |
| 351 | Externe Raumtemperatur HK B | `11/1/95` | 9.001 | lesen/schreiben |

### Gebäudeleittechnik

| Objekt | Name | Gruppenadresse | DPT | Richtung |
|---:|---|---:|---:|---|
| 370 | Externe Außentemperatur (GLT) | `11/1/114` | 9.001 | lesen/schreiben |
| 371 | Externe Feuchte (GLT) | `11/1/115` | 9.007 | lesen/schreiben |
| 380 | Externe Heizanforderung | `11/1/124` | 1.001 | lesen/schreiben |
| 381 | Externe Kühlanforderung | `11/1/125` | 1.001 | lesen/schreiben |
| 382 | Externe WW-Ladeanforderung | `11/1/126` | 1.001 | lesen/schreiben |

### Wärmemengen

| Objekt | Name | Gruppenadresse | DPT | Richtung |
|---:|---|---:|---:|---|
| 400 | Wärmemenge Heizen | `11/1/144` | 14.031 | lesen |
| 401 | Wärmemenge Kühlen | `11/1/145` | 14.031 | lesen |
| 402 | Wärmemenge Warmwasser | `11/1/146` | 14.031 | lesen |
| 420 | Thermische Momentanleistung | `11/1/164` | 9.024 | lesen |

### PV und Batterie

| Objekt | Name | Gruppenadresse | DPT | Richtung |
|---:|---|---:|---:|---|
| 997 | Elektrische Leistungsaufnahme Wärmepumpe | `11/3/229` | 9.024 | lesen |

## Richtung

`lesen` bedeutet: Home Assistant sendet, KNX empfängt. Diese Adressen dürfen von keinem KNX-Gerät beschrieben werden.

`lesen/schreiben` bedeutet zusätzlich: ein KNX-Gerät darf auf diese Adresse schreiben, und die Bridge schreibt den Wert in das zugehörige Modbus-Register. Der Schreibweg läuft durch dieselbe Schreibsicherung wie jede andere Änderung in Home Assistant, inklusive Wertebereichsprüfung und EEPROM-Schutz.

Besonders nützlich sind dabei:

| Adresse | Objekt | Wirkung |
|---:|---:|---|
| `11/1/94` | 350 | externe Raumtemperatur Heizkreis A — ein KNX-Raumthermostat kann damit die Regelung der Wärmepumpe stützen |
| `11/1/95` | 351 | externe Raumtemperatur Heizkreis B |
| `11/1/114` | 370 | externe Außentemperatur, zum Beispiel von der Gira Wetterstation statt vom WP-Fühler |
| `11/1/115` | 371 | externe Luftfeuchte |
| `11/1/124` | 380 | Anforderung Heizen als 1-Bit-Telegramm |
| `11/1/125` | 381 | Anforderung Kühlen |
| `11/1/126` | 382 | Anforderung Warmwasserladung |
| `11/0/4` | 4 | Systembetriebsart, zum Beispiel Umschaltung auf Urlaub über eine Zentralfunktion |
| `11/0/21` | 21 | Warmwasser-Sollwert |
| `11/1/243` | 499 | Fehlerquittierung |

## ETS-Verknüpfung

1. ETS-Projekt sichern.
2. In der Ansicht **Gruppenadressen** den obersten Eintrag rechtsklicken und **Gruppenadressen importieren** wählen.
3. [gruppenadressen-waermepumpe.xml](../ets-import/gruppenadressen-waermepumpe.xml) importieren und den Importbericht prüfen.
4. Bei den anzeigenden Geräten — Glastaster, Display, Visualisierung — die passenden Anzeigeobjekte mit den Adressen aus der Tabelle verbinden. Ein Temperaturwert braucht dort ein Objekt mit DPT 9.001.
5. Bei schreibenden Geräten nur Objekte auf `lesen/schreiben`-Adressen legen.
6. Geräte programmieren.
7. In Home Assistant die KNX-Bridge aktivieren und als Basisadresse `11/0/0` eintragen.
8. Telegramme im ETS-Gruppenmonitor prüfen.

## Leseanfragen

Ein Taster oder eine Visualisierung, die nach einem Neustart den aktuellen Wert aktiv abfragt, sendet ein `GroupValueRead`. Die Bridge beantwortet das mit dem Wert, den die Wärmepumpe gerade liest — als `GroupValueResponse`, genau wie es das BAOS-Modul tut.

Die Option **Auf Leseanfragen antworten** steht in den Bridge-Einstellungen und ist standardmäßig aktiv. Ohne sie bliebe ein solches Gerät leer, bis Home Assistant das nächste Mal von sich aus sendet.

Nicht beantwortet werden Objekte ohne Wert: `Fehlerquittierung` ist ein reines Schreibobjekt, und Werte, die der Regler als unbenutzt meldet, werden übersprungen.

Zusätzlich lässt sich in den Bridge-Einstellungen ein **Intervall für vollständiges Neusenden** setzen. Das ist für Geräte gedacht, die gar nicht erst fragen, sondern nur auf gesendete Telegramme reagieren.

## Home Assistant

Die KNX-Bridge ersetzt die KNX-Integration nicht, sie benutzt sie. Voraussetzung ist also eine funktionierende KNX-Integration mit Verbindung zum IP-Interface, wie in [09 – Home Assistant](09_home_assistant.md) beschrieben.

Die Wärmepumpen-Entitäten selbst kommen weiterhin aus der IDM-Integration über Modbus und sind unabhängig von KNX verfügbar.
