# 21 – Ganglicht und Bewegungsmelder

Stand: 04.08.2026

## Ziel

Im Gang sind zwei getrennte Lichtkreise vorhanden. Beide bleiben einzeln bedienbar und erhalten zusätzlich einen gemeinsamen Schaltbefehl. Der Präsenz-/Bewegungsmelder `1.1.30 Gang Bewegung` schaltet über diesen gemeinsamen Befehl beide Lichtkreise.

## Beteiligte Geräte

| Gerät | Funktion |
|---|---|
| MDT Schaltaktor `1.1.3` | schaltet die beiden Gang-Lichtkreise auf Kanal E und F |
| Präsenz-/Bewegungsmelder `1.1.30` | Automatik für beide Ganglichter |
| MDT Glastaster im Gang | manuelle Einzel- oder Gruppenbedienung |

Die genaue Bestellnummer des Präsenzmelders wird noch anhand des eingebauten Geräts bestätigt. In ETS sind vier aktive Sensorbereiche und bis zu vier Lichtkanäle sichtbar.

## Gruppenadressen im Gang

| Gruppenadresse | Name | DPT | Verwendung |
|---:|---|---|---|
| `1/4/0` | Gang Licht Schalten | 1.001 | einzelner Lichtkreis auf Aktorkanal E |
| `1/4/1` | Gang Licht Status | 1.001 | Rückmeldung von Aktorkanal E |
| `1/4/2` | Licht Gang Neubau Schalten | 1.001 | einzelner Lichtkreis auf Aktorkanal F |
| `1/4/3` | Licht Gang Neubau Status | 1.001 | Rückmeldung von Aktorkanal F |
| `1/4/4` | Gang beide Lichter schalten | 1.001 | gemeinsamer Schaltbefehl für E und F |
| `1/4/5` | Gang beide Lichter Status | 1.001 | geplanter, per Logik gebildeter Sammelstatus |

Die Adressen `1/4/4` und `1/4/5` liegen innerhalb der bereits vorhandenen Mittelgruppe `1/4 Gang`. Eine zusätzliche Mittelgruppe ist nicht erforderlich und wegen des Limits von acht Mittelgruppen unter der Hauptgruppe `1 Licht` auch nicht möglich.

## Schaltaktor `1.1.3`

### Kanal E – Licht Gang

```text
Objekt 49 Schalten EIN/AUS
    -> 1/4/0 Gang Licht Schalten
    -> 1/4/4 Gang beide Lichter schalten

Objekt 56 Status
    -> 1/4/1 Gang Licht Status
```

### Kanal F – Licht Neubau / Gang Neubau

```text
Objekt 61 Schalten EIN/AUS
    -> 1/4/2 Licht Gang Neubau Schalten
    -> 1/4/4 Gang beide Lichter schalten

Objekt 68 Status
    -> 1/4/3 Licht Gang Neubau Status
```

Ein Schaltobjekt darf mehrere Gruppenadressen besitzen. Dadurch können beide Lichtkreise weiterhin einzeln und zusätzlich gemeinsam geschaltet werden.

## Gemeinsamer Status

Die beiden Statusobjekte `1/4/1` und `1/4/3` werden **nicht direkt gemeinsam** auf dieselbe Statusadresse gelegt. Zwei Aktorkanäle würden sonst unabhängig auf dieselbe Gruppenadresse schreiben und der angezeigte Zustand wäre nicht eindeutig.

Der Sammelstatus `1/4/5` wird durch genau eine Logik erzeugt. Empfohlen ist die Bedeutung:

```text
1/4/1 ODER 1/4/3
    -> 1/4/5 Gang beide Lichter Status
```

Damit bedeutet `1` auf `1/4/5`: Mindestens eines der beiden Ganglichter ist eingeschaltet. Alternativ kann eine UND-Logik verwendet werden, wenn `1` ausschließlich „beide Lichter sind eingeschaltet“ bedeuten soll. Die gewählte Bedeutung muss im Logiknamen eindeutig beschrieben werden.

Der gemeinsame Status kann anschließend mit dem Statusobjekt eines Glastasters und bei Bedarf mit dem Status-Eingang des Präsenzmelders verbunden werden.

## Präsenz-/Bewegungsmelder `1.1.30`

### Kommunikationsobjekte

