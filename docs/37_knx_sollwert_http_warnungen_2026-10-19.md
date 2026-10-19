# 37 – KNX-Sollwertabfrage und HTTP-Sicherheitswarnung

Stand: 19.10.2026, live geprüft mit Home Assistant Core 2026.10.2.

## KNX: fehlende Leseantworten behoben

Home Assistant meldete Zeitüberschreitungen beim Lesen der Basis-Komforttemperaturen, unter anderem für `3/3/0`, `3/4/0` und `3/5/0`. Die sechs Klimaentitäten lesen und schreiben bewusst den Basis-Komfortwert. Die getrennte aktuelle AKH-Solltemperatur auf `3/x/5` berücksichtigt dagegen die Betriebsart und darf diesen Basiswert nicht ersetzen.

In ETS war das Flag **Lesen** an den Komfort-Sollwertobjekten nicht gesetzt. Die übrigen Flags Kommunikation, Schreiben und Übertragen waren gesetzt; Aktualisieren war nicht gesetzt. Ein empfangener Schreibwert konnte damit vorhanden sein, ohne dass das Objekt eine GroupValueRead-Anfrage beantwortete.

Das Leseflag wurde je Raum an genau einem AKH-Kanal ergänzt:

| Raum | Basisadresse | Antwortgeber | Kommunikationsobjekt |
|---|---|---|---|
| Wohnzimmer | `3/0/0` | `1.1.5`, G | 127 – Sollwert Komfort |
| Küche | `3/2/0` | `1.1.6`, B | 27 – Sollwert Komfort |
| Arbeitszimmer | `3/3/0` | `1.1.5`, E | 87 – Sollwert Komfort |
| Gang | `3/4/0` | `1.1.5`, D | 67 – Sollwert Komfort |
| Schlafzimmer | `3/5/0` | `1.1.5`, B | 27 – Sollwert Komfort |
| Bad | `3/6/0` | `1.1.5`, A | 7 – Sollwert Komfort |

Die anderen Kanäle mit gemeinsamen Raumadressen wurden nicht als zusätzliche Antwortgeber eingerichtet. ETS bestätigte für `1.1.5` und `1.1.6` jeweils **Programmieren (Part.): Abgeschlossen**. Die HA-Entitätskonfiguration und die getrennten Statusadressen wurden nicht verändert; der Status-Updater bleibt aktiv.

### Nachweis am Bus

Über `knx.read` wurden ausschließlich Leseanfragen für die sechs Basisadressen ausgelöst. Der HA-Gruppenmonitor bestätigte folgende eingehende **GroupValueResponse**-Telegramme; Nutzdaten jeweils `0x0c1a`, dekodiert **21 °C**:

| Uhrzeit am 19.10.2026 | Zieladresse | Quelle |
|---|---|---|
| 17:52:05,588 | `3/0/0` | `1.1.5` |
| 17:52:06,594 | `3/2/0` | `1.1.6` |
| 17:52:07,600 | `3/3/0` | `1.1.5` |
| 17:52:08,605 | `3/4/0` | `1.1.5` |
| 17:52:09,611 | `3/5/0` | `1.1.5` |
| 17:52:10,615 | `3/6/0` | `1.1.5` |

Alle sechs HA-Klimaentitäten zeigten danach Basis-Solltemperatur 21 °C und aktuelle Raumtemperaturen. Die anschließende Prüfung der Core-Protokolle seit 17:45 Uhr enthielt keine neuen `xknx`-Meldungen. `ha core check` endete mit **Command completed successfully**. Es wurden keine Sollwert-Teständerungen und keine gezielten Ventil-, Licht- oder Fahrtests ausgelöst. Ein HA-Neustart oder Langzeittest wurde nicht durchgeführt.

## HTTP: Schutz wirksam, vorgeschaltete Sperre noch offen

Der zweite gemeldete Eintrag lautet:

```text
homeassistant.components.http.security_filter
Filtered a potential harmful request to: /img../.git/config
```

Vor dem eigenen Prüftest war genau ein Vorkommnis von 12:24:35 vorhanden. Der Pfad entspricht einem verdächtigen Versuch, Git-Konfigurationsdaten über einen ungewöhnlichen URL-Pfad zu erreichen. Der Eintrag belegt die Filterung, nicht einen erfolgreichen Zugriff. Absender und Herkunft des ursprünglichen Aufrufs sind aus diesem Eintrag nicht bestimmbar.

Der eigene Prüftest über den vorhandenen HTTPS-nginx-Zugriff bestätigte:

| Prüfung | HTTP-Ergebnis |
|---|---|
| Derselbe verdächtige Pfad, unverändert übertragen | **400 Bad Request** |
| HA-API ohne Authentifizierung über HTTPS-Proxy | **401 Unauthorized** |
| HA-API ohne Authentifizierung direkt im LAN | **401 Unauthorized** |

Der eigene Test erzeugte am 19.10.2026 um **17:53:34** einen zusätzlichen erwarteten `security_filter`-Eintrag. Dieser spätere Eintrag ist dem Prüftest zuzuordnen und kein Nachweis eines weiteren fremden Zugriffs. Unter `/config/www` wurde bei der anschließenden Verzeichnissuche kein `.git`-Verzeichnis gefunden; andere Speicherorte oder mögliche Symlinks wurden damit nicht vollständig geprüft.

Der nginx-Proxy läuft auf einem separaten System; in der geprüften HA-App-/Containerliste ist kein nginx-Proxy vorhanden. Für dieses vorgeschaltete System lag kein funktionierender Verwaltungszugang vor. Deshalb wurde dort keine zusätzliche Sperrregel eingerichtet. Auch Portfreigaben und die externe Erreichbarkeit des Proxyservers wurden nicht abschließend geprüft.

**Verbleibender Schritt:** Auf dem tatsächlich verwendeten nginx-Proxy eine gezielte Sperre für VCS-Metadaten wie `/.git/` einrichten, die Konfiguration mit `nginx -t` prüfen und nach dem Reload nachweisen, dass der verdächtige Pfad bereits am Proxy abgewiesen wird, ohne einen neuen HA-Filtereintrag zu erzeugen. Die konkrete Einbindung hängt von der Proxyverwaltung ab und ist noch nicht umgesetzt.

Der HA-Sicherheitsfilter und seine Warnprotokollierung bleiben aktiv. Historische Protokolle wurden nicht gelöscht. Private Screenshots, rohe Diagnosen und Zugangsdaten werden nicht in das Repository übernommen.

Quellen zur Funktionsweise: [Home Assistant KNX](https://www.home-assistant.io/integrations/knx/), [MDT AKH-0x00.02, Technisches Handbuch](https://www.mdt.de/download/MDT_THB_Heizungsaktor_02.pdf), [Home Assistant HTTP-Sicherheitsfilter, Quellcode](https://github.com/home-assistant/core/blob/2026.10.2/homeassistant/components/http/security_filter.py).
