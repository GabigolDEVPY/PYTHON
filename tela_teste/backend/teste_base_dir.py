import json 
import os
import sys


user = os.getlogin()

base_dir = os.path.join("C:\\Users", user, "Documents", "Register Program")
json_file = os.path.join(base_dir,"dados.json")
os.makedirs(base_dir, exist_ok=False)

# print(base_dir)  
print(json_file)  




def load_file():
    try:
        with open(json_file, "r") as f:
            return json.load(f)
    except (FileExistsError, FileNotFoundError):
        print('File not found or exists')
        return []

def save_file(lista):
    with open(json_file, "w") as f:
        json.dump(lista, f, indent=4)






