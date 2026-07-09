import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.story_generator import generate_story

story = generate_story("Car Racing Game")

print(story)