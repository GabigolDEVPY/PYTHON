idade = int(input("digite sua idade: "))
idade_permitida = 18
login_permitido = 'gabriel'
senha_permitida = '12345678'
repeticoes = 0
operadores_permitidos = '+-/*'

if idade >= idade_permitida:
    login = input('Digite seu login: ').lower()

    while login_permitido != login:
        login = input('Digite seu login novamente: ').lower()
        repeticoes += 1
        if repeticoes >= 5:
            print('Acesso bloqueado')
            break
if login == login_permitido:
    repeticoes = 0
    senha = input('Digite sua senha: ')
    while senha != senha_permitida:
        senha = input('Digite sua senha novamente: ')
        repeticoes += 1
        if repeticoes >= 5:
            print('Acesso bloqueado')
            break














