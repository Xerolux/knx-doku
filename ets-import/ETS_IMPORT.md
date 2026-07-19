# ETS-Import – Gruppenadressen

## Zweck

`gruppenadressen.xml` ist die direkte Importdatei für ETS 6 mit **3-Ebenen-Gruppenadressstil**. Sie verwendet das native KNX-Format `GroupAddress-Export` und enthält die vollständige Hauptgruppen-, Mittelgruppen- und Gruppenadressstruktur.

`gruppenadressen-planung.csv` bleibt die technische Referenz mit den vorgesehenen DPTs. Sie ist **keine** ETS-Importdatei.

## Import in ETS 6

1. ETS-Projekt öffnen und den Gruppenadressstil **3 Ebenen** verwenden.
2. In der Ansicht **Gruppenadressen** den obersten Eintrag rechtsklicken.
3. **Gruppenadressen importieren** wählen.
4. `gruppenadressen.xml` auswählen.
5. Importbericht prüfen.
6. Anschließend Produktdatenbanken importieren, Geräte in den Linien 1.1, 1.2 und bei Bedarf 1.3 einfügen und Kommunikationsobjekte verknüpfen.

Für XML muss beim Import keine CSV-Zeichenkodierung und kein Trennzeichen ausgewählt werden.

> Vor einem erneuten Import das ETS-Projekt sichern. Bereits vorhandene Gruppenadressen mit identischen Adressen müssen im Importdialog bewusst behandelt werden.

## Topologie

```text
Bereich 1
├── 1.1 KNX TP – Innenbereich und Hauptverteilung
├── 1.2 KNX RF – Fenstergriffe und Funkgeräte
└── 1.3 KNX TP – Außenbereich / Reserve
```

Der MDT RF-LK001.02 verbindet die TP-Linie 1.1 mit der RF-Linie 1.2. RF-Teilnehmer erhalten daher physikalische Adressen `1.2.x`, nicht `1.1.x`. Die Linie 1.3 wird erst bei tatsächlichem Ausbau mit TP-Linienkoppler und eigener Busspannungsversorgung angelegt.

## Was die XML bewusst nicht erledigt

- **DPTs:** Die vorgesehenen DPTs stehen in `gruppenadressen-planung.csv` und müssen zu den Kommunikationsobjekten der Produktdatenbanken passen.
- **Physikalische Adressen und Geräte:** Diese werden in ETS nach dem Einfügen der konkreten Produktdatenbanken vergeben.
- **Verknüpfungen:** Aktor-, Taster- und Sensorobjekte müssen gezielt mit den importierten Gruppenadressen verbunden werden.
- **Topologieerstellung:** Die Linien 1.1, 1.2 und 1.3 werden in ETS manuell angelegt; die Gruppenadress-XML importiert nur Gruppenadressen.

## Wichtige Konventionen

- Adressen werden nicht wiederverwendet.
- Befehle und Rückmeldungen sind getrennt.
- Gruppenadressen sind medienunabhängig und können von TP-, RF- und IP-Geräten gemeinsam verwendet werden.
- Schutz- und Grundfunktionen bleiben auch ohne Home Assistant funktionsfähig.
- Die endgültigen DPTs richten sich immer nach den tatsächlich verwendeten Kommunikationsobjekten.
