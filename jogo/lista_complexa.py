# lista_complexa.py
import os
import json
import time
from acertar_palavra import dinheiro_palavra
from shared import meu_dinheiro, salvar_dinheiro  # Corrigido para usar a variável correta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_PALAVRAS = os.path.join(BASE_DIR, 'lista_palavras.json')

def carregar_lista():
    try:
        with open(ARQUIVO_PALAVRAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        pass

while True:
    option = input(
        f"Saldo na conta: {meu_dinheiro}\n"
        "Caça palavras [1] Sair [2]\n"
        "Digite uma opção!: "
    )

    if option == "1":
        os.system('cls')
        dinheiro_ganho = dinheiro_palavra()  # Recebe o dinheiro ganho do jogo
        meu_dinheiro += dinheiro_ganho  # Atualiza a variável do dinheiro
        salvar_dinheiro(meu_dinheiro)  # Salva o novo valor do dinheiro no arquivo
    elif option == "2":
        break
