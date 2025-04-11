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
        return lista_tuple(5)

def save_file(arquivo):
    with open(data_directory, "w") as f:
        return json.dump(arquivo, f, indent=2)


def lista_tuple(num_t):
    tupla = {}
    tupla["sp"] = ["jenoveva", "bocaiuva", "boituvaaa"]
    tupla["sp"][0] = "sao paulo"
    lista_random = [(num * 4) // 2 * (3 + 10) * num_t for num in range(len(tupla["sp"]))]
    return {
        "Cityes": tupla, 
            "Lista Random": lista_random
    }




datas = load_data()
save_file(datas)
print(datas)

