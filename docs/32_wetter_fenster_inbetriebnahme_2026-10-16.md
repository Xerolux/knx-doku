# 32 – Wetterstation und Fenstergriffe: Inbetriebnahme am 16.10.2026

> Späterer Folgeauftrag vom 16.10.: Der Nutzer hat anschließend den direkten KNX-Wetterschutz ausschließlich für die EG-Markise freigegeben. Umsetzung und tatsächlicher Download-/Prüfstand stehen in [Dokument 33](33_markise_eg_wetterschutz.md). Die unten beschriebene reine Anzeige war der davor abgeschlossene Arbeitsstand; OG bleibt unverändert.


## Auftrag und Ergebnis

Die bereits betriebene Gira-Wetterstation wurde für Messwerte und Diagnose eingerichtet und vollständig in einem eigenen Home-Assistant-Dashboard dargestellt. Auf ausdrücklichen Nutzerwunsch wurden **keine Verbindungen zu Rollläden, Markisen oder vergleichbaren Aktoren** hergestellt. Zusätzlich wurden die unbekannten EG-Fensterstellungen untersucht und zwei Konfigurationsprobleme korrigiert. Eine funktionierende Fensterüberwachung ist weiterhin nicht nachgewiesen.

| Bereich | Ergebnis | Nachweisgrenze |
|---|---|---|
| Wetterstation 1.1.40 | B00D29 parametriert, Applikationsdownload abgeschlossen, 33 Ausgänge verbunden | keine physische Kalibrierung oder Regenprüfung |
| Wetter in HA | 31 native KNX-Entitäten, zwei GPS-Templates und zwei abgeleitete Anzeigen | Windorientierungstext noch leer; Statistikreparatur Feuchte offen |
| Lovelace Wetter | drei Ansichten gespeichert und visuell geprüft | keine Aktorbedienung enthalten |
| Fenster-Templates | elf zuvor fehlende Empfangssensoren geladen | noch keine bestätigten Griffzustände |
| HA-Tunnel 1.1.255 | genau 22 Status-/Kippadressen zugeordnet | alleinige Fehlerursache dadurch nicht bewiesen |
| Schlüsselbund | erneuter Export und HA-Import vom Nutzer bestätigt | Entschlüsselung echter Grifftelegramme noch ungeprüft |
| Griffparameter | zyklisches Senden und Empfangszeiten besprochen | in dieser Sitzung keine neuen Griffparameter durch uns geladen |
| Physischer Fenstertest | vom Nutzer auf später verschoben | alle elf Stellungsanzeigen weiterhin Unbekannt |

## Wetterstation: ausgeführte Änderungen

Die tatsächlich verwendete Applikation ist **B00D29**, nicht die ältere Projektangabe B00D21. Die interne Beschattungssteuerung wurde deaktiviert; dabei entfallen die acht zugehörigen Fassadenausgänge. Übrig bleiben 33 Mess-/Diagnoseausgänge und das unverbundene GPS-Anforderungsobjekt 23. Alarmadressen 4/2 und Freigaben 4/3 wurden nicht angebunden.

Wind wird bei drei Prozent Änderung und zyklisch alle 60 Sekunden gesendet. Regen wurde über Grenzwertobjekt 38 angebunden: bei Regen EIN, keine Einschaltverzögerung, bestehende Ausschaltverzögerung zehn Minuten, Versand bei Änderung und alle 60 Sekunden. GPS-Zeit verwendet UTC+1 mit europäischer Sommerzeit und sendet jede Minute; die bestehende KNX-Masterzeit wurde nicht umgestellt.

Für die absolute Luftfeuchte wurde nach ausdrücklicher Freigabe die neu angelegte Zuordnung **4/0/6** gelöst, Objekt 26 und Gruppenadresse auf **DPT 9.029, g/m³** umgestellt und dieselbe Adresse wieder verbunden. ETS bestätigte den anschließenden Applikationsdownload als abgeschlossen. Es wurde keine neue physikalische Adresse programmiert.

Die vollständige Zuordnung aller 33 Ausgänge steht in [Dokument 11](11_wetterstation_gira.md). Die vier Helligkeitssensoren heißen neutral Sensor 1–4, weil ihre reale Himmelsrichtung noch nicht bestätigt ist. Die alten Planungsadressen für Ost/Süd/West und binäre Dämmerung wurden nicht übernommen.

## Home Assistant und Dashboard

