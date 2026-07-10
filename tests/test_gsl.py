import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from language.gsl_parser import GSLParser

parser = GSLParser()

text = """
Title = GTA India
Genre = Open World
Theme = India
Graphics = Ultra
Players = 1
Platform = Windows, Android
"""

parser.parse(text)
parser.show()