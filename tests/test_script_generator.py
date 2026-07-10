import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.script_generator import ScriptGenerator

generator = ScriptGenerator("GTA India")

generator.generate(

    "player",

'''class Player:

    def spawn(self):
        print("Player Spawned")
'''
)