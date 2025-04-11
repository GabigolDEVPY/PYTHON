import os

palavra_secreta = "shampoo"
letras_acertadas = ''
tentativas = 0

while True:
    letra = input('Digite uma letra: ')
    tentativas += 1
    letra_digito = letra.isalpha()
    if letra_digito:
        if len(letra) > 1:
            os.system('cls')
            print('Digite apenas uma letra!!')
            continue

        palavra_formada = ''

        for i in palavra_secreta:
            if i == letra:
                letras_acertadas += i
        
        for let in palavra_secreta:
            if let in letras_acertadas:
                palavra_formada += let
            else:
                palavra_formada += "0"
        os.system('cls')         
        print(palavra_formada)        
    else:
        os.system('cls')
        print('Digite apenas letras')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(
            'Você acertou a palavra secreta\n'
            f'A palavra era {palavra_secreta}\n'
            f'Você teve {tentativas} tentativas'
            )
        break 



