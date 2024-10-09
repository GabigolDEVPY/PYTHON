soma = 0
quantidade = 0

while True:
        peso = input('Ddigite [sair] se o número de pesos tá ok ou de Informe o peso: ')
        if peso.lower() == 'sair':
                if quantidade >1:
                    media = soma / quantidade
                    print(f'A média dos pesos é {media:.2f}')
                    break


        try:
            peso = float(peso)
            soma += peso
            quantidade += 1
            print(f'Quantidade peso atualmente {soma}')

        except Exception:
            print('Digite um número válido')     #soma
             