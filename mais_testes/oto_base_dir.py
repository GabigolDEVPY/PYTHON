import json
import os

directory = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(directory, "data.json")



def load_data():
    try:
        with open(data_directory, "r") as f:
            return json.load(f)
    except: 
        (FileExistsError, FileNotFoundError)
        return [1, 2, 3, 4]

def save_file(arquivo):
    with open(data_directory, "w") as f:
        return json.dump(arquivo, f)


datas = load_data()
save_file(datas)
print(datas)