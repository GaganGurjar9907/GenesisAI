import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.scene import Scene

scene = Scene("Main City")

scene.add_object("Player")
scene.add_object("Police NPC")
scene.add_object("Hospital")
scene.add_object("Sports Car")

scene.show()