Das [Wetterpaket](../home-assistant/knx_wetterstation_gira.yaml) wurde live gespeichert. Es umfasst 23 native numerische/Textsensoren, acht native Binärsensoren, zwei empfangende GPS-Datums-/Zeitsensoren und zwei abgeleitete Anzeigen. Die KNX-Messwerte verwenden `sync_state: "expire 5"`; eine reine Leseautomation fragt GPS-Zeit/-Datum beim Start und alle fünf Minuten ab. GPS-Empfang wird auf Quelle 1.1.40 begrenzt. KNX, Templates und Automationen wurden ohne HA-Core-Neustart neu geladen; die Konfigurationsprüfung war erfolgreich.

Das neue Dashboard **Wetter** unter `/dashboard-wetter/wetter` enthält:

- **Wetter:** Temperatur, gefühlte Temperatur, Feuchte, Luftdruck, gültigen Wind, Windrichtung, Strahlung, Helligkeit, Regen und Versorgungs-/Gesundheitsanzeige.
- **Sonne & Helligkeit:** vier Helligkeitssensoren, Maximal-/Dämmerungswerte, Sonnenwinkel und Verläufe.
- **Diagnose & GPS:** sämtliche Statusbits, Rohwerte, Komfortmeldungen, absolute Feuchte, Windorientierung, GPS-Daten und Statuscode.

Alle 33 Stationsausgänge und beide abgeleiteten Anzeigen sind abgedeckt. Native Karten öffnen bei Antippen die Detailansicht. Die [Lovelace-Datei](../home-assistant/lovelace_wetter_gira.yaml) bildet den gespeicherten Stand ab.

### Behandlung ungültiger Startwerte

Nach dem Download wurden zunächst Initialwerte und der Wind-Ersatzwert 50 m/s beziehungsweise 180 km/h beobachtet. Die gültige Windanzeige prüft Versorgung, Windfehlerbit 12 und internes Fehlerbit 15. Zusätzlich verwirft sie den Ersatzwert unabhängig vom Statuswort: Er kann vor dem zugehörigen Fehlerstatus eintreffen. Die Tests decken diese Reihenfolge ab.

Der Windverlauf wurde aus dem Dashboard entfernt, da der frühere Startwert bereits in der Historie lag. Es wurden keine historischen Daten gelöscht. Temperatur- und Helligkeitsverläufe bleiben enthalten. Betauungsschutz (Bit 0) und Trocknung (Bit 1) sind separat erklärt; GPS-Code 252 zeigt keine gesetzten Fehlerbits 0/1.

Nach der Anlaufphase wurden unter anderem etwa 13 °C, 88 % relative Feuchte, 9 g/m³ absolute Feuchte, 954,4 hPa und 1,4 km/h beobachtet. Das sind Momentwerte, keine Referenzmessungen. Gezielte Leseanfragen aktualisierten anfängliche GPS-/Sonnenwinkel-Nullwerte. Genaue Koordinaten bleiben privat.

Die bisherige Entity-ID `sensor.gira_wetter_absolute_feuchte_rohwert` bleibt bestehen, liefert jetzt aber g/m³. HA meldet dazu eine Änderung der Statistik-Einheit von zuvor ohne Einheit auf g/m³. Diese **Statistikreparatur ist noch offen**; die Meldung wurde nicht als erledigt ausgegeben.

## Fenstergriffe: Diagnose und Korrekturen

Die elf Stellungsanzeigen referenzierten fehlende Telegramm-Empfangssensoren. Ursache war `entity_category: diagnostic`, das im verwendeten Template-Sensorschema unzulässig ist. Die elf Einträge wurden aus Live-Paket und [Repository-Kopie](../home-assistant/knx_fenstergriffe_eg.yaml) entfernt. Nach Template-Neuladen existieren alle elf Empfangssensoren; die HA-Konfigurationsprüfung war erfolgreich. Der Validator verhindert die erneute Einführung des ungültigen Schlüssels.

Die Anzeigen verwenden weiterhin nur tatsächlich eingehende Zustandsbits vom zugeordneten Griff. Ausgehende Telegramme, Leseanfragen und fremde Absender zählen nicht. Die 22 nativen Rohsensoren können initial `off` zeigen; daraus wird kein „Geschlossen“ abgeleitet. `sync_state: false` bleibt für die schlafenden Batteriegeräte erhalten. Es wurden keine Telegramme simuliert und keine Zustände künstlich gesetzt.

Auch nach Korrektur und Schlüsselimport hatten alle elf Empfangssensoren noch keine bestätigten Zustandsbits. Das betrifft ausdrücklich `sensor.eg_fenster_schlafzimmer_rechts_gross_stellung` und die übrigen Stellungsanzeigen. Die weiterhin unbekannten Attribute wurden zusätzlich von Spook beanstandet; dies ist vom behobenen Template-Schemafehler zu unterscheiden.

