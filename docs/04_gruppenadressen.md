# 04 – Gruppenadressen

## Gruppenadressstil

Das Projekt verwendet den ETS-Stil **3 Ebenen**:

`Hauptgruppe / Mittelgruppe / Untergruppe`

Die Datei [../ets-import/gruppenadressen.csv](../ets-import/gruppenadressen.csv) bildet diese Struktur exakt ab und kann direkt in ETS importiert werden. Die DPT-Referenz steht getrennt in [../ets-import/gruppenadressen-planung.csv](../ets-import/gruppenadressen-planung.csv).

## Hauptgruppen

| Nr. | Bereich | Inhalt |
|---:|---|---|
| 0 | Zentral | Hauszustände, zentrale Beschattung und Heizung |
| 1 | Licht | Schalten und Status je Raum |
| 2 | Beschattung | Rollläden und Markise |
| 3 | Heizung | Raumregelung und Fensterstatus |
| 4 | Wetter | Messwerte, Alarme, Automatikfreigaben |
| 5 | Fenster | einzelne RF-Fenstergriffe und Raumstatus |
| 6 | Präsenz | Präsenz, Bewegung und Helligkeit |
| 7 | Szenen | Szenenaufrufe |
| 8 | Status | hausweite Sammelmeldungen |
| 9 | Home Assistant | optionale Diagnose- und Anzeigeobjekte |

## Konventionen

| Art | Benennung | Beispiel |
|---|---|---|
| Befehl | `… Schalten`, `… Soll`, `… Freigabe` | `Wohnzimmer Licht Schalten` |
| Rückmeldung | `… Status`, `… Ist` | `Wohnzimmer Licht Status` |
| Position | `… Position Soll` / `… Position Status` | `Markise Position Status` |
| Schutz | eindeutiger Auslöser und Status | `Markise Einfahren Schutz` / `Wetterschutz Aktiv Status` |

- Eine Gruppenadresse hat genau eine Bedeutung und wird nicht erneut vergeben.
- Taster, Aktor und Visualisierung verwenden für dieselbe Funktion dieselbe Befehlsadresse.
- Rückmeldungen werden nur vom zuständigen Gerät bzw. der Logik geschrieben.
- Der DPT muss zum Kommunikationsobjekt der importierten Produktdatenbank passen. Die Planungsdatei ist eine Sollvorgabe, keine Überschreibung des Geräteobjekts.

## Zentralfunktionen

Zentrale Befehle sind konfliktfrei angelegt:

- Beschattungsautomatik: eine **Freigabe** und eine **Status**-Rückmeldung, keine getrennten Ein-/Aus-Befehle.
- Heizung: eine zentrale **Betriebsart Soll** und eine **Betriebsart Status** mit DPT 20.102, keine parallelen Komfort-/Nacht-/Eco-/Frost-Bitbefehle.
- Rollläden: ein zentraler Auf-/Ab-Befehl sowie ein separater Stop-/Schritt-Befehl.

Die vollständige Liste steht in der Importdatei und in [12 – Zentralfunktionen](12_zentralfunktionen.md).
