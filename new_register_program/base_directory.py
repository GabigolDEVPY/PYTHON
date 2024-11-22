import json
import os

Base_dir = os.path.dirname(os.path.abspath(__file__))
utff = os.path.join(Base_dir, "/codeDecode/utf-8_list.json")
data = os.path.join(Base_dir, "data.json")
print(Base_dir)
print(utff)
print(data)


def load_data(data):
    try:
        with open(data, "r") as data:
            return json.load(data)
    except (FileExistsError, FileNotFoundError):
        return []
    
def load_utf(utff):
    try:
        with open(utff, "r" , encoding="utf-8") as f:
            return json.load(f)
    except (FileExistsError, FileNotFoundError):
        print('ERROR')
    
def save_file(file, x):
    try:
        with open(x, "w") as f:
            return json.dump(file, f)   
    except Exception:
        print('Error to save file')
        return []

