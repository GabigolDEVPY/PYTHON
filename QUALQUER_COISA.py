frase = input('digite uma frase: ')

i = 0
letra_apareceu_mais = ''
vezes_apareceu = 0

while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1 
        continue 

    vezes_apareceu_mais_atualmente = frase.count(letra_atual)

    if vezes_apareceu < vezes_apareceu_mais_atualmente:
        vezes_apareceu = vezes_apareceu_mais_atualmente
        letra_apareceu_mais = letra_atual
    i += 1

print(f' a letra que apareceu mais vezes foi {letra_apareceu_mais} que apareceu {vezes_apareceu} vezes')    

