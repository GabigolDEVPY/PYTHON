import json
import os

# Diretório base e caminho do arquivo JSON
Base_directory = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(Base_directory, "one_list.json")

# Função para carregar o arquivo JSON
def load_file():
    try:
        with open(file, "r") as f:
            # Tenta carregar o conteúdo do arquivo
            content = json.load(f)
            # Se o conteúdo do arquivo for vazio, retorna uma lista vazia
            if not content:
                return []
            return content
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não for encontrado ou estiver corrompido, retorna uma lista vazia
        print('Error to load file or the file is empty')
        return []

# Carregar o conteúdo do arquivo
list_load = load_file()
print(list_load)

# Função para salvar a lista no arquivo JSON
def save_file(FILE):
    with open(file, "w") as f:
        json.dump(FILE, f)  # Aqui você deve passar a variável FILE

# Salvar a lista carregada de volta no arquivo
save_file(list_load)
