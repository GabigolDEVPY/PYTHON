import os
import json
import random
import time
from shared import dados, lista, carregar_dados, salvar_dados

def dinheiros(meu_dinheiro, dinheiro_acumulado):
    print(f'Meu dinheiro: {meu_dinheiro}         Dinheiro Acumulado: {dinheiro_acumulado}')

def dinheiro_palavra():
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

