import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.graphics_backend import GraphicsBackend

graphics = GraphicsBackend()

graphics.initialize()

print()

print("Current Backend :", graphics.get_backend())