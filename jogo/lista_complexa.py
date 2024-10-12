# lista_complexa.py
import os
import json
import time
from acertar_palavra import dinheiro_palavra
from shared import meu_dinheiro, salvar_dinheiro, carregar_dinheiro, limpar  # Corrigido para usar a variável correta
from loja import lojaa



while True:
    limpar()
    meu_dinheiro = carregar_dinheiro()
    option = input(
        f"Saldo na conta: {meu_dinheiro}\n"
        "Caça palavras [1] Sair [2] Loja[3]\n"
        "Digite uma opção!: "
    )

    if option == "1":
        limpar()
        dinheiro_palavra()  # Recebe o dinheiro ganho do jogo


    elif option == "2":
        limpar()
        break


    elif option == "3":
        limpar()
        loja = lojaa()

    else:
        print('Digite umas das opçoes')

