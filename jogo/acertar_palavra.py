import os
import json
import random
import time
from shared import meu_dinheiro

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_PALAVRAS = os.path.join(BASE_DIR, 'lista_palavras.json')
lista_palavras = ARQUIVO_PALAVRAS

def dinheiros(dinheiro_acumulado, meu_dinheiro):
    print(f'Meu dinheiro: {meu_dinheiro}         Dinheiro Acumulado: {dinheiro_acumulado}')



def carregar_lista():
    try:
        with open(lista_palavras, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Tratar a exceção de arquivo não encontrado aqui
        pass

def dinheiro_palavra():
    dinheiro_acumulado = 0
    def palavrazerada():
        if len(letras_acertadas) == 0:
            dinheiros(dinheiro_acumulado, meu_dinheiro)
            print(palavra_e_dica["dica"])
            print()
            star = ''
            for letra in palavra_secreta:
                star += " _ "
            print(star)
        else:
            print(f'Dinheiro {dinheiro_acumulado}')
            print(palavra_e_dica["dica"])
            print()
            print(palavra_formada)

    while True:
        dinheiros(dinheiro_acumulado, meu_dinheiro)
        sair = input('Deseja sair? [S]im [N]ão: ')
        os.system('cls')
        if sair == 's':
            return dinheiro_acumulado
        #Neste código, carregar_lista() é chamado diretamente dentro da função random.choice(), e a dica é acessada imediatamente após selecionar a palavra. 
        palavra_e_dica = random.choice(carregar_lista()[0])
        letras_acertadas = ''
        tentativas = 0
        palavra_secreta = palavra_e_dica["palavra"].lower()
        while True:
            if tentativas == 0:
                palavrazerada()
            letra = input('Digite uma letra: ')
            tentativas += 1
            if len(letra) > 1:
                os.system('cls')
                palavrazerada()
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
            print(f'Dinheiro {dinheiro_acumulado}')
            print(palavra_e_dica["dica"])
            print()         
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

