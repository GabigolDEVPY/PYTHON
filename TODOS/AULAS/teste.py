import time
import os

def tempo():
    print('Aguarde 3 segundos')
    time.sleep(3)



def limpar():
    os.system('cls')
    
lista = []


while True:
    if len(lista) == 1:
        print(
        f'Sua lista tem atualmente, {len(lista)} ITEM\n'
        'Digite uma das opções abaixo para adicionar items a lista'
        )
    else:
        print(
        f'Sua lista tem atualmente, {len(lista)} ITENS\n'
        'Digite uma das opções abaixo para adicionar items a lista'
        )   

    opcao = input('[L]istar [A]pagar [I]nserir: ').lower()
    limpar()
    if opcao.isalpha():
        if opcao == 'a':
            if len(lista) <=0 or lista == []:
                limpar()
                print('Sem itens para apagar')
                tempo()
                os.system('cls')
                continue
            for i, item in enumerate(lista):
                print(i, item)
            apagar = input('Qual índice deseja apagar ?')
            try:
                apagar_int = int(apagar)
                del lista[apagar_int]
                limpar()
                print('O Item foi APAGADO da lista.')
                tempo()
                limpar()
            except ValueError:
                limpar()
                print('Digite apenas números!')
                tempo()
                limpar()
            except IndexError:
                limpar()
                print('Esse item não existe na lista!')
                tempo()
                limpar()
            except Exception:
                limpar()
                print('Um erro inesperado aconteceu!')
                tempo()
                limpar()    


        if opcao == 'i':
            for i, item in enumerate(lista):
                print(i, item)
                
            item = input('Adicionar item: ')
            if item in lista:
                limpar()
                print('WARNING!!! Item já existe na lista')
                tempo()
                limpar()
                continue

            if item.isalpha():
                lista.append(item)
                limpar()
                print('O item foi adicionado na lista!')
                tempo()
                limpar() 
            else:
                limpar()
                print('Apenas letras')
                tempo()
                limpar()
                continue        
            
        if opcao == 'l':
            limpar()
            print()
            print('ITENS NA LISTA:')
            print()
            if len(lista) <=0 or lista == []:
                limpar()
                print('Nada para listar!')
                tempo()
                limpar()
            for i, item in enumerate(lista):
                print(i, item)
        print()                   
    else:
        limpar()
        print('Não digite simbolos nem números, apenas A, B ou C')
        tempo()


