# Haupteingangslicht: Dämmerungssteuerung

Stand: 12.11.2026. Nutzerauftrag: bei Dunkelheit einschalten, bei Helligkeit ausschalten.

Direkte KNX-Steuerung über Gira Wetterstation Plus `1.1.40`, Dämmerungsgrenzwert 2, statt einer zusätzlichen Zeitschaltuhr oder Home-Assistant-Automation.

## Gemeinsamer Stand: Rollläden und Eingangslicht

Beide Funktionen verwenden den Dämmerungssensor derselben Gira, mit getrennten Grenzwertobjekten und Gruppenadressen:

| Funktion | Dunkel: unter 50 Lux, 5 Minuten | Hell: über 100 Lux, 5 Minuten | Gira / Gruppenadresse |
|---|---|---|---|
| Bestätigte EG-Rollläden: Arbeitszimmer, Wohnzimmer Fenster, Badezimmer, Wohnzimmer Türe | Ab | Auf | Grenzwert 1, KO 36 → `0/1/2` |
| Haupteingangslicht, AKS Kanal I | Ein | Aus | Grenzwert 2, KO 52 → `1/4/12` |

Die Rollladenkonfiguration und ihre erfolgreichen Downloads sind im [Protokoll vom 06.11.2026](43_eg_rollladen_daemmerung_2026-11-06.md) dokumentiert; der Gira-Sender wurde am 12.11.2026 erneut mit dieser Verbindung gesehen. Schlafzimmer, OG, Markise und der unbestätigte Küchenkanal gehören nicht zu dieser Dämmerungsautomatik. Die Rollladen-Empfänger wurden am 12.11. nicht erneut heruntergeladen oder physisch getestet.

Das [Treppenhauslicht an Kanal J](43_treppenhaus_licht_2026-11-12.md) wird separat durch den Raumcontroller-Präsenzmelder gesteuert.

## Parameter

- Grenzwert 2: 50 Lux, Hysterese: 50 Lux.
- Unterschreitung von 50 Lux: EIN; Überschreitung von 100 Lux: AUS.
- Ein- und Ausschaltverzögerung jeweils 5 Minuten.
- Senden bei Wertänderung: Ja; zyklisches Senden: 0 (aus).
- Externer Grenzwert: Nein.
- Dämmerungsgrenzwert 1 für die Rollläden bleibt unverändert.

## Verbindung

`1/4/12 Haupteingang Licht Daemmerung Schalten`, 1 Bit Schalten:

- Sender: Gira `1.1.40`, KO 52, Grenzwert 2 Dämmerung.
- Empfänger: AKS `1.1.3`, Kanal I „Licht Haupteingang“, KO 97 Schalten EIN/AUS.

Die Verbindung wurde in beiden Objektansichten geprüft. Ohne zyklisches Senden wird eine manuelle Schaltung erst beim nächsten Hell-/Dunkelwechsel durch die Automatik überschrieben. Die Schwellen sind Startwerte und beziehen sich auf den Montageort der Wetterstation.

## Inbetriebnahme

Die ETS-Historie bestätigt für AKS `1.1.3` und Gira `1.1.40` jeweils „Programmieren(Part.): Abgeschlossen“. Natürliche Dämmerungsreaktion und physische Lichtwirkung sind noch nicht abgenommen. Keine künstlichen Helligkeitswerte wurden auf den Bus geschrieben.

Grundlage: [Gira Produkthandbuch, Dämmerungssensor und Grenzwerte](https://partner.gira.de/data3/20743510.pdf).
