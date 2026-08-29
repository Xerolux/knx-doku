# 13 – MDT Logikmodul

## Ziel

Das Logikmodul übernimmt Schutz- und Grundlogiken direkt auf KNX. Home Assistant kann Zustände anzeigen oder ergänzen, ist aber keine Voraussetzung für deren Ausführung.

## Logikliste

| ID | Auslöser | Aktion | Ergebnis |
|---|---|---|---|
| LOG001 | Windalarm | `Markise Einfahren Schutz` senden | Markise fährt ein |
| LOG002 | Regenalarm | `Markise Einfahren Schutz` senden | Markise fährt ein |
| LOG003 | Frostalarm | Markise sperren, `Wetterschutz Aktiv Status` setzen | Schutz vor Betrieb bei Frost |
| LOG004 | Fensterstatus Raum offen/gekippt | Betriebsart des Raums absenken | keine unnötige Heizenergie |
| LOG005 | Haus verlassen | `Zentral Aus` senden | normale Lichtkreise aus |
| LOG006 | Haus verlassen oder Urlaub | `Heizung Zentral Betriebsart Soll` auf Eco setzen | Heizung abgesenkt |
| LOG007 | Nachtmodus | `Heizung Zentral Betriebsart Soll` auf Nacht setzen | Nachtbetrieb |
| LOG008 | Panik | definierte Lichtgruppen einschalten | Not- und Abschreckfunktion |
| LOG009 | `1/4/1` oder `1/4/3` ist 1 | `1/4/5 Gang beide Lichter Status` senden | gemeinsamer Ganglichtstatus |

## LOG009 – gemeinsamer Ganglichtstatus

Die Logik ist im MDT `SCN-LOG1.02` mit physikalischer Adresse `1.1.8` als Funktion **F1 Gang beide Lichter Status** angelegt.

### Parameter F1

| Parameter | Einstellung |
|---|---|
| Hauptfunktion | Logikgatter / Inverter |
| Unterfunktion | Logikgatter, 8 Eingänge mit Sperre |
| Logikfunktion | ODER |
| Eingang 1 | aktiv, Polarität normal, externes Objekt |
| Eingang 2 | aktiv, Polarität normal, externes Objekt |
| Eingang 3–8 | nicht aktiv |
| Ausgang | normal |
| Objekttyp Ausgang | Ein/Aus, DPT 1.001 Schalten |
| Sperre/Freigabe | nicht aktiv |
| Sendebedingung | bei Änderung Ausgang |
| Ausgang filtern | nicht aktiv |
| Sendeverzögerung / zyklisches Senden | nicht aktiv |
| Eingänge nach Reset abfragen | aktiv |
| Ausgang erst senden, wenn alle Eingänge gültig sind | aktiv |

### Kommunikationsobjekte F1

| Objektnummer | Objektfunktion | Gruppenadresse |
|---:|---|---:|
| 0 | Logik Eingang 1 | `1/4/1 Gang Licht Status` |
| 1 | Logik Eingang 2 | `1/4/3 Licht Gang Neubau Status` |
| 9 | Logik Ausgang | `1/4/5 Gang beide Lichter Status` |

Das Ausgangsobjekt 9 verwendet Priorität **Niedrig**, DPT **1.001 Schalten** und die Flags **Kommunikation, Lesen und Übertragen**. Schreiben und Aktualisieren sind deaktiviert. Dadurch ist das Logikmodul der einzige Sender für `1/4/5` und kann eine `GroupValueRead`-Anfrage von Home Assistant beantworten.

Die Parametrierung und Verknüpfungen sind im ETS-Projekt bestätigt. Als nächster Schritt wird `1.1.8` vollständig programmiert und anschließend im Gruppenmonitor geprüft. Vor diesem Download kann Home Assistant weiterhin einen Timeout beim Lesen von `1/4/5` melden.

## Regeln für die Umsetzung

- Nur die Logik bzw. das zuständige Gerät schreibt Statusgruppenadressen.
- Schutzbefehle haben Vorrang vor Komfort- und Tasterbefehlen.
- Ein Schutzende gibt die Markise nicht automatisch wieder frei; die Freigabe folgt der sicheren Parametrierung des Jalousieaktors.
- Die konkreten Objektbezeichnungen und Werte der MDT- und Gira-Produktdatenbanken werden beim Verknüpfen in ETS geprüft.

Jede Logik erhält in ETS einen klaren Namen mit ID, damit Auslöser und Wirkung nachvollziehbar bleiben.
