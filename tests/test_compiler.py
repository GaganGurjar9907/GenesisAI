import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from compiler.compiler_manager import CompilerManager

compiler = CompilerManager()

compiler.compile("GTA India")