import os
import time
import json
from functions import validador, validnome, idadevalid

# Obter o caminho absoluto para o arquivo clientes.json na mesma pasta do script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_CLIENTES = os.path.join(BASE_DIR, 'clientes.json')

def limpar():
    os.system('cls')
def descansar():
    time.sleep(3)

# Função para salvar a lista de clientes em um arquivo JSON
def salvar_clientes():
    with open(ARQUIVO_CLIENTES, 'w') as f:
        json.dump(clientes, f)

# Função para carregar a lista de clientes do arquivo JSON
def carregar_clientes():
    try:
        with open(ARQUIVO_CLIENTES, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return [] # Retorna uma lista vazia se o arquivo não existir ou estiver vazio/corrompido

clientes = carregar_clientes()

def excluir():
    while True:
        if len(clientes) <1:
            limpar()
            print('Não há clientes na lista!')
            descansar()
            break
        ID = input('Digite o ID do cliente que deseja excluir:')
        for cliente in clientes:
            if ID in cliente["CPF"]:
                del clientes[cliente]
                break
            else:
                print('ID inválido')
                    


def adiciona_cliente():
    nome = validnome()
    limpar()
    CPF = validador()
    for cliente in clientes:
        if cliente["CPF"] == CPF:
            print('Esse cliente já existe na lista')
            descansar()
            return    
    idade = idadevalid()

    cliente = {
        "nome": nome,
        "CPF": CPF,
        "idade": idade
    }
    clientes.append(cliente)
    limpar()
    print(f'Cliente {cliente["nome"]} foi cadastrado')
    descansar()


def buscar():
    while True:
        if len(clientes) <1:
            limpar()
            print("Não há clientes nas lista")
            descansar()
            break
        busca = input('Qual cliente deseja consultar[ID]?: ')
        for cliente in clientes:
            if busca in cliente["CPF"]:
                print('Cliente encontrado!!')
                print()
                print(
                    f'Nome: {cliente["nome"]}\n'
                    f'CPF: {cliente["CPF"]}\n'
                    f'idade: {cliente["idade"]}\n'
                    )
                conttt = input('[ENTER] para continuar...')
                return
            print('Cliente não existe na lista!')
            descansar()

def listar():
    if clientes == '' or len(clientes) == 0:
        print('Não há clientes na lista')
        descansar()
    for i, cliente in enumerate(clientes):
        clientecpf = cliente["CPF"]
        print(f'{i+1}. {cliente["nome"]} ID:{clientecpf[:5]}') 
        continuar = input("press [ENTER] to continue...")    


def opcao():
    while True:
        limpar()
        print('[1]Listar  [2]Adicionar Cliente  [3]Buscar Cliente  [4]Excluir Cliente  [5]sair')
        opp = input('Selecione uma opção!: ')
        
        if opp == '2':
            limpar()
            adiciona_cliente()
            salvar_clientes()
        elif opp == '3':
            limpar()
            buscar()
        elif opp == '1':
            limpar()
            listar()
        elif opp == '5':
            salvar_clientes()
            limpar()
            break 
        elif opp == '4':
            excluir()
            salvar_clientes()   
        else:
            print('Digite apenas umas das opções listadas!')
            descansar()

opcao()
    

