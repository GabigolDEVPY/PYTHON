import os
import json   

# 1 opção ########################

# dirname = name of the directory this file is being executed in
FILE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
DADOS = os.path.join(FILE_DIRECTORY, "dados.json")
print(DADOS)
ctt = input("vvvv")
def load_function():
    try:
        with open(DADOS, "r") as f:
            return json.load(f) 
    except FileNotFoundError:
        return []

# 2 opção #######################

ARQUIVO = "/home/gabigordo/Downloads/PYTHON/dados.json"
def load2():
    with open(ARQUIVO, "r") as f:
        return json.load(f)
    
carregado = load2()
print(carregado)    