import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.context import Context

ctx = Context()

ctx.set("project", "GTA India")
ctx.set("genre", "Open World")
ctx.set("theme", "India")
ctx.set("graphics", "Ultra")

ctx.show()