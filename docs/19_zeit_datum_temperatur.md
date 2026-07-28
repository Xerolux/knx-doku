# 19 – Zeit, Datum, Temperatur und Display

## Aktueller Stand

Für die KNX-Zeitversorgung wird die zusätzliche E-Mail- und Zeitserver-Applikation eines vorhandenen MDT SCN-IP100.03 verwendet.

| Physikalische Adresse | Applikation | Aufgabe |
|---:|---|---|
| 1.1.0 | IP-Router-Applikation | KNX/IP-Routing und ETS-Zugang |
| 1.1.31 | E-Mail- und Zeitserver-Applikation | NTP-Zeit empfangen und auf KNX senden |

`1.1.0` und `1.1.31` können zum selben realen SCN-IP100.03 gehören. Es handelt sich um zwei getrennte ETS-Applikationen mit zwei physikalischen Adressen, nicht um zwei zusätzliche Hardwaregeräte.

## Festgelegte Gruppenadressen

| Gruppenadresse | Name | DPT | Verwendung |
|---:|---|---|---|
| 0/5/0 | Uhrzeit | 10.001 | reine Tageszeit, 3 Byte |
| 0/5/1 | Datum | 11.001 | reines Datum, 3 Byte |
| 0/5/2 | Datum/Uhrzeit | 19.001 | kombinierter Wert, 8 Byte |

Für den MDT Glastaster II Smart wird bevorzugt `0/5/2` verwendet, weil Datum und Uhrzeit gemeinsam übertragen werden können. Die getrennten Adressen `0/5/0` und `0/5/1` bleiben für Geräte bestehen, die nur den jeweiligen Einzelwert unterstützen.

Die in ETS sichtbare Gruppenadresse `0/5/3 Aktuelle Werte empfangen` hat derzeit keine sauber definierte eigene Funktion. Ein Kommunikationsobjektname ist keine Gruppenadressfunktion. Vor der endgültigen Abnahme prüfen, ob sie verknüpft ist; andernfalls löschen.

## SCN-IP100.03 – Kommunikationsobjekte

Bei der E-Mail- und Zeitserver-Applikation `1.1.31` sind folgende Objekte relevant:

| Objekt | Funktion | Gruppenadresse |
|---:|---|---:|
| 2 | Uhrzeit – aktuelle Zeit senden | 0/5/0 |
| 3 | Datum – aktuelles Datum senden | 0/5/1 |
| 4 | Datum/Uhrzeit – aktuelles Datum und Zeit senden | 0/5/2 |
| 53 | NTP-Zeitserver – Fehler | optional eigene Diagnoseadresse |

Der Zeitserver wird auf die lokale Zeitzone Deutschland mit automatischer Sommer-/Winterzeitumschaltung eingestellt. Datum und Uhrzeit sollen zyklisch gesendet werden, beispielsweise alle 10 bis 60 Minuten sowie nach erfolgreicher NTP-Synchronisierung.

Es darf nur **einen aktiven Zeitmaster** geben. Die zweite IP-Schnittstelle, Home Assistant und die MDT SCN-RTC20.01 dürfen nicht parallel abweichende Zeitwerte senden. Die Schaltuhr kann Datum und Uhrzeit als Slave vom Bus übernehmen.

## Glastaster 1.1.20

Der Taster `1.1.20 Eingang` ist ein MDT Glastaster II Smart mit Temperatursensor.

Für die kombinierte Zeitversorgung:

```text
1.1.31 Objekt 4 Datum/Uhrzeit senden
    -> 0/5/2 Datum/Uhrzeit
    -> 1.1.20 Objekt 114 Uhrzeit/Datum – aktuelle Werte empfangen
```

Alternativ kann ausschließlich die Uhrzeit über `0/5/0` mit Objekt 112 des Tasters empfangen werden. Beide Wege gleichzeitig sind für die reine Anzeige nicht notwendig.

## Temperaturanzeige

Der interne Temperatursensor muss unter **Temperaturmessung / Grundeinstellung** aktiviert sein. Für die Anzeige wird in der Info- oder Standbyanzeige die interne Raumtemperatur ausgewählt.

Soll der Messwert zusätzlich auf dem KNX-Bus verfügbar sein, wird das Sendeobjekt der gemessenen Temperatur mit der Isttemperatur-Gruppenadresse des Raumes verbunden. Wenn `1.1.20` dem Eingang beziehungsweise Gang zugeordnet bleibt, ist dafür `3/4/1 Gang Isttemperatur` vorgesehen.

## Display ausschalten und aufwecken

Empfohlene Parametrierung:

- Standby nach einer einstellbaren Zeit aktivieren, beispielsweise nach 20 Sekunden.
- Standbyanzeige auf dunkel beziehungsweise Display aus stellen.
- Ersten Tastendruck wahlweise nur zum Aufwecken verwenden.
- Alternativ kann der erste Tastendruck das Display aufwecken und gleichzeitig die Tastenfunktion ausführen.

Für eine eindeutige Bedienung wird empfohlen, dass der erste Tastendruck bei ausgeschaltetem Display nur aufweckt und erst der zweite Tastendruck schaltet.

## Prüfung

1. Gruppenmonitor öffnen und Telegramme auf `0/5/2` beobachten.
2. Nach Programmierung von `1.1.31` muss zyklisch ein DPT-19.001-Telegramm erscheinen.
3. Bei fehlender Zeit Objekt 53 beziehungsweise die NTP-Einstellungen, Netzwerkzugang, DNS und Gateway prüfen.
4. Taster `1.1.20` anschließend vollständig programmieren.
5. Anzeige von Uhrzeit, Datum und interner Temperatur prüfen.
