import sys
import os

# sys.path.append
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import base_directory as bd


file = bd.load_utf(bd.utff)

print(file)