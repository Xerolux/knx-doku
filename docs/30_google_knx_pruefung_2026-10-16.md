# Google-/KNX-Prüfung vom 16.10.2026

## Anlass

Der Nutzer meldet, alle KNX-Applikationen geladen zu haben. Zugleich hört Google Home bei „OK Google“ zu, beendet die Anzeige aber ohne Antwort oder Geräteaktion. Der Nutzer bestätigte anschließend: Die Uhrzeit wird normal beantwortet. Damit ist die allgemeine Sprachverarbeitung funktionsfähig; der Fehler ist gezielt bei der Haussteuerung weiter einzugrenzen.

## Aktuell geprüft

- Home Assistant ist erreichbar.
- Google Assistant in HA: eingeschaltet. Automatische Freigabe neuer unterstützter Entitäten und Zustandsmeldungen: eingeschaltet.
- HA-Cloud-Fernzugriff: `binary_sensor.remote_ui = on`. Dies allein bestätigt keine erfolgreiche Google-Home-Kontoverknüpfung oder Sprachverarbeitung.
- Die HA-Cloud-Kontoseite zeigt „Alexa und Google verknüpft“ sowie ein aktives Abonnement. Dies bestätigt die HA-seitige Anzeige, keinen erfolgreichen Google-Gerätebefehl.
- Alle sechs am 14.10.2026 eingerichteten Etagenziele sind vorhanden und verfügbar: EG/OG/DG-Lichter jeweils `off`, EG/OG/DG-Rollläden jeweils `open`. Dies sind Momentaufnahmen, keine in dieser Prüfung ausgeführten Licht-/Fahrbefehle.
- Die zwölf Sondergeräte-Einzelskripte haben weiterhin keinen `last_triggered`-Zeitpunkt. Sie wurden auch für diese Diagnose nicht ausgeführt.
- Das HA-KNX-Panel zeigt `Verbunden`, Adresse `1.1.255`.
- Der Google-Home-/Cast-Mediaplayer `media_player.googlehome2680` (Name „Bad“) steht auf `unavailable`; Lautstärke und Stummschaltung sind nicht auslesbar. Dies beweist weder einen neuen Ausfall noch die Ursache des Sprachproblems. Im HA-Protokollfilter `cast` wurden keine Einträge gefunden.
- ETS-Downloadnachweise stehen im [Programmierstand](22_programmierstand_ets.md#nachtrag-vom-16102026-applikationen-geladen).

## Google-Cloud-Warnung

In HA ist `Error reporting state - 14: Stream refused by server` protokolliert. Logger: `homeassistant.components.cloud.google_config`, Quelle: `components/cloud/google_config.py:378`; erstes Auftreten 08:22:11, letztes Auftreten 09:45:09, drei Vorkommnisse.

Die Warnung betrifft die Zustandsübermittlung. Sie ist ein konkreter Fehlerhinweis, aber kein Beweis, dass sie auch das stumme Ende der Google-Sprachverarbeitung verursacht. Der offizielle Nabu-Casa-Status meldete bei der Abfrage keine allgemeine Störung. Der Fehlertext ist auch aus einem älteren [HA-Core-Issue](https://github.com/home-assistant/core/issues/131453) bekannt; daraus wird keine Diagnose für diese Installation abgeleitet.

## Vorgenommene Maßnahme

Die Google-Anbindung wurde gezielt über `switch.cloud_google` einmal aus- und wieder eingeschaltet. Vorher war der Schalter EIN; AUS wurde beobachtet, anschließend wieder EIN. Keine Kontoabmeldung, keine neue Kontoverknüpfung, keine Änderung von PIN-/Sicherheitseinstellungen, keine Änderung der festen Etagenmitgliedschaften und keine ETS-Parameteränderung.

Die Neuanbindung ist eine begrenzte Wiederanlaufmaßnahme. Sie bestätigt nicht, dass die vom Nutzer gemeldete Sprachstörung behoben ist. Ein Synchronisationsdienst für Google war im aktuellen HA-Aktionskatalog nicht vorhanden; ein solcher Dienst wurde nicht erfunden oder aufgerufen.

Nach dem Wiedereinschalten wurden die Google-Freigaben aller sechs Etagenziele erneut in der HA-Oberfläche geprüft: weiterhin freigegeben.

## Vom Nutzer bestätigte Sprachtests

- „Hey Google, wie spät ist es?“: normale Antwort.
- Nach dem Wiederanlauf: „Hey Google, schalte Bad vorne Licht ein“: Nutzer bestätigt „Licht schaltet“. Damit ist dieser einzelne Google-/HA-/Lichtpfad erfolgreich getestet. Ob der Wiederanlauf die Ursache behoben hat, ist daraus allein nicht ableitbar.

Der zuvor gemeldete Ausfall lässt sich beim getesteten Einzellicht nicht mehr reproduzieren. Eine erfolgreiche Etagen- oder Haus-Sammelsteuerung wird daraus nicht abgeleitet.

## Noch offen

- Echte Google-Sprachtests für die Etagenbefehle und allgemeine Hausbefehle.
- Google-Home-App, Kontoverknüpfung, dortige Räume/Routinen und Lautsprecher-Netzwerk wurden nicht über die App geprüft.

Die sechs festen Etagenziele und ihre Ausschlüsse sind weiter dokumentiert in [Google Assistant: Etagensteuerung](29_google_assistant_etagensteuerung.md). Sie ersetzen keine Prüfung aller anderen globalen Google-Sammelpfade. Insbesondere ist das Vorhandensein einer HA-Freigabe kein erfolgreicher Sprachtest.
