# ETS-Import – Gruppenadressen

## Zweck

`gruppenadressen.csv` ist die direkte Importdatei für ETS mit **3-Ebenen-Gruppenadressstil**. Sie enthält ausschließlich die von ETS erwartete Struktur aus Hauptgruppe, Mittelgruppe, Gruppenadresse und Adresse.

`gruppenadressen-planung.csv` ist die technische Referenz mit dem vorgesehenen DPT. Sie ist **nicht** die Importdatei.

## Import in ETS

1. Neues ETS-Projekt mit dem Gruppenadressstil **3 Ebenen** anlegen bzw. öffnen.
2. In der Ansicht **Gruppenadressen** auf den obersten Eintrag rechtsklicken.
3. **Gruppenadressen importieren** wählen.
4. `gruppenadressen.csv` auswählen; ETS erkennt das 3-Ebenen-CSV-Format automatisch.
5. Importbericht prüfen. Danach die Produktdatenbanken importieren, Geräte einfügen und deren Kommunikationsobjekte mit den Gruppenadressen verbinden.

> Der Import ersetzt bereits vorhandene Elemente mit gleicher Struktur bzw. Adresse. Vor einem erneuten Import daher das ETS-Projekt sichern.

## Was die Datei bewusst nicht erledigt

- **DPTs:** Das ETS-CSV-Format für den 3-Ebenen-Import umfasst nur vier Spalten. Die vorgesehenen DPTs stehen in `gruppenadressen-planung.csv` und werden beim Verknüpfen der Kommunikationsobjekte geprüft bzw. durch die Produktdatenbank vorgegeben.
- **Physikalische Adressen und Geräte:** Diese entstehen erst nach dem Einfügen der konkreten Produktdatenbanken in ETS. `physikalische-adressen.csv` dient dafür als Vergabe- und Beschriftungsliste.
- **Verknüpfungen:** Aktor-, Taster- und Sensorobjekte werden nach dem Import gezielt auf die vorhandenen Gruppenadressen gezogen.

## Wichtige Konventionen

- Adressen werden nicht wiederverwendet.
- Befehle und Rückmeldungen sind getrennt.
- Zentralfunktionen verwenden je Funktion genau ein eindeutiges Objekt: Die Beschattungsautomatik hat eine Freigabe und eine Rückmeldung; die zentrale Heizung verwendet eine Betriebsart Soll und Status statt vier widersprüchlicher Bit-Befehle.
- Die endgültigen DPTs richten sich immer nach den tatsächlich verwendeten Kommunikationsobjekten der importierten Geräte.

Die CSV-Struktur folgt dem von ETS exportierten und wieder importierbaren 3-Ebenen-Format. Details: [KNX Association – Gruppenadresse und Export](https://support.knx.org/hc/de/articles/360022237580-Gruppenadresse-und-Export).
