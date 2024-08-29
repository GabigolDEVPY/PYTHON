frase = 'Somos nós'
i = 0

letra_apareceu_mais = ''
vezes_apareceu = 0

while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1 
        continue

    quantidade_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if vezes_apareceu < quantidade_apareceu_mais_vezes_atual:
        vezes_apareceu = quantidade_apareceu_mais_vezes_atual
        letra_apareceu_mais = letra_atual

    i += 1 

print(f'''A letra que apareceu mais vezes foi
    {letra_apareceu_mais} que apareceu {vezes_apareceu}x
''')




