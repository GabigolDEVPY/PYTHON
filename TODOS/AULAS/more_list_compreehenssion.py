import random

list4 = []

for num in range(10):
    num = random.randint(0, 10)
    list4.append(num * 2 if num % 2 == 0 else (num * 10))

print(list4)    



listaaa = [random.randint(1, 10) for num in range(10)]




# Lista original
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtra os números pares usando filter
lista_pares = list(filter(lambda num: num % 2 == 0, lista))

print(lista_pares)
