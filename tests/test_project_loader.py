import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.project_loader import ProjectLoader

loader = ProjectLoader()

project = loader.load("GTA India")

print(project.keys())