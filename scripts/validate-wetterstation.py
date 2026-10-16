"""Read-only validation of the weather package and dashboard contract."""
from pathlib import Path
import re
import yaml
from jinja2 import Environment

root = Path(__file__).resolve().parents[1]
package = yaml.safe_load((root / "home-assistant/knx_wetterstation_gira.yaml").read_text(encoding="utf-8"))
dashboard_text = (root / "home-assistant/lovelace_wetter_gira.yaml").read_text(encoding="utf-8")
dashboard = yaml.safe_load(dashboard_text)
assert set(package) == {"knx", "template", "automation"}
assert set(package["knx"]) == {"sensor", "binary_sensor"}
native = package["knx"]["sensor"] + package["knx"]["binary_sensor"]
assert len(native) == 31
assert len({s["state_address"] for s in native}) == 31
assert all(s["sync_state"] == "expire 5" for s in native)
assert all(s["state_address"].startswith(("4/0/", "4/1/")) for s in native)
absolute = next(s for s in native if s["state_address"] == "4/0/6")
assert absolute["type"] == "absolute_humidity"
for block in package["template"][:2]:
    trigger = block["triggers"][0]
    assert trigger["outgoing"] is False and trigger["group_value_read"] is False
    assert "trigger.source == '1.1.40'" in block["conditions"][0]["value_template"]
wind = package["template"][2]["sensor"][0]
assert "bitwise_and(36864)" in wind["availability"]
assert "gira_wetter_versorgung_ok" in wind["availability"]
for status, valid in [(0, True), (1, True), (4096, False), (12289, False), (32768, False), (65535, False)]:
    assert ((status & 36864) == 0) == valid
env = Environment()
env.filters["bitwise_and"] = lambda a, b: a & b
for status, raw, unit, supply, expected in [
    (1, 1.4, "km/h", True, True),
    (1, .4, "m/s", True, True),
    (0, 180, "km/h", True, False),  # replacement before fault telegram
    (0, 50, "m/s", True, False),
    (4096, 1.4, "km/h", True, False),
    (32768, 1.4, "km/h", True, False),
    (1, 1.4, "km/h", False, False),
]:
    context = dict(has_value=lambda _: True,
                   is_state=lambda *_: supply,
                   states=lambda entity: status if entity.endswith("sensorstatus") else raw,
                   state_attr=lambda *_: unit)
    actual = env.from_string(wind["availability"]).render(context).strip()
    assert actual == str(expected), (status, raw, unit, supply, actual)
assert {a["action"] for automation in package["automation"] for a in automation["actions"]} == {"knx.read"}
assert [v["path"] for v in dashboard["views"]] == ["wetter", "sonne", "diagnose"]
ids = {s["default_entity_id"] for s in native}
ids.update(s["default_entity_id"] for block in package["template"] for s in block["sensor"])
refs = set(re.findall(r"(?:sensor|binary_sensor)\.gira_wetter_[a-z_0-9]+", dashboard_text))
assert refs == ids, (ids - refs, refs - ids)
assert "call-service" not in dashboard_text and "perform-action" not in dashboard_text
assert "DPT 7" not in dashboard_text
print("OK: 33 station outputs, 2 derived displays, 3 views, humidity DPT 9.029, wind fault gating, read-only automation.")
