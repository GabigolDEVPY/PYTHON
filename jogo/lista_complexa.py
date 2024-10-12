# lista_complexa.py
import os
import json
import time
from acertar_palavra import dinheiro_palavra
from shared import meu_dinheiro, salvar_dinheiro  # Corrigido para usar a variável correta
from loja import lojaa



while True:
    option = input(
        f"Saldo na conta: {meu_dinheiro}\n"
        "Caça palavras [1] Sair [2] Loja[3]\n"
        "Digite uma opção!: "
    )

    if option == "1":
        os.system('cls')
        dinheiro_ganho = dinheiro_palavra()  # Recebe o dinheiro ganho do jogo
        meu_dinheiro += dinheiro_ganho  # Atualiza a variável do dinheiro
        salvar_dinheiro(meu_dinheiro)  # Salva o novo valor do dinheiro no arquivo
    elif option == "2":
        break


    elif option == "3":
        os.system('cls')
        loja = lojaa()

    else:
        print('Digite umas das opçoes')

