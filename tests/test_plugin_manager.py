import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.plugin_manager import PluginManager

manager = PluginManager()

manager.register("Weather", object())
manager.register("Traffic", object())
manager.register("Physics", object())

manager.list_plugins()

manager.load("Weather")
manager.load("Physics")