import json
import os

Base_dir = os.path.dirname(__file__)
data = os.path.join(Base_dir, "data.json")


def load_data():
    try:
        with open(data, "r") as data:
            return json.load(data)
    except (FileExistsError, FileNotFoundError):
        return []
    
def save_file(file):
    try:
        with open(data, "w") as f:
            return json.dump(file, data, indent=3)   
    except Exception:
        print('Error to save file')


