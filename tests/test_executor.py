import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.executor import Executor

executor = Executor()

executor.execute_project("GTA India")