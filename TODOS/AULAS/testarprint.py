def triangulo(numero):
    for i in range(numero):
        estrelas = "*" * (2*i + 1)
        print(estrelas.center(2*numero - 1))

triangulo(9)        