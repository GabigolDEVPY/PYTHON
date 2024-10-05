numero =  int(input("digite um número: "))
vezes = 0
numero_novo = numero
while numero_novo >0:
    numero_novo -= 2
    vezes += 1 

print(f'O {numero} foi subtráido {vezes} vezes')    