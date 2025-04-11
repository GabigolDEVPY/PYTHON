import json
import os

FILE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(FILE_DIRECTORY, "dados.json")

def load_file():
    try:
        with open(DATA, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print("Erro inerperado:", e)
        
DICTIONARY = load_file()

def search(dictionary, name):
    first_word_name = name[0].upper()  # Garante que a primeira letra esteja em maiúscula

    for dic in dictionary:
        for letra, lista in dic.items():
            if letra == first_word_name:
                for item in lista:
                    if item.lower() == name.lower():  # Verifica se o nome corresponde
                        return name, letra
    return None  # Retorna None caso não encontre o nome

# Testando a função
result = search(DICTIONARY, "Bruno Gomes")
print(result)


