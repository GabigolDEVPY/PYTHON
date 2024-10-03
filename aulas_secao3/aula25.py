import os

palavra_secreta = 'gabriel'
letras_acertadas = ''
repeticoes = 0

while True:
        letra = input('Digite uma letra: ')
        repeticoes += 1
        if repeticoes >= 5:
            os.system('cls')
            print('seu número de tentativas se expirou, GAME OVER')
            tentar = input('Deseja tentar novamente?: ').lower().startswith('s')

            if tentar:
                repeticoes = 0
                os.system('cls')
                print('NOVA TENTATIVA POIS VOCÊ É BURRO')
                continue
            else:
                break

        if letra in palavra_secreta:
            letras_acertadas += letra
        palavra_formada = ''

        for i in palavra_secreta:
            if i in letras_acertadas:
                palavra_formada += i
            else:
                palavra_formada += '*'
        print(palavra_formada)

        if palavra_formada == palavra_secreta:
            os.system('cls')
            print('Você acertou a palavra secreta')
            break



