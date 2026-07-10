import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.asset_registry import AssetRegistry

registry = AssetRegistry()

registry.register("Vehicles", "Sports Car")
registry.register("Vehicles", "Police Car")

registry.register("Buildings", "Hospital")
registry.register("Buildings", "Police Station")

registry.register("NPCs", "Police Officer")
registry.register("NPCs", "Civilian")

registry.show()