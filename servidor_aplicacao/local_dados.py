import json
import os


local = os.path.dirname(__file__)
dir_dados = os.path.join(local, "dados.json")


def load_data():
    try:
        with open(dir_dados, "r") as f:
            return json.load(f)
        
    except:
        return []
    
def save_data(dados):
    try:
        with open(dir_dados, "w") as f:
            return json.dump(dados, f)
        
    except:
        return "Não foi possível"
    

def criar_dado():
    result = load_data()
    print(result)
    nome = input("nome: ")
    result.append(nome)
    save_data(result)

criar_dado()

result = load_data()

print(result)