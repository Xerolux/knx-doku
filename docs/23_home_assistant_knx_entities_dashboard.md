# 23 – Home Assistant: KNX-Entitäten und Lovelace-Dashboard

Stand: 05.08.2026

## Ziel

Home Assistant visualisiert und bedient die bereits in ETS angelegten KNX-Funktionen. Die KNX-Grundfunktionen bleiben unabhängig von Home Assistant funktionsfähig.

Die KNX-Projektdatei kann in Home Assistant importiert werden. Wird dabei ein Passwort abgefragt, ist das in ETS gesetzte **Projektpasswort** gemeint. Es ist nicht der KNX-IP-Secure-Gerätecode, kein Web-PIN und kein Passwort des Sicherheitsmoduls.

Passwörter, PINs, Schlüsselbunddateien und private ETS-Projektdateien gehören nicht in dieses öffentliche Repository.

## Angelegte Rollladen- und Markisenentitäten

Entitätstyp in Home Assistant: **Abdeckung**.

| Home-Assistant-Entität | Funktion | Auf/Ab | Stopp | Position Soll | Position Status |
|---|---|---:|---:|---:|---:|
| `cover.eg_wohnzimmer_rollladen_fenster` | Wohnzimmer Rollladen Fenster | `2/0/0` | `2/0/1` | `2/0/2` | `2/0/3` |
| `cover.eg_wohnzimmer_rollladen_tur` | Wohnzimmer Rollladen Türe | `2/0/10` | `2/0/11` | `2/0/12` | `2/0/13` |
| `cover.eg_arbeitszimmer_rollladen` | Arbeitszimmer Rollladen | `2/1/0` | `2/1/1` | `2/1/2` | `2/1/3` |
| `cover.eg_schlafzimmer_rollladen_fenster` | Schlafzimmer Rollladen Fenster | `2/2/10` | `2/2/11` | `2/2/12` | `2/2/13` |
| `cover.eg_schlafzimmer_rollladen_tur` | Schlafzimmer Rollladen Türe | `2/2/0` | `2/2/1` | `2/2/2` | `2/2/3` |
| `cover.eg_markise` | Markise | `2/4/0` | `2/4/1` | `2/4/2` | `2/4/3` |

### Einstellungen je Abdeckung

- Öffnen/Schließen umkehren: nicht aktiv
- Schrittweise Bewegung: nicht verwendet
- Kippen/Lamellen: nicht verwendet
- Positions-Sendeadresse und Positions-Statusadresse eintragen
- Geräteklasse: Rollladen; bei der Markise Markise
- Fahrzeit in Home Assistant nur als Hilfswert verwenden; maßgeblich bleibt die Fahrzeitmessung des JAL

KNX verwendet bei der Position `0 % = oben/eingefahren` und `100 % = unten/ausgefahren`. Home Assistant stellt Rollläden als Öffnungsgrad dar und wandelt den Wert entsprechend für `current_position` um. Deshalb zeigt die Lovelace-Karte bei einem vollständig geöffneten Rollladen `100 % offen`.

Die Prozentanzeige ist erst zuverlässig, wenn folgende Punkte erfüllt sind:

1. `Status aktuelle Position` am JAL ist aktiviert.
2. Das Statusobjekt des JAL ist mit der richtigen Statusgruppenadresse verbunden.
3. Die gleiche Statusgruppenadresse ist in Home Assistant als Zustandsadresse eingetragen.
4. JAL und Glastaster wurden vollständig programmiert.
5. Die Fahrzeitmessung wurde ausgeführt.

## Angelegte Lichtentitäten

Entitätstyp in Home Assistant: **Leuchte**. Helligkeit, Farbtemperatur und Farbe bleiben leer, weil es sich um reine Schaltkanäle handelt.

| Home-Assistant-Entität | Funktion | Schalten | Status |
|---|---|---:|---:|
| `light.eg_wohnzimmer_licht` | Wohnzimmer Licht | `1/0/0` | `1/0/1` |
| `light.eg_arbeitszimmer_licht` | Arbeitszimmer Licht | `1/3/0` | `1/3/1` |
| `light.eg_kuche_licht` | Küche Licht | `1/2/0` | `1/2/1` |
| `light.eg_schlafzimmer_licht` | Schlafzimmer Licht | `1/5/0` | `1/5/1` |
| `light.eg_gang_licht` | Gang Altbau | `1/4/0` | `1/4/1` |
| `light.eg_gang_neubau_licht` | Gang Neubau | `1/4/2` | `1/4/3` |
| `light.eg_gang_licht_alle` | beide Ganglichter | `1/4/4` | `1/4/5` |

