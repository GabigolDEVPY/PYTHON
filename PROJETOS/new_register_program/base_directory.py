import json
import os
from codeDecode import code_decode as cd
import sys

if getattr(sys, 'frozen', False):
    Base_dir = os.path.dirname(sys.executable)
else:
    Base_dir = os.path.dirname(os.path.abspath(__file__))

# Caminhos dos arquivos
utff = os.path.join(Base_dir, "codeDecode/utf-8_list.json")
data = os.path.join(Base_dir, "data.json")


def load_data(data_path):
    """
    Carrega dados do arquivo JSON. Se o arquivo não existir, retorna uma lista vazia.
    """
    try:
        with open(data_path, "r", encoding="utf-8") as data_file:
            users = json.load(data_file)
            users = cd.decode(users)  # Decodifica os dados
            return users
    except (FileNotFoundError, FileExistsError):  # Lida com arquivos inexistentes
        return []


def save_file(data_list, file_path):
    """
    Salva os dados codificados no arquivo JSON. Cria o arquivo se ele não existir.
    """
    file_att = cd.code(data_list)  # Codifica os dados antes de salvar
    try:

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(file_att, f)
    except Exception as e:
        print(f"Error to save file: {e}")