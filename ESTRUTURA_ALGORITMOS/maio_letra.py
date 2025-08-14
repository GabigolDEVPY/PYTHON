palavra = str(input("Digite uma palavra: "))

mais_vezes = 0
letra_maior = None
for letra in palavra:
    vez = palavra.count(letra)
    if vez >= mais_vezes:
        letra_maior = letra
        mais_vezes = vez
print("A letra que apareceu mais foi", letra_maior, mais_vezes,"X")        