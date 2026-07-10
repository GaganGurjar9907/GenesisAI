import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.builder import Builder

builder = Builder()

builder.build_all("GTA India")