"""Validiert EG-Fensterkonfiguration ohne Telegramme oder Buszugriff."""
from itertools import product
from pathlib import Path
import yaml
from jinja2 import Environment

root = Path(__file__).resolve().parents[1]
package = yaml.safe_load((root / "home-assistant/knx_fenstergriffe_eg.yaml").read_text(encoding="utf-8"))
raw = package["knx"]["binary_sensor"]
assert len(raw) == 24
assert len({x["state_address"] for x in raw}) == 24
assert all(x["sync_state"] is False for x in raw)
assert len({x["device"]["id"] for x in raw}) == 12
blocks = package["template"]
assert len(blocks) == 12
status = [block["sensor"][0] for block in blocks]
assert all("entity_category" not in sensor for sensor in status)
assert len({sensor["unique_id"] for sensor in status}) == 12
for block in blocks:
    trigger = block["triggers"][0]
    assert trigger["trigger"] == "knx.telegram"
    assert trigger["group_value_read"] is False and trigger["outgoing"] is False
    assert len(trigger["destination"]) == 2
    assert "trigger.source ==" in block["conditions"][0]["value_template"]
    assert "trigger.payload in [0, 1]" in block["conditions"][0]["value_template"]
    sensor = block["sensor"][0]
    assert "state_attr(" not in sensor["state"]
    for opened, tilted in product((-1, 0, 1), repeat=2):
        for destination in trigger["destination"]:
            payload = opened if destination == trigger["destination"][0] else tilted
            context = {"trigger": {"destination": destination, "payload": payload},
                       "this": {"attributes": {"offen": opened, "gekippt": tilted}}}
            actual = Environment().from_string(sensor["state"]).render(context).strip()
            expected = "Gekippt" if tilted == 1 else "Offen" if opened == 1 else "Geschlossen" if opened == tilted == 0 else "Unbekannt"
            assert actual == expected, (sensor["name"], opened, tilted, actual)
    for destination, payload in product(trigger["destination"], (0, 1)):
        context = {"trigger": {"destination": destination, "payload": payload},
                   "this": {"attributes": {"offen": -1, "gekippt": -1}}}
        for attribute in ("offen", "gekippt"):
            expected = payload if destination == trigger["destination"][0 if attribute == "offen" else 1] else -1
            actual = Environment().from_string(sensor["attributes"][attribute]).render(context).strip()
            assert actual == str(expected), (destination, attribute, actual)
bad = next(block for block in blocks if block["sensor"][0]["unique_id"] == "eg_fenster_bad_vorne_stellung")
assert bad["triggers"][0]["destination"] == ["5/2/0", "5/2/20"]
assert "trigger.source == '1.1.44'" in bad["conditions"][0]["value_template"]
view = yaml.safe_load((root / "home-assistant/lovelace_fenster_eg_view.yaml").read_text(encoding="utf-8"))[0]
cards = view["sections"][0]["cards"][1]["cards"]
assert len(cards) == 12
assert {c["entity"] for c in cards} == {s["default_entity_id"] for s in status}
assert all(c["tap_action"]["action"] == "more-info" for c in cards)
full = yaml.safe_load((root / "home-assistant/lovelace_knx_eg.yaml").read_text(encoding="utf-8"))
assert [v["path"] for v in full["views"]] == ["licht", "rolllaeden", "heizung", "raumklima", "fenster"]
full_cards = next(v for v in full["views"] if v["path"] == "fenster")["sections"][0]["cards"][1]["cards"]
assert {c["entity"] for c in full_cards} == {s["default_entity_id"] for s in status}
print("OK: 12 Griffe, 24 eindeutige Empfangsadressen, 108 Zustandskombinationen, Telegrammfilter und 12 Anzeigekarten.")
