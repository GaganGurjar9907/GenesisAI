import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.project_creator import ProjectCreator

creator = ProjectCreator()

creator.create("GTA India")