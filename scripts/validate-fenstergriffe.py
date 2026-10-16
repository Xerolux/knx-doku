"""Validiert EG-Fensterkonfiguration ohne Telegramme oder Buszugriff."""
from itertools import product
from pathlib import Path
import yaml
from jinja2 import Environment

root = Path(__file__).resolve().parents[1]
package = yaml.safe_load((root / "home-assistant/knx_fenstergriffe_eg.yaml").read_text(encoding="utf-8"))

# --- 22 empfangende KNX-Binärsensoren auf 11 Geräten ---
raw = package["knx"]["binary_sensor"]
assert len(raw) == 22
assert len({x["state_address"] for x in raw}) == 22
assert all(x["sync_state"] is False for x in raw)
assert len({x["device"]["id"] for x in raw}) == 11
knx_addresses = {x["state_address"] for x in raw}

# --- 11 trigger-basierte Stellungsanzeigen ---
blocks = package["template"]
assert len(blocks) == 11, "erwartet: genau elf trigger-basierte Stellungsanzeigen"

sensors = []
for block in blocks:
    trigger = block["triggers"][0]
    assert trigger["trigger"] == "knx.telegram"
    assert trigger["group_value_read"] is False and trigger["outgoing"] is False
    assert len(trigger["destination"]) == 2
    condition = block["conditions"][0]["value_template"]
    assert "trigger.source ==" in condition and "trigger.payload in [0, 1]" in condition
    sensor = block["sensor"][0]
    texts = [sensor["state"], sensor["icon"], *sensor["attributes"].values()]
    # Spook-Regressionswächter: keine Querverweise auf andere Entitäten
    assert all("state_attr(" not in t for t in texts), sensor["unique_id"]
    # knx.telegram stellt kein trigger.timestamp bereit (würde beim Rendern werfen)
    assert all("trigger.timestamp" not in t for t in texts), sensor["unique_id"]
    # HA template entities reject this key; previously all reception helpers failed
    # to load while the position sensors silently kept displaying Unbekannt.
    assert "entity_category" not in sensor
    # Trigger-Ziele gehören zu den KNX-Empfangsadressen desselben Griffs
    assert set(trigger["destination"]) <= knx_addresses
    sensors.append((trigger, sensor))

assert len({s["unique_id"] for _, s in sensors}) == 11


def render(text, destination, payload, previous):
    env = Environment()
    context = {
        "trigger": {"destination": destination, "payload": payload, "source": "1.1.11"},
        "this": {"attributes": previous},
    }
    return env.from_string(text).render(context).strip()


# --- Zustandslogik: jede Vorbelegung × jedes Telegramm × beide Nutzdaten ---
# None steht für "Attribut fehlt" (noch kein Telegramm); live ist der gespeicherte
# Wert dank des -1-Defaults immer int, None tritt nicht auf.
for trigger, sensor in sensors:
    offen_ga, kipp_ga = trigger["destination"]
    for previous_offen, previous_gekippt in product((None, 0, 1), repeat=2):
        previous = {}
        if previous_offen is not None:
            previous["offen"] = previous_offen
        if previous_gekippt is not None:
            previous["gekippt"] = previous_gekippt
        for destination, payload in product(trigger["destination"], (0, 1)):
            new_offen = payload if destination == offen_ga else previous.get("offen", -1)
            new_gekippt = payload if destination == kipp_ga else previous.get("gekippt", -1)

            actual = render(sensor["state"], destination, payload, previous)
            if new_gekippt == 1:
                expected = "Gekippt"
            elif new_offen == 1:
                expected = "Offen"
            elif new_offen == 0 and new_gekippt == 0:
                expected = "Geschlossen"
            else:
                expected = "Unbekannt"
            assert actual == expected, (sensor["name"], destination, payload, previous, actual)

            attr_offen = render(sensor["attributes"]["offen"], destination, payload, previous)
            attr_gekippt = render(sensor["attributes"]["gekippt"], destination, payload, previous)
            assert attr_offen == str(new_offen), (sensor["name"], attr_offen)
            assert attr_gekippt == str(new_gekippt), (sensor["name"], attr_gekippt)

# --- Lovelace-Karten zeigen nur die Stellungsanzeigen ---
view = yaml.safe_load((root / "home-assistant/lovelace_fenster_eg_view.yaml").read_text(encoding="utf-8"))[0]
cards = view["sections"][0]["cards"][1]["cards"]
assert len(cards) == 11
assert {c["entity"] for c in cards} == {s["default_entity_id"] for _, s in sensors}
assert all(c["tap_action"]["action"] == "more-info" for c in cards)
full = yaml.safe_load((root / "home-assistant/lovelace_knx_eg.yaml").read_text(encoding="utf-8"))
assert [v["path"] for v in full["views"]] == ["licht", "rolllaeden", "heizung", "raumklima", "fenster"]
print("OK: 11 Griffe, 22 eindeutige Empfangsadressen, 444 Zustandskombinationen, keine state_attr-Querverweise, 11 Anzeigekarten.")
