import os
import time
import json
from shared import lista, meu_dinheiro, salvar_dinheiro, carregar_dinheiro, limpar


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
                        else:
                            limpar()
                            print('Dinheiro insuficiente')
                            time.sleep(3)
                            break
                        salvar_dinheiro(meu_dinheiro)
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
        meu_dinheiro = carregar_dinheiro()
        print(f'Meu dinheiro: {meu_dinheiro}')
        opcao = input('[1] Periféricos [2] Casas [3] Carros [4] sair\n'
                'Digite uma das opcoes acima: ')
        if opcao == '4':
            return
        
        elif opcao == '1':
            iterar_lista(lista[3], meu_dinheiro)

        elif opcao == '2':
            iterar_lista(lista[1], meu_dinheiro)


        elif opcao == '3':
            iterar_lista(lista[2], meu_dinheiro)

        elif opcao == '4':
            limpar()
            break

        else:
            print("Digite uma das opções acima!")
    



