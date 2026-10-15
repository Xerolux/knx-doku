# ETS-Protokoll vom 14.10.2026: Bad vorne und HF-Präsenzmelder

## Auftrag und Ausgangszustand

Auf Nutzerwunsch wurden der Lichttaster und der Schaltaktor für Bad vorne verknüpft sowie die HF-Reichweiten der neuen Melder in Küche und Bad reduziert. Die früheren ETS-Namen „Bad alt“ und „Licht Bad alt“ wurden auf ausdrücklichen Wunsch in „Bad vorne“ und „Licht Bad vorne“ geändert.

Direkt im geöffneten ETS6-Projekt geprüft:

- `1.1.36 Bad vorne`: Schaltaktor mit KO 0 Kanal A Schalten und KO 7 Kanal A Status, ursprünglich ohne Gruppenadressen.
- `1.1.38 Licht Bad vorne`: Tasterobjekte KO 0 (Ausgang A1 schalten, Wippe A+B) und KO 16 (Ausgang C1 schalten, Wippe C+D), ursprünglich ohne Gruppenadressen.
- `1.1.37 AKK-01UP.03 Schaltaktor 1fach, UP, 16A`: KO 0 Kanal A Schalten und KO 7 Kanal A Status, bisher ohne Gruppenadressen.
- Die vorhandenen Lichtadressen sind `1/6/0–1 Badezimmer` und `1/7/0–1 Bad vorne`.

Die erste Einordnung von `1.1.36` als Taster war falsch: Nach Auswahl eines Geräts zeigte ETS kurz noch die vorherige Objektliste. Nach vollständigem Laden wurde `1.1.36` eindeutig als Schaltaktor bestätigt. Der Nutzer bestätigte die gewünschte Richtung `1.1.38 → 1.1.36`; `1.1.37` gehört nicht zu dieser Schaltverknüpfung.

## Lichtverknüpfung und Benennung

| Gerät | Objekt | Gruppenadresse |
|---|---|---|
| `1.1.38 Licht Bad vorne` | KO 0 Ausgang A1 schalten, Wippe A+B | `1/7/0 Bad vorne Licht Schalten` |
| `1.1.36 Bad vorne` | KO 0 Kanal A Schalten | `1/7/0 Bad vorne Licht Schalten` |
| `1.1.36 Bad vorne` | KO 7 Kanal A Status | `1/7/1 Bad vorne Licht Status` |

Die Wippe A+B ist freigegeben und auf Schalten eingestellt. Aktion A/B: EIN/AUS; Sperrfunktion: NEIN. Taste A sendet EIN, Taste B AUS. Wippe C+D und die Sensorobjekte wurden nicht zusätzlich verknüpft. Die oben genannten Verbindungen wurden in den ETS-Objektlisten geprüft. Geräteadressen und bestehende Gruppenadressnamen bleiben erhalten; beide neuen Gerätenamen wurden in ETS gespeichert.

Die Applikationsdownloads für `1.1.38 Licht Bad vorne` und `1.1.36 Bad vorne` wurden nach der Verknüpfung erfolgreich abgeschlossen. Die ETS-Historie zeigt für beide Geräte einen grünen Downloadpfeil und `Programmieren(Appl.): Abgeschlossen`. Der Nutzer bestätigte anschließend am 14.10.2026 mit „funktioniert“ die erfolgreiche Lichtschaltung vor Ort. Dies ist eine Nutzerbestätigung des Funktionstests; eine eigene Beobachtung oder Gruppenmonitoraufzeichnung liegt nicht vor.

## Home Assistant: Licht Bad vorne

Am 14.10.2026 auf ausdrücklichen Nutzerwunsch live über das KNX-Panel eingerichtet:

- Entität `light.eg_bad_vorne_licht`, Anzeigename `EG Bad vorne Licht`.
- HA-Gerät `EG Bad vorne`, neuer Bereich `Bad vorne`.
- Schaltadresse `1/7/0`, Zustandsadresse `1/7/1`; reine Ein-/Aus-Leuchte, keine Dimmadresse.
- Vor der Anlage enthielt die KNX-Lichtliste keinen Eintrag für Bad vorne. Nach dem Speichern wurde genau ein neuer Eintrag mit den beiden Adressen und dem Bereich bestätigt.
- Die Detailansicht zeigt einen gültigen Zustand `Aus`; die Zustandsanzeige ist verfügbar. Ein eigener HA-Schalttest wurde nicht durchgeführt.
- Im EG-Dashboard, Ansicht Licht, wurde das vorhandene Raster um eine Karte `Bad vorne` mit dem bestehenden Template `card_light` ergänzt. Speichern wurde von HA bestätigt, die Karte anschließend in der normalen Ansicht sichtbar geprüft.
- Die Entität wurde über die HA-Oberfläche angelegt; nicht zusätzlich als YAML-KNX-Entität importieren.

## HF-Reichweitenwerte

| Gerät | Vorher | Neuer ETS-Wert |
|---|---|---|
| `1.1.34 Raumcontroller Küche` | 0,35 bis 5,95 m | 0,35 bis 3,15 m |
| `1.1.35 Raumcontroller Bad` | 0,35 bis 5,95 m | 0,35 bis 2,45 m |

Die Änderungen wurden jeweils auf der Seite Präsenzmelder → HF-Sensor vorgenommen und in der Anzeige geprüft. Weiter entfernte Entfernungsbereiche werden dadurch nicht mehr angezeigt. Trigger- und Halteschwellwerte, Haltedauer (30 Sekunden), Lichtverknüpfungen und Raumklimamesswerte wurden bei dieser Anpassung nicht verändert.

Die neuen Reichweiten sind Startwerte zur Eingrenzung der gemeldeten Außenraumerfassung. Raumabmessungen und eine Messung an der Grundstücksgrenze liegen nicht vor. Ein Innenraum-/Vorgartentest ist erforderlich; aus der ETS-Anzeige allein folgt keine bestätigte Unterdrückung von Außenbewegung.

## Übertragung und Prüfung

Die Applikationsdownloads für beide Geräte wurden erfolgreich abgeschlossen. Die ETS-Historie zeigt jeweils einen grünen Downloadpfeil und `Programmieren(Appl.): Abgeschlossen`. Für Bad wurde Start 17:33:34 und Ende 17:33:54 angezeigt. Damit sind die Änderungen nicht nur im Projekt vorhanden, sondern laut ETS auch auf die Geräte übertragen. Die HF-Seite weist ausdrücklich darauf hin, dass dauerhafte Speicherung im Sensor einen ETS-Gerätedownload erfordert.

Der Taster-/Lichttest ist durch die Nutzerbestätigung abgeschlossen. Offen bleibt der Innenraum-/Vorgartentest der Präsenzmelder. ETS-Exportdateien wurden noch nicht erneuert. Die Gruppenadressprüfung mit `scripts/validate-group-addresses.ps1` war erfolgreich; `git diff --check` meldete keine Inhaltsfehler.
