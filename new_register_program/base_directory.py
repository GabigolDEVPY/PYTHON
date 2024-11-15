import json
import os

Base_dir = os.path.dirname(__file__)
data = os.path.join(Base_dir, "data.json")


def load_data(data):
    try:
        with open(data, "r") as data:
            return json.load(data)
    except (FileExistsError, FileNotFoundError):
        return []
    
def save_file(file, x):
    try:
        with open(x, "w") as f:
            return json.dump(file, f)   
    except Exception:
        print('Error to save file')
        return []


