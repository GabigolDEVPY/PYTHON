def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) -1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        elif chute < item:
            baixo = meio + 1
        else:
            alto = meio - 1    
    return None


lista = [1, 4, 7, 8, 12, 56, 78, 122, 144, 155, 166, 178]
alvo  = 144
indice = busca_binaria(lista, alvo)
print(indice)