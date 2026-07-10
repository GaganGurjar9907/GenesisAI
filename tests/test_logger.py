import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.logger import Logger

logger = Logger("GTA India")

logger.log("Genesis AI Started")
logger.log("Story Generated")
logger.log("World Generated")
logger.log("NPC Generated")
logger.log("Mission Generated")