### Beide Ganglichter

Die Gruppenadresse `1/4/4 Gang beide Lichter schalten` liegt zusätzlich auf den Schaltobjekten der Aktorkanäle E und F. Dadurch können beide Kanäle gemeinsam und trotzdem weiterhin einzeln geschaltet werden.

Die Statusadresse `1/4/5 Gang beide Lichter Status` darf nicht direkt von beiden Aktorkanälen beschrieben werden. Sie wird durch genau eine Logik erzeugt:

```text
1/4/1 ODER 1/4/3
    -> 1/4/5 Gang beide Lichter Status
```

Damit bedeutet `1`: Mindestens eines der beiden Ganglichter ist eingeschaltet.

Solange die Logik nicht eingerichtet und programmiert ist, kann die gemeinsame Lichtentität zwar schalten, ihr Status ist jedoch nicht zuverlässig.

## Heizung im Dashboard

Im Dashboard werden derzeit vorhandene Klimaentitäten aus dem Altbestand angezeigt:

```text
climate.heizkorper_omaopa_dusche_1
climate.heizung_heizung_treppenhaus
climate.heizkorper_omaopa_bad
```

Diese drei Entitäten sind nicht Teil der heute neu angelegten KNX-Licht- und Rollladenentitäten. Ihre Namen und Zuordnung werden später bei Bedarf vereinheitlicht.

## Lovelace-Dashboard

Die aktuelle Dashboard-Datei liegt unter:

```text
home-assistant/lovelace_knx_eg.yaml
```

Voraussetzung ist die über HACS installierte Custom Card:

```text
custom:button-card
```

Das Dashboard enthält genau drei Reiter:

1. Licht
2. Rollläden
3. Heizung

### Gestaltung

- Kartenhöhe: `140 px`
- Symbolgröße: maximal `60 px`
- drei Karten pro Zeile
- Lichtkarten werden bei eingeschaltetem Licht gelb dargestellt
- Rollladenkarten zeigen Position, Fahrzustand und ein passendes Symbol
- Markise zeigt:
  - bis `5 %`: `Eingefahren`
  - ab `95 %`: `Ausgefahren`
  - dazwischen: Prozentwert `ausgefahren`
- Rollladenkarten dienen in der Übersicht nur als Anzeige
- Tippen öffnet den Home-Assistant-Dialog **Mehr Informationen**; dort erfolgt die Bedienung
- direkte Auf/Stopp/Ab-Schaltflächen wurden bewusst aus der Karte entfernt

### Dashboard-Entitäten

Licht:

```text
light.eg_wohnzimmer_licht
light.eg_arbeitszimmer_licht
light.eg_kuche_licht
light.eg_schlafzimmer_licht
light.eg_gang_licht
light.eg_gang_neubau_licht
light.eg_gang_licht_alle
```

Rollläden und Markise:

```text
cover.eg_wohnzimmer_rollladen_fenster
cover.eg_wohnzimmer_rollladen_tur
cover.eg_arbeitszimmer_rollladen
cover.eg_schlafzimmer_rollladen_fenster
cover.eg_schlafzimmer_rollladen_tur
cover.eg_markise
```

## Prüfung

### Rollläden

1. Öffnen, Schließen und Stopp im Mehr-Informationen-Dialog testen.
2. Eine Zwischenposition anfahren.
3. Prüfen, ob `current_position` aktualisiert wird.
4. Obere Endlage muss in Home Assistant `100 % offen` ergeben.
5. Untere Endlage muss `0 % offen` ergeben.
6. Bei der Markise muss die eingefahrene Endlage `Eingefahren` anzeigen.

### Licht

1. Jedes Licht einzeln schalten.
2. Rückmeldung nach Bedienung am KNX-Taster prüfen.
3. Beide Ganglichter über `light.eg_gang_licht_alle` schalten.
4. Gemeinsamen Status erst nach Programmierung der ODER-Logik bewerten.

## Offene Punkte

- Sammelstatus `1/4/5` per ODER-Logik erzeugen und programmieren
- weitere Lichtkanäle und Räume in Home Assistant ergänzen, sobald sie in ETS bestätigt sind
- Heizungskreise des aktuellen KNX-Projekts als Klimaentitäten anlegen
- Bereiche und Gerätenamen in Home Assistant endgültig vereinheitlichen
- Dashboard nach Erweiterungen aktualisieren
