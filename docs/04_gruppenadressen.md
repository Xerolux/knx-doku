# 04 – Gruppenadressen

## Gruppenadressstil

Das Projekt verwendet den ETS-Stil **3 Ebenen**:

`Hauptgruppe / Mittelgruppe / Untergruppe`

Die Datei [../ets-import/gruppenadressen.xml](../ets-import/gruppenadressen.xml) verwendet das native ETS-/KNX-XML-Format `GroupAddress-Export` und kann direkt in ETS 6 importiert werden. Die DPT-Referenz steht getrennt in [../ets-import/gruppenadressen-planung.csv](../ets-import/gruppenadressen-planung.csv).

Gruppenadressen sind unabhängig von der physikalischen Linie. Geräte auf KNX TP 1.1, KNX RF 1.2 und der optionalen Außenlinie 1.3 können dieselben Gruppenadressen verwenden, sofern ihre Kommunikationsobjekte passend verknüpft sind.

## Hauptgruppen

| Nr. | Bereich | Inhalt |
|---:|---|---|
| 0 | Zentral | Hauszustände, zentrale Beschattung und Heizung |
| 1 | Licht | Schalten und Status je Raum |
| 2 | Beschattung | Rollläden und Markise |
| 3 | Heizung | Raumregelung und Fensterstatus |
| 4 | Wetter | Messwerte, Alarme und Automatikfreigaben |
| 5 | Fenster | einzelne RF-Fenstergriffe und Raumstatus |
| 6 | Präsenz | Präsenz, Bewegung und Helligkeit |
| 7 | Szenen | Szenenaufrufe |
| 8 | Status | hausweite Sammelmeldungen |
| 9 | Home Assistant | optionale Diagnose- und Anzeigeobjekte |

Die Hauptgruppen 10 bis 15 bleiben als Reserve für Energie, Störungen, Lüftung/Kühlung, Außenanlagen und spätere Erweiterungen frei.

## Konventionen

| Art | Benennung | Beispiel |
|---|---|---|
| Befehl | `… Schalten`, `… Soll`, `… Freigabe` | `Wohnzimmer Licht Schalten` |
| Rückmeldung | `… Status`, `… Ist` | `Wohnzimmer Licht Status` |
| Position | `… Position Soll` / `… Position Status` | `Markise Position Status` |
| Schutz | eindeutiger Auslöser und Status | `Markise Einfahren Schutz` / `Wetterschutz Aktiv Status` |

- Eine Gruppenadresse hat genau eine Bedeutung und wird nicht erneut vergeben.
- Taster, Aktor und Visualisierung verwenden für dieselbe Funktion dieselbe Befehlsadresse.
- Rückmeldungen werden nur vom zuständigen Gerät beziehungsweise der zuständigen Logik geschrieben.
- Der DPT muss zum Kommunikationsobjekt der importierten Produktdatenbank passen.
- Die XML importiert die Gruppenadressstruktur, aber keine Geräte, physikalischen Adressen, DPT-Zuordnungen oder Objektverknüpfungen.

## Zentralfunktionen

Zentrale Befehle sind konfliktfrei angelegt:

- Beschattungsautomatik: eine **Freigabe** und eine **Status**-Rückmeldung, keine getrennten Ein-/Aus-Befehle.
- Heizung: eine zentrale **Betriebsart Soll** und eine **Betriebsart Status** mit DPT 20.102.
- Rollläden: ein zentraler Auf-/Ab-Befehl sowie ein separater Stop-/Schritt-Befehl.

Die vollständige Liste steht in der XML-Importdatei und in [12 – Zentralfunktionen](12_zentralfunktionen.md).
