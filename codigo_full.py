idade = int(input("digite sua idade: "))
idade_permitida = 18
login_permitido = 'gabriel'
senha_permitida = '12345678'
repeticoes = 0
operadores_permitidos = '+-/*'
operadoress = "1"



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
            print('Acesso bloqueado, você tentou mais de 5 vezes')
            break
if senha == senha_permitida:
    nome = input('Digite seu nome: ')
    peso = float(input("Digite seu peso em KG: "))
    altura = float(input('Digite sua altura: '))

def informacoes(nome, idade, peso, altura, tamanho):
    print(f"""seu nome é {nome} e sua idade é {idade} anos
        seu nome de trás pra frente é {nome[::-1]}
        seu nome tem {len(nome)} letras e seu nome começa com a letra {nome[0]}
        e termina com a letra {nome[-1]} e seu tamanho é {tamanho}
        """) 

if peso and altura:
    if peso <= 60 and altura <= 1.60:
        informacoes(nome, idade, peso, altura, "p")

    elif peso <= 70 and altura <= 1.70:
        informacoes(nome, idade, peso, altura, "M")

    elif peso <= 80 and altura <= 1.80:
        informacoes(nome, idade, peso, altura, "G")

    elif peso <= 90 and altura <= 1.90:
        informacoes(nome, idade, peso, altura, "GG")
    
    else:
        print('Não encontramos o seu tamanho')

texto = input('Digite um texto: ')

i = 0

while i < len(texto):
    print(f'{texto[i]}f')
    i += 1 

numero = int(input('Digite um número: '))

for num in range (numero):
    print(num)

numero1 = int(input('Digite um número: '))
numero2 = int(input('digite oturo número: '))

operador = input('Digite um operador desse "-+/*": ')

if operador not in operadores_permitidos:
    print('Operador não encontrado')
    operador = input('Digite o operador novamente: ')

if len(operador) > len(operadoress):
        operador = input('você digitou mais de um operador')
else:
    print("somando seu calculo")        

if operador == '+':
    print(numero1 + numero2)

elif operador == '-':
    print(numero1 - numero2)

elif operador == '*':
    print(numero1 * numero2)

elif operador == '/':
    print(numero1 / numero2)
else:
    print('Não encontramos a resposta, algo deu errado')


descobrir = input('Digite um texto: ').lower()


palavra = input('Digite a palavra que quer saber quantas vezes aparece no texto: ').lower()


palavra_apareceu_mais = descobrir.count(palavra)

print(f' a palavra que apareceu mais foi {palavra} que apareceu {palavra_apareceu_mais}X')





















