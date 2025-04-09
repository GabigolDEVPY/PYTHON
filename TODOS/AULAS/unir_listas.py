lista1 = ["Salvador", "Ubatuba", "Belo Horizonte"]
lista2 = ["BA", "SP", "MG", "RJ"]

lista_nova = []
indice = 0
for capital in lista1:
    lista_nova.append((capital, lista2[indice]))
    indice += 1
print(lista_nova)