import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_DINHEIRO = os.path.join(BASE_DIR, 'dados.json')

ARQUIVO_PALAVRAS = os.path.join(BASE_DIR, 'lista_palavras.json')

def carregar_lista():
    try:
        with open(ARQUIVO_PALAVRAS, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        pass
def limpar():
    os.system('cls')

lista = carregar_lista()

def carregar_dinheiro():
    try:
        with open(ARQUIVO_DINHEIRO, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

def salvar_dinheiro(valor):
    with open(ARQUIVO_DINHEIRO, 'w') as f:
        json.dump(valor, f)

# Carrega o dinheiro ao iniciar o programa
meu_dinheiro = carregar_dinheiro()

