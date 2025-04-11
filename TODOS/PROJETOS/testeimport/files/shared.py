import os
import json


file_directory = os.path.dirname(os.path.abspath(__file__))
charge = os.path.join(file_directory, "lista.json")


def load_lista():
    try:
        with open(charge, "r") as f:
            return json.load(f)
    except (FileNotFoundError, FileExistsError):
        return []

def save_list(file):
        with open(charge, "w") as f:
            return json.dump(file, f)