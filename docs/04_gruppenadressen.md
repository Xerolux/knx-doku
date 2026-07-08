# 04 – Gruppenadressen

## Hauptgruppen

```text
0 Zentral
1 Licht
2 Beschattung
3 Heizung
4 Wetter
5 Fenster
6 Präsenz
7 Szenen
8 Status
9 Home Assistant
```

## Licht

Pro Raum werden zuerst nur zwei Gruppenadressen benötigt:

```text
1/x/0 Licht Schalten
1/x/1 Licht Status
```

## Beschattung

Pro Rollladen:

```text
2/x/0 Auf/Ab
2/x/1 Stop
2/x/2 Position Soll
2/x/3 Position Status
```

## Heizung

Pro Raum:

```text
3/x/0 Solltemperatur
3/x/1 Isttemperatur
3/x/2 Betriebsmodus
3/x/3 Ventilstellung
3/x/4 Fensterstatus Raum
```

## Fenster

Pro Fenstergriff:

```text
5/x/y Fenstergriff Status
```

## Wetter

```text
4/0/0 Außentemperatur
4/0/1 Windgeschwindigkeit
4/0/2 Regen
4/0/3 Helligkeit Ost
4/0/4 Helligkeit Süd
4/0/5 Helligkeit West
```
