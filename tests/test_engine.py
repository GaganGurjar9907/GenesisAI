import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.scene import Scene
from engine.game_object import GameObject

scene = Scene("Main City")

player = GameObject("Player")

player.add_component("Transform")
player.add_component("Camera")
player.add_component("Renderer")

scene.add_object(player.name)

player.show()

scene.show()