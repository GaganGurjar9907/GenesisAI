import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.planner import Planner
from core.game_blueprint import GameBlueprint

bp = GameBlueprint()

bp.data["genre"] = "Open World Action"

planner = Planner()

planner.create_plan(bp)

planner.show()