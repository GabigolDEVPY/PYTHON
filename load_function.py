import os
import json   
# dirname = name of the directory this file is being executed in
DIRECTORY_THIS_FILE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(DIRECTORY_THIS_FILE, "dados.json")

def load_file():
    try:
        with open(DATA, "r") as f:
            return json.load(f)
        
    except FileNotFoundError:
        return []
    
load_list = load_file()
print(load_list)