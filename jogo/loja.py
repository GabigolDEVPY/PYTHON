import os
import json
from shared import lista, meu_dinheiro, salvar_dinheiro


def iterar_lista(lista):
        for i, item in enumerate(lista):
            print(f'{i}: {item['Periférico']}       Valor: {item['valor']}')
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
    #     os.system('cls')
    #     listap = lista[3]
    #     for i, item in enumerate(listap):
    #         print(f'{i}: {item['Periférico']}       Valor: {item['valor']}')
    #         print()
    #         comprar = input('Qual item deseja comprar [indice] ?: ')

    elif opcao == '2':
        os.system('cls')
        listap = lista[1]
        for i, item in enumerate(listap):
            print(f'{i}: {item['Casa']}       Valor: {item['valor']}')
            print()
            comprar = input('Qual item deseja comprar [indice] ?: ')

    elif opcao == '3':
        os.system('cls')
        listap = lista[2]
        for i, item in enumerate(listap):
            print(f'{i}: {item['Carro']}       Valor: {item['Valor']}')
            print()
            comprar = input('Qual item deseja comprar [indice] ?: ')

    elif opcao == '4':
        os.system('cls')
        return

    else:
        print("Digite uma das opções acima!")
    

