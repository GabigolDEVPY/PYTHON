import os
import json
import random
from packagess import shared, agee


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
        
def save_file(arquivo):
    with open(directory2, 'w') as f:
        return json.dump(arquivo, f, indent=4)
    
file = load_file()

print(file)

ctt = input('press any button to continue...')

list2 = [num * 2 + (10 // num) ** 2 if (num % 2 == 0) else num + 10 for num in [random.randint(1, 10) for num in range(10)]]

print(list2)

os.system("clear")

datas = shared.take_data(list2)


option = input('Enter to save file...')
save_file(datas)
    
