import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.project_validator import ProjectValidator

validator = ProjectValidator()

validator.validate("GTA India")