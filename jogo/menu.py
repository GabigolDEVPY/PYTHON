import os
import json
import time
from forca import dinheiro_palavra
from shared import dados, limpar, carregar_dados, salvar_dados, lista
from loja import lojaa

def ver_inventario(itens):
        limpar()
        if len(itens) == 0:
            limpar()
            print(f"SEU INVENTÁRIO ESTÁ VAZIO")
            time.sleep(2)
            return
        print(f"MEU DINHEIRO {meu_dinheiro}\n" 
            "\n"
            "INVENTÁRIO:")
        print()
        for i, item in enumerate(itens):
            print(f'{i}: {item["item"]}  Valor - {item["complemento"]}')
        print()
        continuar = input('PRESSIONE [ENTER] CONTINUAR: ')

while True:
    dados = carregar_dados()
    limpar()
    meu_dinheiro = dados["meu_dinheiro"]
    option = input(
        f"Saldo na conta: {meu_dinheiro}\n"
        "\n"
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
        lojaa()
    
    elif option == "2":
            while True:
                limpar()
                escolha = input(f"MEU DINHEIRO {meu_dinheiro}\n"
                                "\n"
                                "SELECIONE O QUE DESEJA VER:\n"
                                "[1]Periféricos [2]Casas [3]Carros [4]Sair\n"
                                "Digite uma opção: ")
                
                if escolha == "1":
                    ver_inventario(dados["perifericos"])
                elif escolha == "2":
                    ver_inventario(dados["casas"])
                elif escolha == "3":
                    ver_inventario(dados["carros"])
                elif escolha == "4":
                    break
                else:
                    limpar()
                    print('Digite uma das opções!')
                    time.sleep(2)
                    
    else:
        limpar()
        print('Digite uma das opções')
        time.sleep(2)
