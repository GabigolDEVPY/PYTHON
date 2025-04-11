# Básico


# Desempacotar um dicionário e passar como argumentos para uma função

dados = {"nome": "Moranguinha", "idade": 18}

def exibir_dados(nome, idade):
    return f"{nome} tem {idade} anos."

# Use desempacotamento para chamar a função
print(exibir_dados(**dados))  #desempacotar o dicionário faz o mesmo que o passado abaixo 
print(exibir_dados(nome ="Moranguinha", idade =18))


# Criar um dicionário com**kwargs


def criar_pessoa(**kwargs):
    return kwargs


pessoa1 = criar_pessoa(nome = "gabriel", idade = 18, peso = 78)
print(pessoa1)

for chave, valor in pessoa1.items():
    print(chave, valor)


# Intermediário


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Combine os dicionários usando desempacotamento
combinado = {**dict1, **dict2}
print(combinado)



# Usar *argse **kwargsna mesma moeda

def misturar_args_kwargs(*args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)
    
misturar_args_kwargs(1, 2, 3, nome = "morango", hobby = "musica")    
    
    

# Avançado

# Filtrar dicionários com desempacotamento

def filtrar_chaves(dicionario, *chaves):
    return {i: dicionario[i] for i in chaves if i in dicionario}

dados = {"nome": "Gabigordo", "idade": 25, "cidade": "São Paulo"}
filtrado = filtrar_chaves(dados, "nome", "cidade", "idade")
print(filtrado)


# Função que aceita diferentes argumentos e retorna uma resposta formatada
print("_________________________________________________________________________________________________________________________\n"
    "\n")

def formatar_resposta(*args, **kwargs):
    posicional = ", ".join(map(str, args))
    nomeado = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
    return f"Posicionais: [{posicional}] | Nomeados: [{nomeado}]"

print(formatar_resposta(1, 2, 3, nome="Gabigordo", altura=1.79))


# Repassar argumentos para outra função


print("_________________________________________________________________________________________________________________________\n"
    "\n")


def funcao_secundaria(nome, idade, cidade):
    print(f"{nome} tem {idade} anos e mora em {cidade}.")

def funcao_principal(**kwargs):
    funcao_secundaria(**kwargs)

dados = {"nome": "Moranguinha", "idade": 23, "cidade": "São Paulo"}
funcao_principal(**dados)
