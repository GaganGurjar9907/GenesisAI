import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.resource_manager import ResourceManager

manager = ResourceManager("GTA India")

data = {

    "city": "Mumbai",
    "population": 1500

}

manager.save("test.json", data)

loaded = manager.load("test.json")

print(loaded)