import json
import os

DIRECTORY_FILE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(DIRECTORY_FILE, "dados.json")

def load_file():
    try:
        with open(DATA, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
DADOS_LOAD = load_file()
print(DADOS_LOAD)    