while True:
    palavra = str(input("Digite uma palavra"))
    letra_apareceu_mais = ""
    vezes = 0

    for letra in palavra:
        mais = palavra.count(letra)
        if mais > vezes:
            letra_apareceu_mais = letra
            vezes = mais

    print(f"letra_apareceu_mais foi {letra_apareceu_mais} que apareceu {vezes}X")    


