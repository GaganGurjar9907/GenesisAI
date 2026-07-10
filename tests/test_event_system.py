import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.event_system import EventSystem

events = EventSystem()


def on_story():
    print("Story Event Triggered")


def on_world():
    print("World Event Triggered")


events.register("story_generated", on_story)
events.register("world_generated", on_world)

events.trigger("story_generated")
events.trigger("world_generated")