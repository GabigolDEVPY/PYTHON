import json 
import os


base_dir = os.path.dirname(os.path.abspath(__file__))
json_file = os.path.join(base_dir, "dados.json")


def load_file(file):
    try:
        with open(json_file, "r") as f:
            return json.load(f)
    except:
        (FileExistsError, FileNotFoundError)
        print('File not found or exists')
        return []

def save_file(lista):
    with open(json_file, "w") as f:
        json.dump(lista, f, indent=4)
    






