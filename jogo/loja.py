import os
import time
import json
from shared import dados, limpar, ver_inventario, salvar_dados, carregar_dados, lista

def iterar_lista(lista, meu_dinheiro):
        while True:
            limpar()
            for i, item in enumerate(lista):
                print(f'{i}: {item['item']}       Valor: {item['complemento']}')
                print()
            comprar = input('Qual item deseja comprar [indice] [S]air ?: ')
            if comprar.isdigit():
                        comprar = int(comprar)
                        comprar_item = lista[comprar]["complemento"]
                        if meu_dinheiro >= comprar_item:
                            meu_dinheiro -= comprar_item
                            comprar_item = int(lista[comprar]["complemento"])
                            dados_comprar_atual.append(lista[comprar])
                            print(dados)
                            time.sleep(3)
                        else:
                            limpar()
                            print('Dinheiro insuficiente')
                            time.sleep(3)
                            break
                        salvar_dados("meu_dinheiro", meu_dinheiro)
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
        meu_dinheiro = dados["meu_dinheiro"]
        print(f'Meu dinheiro: {meu_dinheiro}')
        opcao = input('[1]Sair___[2]Comprar___[3]Vender')
        if opcao == '1':
            break
        elif opcao == '2':
            salvar_dados()
            limpar()
            opcao = input('[1]Periféricos___[2]Casas___[3]Carros___[4]sair\n'
                    'Digite uma das opcoes acima: ')
            if opcao == '4':
                return
            
            elif opcao == '1':
                global dados_comprar_atual
                dados_comprar_atual = dados["perifericos"]
                iterar_lista(lista[3], meu_dinheiro)

            elif opcao == '2':
                iterar_lista(lista[1], meu_dinheiro)


            elif opcao == '3':
                iterar_lista(lista[2], meu_dinheiro)

            else:
                print("Digite uma das opções acima!")
        elif opcao == "3":
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
    


