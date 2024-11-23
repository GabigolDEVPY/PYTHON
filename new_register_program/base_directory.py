import json
import os
from codeDecode import code_decode as cd

Base_dir = os.path.dirname(os.path.abspath(__file__))
utff = os.path.join(Base_dir, "codeDecode/utf-8_list.json")
data = os.path.join(Base_dir, "data.json")



def load_data(data):
    try:
        with open(data, "r") as data:
            users = json.load(data)
            users = cd.decode(users)
            return users
    except (FileExistsError, FileNotFoundError):
        return []

def save_file(file, xdata):
    file_att = cd.code(file)
    try:
        with open(xdata, "w") as f:
            return json.dump(file_att, f)   
    except Exception:
        print('Error to save file')
        return []

