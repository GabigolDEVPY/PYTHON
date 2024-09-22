lista = ['salame', 'queijo', 'torta', 'presunto']

nova_lista = []

for i, elemento in enumerate(lista):
    nova_lista += (i, elemento)
    print(i, elemento)
print(nova_lista)
