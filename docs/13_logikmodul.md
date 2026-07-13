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

## Regeln für die Umsetzung

- Nur die Logik bzw. das zuständige Gerät schreibt Statusgruppenadressen.
- Schutzbefehle haben Vorrang vor Komfort- und Tasterbefehlen.
- Ein Schutzende gibt die Markise nicht automatisch wieder frei; die Freigabe folgt der sicheren Parametrierung des Jalousieaktors.
- Die konkreten Objektbezeichnungen und Werte der MDT- und Gira-Produktdatenbanken werden beim Verknüpfen in ETS geprüft.

Jede Logik erhält in ETS einen klaren Namen mit ID, damit Auslöser und Wirkung nachvollziehbar bleiben.