Am Beispiel **1.1.17** wurden Objekt 2 → 5/4/0 und Objekt 3 → 5/4/20, Polarität jeweils 1, K/Ü ohne L-Flag und deaktiviertes zyklisches Senden beider Zustände geprüft. Das wurde nicht als Einzelprüfung aller elf Geräte ausgegeben. Das sichtbare HA-Protokoll zeigte keinen neuen Entschlüsselungsfehler; ohne echte Grifftelegramme beweist dies keine funktionierende Secure-Kommunikation.

### Tunnelzuordnung und Schlüsselbund

HA verwendet den Tunnel **1.1.255**, ETS den Tunnel **1.1.254**. Der HA-Endpunkt hatte zunächst null Assoziationen. Nach ausdrücklicher Freigabe wurden genau die 22 Status-/Kippadressen aus [Dokument 08](08_rf_fenstergriffe.md) zugeordnet; ETS zeigte anschließend 22 Assoziationen. Sammeladressen und der ungenutzte Bereich 5/2 blieben außen vor.

Die Zuordnung dient der Bereitstellung der benötigten gesicherten Gruppeninformationen und Schlüssel für diesen Endpunkt. Sie erzeugt keine Fensterzustände und steuert keine Aktoren. Dass sie allein „Unbekannt“ verursacht hatte, wurde nicht bewiesen.

Der Nutzer exportierte den neuen passwortgeschützten Schlüsselbund und bestätigte danach den Import direkt in HA. Anschließend zeigte HA wieder Verbunden unter 1.1.255. Passwort und Schlüsseldatei wurden nicht ins Repository übernommen. Ein neuer Download von Router-/Kopplertabellen wurde in dieser Diagnose nicht nachgewiesen. Die bereits erfolgten Griffdownloads sind gesondert in [Dokument 22](22_programmierstand_ets.md) dokumentiert.

### Besprochene Parameter

Für Fensterstellung **und** Fensterkippstellung wurde jeweils ein zyklischer Versand alle **eine Stunde** empfohlen; kürzere Intervalle erhöhen den Batteriebedarf. MDT nennt fünf Stunden als Voreinstellung. Die Stunde ist die besprochene Empfehlung, kein bestätigter Downloadstand.

Das Nutzerbild zeigte „In Betrieb“ nicht aktiv, Empfang nach Griffbewegung aktiv für **drei Sekunden** (`00:03` mm:ss) und nach Neustart aktiv für **fünf Minuten** (`05:00`). Diese Empfangszeiten können beibehalten werden. Empfangsbereitschaft ist kein zyklischer Zustandsversand; „In Betrieb“ ist nur ein optionales Lebenszeichen. Das Bild belegt weder eine Einstellung aller elf Griffe noch eine Geräteprogrammierung. Durch uns wurden in dieser Sitzung keine neuen Griffparameter geladen.

## Prüfungen und offene Abnahme

Die lokalen Validatoren [Fenstergriffe](../scripts/validate-fenstergriffe.py) und [Wetterstation](../scripts/validate-wetterstation.py) prüfen unter anderem Zuordnungen, Quellenfilter, Anzeigeabdeckung, DPT 9.029, Windfehlerfälle und ausschließlich lesende Wetterautomationen. HA-Konfigurationsprüfung und visuelle Dashboardprüfung waren erfolgreich. Diese Prüfungen ersetzen keine Bus-/Funk-Abnahme.

Noch offen:

1. Je Griff einen echten Wechsel geschlossen → offen → gekippt → geschlossen mit ETS-/HA-Monitor verfolgen: Quelle, Ziel, Nutzdaten, Empfangsattribute und Stellungsanzeige. Der Nutzer kann die Griffe erst später bewegen.
2. Bei ausbleibendem Empfang die konkrete RF-/Secure-Strecke anhand dieser Telegramme weiter untersuchen. Nicht pauschal geschlossene Zustände setzen.
3. Eine gegebenenfalls gewünschte zyklische Griffparametrierung pro Gerät laden und anschließend prüfen.
4. Statistik-Einheitenkonflikt der absoluten Luftfeuchte in HA bereinigen; bisher nicht durchgeführt.
5. Regenfunktion, Helligkeitsausrichtung und noch leeren Windorientierungstext prüfen.
6. Eine spätere Beschattungs-/Wetterschutzanbindung separat planen und beauftragen.

Die Dokumentation und YAML-Kopien enthalten keine Secure-Schlüssel, Passwörter oder exakten GPS-Koordinaten. Git-Veröffentlichung ist kein Bestandteil dieses Dokumentationsauftrags.
