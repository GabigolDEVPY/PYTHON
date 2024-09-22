idade = int(input('Digite sua idade: '))
idade_permitida = 18

def informacoes(nome, idade, peso, altura, tamanho):
    print(f'''Seu nome é {nome} e seu nome de trás pra frente é {nome[::-1]} 
        seu nome tem {len(nome)} letras, a primeira letra do seu nome é {nome[0]}
        e a última letra do seu nome é {nome[-1]}
        sua idade é {idade} 
        e seu tamanho é {tamanho}
        ''')

if idade >= idade_permitida:
    login = input('Digite seu login: ').lower()
    senha = input('Digite sua senha: ')

    login_permitido = 'gabriel'
    senha_permitida = '12345678'

    if login == login_permitido and senha == senha_permitida:
        nome = input('Digite seu nome: ')
        altura = float(input('Digite sua altura: '))
        peso = float(input('Digite seu peso em KG: '))

        if altura and peso:
            if altura <= 1.60 and peso <= 60:
                informacoes(nome, idade, peso, altura, 'P')

            elif altura <= 1.70 and peso <= 70:
                informacoes(nome, idade, peso, altura, 'M')

            elif altura <= 1.80 and peso <= 80:
                informacoes(nome, idade, peso, altura, 'G')

            elif altura <= 1.90 and peso <= 90:
                informacoes(nome, idade, peso, altura, 'GG')

        else:
            print('não encontramos seu tamanho')        
    else:
        print('Login não permitido')
else:
    print('Sua idade não é permitida')
