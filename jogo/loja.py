import os
import json
from shared import lista, meu_dinheiro, salvar_dinheiro


def iterar_lista(lista):
        os.system('cls')
        for i, item in enumerate(lista):
            print(f'{i}: {item['item']}       Valor: {item['complemento']}')
            print()
        comprar = input('Qual item deseja comprar [indice] ?: ')

def lojaa():
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
        os.system('cls')
        return

    else:
        print("Digite uma das opções acima!")
    

