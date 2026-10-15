# Google Assistant: Etagensteuerung vom 14.10.2026

## Auftrag und Umsetzung

Lichter und Rollläden sollen getrennt für Erdgeschoss, Obergeschoss und Dachgeschoss gemeinsam steuerbar sein. Markisen, Garage, Garagentor und Freisitz sollen ausschließlich einzeln angesprochen werden.

Das Paket [google_etagensteuerung.yaml](../home-assistant/google_etagensteuerung.yaml) wurde über den HA-Dateieditor als `packages/google_etagensteuerung.yaml` live gespeichert. Die bestehende Konfiguration lädt Pakete bereits über `homeassistant.packages`. HA bestätigte die Konfigurationsprüfung mit „Die Konfiguration verhindert nicht den Start von Home Assistant!“. Template-Entitäten und Skripte wurden ohne Neustart neu geladen.

## Feste Etagenziele

| Etage | Lichtziel | Lichtmitglieder | Rollladenziel | Rollladenmitglieder |
|---|---|---:|---|---:|
| Erdgeschoss | `light.erdgeschoss_lichter` | 7 | `cover.erdgeschoss_rollladen` | 5 |
| Obergeschoss | `light.obergeschoss_lichter` | 9 | `cover.obergeschoss_rollladen` | 6 |
| Dachgeschoss | `light.dachgeschoss_lichter` | 2 | `cover.dachgeschoss_rollladen` | 1 |

Die genauen Mitglieder stehen ausdrücklich im Paket. Kein Ziel verwendet `entity_id: all`, eine automatische Etagen-/Bereichsauswahl oder einen Namensfilter. Neue Geräte werden erst nach Prüfung aufgenommen.

EG-Licht: Wohnzimmer, Arbeitszimmer, Küche, Schlafzimmer, Gang Altbau, Gang Neubau und Bad vorne. Die gemeinsame Gangentität wird nicht zusätzlich aufgenommen, damit dieselben Ausgänge nicht doppelt angesprochen werden.

OG-Licht: Gang, Schlafzimmer, Dusche, Esszimmer, Küche, Melina, Wohnzimmer, Bad und Arbeitszimmer. Diese bestehenden Homematic-Lichter sind `switch`-Entitäten; die neue Lichtentität bündelt sie mit expliziten `homeassistant.turn_on`-/`turn_off`-Aktionen.

DG-Licht: Wendeltreppe und Tizian. Der vorhandene DG-Rollladen ist Wendeltreppe.

Nicht eindeutig zugeordnet: `light.h1` bis `light.h4` und die Treppenhaus-Lichtentitäten. Sie wurden nicht geraten oder einer Etage zugeschlagen. Das Hauptbad-Licht auf `1/6/0–1` ist in der geprüften aktiven KNX-Lichtliste nicht vorhanden; diese neue Gruppe enthält daher das bestätigte Bad-vorne-Licht, nicht einen erfundenen Hauptbad-Eintrag.

Die Lichtzustände melden EIN, sobald mindestens ein Mitglied EIN ist. Rollladenziele melden offen, sobald mindestens ein Mitglied offen oder in Bewegung ist; eine gemittelte Prozentposition wird nicht erfunden. Ein Ziel ist verfügbar, wenn mindestens ein Mitglied einen gültigen Zustand hat. Der Sammelzustand ist keine Aussage, dass alle Geräte denselben Zustand haben.

## Sondergeräte und Einzelbefehle

Die festen Sammellisten enthalten weder `cover.eg_markise`, `cover.markiese`, `cover.garagentor`, `cover.hmip_broll_2_0036a0c99cc6c4` noch Freisitz und dessen virtuelle Kanäle. Auch die Pool-Abdeckung gehört nicht zu den neuen Etagenzielen.

Die direkte Sprachfreigabe der Markisen, von Freisitz und Garage Mitte war bereits aus. Das wurde anhand der Verfügbarkeitslisten geprüft und beibehalten. `cover.markiese` ist trotz des Namens als `shutter` klassifiziert; auch Freisitz und Garage Mitte sind `shutter`. Eine direkte Freigabe dieser Geräte könnte sie erneut in allgemeine Rollladenbefehle aufnehmen.

Stattdessen wurden zwölf Skripte angelegt und für Google Assistant sowie Assist freigegeben: jeweils Öffnen, Schließen und Stoppen für Markise Erdgeschoss, Markise Obergeschoss, Freisitz und Garage Mitte. Jedes Skript hat genau ein festes Ziel. Markisen/Freisitz sind dem Bereich Garten zugeordnet, Garage Mitte dem Bereich Garage. Dadurch erhalten die Skripte auch die für gemeinsam genutzte Google-Haushalte relevante Bereichszuordnung.

Das bereits vorhandene `cover.garagentor` bleibt als Gerät der Klasse `garage` einzeln verfügbar. Bestehende Sicherheits-/PIN-Einstellungen wurden nicht verändert. Der rohe Impulsschalter `switch.garagentor_1` wurde nicht zusätzlich freigegeben. Die Funktionsfähigkeit der einzelnen physischen Aktoren wurde nicht durch Fahrbefehle getestet.

## Google-Freigabe und Sprachtest

Alle sechs Etagenziele zeigen in HA das Google-Assistant-Symbol. Die zwölf Skripte zeigen ebenfalls die Freigabe. Home Assistant Cloud ist mit Google verknüpft und synchronisiert geänderte Freigaben automatisch; ein erfolgreicher Sprachtest am Google-Gerät wurde nicht behauptet. [Offizielle Synchronisationsbeschreibung](https://www.home-assistant.io/actions/google_assistant.request_sync/).

Vorgesehene Befehle:

- „Hey Google, schalte Erdgeschoss Lichter an/aus.“
- „Hey Google, öffne/schließe Erdgeschoss Rollläden.“
- Entsprechend mit Obergeschoss oder Dachgeschoss.
- Einzelbefehle als Szenen/Skripte, beispielsweise „Hey Google, aktiviere Freisitz öffnen“ oder „aktiviere Markise Erdgeschoss schließen“.

Die gewünschten umgangssprachlichen Varianten mit „alle“ müssen am Google-Gerät getestet werden. Wenn Google sie als Raum- statt Gerätenamen auslegt, kann eine Google-Home-Routine die exakte Formulierung auf das neue Etagenziel abbilden. Google-Home-Routinen und dort manuell gepflegte Raumzuordnungen wurden in dieser Sitzung nicht bearbeitet oder geprüft.

## Nachweise und Grenzen

- Live-Zustände: EG-Lichter AUS, OG-Lichter EIN, DG-Lichter AUS; alle drei Rollladenziele geschlossen. Momentaufnahme, keine Schaltaktion.
- Zwölf Skripte vorhanden, `last_triggered` bei allen leer; keines wurde zur Prüfung ausgeführt.
- Lokale YAML-Prüfung bestätigt sechs Ziele, zwölf Skripte und keine Sondergeräte in den Sammelaktionslisten.
- Keine Licht- oder Fahrbefehle zur Funktionsprüfung gesendet. Der echte Sprach-/Fahrtest bleibt offen.
- Die Ausschlüsse gelten nachgewiesen für die neuen festen Etagenziele und die geprüfte HA-Sprachfreigabe. Bestehende Google-Home-Routinen, externe Integrationen und sonstige Sammelpfade sind nicht dadurch automatisch geprüft.

Zur Rücknahme die Google-Freigaben der neuen Ziele entfernen, das Paket entfernen und Template-Entitäten/Skripte neu laden. Vor einer Rücknahme prüfen, ob inzwischen Dashboards oder Automationen auf die neuen IDs verweisen.
