DICTIONARY = [
    {"A": ["Ana Silva", "Ana Oliveira", "Ana Costa", "Ana Santos", "Ana Almeida"]},
    {"B": ["Bruno Lima", "Bruno Cardoso", "Bruno Rocha", "Bruno Ferreira", "Bruno Gomes"]},
    {"C": ["Carla Mendes", "Carla Pinto", "Carla Teixeira", "Carla Figueiredo", "Carla Martins"]}
]

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