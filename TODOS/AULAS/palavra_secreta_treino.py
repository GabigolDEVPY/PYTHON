palavra_secreta = "Navio"
letras_acertadas = set()
tentativas = 0

while True:
    letra = input('Digite uma letra: ')
    if letra in palavra_secreta:
        letras_acertadas.add(letra)
    
    palavra_formada = ''

    for i in palavra_secreta:
        if i in letras_acertadas:
            palavra_formada += i
        else:
            palavra_formada += "*"

    print(palavra_formada)            
    
    if palavra_formada ==  palavra_secreta:
        print('Parabéns você ganhou!!')
        break

