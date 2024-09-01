palavra_secreta = 'gabriel'
tentativas = 0
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    print(palavra_formada)        












