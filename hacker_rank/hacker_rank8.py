x = int(input())
y = int(input())
z = int(input())
n = int(input())

listas = []

for num in range(x):
    lista = []
    lista.append(num)
    for num in range(y):
        lista.append(num)
        for num in range(z):
            lista.append(num)
        listas.append(lista)        
print(listas)            