import os

frase = input('Digite uma frase para saber qual letra aparece mais: ')

i = 0
letra_apareceu_mais = ''
quantidade_vezes_apareceu = 0

while i < len(frase):
    letra_atual = frase[i]
    i += 1

    letra_apareceu_mais_atual = frase.count(letra_atual)

    if quantidade_vezes_apareceu <= letra_apareceu_mais_atual:
        quantidade_vezes_apareceu = letra_apareceu_mais_atual
        letra_apareceu_mais = letra_atual 

os.system('cls')
print(f'A letra que apareceu mais foi {letra_apareceu_mais} que apareceu {quantidade_vezes_apareceu} vezes')

    