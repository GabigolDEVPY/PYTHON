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
                print(f'Seu nome Ã© {nome} e sua idade Ã© {idade}')
                print(f'seu nome tem len{nome} letras')
                print(f'Seu nome de trÃ¡s pra frente Ã© {nome[::-1]}')
                print(f'a primeira letra do seu nome Ã© {nome[0]}') 
                print(f'e a Ãºltima letra do seu nome Ã© {nome[-1]}')
                print('VocÃª veste tamanho P') 
            elif altura <= 1.70 and peso <= 70:
                print(f'Seu nome Ã© {nome} e sua idade Ã© {idade}')
                print(f'seu nome tem len{nome} letras')
                print(f'Seu nome de trÃ¡s pra frente Ã© {nome[::-1]}')
                print(f'a primeira letra do seu nome Ã© {nome[0]}') 
                print(f'e a Ãºltima letra do seu nome Ã© {nome[-1]}')
                print('VocÃª veste tamanho M')
                
            elif altura <= 1.80 and peso <= 80:
                print(f'Seu nome Ã© {nome} e sua idade Ã© {idade}')
                print(f'seu nome tem len{nome} letras')
                print(f'Seu nome de trÃ¡s pra frente Ã© {nome[::-1]}')
                print(f'a primeira letra do seu nome Ã© {nome[0]}') 
                print(f'e a Ãºltima letra do seu nome Ã© {nome[-1]}')
                print('VocÃª veste tamanho g')
            elif altura <= 1.90 and peso <= 90:
                print(f'Seu nome Ã© {nome} e sua idade Ã© {idade}')
                print(f'seu nome tem len{nome} letras')
                print(f'Seu nome de trÃ¡s pra frente Ã© {nome[::-1]}')
                print(f'a primeira letra do seu nome Ã© {nome[0]}') 
                print(f'e a Ãºltima letra do seu nome Ã© {nome[-1]}')
                print('VocÃª veste tamanho gg')
            else:
                print('NÃ£o encontramos seu tamanho')
        else:
            print('Login e senha nÃ£o permitidos')        
    else:
        print('Sua idade nÃ£o Ã© permitida')                
else:
    print('VocÃª nÃ£o digitou seu nome e idade')
