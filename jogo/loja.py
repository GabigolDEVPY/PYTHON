import os
import time
import json
from shared import lista, meu_dinheiro, salvar_dinheiro, carregar_dinheiro, limpar


def iterar_lista(lista, meu_dinheiro):
        limpar()
        while True:
            for i, item in enumerate(lista):
                print(f'{i}: {item['item']}       Valor: {item['complemento']}')
                print()
            comprar = input('Qual item deseja comprar [indice] [S]air ?: ')
            if comprar.isdigit():
                        comprar = int(comprar)
                        comprar_item = lista[comprar]["complemento"]
                        meu_dinheiro -= comprar_item
                        salvar_dinheiro(meu_dinheiro)
                        break
            elif comprar.isalpha():
                print('Saindo...')
                time.sleep(2)
                return
            else:
                print('Digite algo válido')
                time.sleep(3)



def lojaa():
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
        return

    else:
        print("Digite uma das opções acima!")
    



