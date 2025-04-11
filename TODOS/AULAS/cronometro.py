import os 
import time

numero = int(input('Quantos segundos deseja ?: '))

for i in range(numero):
    if numero == 1:
        os.system('cls')
        print(f'Fechando programa em {numero} segundo')
        time.sleep(1)
        break
    os.system('cls')    
    print(f"fechando o programa em {numero} segundos")
    time.sleep(1)
    numero -= 1

