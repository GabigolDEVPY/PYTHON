import os
import time

def limpar():
    os.system('cls')
def descansar():
    time.sleep(3)

clientes = []

def adiciona_cliente():
    nome = input('Digite o nome do cliente: ')
    CPF = input('Digite o CPF do cliente: ')
    if len(CPF) < 11 or len(CPF) > 11:
        print('CPF não coném 11 dígitos')
        descansar()
        return
    CPF.isdigit
    if CPF is True:
        idade = input('Digite a idade do cliente: ')
        cliente = {
            "nome": nome,
            "CPF": CPF,
            "idade": idade
        }
        for pessoa in clientes:
            if cliente["CPF"] == pessoa["CPF"]:
                print('Esse cliente já existe na lista')
                descansar()
                return
        clientes.append(cliente)
    print('CPF inválido')
    descansar()




def buscar():
    busca = input('Qual cliente deseja consultar?: ')
    for cliente in clientes:
        if cliente["nome"].lower() == busca.lower():
            print('Cliente encontrado!!')
            print()
            print(
                f'Nome: {cliente["nome"]}\n'
                f'CPF: {cliente["CPF"]}\n'
                f'idade: {cliente["idade"]}\n'
                )
            descansar()
            return
        print('Cliente não existe na lista!')
        descansar()

def listar():
    if len(clientes) == 0:
        print('Não há clientes na lista')
        descansar()
    for i, cliente in enumerate(clientes):
        print(f'{i+1}. {cliente["nome"]}')
        continuar = input("press SPACE to continue...")    


def opcao():
    while True:
        limpar()
        print('[1]Listar [2]Adicionar Cliente [3]Buscar Cliente [4]sair')
        opp = input('Selecione uma opção!: ')
        
        if opp == '2':
            limpar()
            adiciona_cliente()
        elif opp == '3':
            limpar()
            buscar()
        elif opp == '1':
            limpar()
            listar()
        elif opp == '4':
            limpar()
            break    
        else:
            print('Digite apenas umas das opções listadas!')
            descansar()

opcao()
    

