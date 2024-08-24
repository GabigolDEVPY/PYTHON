nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
login = input('Digite seu login: ').lower()
senha = input('Digite sua senha: ')
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em KG: '))


idade_permitida = 18
senha_permitida = 12345678
login_permitido = 'gabriel'

if nome and idade:
    if idade >= idade_permitida:
        if login == login_permitido and idade == idade_permitida:
            if altura <= 1.60 and peso <= 60:
                print(f'Seu nome é {nome} e sua idade é {idade}')
                print(f'seu nome tem len{nome} letras')
                print(f'Seu nome de trás pra frente é {nome[::-1]}')
                print(f'a primeira letra do seu nome é {nome[0]}') 
                print(f'e a última letra do seu nome é {nome[-1]}')
                print('Você veste tamanho P') 
            elif altura <= 1.70 and peso <= 70:
                print(f'Seu nome é {nome} e sua idade é {idade}')
                print(f'seu nome tem len{nome} letras')
                print(f'Seu nome de trás pra frente é {nome[::-1]}')
                print(f'a primeira letra do seu nome é {nome[0]}') 
                print(f'e a última letra do seu nome é {nome[-1]}')
                print('Você veste tamanho M')
                
            elif altura <= 1.80 and peso <= 80:
                print(f'Seu nome é {nome} e sua idade é {idade}')
                print(f'seu nome tem len{nome} letras')
                print(f'Seu nome de trás pra frente é {nome[::-1]}')
                print(f'a primeira letra do seu nome é {nome[0]}') 
                print(f'e a última letra do seu nome é {nome[-1]}')
                print('Você veste tamanho g')
            
            elif altura <= 1.90 and peso <= 90:
                print(f'Seu nome é {nome} e sua idade é {idade}')
                print(f'seu nome tem len{nome} letras')
                print(f'Seu nome de trás pra frente é {nome[::-1]}')
                print(f'a primeira letra do seu nome é {nome[0]}') 
                print(f'e a última letra do seu nome é {nome[-1]}')
                print('Você veste tamanho gg')
            else:
                print('Não encontramos seu tamanho')
        else:
            print('Login e senha não permitidos')        
    else:
        print('Sua idade não é permitida')                
else:
    print('Você não digitou seu nome e idade')









