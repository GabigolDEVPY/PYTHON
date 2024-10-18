import os
import json
import time
from shared import dados, limpar
from loja import lojaa

def ver_inventario(itens):
    for i, item in enumerate(itens):
        print(f'{i}: {item["item"]} - Valor: {item["Valor"]}')
    time.sleep(3)

while True:
    limpar()
    meu_dinheiro = dados["meu_dinheiro"]
    option = input(
        f"Saldo na conta: {meu_dinheiro}\n"
        "[1]Forca___[2]Inventário___[3]Loja___[4]sair\n"
        "Digite uma opção!: "
    )

    if option == "1":
        limpar()
        dinheiro_palavra()  # Recebe o dinheiro ganho do jogo

    elif option == "4":
        limpar()
        break

    elif option == "3":
        limpar()
        loja = lojaa()
    
    elif option == "2":
        limpar()
        escolha = input('SELECIONE O QUE DESEJA VER:\n'
                        "[1]Periféricos [2]Casas [3]Carros\nDigite uma opção: ")
        
        if escolha == "1":
            ver_inventario(dados["perifericos"])
        elif escolha == "2":
            ver_inventario(dados["casas"])
        elif escolha == "3":
            ver_inventario(dados["carros"])
        else:
            print('Opção inválida!')
    
    else:
        print('Digite uma das opções')