| Objekt | Funktion | Verbindung / Stand |
|---:|---|---|
| 0 | Lichtkanal 1 – Ausgang 1, Schalten | `1/4/4 Gang beide Lichter schalten` |
| 3 | Externer Taster kurz | derzeit frei |
| 4 | Externer Taster lang | derzeit frei |
| 5 | Externe Bewegung / Slave | derzeit frei |
| 6 | Status Aktorkanal | frei lassen, bis `1/4/5` per Logik erzeugt wird |
| 7 | Bewegungserkennung sperren | derzeit frei |
| 8 | Zwangsführung | derzeit frei |
| 11 | Dunkel schalten | derzeit frei |
| 13 | Nachlaufzeit über Objekt | derzeit frei |
| 90 | Tag/Nacht | derzeit noch frei |
| 92 | LED Rot blinken | derzeit frei; deaktivieren, wenn ungenutzt |
| 97 | Helligkeit Messwert | derzeit frei |
| 98 | Einschaltschwelle einstellen | derzeit frei |
| 99 | Teach-In starten | derzeit frei |

### Allgemeine Einstellungen – aktueller ETS-Stand

```text
„In Betrieb“ zyklisch senden: nicht aktiv
Tag/Nacht-Objekt: abfragen nach Reset
Wert für Tag/Nacht: Tag = 1 / Nacht = 0
Umschaltung Tag/Nacht: bei nächster Präsenz

Auslöseempfindlichkeit Tag: 6
Auslöseempfindlichkeit Nacht: 3 (niedrig)
Präsenzempfindlichkeit: 8 (hoch)
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
Zyklisches EIN: nicht aktiv
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

Das vorhandene Hausobjekt `0/0/2 Nachtmodus` ist als `1 = Nacht` vorgesehen. Der Präsenzmelder steht aktuell jedoch auf `Tag = 1 / Nacht = 0`. Diese Kombination darf nicht direkt verbunden werden.

Vor der Verbindung mit `0/0/2` wird im Präsenzmelder die Polarität auf folgende Einstellung geändert:

```text
Tag = 0 / Nacht = 1
```

Danach kann verbunden werden:

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

Die Statusanzeige wird erst verbunden, wenn `1/4/5 Gang beide Lichter Status` durch eine Logik eindeutig erzeugt wird:

```text
1/4/5 Gang beide Lichter Status
    -> Status für Anzeige am Glastaster
```

## Programmierung

Nach Abschluss der Verknüpfungen vollständig programmieren:

1. Schaltaktor `1.1.3`
2. Präsenz-/Bewegungsmelder `1.1.30`
3. betroffene Glastaster
4. Logikgerät beziehungsweise Glastaster mit der Sammelstatuslogik

Bei blockiertem ETS-Zugriff wird am MDT SCN-SAFE.01 vorübergehend die zeitlich begrenzte Programmierfreigabe aktiviert. Passwörter, Schlüssel und private ETS-Projektdateien gehören nicht in dieses Repository.

## Funktionstest

1. Über `1/4/0` nur Kanal E schalten.
2. Über `1/4/2` nur Kanal F schalten.
3. Über `1/4/4` beide Kanäle gleichzeitig ein- und ausschalten.
4. Im Gruppenmonitor prüfen, dass der Bewegungsmelder bei erkannter Bewegung `1` auf `1/4/4` sendet.
5. Ohne weitere Bewegung muss nach 3 Minuten am Tag beziehungsweise 1 Minute in der Nacht `0` gesendet werden.
6. Helligkeitsabhängigkeit zunächst bei ausreichend dunkler Umgebung prüfen; für einen reinen Funktionstest vorübergehend helligkeitsunabhängig parametrieren.
7. Manuelle Bedienung und Rückfall aus dem Handbetrieb testen.
8. Nach Einrichtung der Logik prüfen, dass `1/4/5` der festgelegten ODER- oder UND-Bedeutung entspricht.
9. Nach Busspannungswiederkehr Tag/Nacht, Status und Automatik erneut prüfen.

## Offene Punkte

- genaue Bestellnummer des Präsenzmelders bestätigen
- `1/4/5` als ODER- oder UND-Sammelstatus festlegen und Logik programmieren
- Tag/Nacht-Polarität ändern und Objekt 90 mit `0/0/2` verbinden
- rote Blink-LED deaktivieren, sofern nicht benötigt
- Luxschwelle im realen Betrieb optimieren
- Bezeichnung `Licht Neubau` beziehungsweise `Licht Gang Neubau` vereinheitlichen
