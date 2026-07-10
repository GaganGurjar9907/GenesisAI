import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.project_context import ProjectContext

context = ProjectContext("GTA India")

print(context.path())

print(context.file("story.json"))

print(context.exists())