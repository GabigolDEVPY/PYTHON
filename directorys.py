import os
import json
        # this function returns the file directory 
directory = os.path.dirname(os.path.abspath(__file__))
filee = os.path.join(directory, "dados.json")

directory2 = (f"{directory}/dados.json")


def load_file():
    try:
        with open(directory2, "r") as f:
            return json.load(f)
        
    except (FileExistsError, FileNotFoundError):
        return [1, 2, 3, 4, 5]
        