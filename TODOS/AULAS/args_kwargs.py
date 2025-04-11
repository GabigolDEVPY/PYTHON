dados = {'nome': 'Gabriel', 'idade': 25}

def saudacao(nome, idade):
    print(f"Hello, {nome}! You have {idade} years.")
    
    
saudacao(**dados)    

dados = {'nome': 'Gabriel', 'idade': 25}

# Desempacotando os itens de um dicionário
novo_dados = {**dados, 'cidade': 'São Paulo'}
print(novo_dados)


def soma(*args):
    return sum(args)

# Passando vários argumentos
resultado = soma(1, 2, 3, 4, 5)
print(resultado)


def exibir_pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Passando argumentos nomeados
exibir_pessoa(nome="Gabriel", idade=25, cidade="São Paulo")



def apresentar(nome, *args, **kwargs):
    print(f"Nome: {nome}")
    print("Outros argumentos:", args)
    print("Argumentos nomeados:", kwargs)

# Passando argumentos posicionais e nomeados
apresentar("Gabriel", 25, "São Paulo", ocupacao="Programador", hobby="Jogar videogame")

def cadastrar_usuario(*args, **kwargs):
    print("Dados do usuário:")
    print(f"Nome: {args[0]}")  # O primeiro argumento posicional será o nome
    print(f"Idade: {args[1]}")  # O segundo argumento posicional será a idade
    
    # Usando kwargs para acessar dados nomeados
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Empacotando os dados em um dicionário e usando *args para dados posicionais
dados_usuario = {'endereco': 'Rua 123', 'email': 'gabriel@exemplo.com'}

cadastrar_usuario("Gabriel", 25, **dados_usuario)


# todos os exemplos de args e Kwargs