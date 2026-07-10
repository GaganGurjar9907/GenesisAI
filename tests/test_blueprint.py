import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.game_blueprint import GameBlueprint

bp = GameBlueprint()

bp.set("title", "GTA India")
bp.set("genre", "Open World")
bp.set("theme", "India")
bp.set("graphics", "Ultra")
bp.set("camera", "Third Person")
bp.set("platform", ["Windows", "Android"])

bp.show()