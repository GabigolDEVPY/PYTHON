import random
import time
import os

lista = []

def adiciona():
    for vez in range(vezes):
        pessoa = input('Digite o nome da pessoa que deseja colocar na lista: ')
        lista.append(pessoa)


vezes = int(input("quantas pessoas deseja adicionar na lista ?: "))

adiciona()
lista.sort()
pessoa_aleatoria = random.choice(lista)
print(lista)

print("Pessoa aleatoria em 3")
time.sleep(1)
print("Pessoa aleatoria em 2")
time.sleep(1)
print("Pessoa aleatoria em 1")
time.sleep(1)
os.system('cls')

if pessoa_aleatoria == " " or pessoa_aleatoria == '':
    print('A pessoa aleatória é inválida')
else:
    print(f'A pessoa aleatória é {pessoa_aleatoria}')






tempo = int(input('Tempo do temporizador: '))

for segundo in range(tempo):
    if tempo == 1:
        os.system('cls')
        print(f'Fechando programa em {tempo} segundo')
        time.sleep(1)
        break
    os.system('cls')
    print(f'Fechando programa em {tempo} segundos')
    tempo -= 1
    time.sleep(1)


