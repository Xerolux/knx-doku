"""Validiert EG-Fensterkonfiguration ohne Telegramme oder Buszugriff."""
from itertools import product
from pathlib import Path
import yaml
from jinja2 import Environment

root = Path(__file__).resolve().parents[1]
package = yaml.safe_load((root / "home-assistant/knx_fenstergriffe_eg.yaml").read_text(encoding="utf-8"))
raw = package["knx"]["binary_sensor"]
assert len(raw) == 22
assert len({x["state_address"] for x in raw}) == 22
assert all(x["sync_state"] is False for x in raw)
assert len({x["device"]["id"] for x in raw}) == 11
status = package["template"][0]["sensor"]
# HA template sensors reject this key; previously all reception helpers failed
# to load while the position sensors silently kept displaying Unbekannt.
assert all("entity_category" not in sensor
           for block in package["template"] for sensor in block.get("sensor", []))
assert len(status) == 11
for sensor in status:
    for opened, tilted in product((None, 0, 1), repeat=2):
        env = Environment()
        env.globals["state_attr"] = lambda entity, attribute: {"offen": opened, "gekippt": tilted}[attribute]
        actual = env.from_string(sensor["state"]).render().strip()
        expected = "Gekippt" if tilted == 1 else "Offen" if opened == 1 else "Geschlossen" if opened == tilted == 0 else "Unbekannt"
        assert actual == expected, (sensor["name"], opened, tilted, actual)
for block in package["template"][1:]:
    trigger = block["triggers"][0]
    assert trigger["trigger"] == "knx.telegram"
    assert trigger["group_value_read"] is False and trigger["outgoing"] is False
    assert len(trigger["destination"]) == 2
    assert "trigger.source ==" in block["conditions"][0]["value_template"]
    assert "trigger.payload in [0, 1]" in block["conditions"][0]["value_template"]
    helper = block["sensor"][0]
    for destination, payload in product(trigger["destination"], (0, 1)):
        previous = {"offen": None, "gekippt": None}
        context = {"trigger": {"destination": destination, "payload": payload}, "this": {"attributes": previous}}
        env = Environment()
        for attribute, text in helper["attributes"].items():
            expected = payload if destination == trigger["destination"][0 if attribute == "offen" else 1] else None
            actual = env.from_string(text).render(context).strip()
            assert actual == str(expected), (destination, attribute, actual)
view = yaml.safe_load((root / "home-assistant/lovelace_fenster_eg_view.yaml").read_text(encoding="utf-8"))[0]
cards = view["sections"][0]["cards"][1]["cards"]
assert len(cards) == 11
assert {c["entity"] for c in cards} == {s["default_entity_id"] for s in status}
assert all(c["tap_action"]["action"] == "more-info" for c in cards)
full = yaml.safe_load((root / "home-assistant/lovelace_knx_eg.yaml").read_text(encoding="utf-8"))
assert [v["path"] for v in full["views"]] == ["licht", "rolllaeden", "heizung", "raumklima", "fenster"]
print("OK: 11 Griffe, 22 eindeutige Empfangsadressen, 99 Zustandskombinationen, Telegrammfilter und 11 Anzeigekarten.")
