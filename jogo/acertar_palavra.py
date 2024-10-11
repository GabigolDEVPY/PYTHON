import os
import json
import random
import time
from shared import meu_dinheiro, salvar_dinheiro  # Usa a variável correta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_PALAVRAS = os.path.join(BASE_DIR, 'lista_palavras.json')

def dinheiros(dinheiro_acumulado):
    print(f'Meu dinheiro: {meu_dinheiro}         Dinheiro Acumulado: {dinheiro_acumulado}')

def carregar_lista():
    try:
        with open(ARQUIVO_PALAVRAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        pass

def dinheiro_palavra():
    dinheiro_acumulado = 0

    while True:
        dinheiros(dinheiro_acumulado)
        sair = input('Deseja sair? [S]im [N]ão: ')
        os.system('cls')
        if sair.lower() == 's':
            salvar_dinheiro(meu_dinheiro + dinheiro_acumulado)  # Salva o dinheiro acumulado ao sair
            return dinheiro_acumulado
        
        palavra_e_dica = random.choice(carregar_lista()[0])
        letras_acertadas = ''
        tentativas = 0
        palavra_secreta = palavra_e_dica["palavra"].lower()

        while True:
            if tentativas == 0:
                print(palavra_e_dica["dica"])
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
            dinheiros(dinheiro_acumulado)
            print(palavra_e_dica["dica"])         
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
