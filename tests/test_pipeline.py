import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.pipeline import Pipeline
from core.game_blueprint import GameBlueprint

bp = GameBlueprint()

bp.data["genre"] = "Open World Action"
bp.data["theme"] = "India"
bp.data["graphics"] = "Ultra"

pipeline = Pipeline()

pipeline.execute(bp)