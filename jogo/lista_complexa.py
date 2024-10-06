import os
import json
import time
from acertar_palavra import dinheiro_palavra

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_PALAVRAS = os.path.join(BASE_DIR, 'lista_palavras.json')

lista_palavras = ARQUIVO_PALAVRAS

def carregar_lista():
    try:
        with open(lista_palavras, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Tratar a exceção de arquivo não encontrado aqui
        pass

meu_dinheiro = 0

while True:
    option = input(
        f"Saldo na conta {meu_dinheiro}\n"
        "Caça palavras[1] Sair[2] "
        "Digite uma opção!: "
        )

    if option == "1":
        os.system('cls')
        meu_dinheiro += dinheiro_palavra()