import os #lista versão um 

lista = []

while True:
    print('Escolha uma opção abaixo')
    opcao = input('[S]air [L]istar [I]nserir [A]pagar: ').lower()
    if opcao == 's':
        break

    elif opcao == 'i':
        valor = input('Digite um intem para adicionar a lista: ')
        lista.append(valor)
        os.system('cls')

    elif opcao == 'l':
        if len(lista) < 1:
            print('Não a nada para listar')
        else:
            for i, item in enumerate(lista):
                print(i, item)    
            
    elif opcao == 'a':
        indice = input('Qual indice deseja apagar?: ')

        try:
            indice_int = int(indice)
            del lista[indice_int]
        except ValueError:
            print('Digite apenas int.')
        except IndexError:
            print('Esse indice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')                 