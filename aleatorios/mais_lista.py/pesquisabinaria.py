def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

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


lista = [1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 19]
alvo = 12
resultado = busca_binaria(lista, alvo)

print(resultado)