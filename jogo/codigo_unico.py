import os
import json
import time
import random


BASE_DIR = os.path.dirname(os.path.abspath(__file__))           #
DADOS = os.path.join(BASE_DIR, 'dados.json')                    #
ARQUIVO_PALAVRAS = os.path.join(BASE_DIR, 'lista_palavras.json')# 
                                                                #
# Função para carregar a lista de palavras                       #
def carregar_lista():                                              #
    try:                                                             #
        with open(ARQUIVO_PALAVRAS, 'r', encoding="utf-8") as f:    #
            return json.load(f)                                     #
    except FileNotFoundError:                                        # 
        return []  # Retorna uma lista vazia se o arquivo não existir  #
                                                                        #
# Função para limpar a tela                                            #
def limpar():
    os.system('cls')

lista = carregar_lista()

# Função para carregar dados do arquivo JSON
def carregar_dados():
    try:
        with open(DADOS, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existir ou estiver corrompido, retorna o dicionário padrão
        return {"meu_dinheiro": 0, "carros": [], "casas": [], "perifericos": []}


def salvar_dados(dados):   
    with open(DADOS, 'w') as f:
        json.dump(dados, f, indent=4) 


dados = carregar_dados()

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
                        print(comprar_item)
                        if meu_dinheiro >= comprar_item:
                            meu_dinheiro -= comprar_item
                            dados["meu_dinheiro"] = meu_dinheiro
                            dados[dados_comprar_atual].append(lista[comprar])
                            salvar_dados(dados)
                        else:
                            limpar()
                            print('Dinheiro insuficiente')
                            time.sleep(3)
                            break
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
        opcao = input('[1]Sair___[2]Comprar___[3]Vender: ')
        if opcao == '1':
            break
        elif opcao == '2':
            salvar_dados(dados)
            limpar()
            opcao = input('[1]Periféricos___[2]Casas___[3]Carros___[4]Inventário [5]sair\n'
                    'Digite uma das opcoes acima: ')
            if opcao == '5':
                return
            
            elif opcao == '1':
                global dados_comprar_atual
                dados_comprar_atual = "perifericos"
                iterar_lista(lista[3], meu_dinheiro)

            elif opcao == '2':
                dados_comprar_atual = "casas"
                iterar_lista(lista[1], meu_dinheiro)


            elif opcao == '3':
                dados_comprar_atual = "carros"
                iterar_lista(lista[2], meu_dinheiro)


            else:
                print("Digite uma das opções acima!")
        elif opcao == "4":
                    limpar()
                    escolha = input("SELECIONE O QUE DESEJA VER:\n"
                        "[1]Periféricos [2]Casas [3]Carros [4]Sair\n"
                        "Digite uma opção: ")
                    
                    if escolha == "1":
                        ver_inventario(dados["perifericos"])
                    elif escolha == "2":
                        ver_inventario(dados["casas"])
                    elif escolha == "3":
                        ver_inventario(dados["carros"])
                    elif escolha == "4":
                        break    
                    else:
                        print('Opção inválida!')
    
        else:
            print('Digite uma das opções') 

def dinheiro_palavra():
    def dinheiros(meu_dinheiro, dinheiro_acumulado):
        print(f'Meu dinheiro: {meu_dinheiro}         Dinheiro Acumulado: {dinheiro_acumulado}')
    dinheiro_acumulado = 0
    
    while True:
        meu_dinheiro = dados["meu_dinheiro"]
        dinheiros(meu_dinheiro, dinheiro_acumulado)
        sair = input('Deseja sair? [S]im [N]ão: ')
        os.system('cls')
        if sair.lower() == 's':
            dados["meu_dinheiro"] = meu_dinheiro + dinheiro_acumulado
            salvar_dados(dados)  # Salva o dinheiro acumulado ao sair
            break
        
        palavra_e_dica = random.choice(lista[0])
        letras_acertadas = ''
        tentativas = 0
        palavra_secreta = palavra_e_dica["complemento"].lower()

        while True:
            if tentativas == 0:
                print(palavra_e_dica["item"])
                print("Palavra: " + " _ " * len(palavra_secreta))  # Exibe a palavra como traços
            letra = input('Digite uma letra: ')
            tentativas += 1
            
            if len(letra) > 1:
                os.system('cls')
                print('Digite apenas uma letra!!')
                continue

            palavra_formada = ''

            for i in palavra_secreta:
                if i == letra:
                    letras_acertadas += i
            
            for let in palavra_secreta:
                if let in letras_acertadas:
                    palavra_formada += let
                else:
                    palavra_formada += " _ "
                    
            os.system('cls')
            dinheiros(meu_dinheiro, dinheiro_acumulado)
            print(palavra_e_dica["item"])         
            print(palavra_formada)        

            if palavra_formada == palavra_secreta:
                dinheiro_acumulado += 10000
                os.system('cls')
                print(
                    'Você acertou a palavra secreta\n'
                    f'A palavra era {palavra_secreta}\n'
                    f'Você teve {tentativas} tentativas'
                )
                time.sleep(2)
                os.system('cls')
                break        

def ver_inventario(itens):
    limpar()
    print("INVENTÁRIO")
    print()
    for i, item in enumerate(itens):
        print(f'{i}: {item["item"]}  Valor - {item["complemento"]}')
    print()
    continuar = input('[ENTER] para continuar')

while True:
    dados = carregar_dados()
    limpar()
    meu_dinheiro = dados["meu_dinheiro"]
    option = input(
        f"Saldo na conta: {meu_dinheiro}\n"
        "[1]Forca___[2]Inventário___[3]Loja___[4]sair\n"
        "Digite uma opção!: "
    )

    if option == "1":
        limpar()
        dinheiro_palavra()  # Recebe o dinheiro ganho do jogo

    elif option == "4":
        limpar()
        break

    elif option == "3":
        limpar()
        lojaa()
    
    elif option == "2":
            while True:
                limpar()
                escolha = input('SELECIONE O QUE DESEJA VER:\n'
                                "[1]Periféricos [2]Casas [3]Carros [4]Sair\n"
                                "Digite uma opção: ")
                
                if escolha == "1":
                    ver_inventario(dados["perifericos"])
                elif escolha == "2":
                    ver_inventario(dados["casas"])
                elif escolha == "3":
                    ver_inventario(dados["carros"])
                elif escolha == "4":
                    break


                else:
                    limpar()
                    print('Digite uma das opções!')
                    time.sleep(2)
    else:
        limpar()
        print('Digite uma das opções')
        time.sleep(2)