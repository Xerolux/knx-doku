# 09 – Home Assistant

Stand: 05.08.2026

## Rolle von Home Assistant

Home Assistant ergänzt KNX, ersetzt aber nicht die Grundfunktionen.

KNX übernimmt:

- Licht schalten
- Rollläden fahren
- Heizung regeln
- Fensterstatus auswerten
- Wetterwerte für Beschattung verwenden
- zentrale Lichtfunktion
- Datum und Uhrzeit über den KNX-Zeitmaster bereitstellen

Home Assistant übernimmt:

- Visualisierung
- Bedienung über App und Browser
- Benachrichtigungen
- Statistik
- Energieauswertung
- Komfortlogiken
- Fernzugriff

## Verbindung

```text
Home Assistant
↕ LAN
MDT SCN-IP100.03
↕ KNX TP
KNX Linie 1.1
```

Für parallelen Betrieb von ETS und Home Assistant müssen freie KNXnet/IP-Tunnel beziehungsweise zusätzliche physikalische Tunneladressen vorhanden sein. Bei einer von ETS gemeldeten Zugriffsverweigerung ist zusätzlich das Sicherheitsmodul `1.1.9 MDT SCN-SAFE.01` zu prüfen.

## KNX-Projektimport

Beim Import der `.knxproj`-Datei in Home Assistant wird gegebenenfalls das in ETS gesetzte **Projektpasswort** abgefragt. Nicht gemeint sind:

- KNX-IP-Secure-Gerätecode
- Web-PIN
- Sicherheitsmodul-PIN
- Home-Assistant-Passwort

Hat das ETS-Projekt kein Projektpasswort, bleibt das Feld leer.

## Zeit und Datum

Der KNX-Zeitmaster ist die E-Mail- und Zeitserver-Applikation `1.1.31` des MDT SCN-IP100.03. Home Assistant darf die Zeitgruppenadressen lesen, soll aber nicht gleichzeitig als weiterer Zeitmaster auf dieselben Adressen schreiben.

Verwendete Adressen:

```text
0/5/0 Uhrzeit
0/5/1 Datum
0/5/2 Datum/Uhrzeit
```

## Zentral Licht

Home Assistant kann `0/4/0 Alle Lichter schalten` optional bedienen. Die Grundfunktion zwischen Taster `1.1.20` und Schaltaktor `1.1.3` funktioniert unabhängig von Home Assistant.

## Angelegte Entitäten

Die aktuell angelegten Licht-, Rollladen- und Markisenentitäten sowie ihre Gruppenadressen sind vollständig in [23 – Home Assistant: KNX-Entitäten und Lovelace-Dashboard](23_home_assistant_knx_entities_dashboard.md) dokumentiert.

Kurzüberblick:

- sechs Abdeckungsentitäten für Rollläden und Markise
- sieben Lichtentitäten einschließlich beider Ganglichter
- drei vorhandene Klimaentitäten aus dem Altbestand im Dashboard
- gemeinsamer Gang-Schaltbefehl über `1/4/4`
- gemeinsamer Gang-Status über `1/4/5`; ODER-Logik in ETS angelegt, Download und Busprüfung noch offen

## Lovelace

Die aktuelle Dashboard-Datei liegt unter:

```text
home-assistant/lovelace_knx_eg.yaml
```

Das Dashboard verwendet `custom:button-card` und besitzt genau drei Reiter:

- Licht
- Rollläden
- Heizung

Die Rollladenkarten sind reine Anzeigen. Ein Tipp öffnet den Home-Assistant-Dialog **Mehr Informationen**, über den Auf, Ab, Stopp und Position bedient werden.

## OpenKNX RaumController

Home Assistant liest die Raumklimawerte des OpenKNX RaumControllers `1.1.29` über `13/0/0` bis `13/0/6`. Die Adressen liegen bewusst in der gemeinsamen Hauptgruppe `13 Raumklima`, damit später auch KNX-Anzeigen, Logiken oder eine Lüftungssteuerung dieselben Werte verwenden können.

Die vollständige Objektzuordnung und die Home-Assistant-YAML-Konfiguration stehen in [24 – OpenKNX RaumController](24_openknx_raumcontroller.md).

## Empfehlung

In Home Assistant nur Gruppenadressen einbinden, die tatsächlich gebraucht werden. Schreibende Automationen für Schutzfunktionen oder Zeitversorgung dürfen nicht mit den nativen KNX-Mastern konkurrieren. Die ETS bleibt die verbindliche Hauptdokumentation.

Passwörter, Tokens, Schlüsselbunddateien, private ETS-Projekte und Screenshots werden nicht in das öffentliche Repository übernommen.
