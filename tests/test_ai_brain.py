import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from brain.ai_brain import AIBrain

brain = AIBrain()


def demo():
    print("AI Brain executed task successfully!")


brain.execute_task("Generate Config", demo)

brain.show_status()