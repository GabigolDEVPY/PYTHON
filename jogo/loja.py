import os
import time
import json
from shared import dados, limpar, ver_inventario, salvar_dados, carregar_dados, lista

def vender(itens):
        if len(itens) == 0:
            limpar()
            print(f"SEU INVENTÁRIO DE {dados_vender_atual.upper()} ESTÁ VAZIO")
            time.sleep(2)
            return
        limpar()
        print(f"MEU DINHEIRO: {meu_dinheiro}\n" 
            "\n"
            "INVENTÁRIO:")
        print()
        for i, item in enumerate(itens):
            print(f'{i+1}: {item["item"]}  Valor - {item["complemento"]}')
        print()
        item_vender = int(input('INFORME [NUMERO] DO ITEM QUE DESEJA VENDER [0]sair: ')) 
        if item_vender == 0:
            limpar()
            print('Saindo...')
            time.sleep(2)
            return
        if len(itens) > 1:
            dados["meu_dinheiro"] = meu_dinheiro + item["complemento"]
            item_vender - 1
            del dados[dados_vender_atual][item_vender]
            salvar_dados(dados)
            return
        dados["meu_dinheiro"] = meu_dinheiro + item["complemento"]
        del dados[dados_vender_atual][0]
        salvar_dados(dados)

def iterar_lista(lista, meu_dinheiro):
        while True:
            limpar()   
            print(f"MEU DINHEIRO {meu_dinheiro}\n" 
            "\n"
            "INVENTÁRIO:\n"
            "   ")

            for i, item in enumerate(lista):
                print(f'{i}: {item['item']}       Valor: {item['complemento']}')
                print()
            comprar = input('Qual item deseja comprar [indice] [S]air ?: ')
            if comprar.isdigit():
                        comprar = int(comprar)
                        comprar_item = lista[comprar]["complemento"]
                        print(comprar_item)
                        if meu_dinheiro >= comprar_item:
                            meu_dinheiro -= comprar_item
                            dados["meu_dinheiro"] = meu_dinheiro
                            dados[dados_comprar_atual].append(lista[comprar])
                            salvar_dados(dados)
                        else:
                            limpar()
                            print('Dinheiro insuficiente')
                            time.sleep(3)
                            break
                        break
            elif comprar.isalpha():
                limpar()
                print('Saindo...')
                time.sleep(2)
                break
            else:
                limpar()
                print('Digite algo válido')
                time.sleep(3)

def lojaa():
    while True:
        limpar()
        dados = carregar_dados()
        global meu_dinheiro
        meu_dinheiro = dados["meu_dinheiro"]
        print(f'Meu dinheiro: {meu_dinheiro}\n'
            "  ")
        opcao = input('[1]Sair___[2]Comprar___[3]Vender: ')
        if opcao == '1':
            break
        elif opcao == '2':
            salvar_dados(dados)
            limpar()
            opcao = input(f'Meu dinheiro: {meu_dinheiro}\n'
                        '\n'
                        "OQUE DESEJA COMPRAR:\n"
                '[1]Periféricos___[2]Casas___[3]Carros___[4]sair\n'
                    'Digite uma das opcoes acima: ')
            if opcao == '4':
                return
            
            elif opcao == '1':
                global dados_comprar_atual
                dados_comprar_atual = "perifericos"
                iterar_lista(lista[3], meu_dinheiro)

            elif opcao == '2':
                dados_comprar_atual = "casas"
                iterar_lista(lista[1], meu_dinheiro)


            elif opcao == '3':
                dados_comprar_atual = "carros"
                iterar_lista(lista[2], meu_dinheiro)

            else:
                print("Digite uma das opções acima!")
        elif opcao == "3":
                    while True:
                        dados = carregar_dados()
                        limpar()
                        escolha = input(f"Meu dinheiro: {meu_dinheiro}\n"
                            "\n"
                            "SELECIONE O QUE DESEJA VENDER:\n"
                            "[1]Periféricos [2]Casas [3]Carros [4]Sair\n"
                            "Digite uma opção: ")
                        
                        if escolha == "1":
                            global dados_vender_atual
                            dados_vender_atual = "perifericos"
                            vender(dados["perifericos"])
                        elif escolha == "2":
                            dados_vender_atual = "casas"
                            vender(dados["casas"])
                        elif escolha == "3":
                            dados_vender_atual = "carros"
                            vender(dados["carros"])
                        elif escolha == "4":
                            break
                        else:
                            limpar()
                            print('Digite uma das opções!')
                            time.sleep(2)
        else:
            limpar()
            print('Digite uma das opções')
            time.sleep(3)      


