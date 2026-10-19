# 36 – Home Assistant: Bad ergänzt und Vollständigkeit geprüft

Stand: 18.10.2026. Live-Abgleich der KNX-Entitätenverwaltung und des EG-Dashboards mit den dokumentierten ETS-Kanälen. Keine Schalt-, Fahr- oder Heiztests ausgeführt, keine ETS-Änderungen.

## Live ergänzt

Das große Bad fehlte sowohl als Licht- als auch als Rollladenentität. Der vorhandene Bereich **Bad** wurde für beide Entitäten verwendet; **Bad vorne** bleibt ein eigener Bereich.

| Entität | Befehl | Rückmeldung | Einstellungen |
|---|---|---|---|
| `light.eg_bad_licht` | `1/6/0` | `1/6/1` | reine Schaltleuchte, AKS Kanal G |
| `cover.eg_bad_rollladen` | Auf/Ab `2/3/0`, Stopp `2/3/1` | Position `2/3/3` | JAL Kanal E, Öffnen 23 s, Schließen 26 s |

Die Fahrzeiten stammen aus der [bereits durchgeführten Messung](34_abstellkammer_zentral_bad_2026-10-18.md), nicht aus einer neuen Messfahrt. Die absolute KNX-Positions-Sendeadresse bleibt leer, weil das entsprechende Aktorobjekt nicht verbunden ist. Öffnen/Schließen und Positionsverarbeitung sind nicht invertiert; KNX 100 % geschlossen entspricht HA 0 % offen.

Die beiden Karten **Bad** wurden im vorhandenen Raster unter **EG → Licht** beziehungsweise **EG → Rollläden** gespeichert. Nach dem Speichern zeigt das Licht **Aus**, der Rollladen **Geschlossen** und in der Detailansicht **Position 0 %**. Das bestätigt die HA-Zustandsanzeige, keine physische Sichtprüfung oder neue Befehlsprüfung. Die lokale [Dashboardvorlage](../home-assistant/lovelace_knx_eg.yaml) enthält ebenfalls beide Karten. Die Entitäten sind in der KNX-Oberfläche gespeichert; keine zusätzlichen YAML-Entitäten importieren.

## Abgleich Licht, Rollläden und Heizung

| Funktion | Ergebnis |
|---|---|
| Licht Wohnzimmer, Arbeitszimmer, Küche, Schlafzimmer | Entitäten und Dashboardkarten vorhanden |
| Licht Gang Altbau, Gang Neubau und Gang gemeinsam | Entitäten und Dashboardkarten vorhanden |
| Licht Bad, Bad vorne und Abstellkammer | nach Ergänzung vollständig für die neun dokumentierten Einzellichtkreise; Gang gemeinsam ist eine zusätzliche Sammelfunktion |
| Rollläden Wohnzimmer Fenster/Tür, Arbeitszimmer, Schlafzimmer Fenster/Tür, Bad | nach Ergänzung sechs einzeln adressierte Rollläden mit Entitäten und Dashboardkarten |
| Markise | separat vorhanden; keine Änderung ihrer Befehle, Freigaben oder Schutzverknüpfungen |
| FBH Wohnzimmer, Küche, Arbeitszimmer, Gang, Schlafzimmer, Bad | alle sechs `climate.eg_<raum>_mdt_komforttemperatur` und sechs AKH-Sollwertsensoren vorhanden; Thermostatkarten zeigen gültige Temperaturen, alle sechs AKH-Sollwerte 21 °C |
| Bestehende weitere Heizungen | Dashboardkarten Abstellraum, Treppenhaus und WC vorhanden; keine neue KNX-Zone daraus abgeleitet |

Die lokale Dashboardvorlage enthielt außerdem die sechs bereits live vorhandenen MDT-Thermostate und AKH-Sollwertsensoren noch nicht. Diese Karten werden in der Vorlage nachgeführt; live werden keine doppelten Karten erzeugt.

## Verbleibende Lücken

- **Küchenrollladen:** JAL Kanal F ist benannt, aber ohne bestätigte Einzelgruppenadressen; reale Motorzuordnung offen. Deshalb keine erfundene HA-Entität. Siehe [Kanalbelegung](05_kanalbelegung.md) und [aktuellen Zentralstand](34_abstellkammer_zentral_bad_2026-10-18.md).
- **Terrassenlicht:** Aktorkanal und Schalt-/Statusadresse noch nicht bestätigt. Zuerst die reale Zuordnung ermitteln.
- **Heizung Bad vorne und Esszimmer:** keine bestätigten eigenen AKH-Ausgänge im dokumentierten Kanalstand. Die sechs tatsächlich bestätigten Regelzonen sind vollständig in HA vorhanden. Keine zusätzlichen Regler aus den alten Planadressen ableiten.
- **Etagen-Sammelsteuerung:** In der lokalen Datei `google_etagensteuerung.yaml` fehlen Badlicht, Abstellkammerlicht und Badrollladen. Diese Auslassung betrifft sowohl Status-/Verfügbarkeitstemplates als auch Befehlsziele. Die Datei wird lokal korrigiert. Die entsprechende Live-Datei konnte bei dieser Prüfung nicht gelesen werden: Der HA-Dateieditor blieb beim Laden. Live-Mitgliedschaften und Aktivierung der korrigierten Vorlage bleiben daher offen. Keine Etagenbefehle oder Sprachtests ausgeführt.
- **Undokumentierte Reservekanäle:** keine Verbraucher aus unbestätigten Kanalnamen oder Reserven ergänzt. Der Abgleich deckt die dokumentierten KNX-EG-Funktionen ab, keine vollständige neue Verdrahtungsaufnahme des Hauses.

Bereits bestehende Grenzen zur Inbetriebnahme von Fenstergriffen, zur realen Heizkreiszuordnung und zu physischer Funktionsprüfung gelten weiter. Private Sicherungen und Screenshots werden nicht ins Repository aufgenommen.
