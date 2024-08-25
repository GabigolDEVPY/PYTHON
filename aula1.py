# Entrada de dados do usuário
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
login = input('Digite seu login: ').lower()
senha = input('Digite sua senha: ')
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em KG: '))

# Definindo critérios permitidos
idade_permitida = 18
login_permitido = 'gabriel'
senha_permitida = '12345678'

# Função para exibir informações do usuário e tamanho da roupa
def exibir_informacoes(nome, idade, altura, peso, tamanho):
    print(f"""
    Seu nome é {nome} e sua idade é {idade}
    Seu nome tem {len(nome)} letras
    Seu nome de trás pra frente é {nome[::-1]}
    A primeira letra do seu nome é {nome[0]}
    A última letra do seu nome é {nome[-1]}
    Você veste tamanho {tamanho}
    """)

# Verificações de login, senha e idade
if nome and idade:
    if idade >= idade_permitida:
        if login == login_permitido and senha == senha_permitida:
            if altura <= 1.60 and peso <= 60:
                exibir_informacoes(nome, idade, altura, peso, 'P')
            elif altura <= 1.70 and peso <= 70:
                exibir_informacoes(nome, idade, altura, peso, 'M')
            elif altura <= 1.80 and peso <= 80:
                exibir_informacoes(nome, idade, altura, peso, 'G')
            elif altura <= 1.90 and peso <= 90:
                exibir_informacoes(nome, idade, altura, peso, 'GG')
            else:
                print('Não encontramos seu tamanho')
        else:
            print('Login ou senha não permitidos')
    else:
        print('Sua idade não é permitida')
else:
    print('Você não digitou seu nome ou idade')
