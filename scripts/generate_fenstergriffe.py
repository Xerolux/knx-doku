"""Erzeugt home-assistant/knx_fenstergriffe_eg.yaml aus der Griff-Tabelle der Doku (docs/08)."""
from pathlib import Path

# Quelle: docs/08_rf_fenstergriffe.md — Adresse, Name, Offen-GA, Kipp-GA
GRIFFE = [
    ("1.1.11", "Küche links klein",        "kuche_links_klein",        "5/1/0", "5/1/20", "window"),
    ("1.1.12", "Küche rechts groß",        "kuche_rechts_gross",       "5/1/1", "5/1/21", "window"),
    ("1.1.13", "Wohnzimmer links klein",   "wohnzimmer_links_klein",   "5/0/0", "5/0/20", "window"),
    ("1.1.14", "Wohnzimmer rechts groß",   "wohnzimmer_rechts_gross",  "5/0/1", "5/0/21", "window"),
    ("1.1.15", "Arbeitszimmer links klein","arbeitszimmer_links_klein","5/3/0", "5/3/20", "window"),
    ("1.1.16", "Arbeitszimmer rechts groß","arbeitszimmer_rechts_gross","5/3/1","5/3/21", "window"),
    ("1.1.17", "Schlafzimmer rechts groß", "schlafzimmer_rechts_gross","5/4/0", "5/4/20", "window"),
    ("1.1.18", "Schlafzimmer Tür",         "schlafzimmer_tur",         "5/4/1", "5/4/21", "door"),
    ("1.1.19", "Wohnzimmer Tür",           "wohnzimmer_tur",           "5/0/2", "5/0/22", "door"),
    ("1.1.39", "Bad links",                "bad_links",                "5/5/0", "5/5/20", "window"),
    ("1.1.42", "Bad rechts",               "bad_rechts",               "5/5/1", "5/5/21", "window"),
]

HEADER = """\
# EG MDT RF+ Fenstergriffe – nur empfangende Zustände, kein Bus-Polling.
# ETS: Objekt 2 -> Offen; Objekt 3 -> Gekippt; 1 = aktiv (vor Inbetriebnahme prüfen).
# Stellungsanzeige ist trigger-basiert: Sie führt offen/gekippt in eigenen Attributen
# und wertet nur bestätigte Telegramme der jeweiligen Geräteadresse aus (kein state_attr
# auf andere Entitäten – Ursache der Spook-Reparaturen vom 16.10.2026).
"""


def knx_sensor(slug, label, address, kind, side):
    name = "EG Fenstergriff " + label
    return f"""    - name: "{'Offen' if side == 'offen' else 'Gekippt'}"
      unique_id: "eg_fenstergriff_{slug}_{side}"
      default_entity_id: "binary_sensor.eg_fenster_{slug}_{side}"
      state_address: "{address}"
      sync_state: false
      device_class: {kind}
      device:
        id: "eg_fenstergriff_{slug}"
        name: "{name}"
"""


def template_block(addr, slug, label, offen_ga, kipp_ga):
    indent = " " * 10
    state_sets = (
        "{% set offen = trigger.payload if trigger.destination == '"
        + offen_ga
        + "' else this.attributes.get('offen', -1) %}\n"
        + indent
        + "{% set gekippt = trigger.payload if trigger.destination == '"
        + kipp_ga
        + "' else this.attributes.get('gekippt', -1) %}\n"
    )
    body_sets = (
        "{{ trigger.payload if trigger.destination == '"
        + offen_ga
        + "' else this.attributes.get('offen', -1) }}"
    )
    kipp_sets = (
        "{{ trigger.payload if trigger.destination == '"
        + kipp_ga
        + "' else this.attributes.get('gekippt', -1) }}"
    )
    return f"""  - triggers:
      - trigger: knx.telegram
        destination: ["{offen_ga}", "{kipp_ga}"]
        group_value_read: false
        outgoing: false
    conditions:
      - condition: template
        value_template: "{{{{ trigger.source == '{addr}' and trigger.payload in [0, 1] }}}}"
    sensor:
      - name: "EG Fenster {label} Stellung"
        unique_id: "eg_fenster_{slug}_stellung"
        default_entity_id: "sensor.eg_fenster_{slug}_stellung"
        state: >-
          {state_sets}\
          {{% if gekippt == 1 %}}Gekippt
          {{% elif offen == 1 %}}Offen
          {{% elif offen == 0 and gekippt == 0 %}}Geschlossen
          {{% else %}}Unbekannt{{% endif %}}
        icon: >-
          {state_sets}\
          {{% if gekippt == 1 %}}mdi:window-open-variant
          {{% elif offen == 1 %}}mdi:window-open
          {{% elif offen == 0 and gekippt == 0 %}}mdi:window-closed
          {{% else %}}mdi:help-circle-outline{{% endif %}}
        attributes:
          offen: "{body_sets}"
          gekippt: "{kipp_sets}"
          letzte_meldung: "{{{{ now().strftime('%d.%m. %H:%M:%S') }}}} von {{{{ trigger.source }}}} auf {{{{ trigger.destination }}}}"
"""


def main():
    out = [HEADER, "knx:\n  binary_sensor:\n"]
    for addr, label, slug, offen, kipp, kind in GRIFFE:
        out.append(knx_sensor(slug, label, offen, kind, "offen"))
        out.append(knx_sensor(slug, label, kipp, kind, "gekippt"))
    out.append("template:\n")
    for addr, label, slug, offen, kipp, kind in GRIFFE:
        out.append(template_block(addr, slug, label, offen, kipp))
    path = Path(__file__).resolve().parents[1] / "home-assistant" / "knx_fenstergriffe_eg.yaml"
    path.write_text("".join(out), encoding="utf-8", newline="\n")
    print(f"geschrieben: {path}")


if __name__ == "__main__":
    main()
