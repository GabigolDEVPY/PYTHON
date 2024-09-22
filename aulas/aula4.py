senha_salva = '1234'
repeticoes = 1
senha = input('Digite a senha: ')


while senha != senha_salva:
    senha = input(f'Digite sua senha novamente, sua senha já foi digitada ({repeticoes}X): ')
    repeticoes += 1

    if repeticoes > 5:
        print('Acesso negado')
        break

print(repeticoes)


12