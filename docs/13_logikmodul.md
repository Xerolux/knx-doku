# 13 – MDT Logikmodul

## Ziel

Das Logikmodul übernimmt wichtige Grundlogiken direkt auf KNX. Home Assistant darf diese Logiken anzeigen oder ergänzen, aber nicht ersetzen.

## Logikliste

### LOG001 – Windalarm Markise

```text
Wenn Windalarm = 1
Dann Markise Einfahren Zentral = 1
Und Wetterschutz Aktiv = 1
```

Zweck: Markise vor Wind schützen.

### LOG002 – Regenalarm Markise

```text
Wenn Regenalarm = 1
Dann Markise Einfahren Zentral = 1
Und Wetterschutz Aktiv = 1
```

Zweck: Markise bei Regen einfahren.

### LOG003 – Frostalarm Markise sperren

```text
Wenn Frostalarm = 1
Dann Wetterschutz Aktiv = 1
```

Zweck: Schutzfunktion bei Frost.

### LOG004 – Fenster offen Heizung absenken

```text
Wenn Fensterstatus Raum = offen/gekippt
Dann Heizung Raum Eco oder Frostschutz
```

Zweck: keine Heizenergie verschwenden.

### LOG005 – Haus verlassen Licht aus

```text
Wenn Haus verlassen = 1
Dann Zentral Aus = 1
```

Zweck: alle normalen Lichtkreise ausschalten.

### LOG006 – Haus verlassen Heizung Eco

```text
Wenn Haus verlassen = 1
Dann Heizung Eco = 1
```

Zweck: Heizung absenken.

### LOG007 – Nachtmodus

```text
Wenn Nachtmodus = 1
Dann Heizung Nacht = 1
Und Ganglicht nur reduziert schalten, falls Dimmung später vorhanden
```

Aktuell ist Licht nur ein/aus geplant. Eine reduzierte Gangbeleuchtung ist daher eine spätere Erweiterung mit DALI, Dimmer oder LED.

### LOG008 – Urlaub

```text
Wenn Urlaub = 1
Dann Heizung Eco = 1
Dann Beschattungsautomatik Ein = 1
```

Zweck: längere Abwesenheit.

### LOG009 – Panik

```text
Wenn Panik = 1
Dann ausgewählte Lichter ein
```

Zweck: Not- oder Abschreckfunktion.

## Empfehlung

Jede Logik bekommt in ETS einen klaren Namen mit Nummer. So kann später nachvollzogen werden, warum eine Funktion ausgelöst wurde.
