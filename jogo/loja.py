import os
import json
from shared import lista, meu_dinheiro, salvar_dinheiro, carregar_dinheiro, limpar


def iterar_lista(lista):
        limpar()
        for i, item in enumerate(lista):
            print(f'{i}: {item['item']}       Valor: {item['complemento']}')
            print()
        comprar = input('Qual item deseja comprar [indice] ?: ')

def lojaa():
    meu_dinheiro = carregar_dinheiro()
    print(f'Meu dinheiro: {meu_dinheiro}')
    opcao = input('[1] Periféricos [2] Casas [3] Carros [4] sair\n'
            'Digite uma das opcoes acima: ')
    if opcao == '4':
        return
    
    elif opcao == '1':
        iterar_lista(lista[3])

    elif opcao == '2':
        iterar_lista(lista[1])


    elif opcao == '3':
        iterar_lista(lista[2])

    elif opcao == '4':
        limpar()
        return

    else:
        print("Digite uma das opções acima!")
    

