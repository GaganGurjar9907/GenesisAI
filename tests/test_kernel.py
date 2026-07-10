import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from kernel.kernel import GenesisKernel

kernel = GenesisKernel()

kernel.boot()