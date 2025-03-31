def calcular_fatorial(numero):
    if numero < 0:
        print('Fatorial indisponível para números negativos')
    if numero == 0 or numero == 1:
        return 1    
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial    

numero = int(input('Digite um número: '))
resultado = calcular_fatorial(numero)

print(f'O fatorial de {numero} é {resultado}')


