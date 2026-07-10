import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from compiler.build_pipeline import BuildPipeline

pipeline = BuildPipeline()

pipeline.run()