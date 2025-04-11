numero = int(input('Digite um número inteiro:'))

vezes = 0
while True:
    if numero >= 0:
        numero -= 2
        vezes += 1 
    else:
        break

print(f'O número de vezes que foi subtraído o valor 2 foi {vezes}')

