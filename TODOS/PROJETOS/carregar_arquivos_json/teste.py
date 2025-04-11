import json
import os

file_directory = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(file_directory, 'file.json')

def load_file():
    try:
        with open(file, "r") as f:
            content =  json.load(f)

            if not content:
                return [1, 2, 3, 4, 5]
            return content
    except (FileNotFoundError, json.JSONDecodeError):

        print('Error to load file or the file is empty')
        return [1, 2, 3, 4, 5]        
    
def save_file(Arquivo):
    with open(file, "w") as f:
        print("File saved")
        return json.dump(Arquivo, f)
    


file_loaded = load_file()

print(file_loaded)

new_list = [num * 2 if num % 2 == 0 else num * 2 / 20 + 2 for num in file_loaded]

option = input("[1]save for save list in a file")

if option == "1":
    savee = save_file(new_list)
    print(new_list)
