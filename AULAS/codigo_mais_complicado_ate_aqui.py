import os
import random
from decimal import Decimal
import copy

os.system('cls')

def calcula_saldo_inicial(idade, saldo_base=Decimal('100.50')):
    fator_idade = Decimal(idade) * Decimal('0.1')
    saldo_final = saldo_base + fator_idade
    return saldo_final

def gera_cpf():
    return ''.join([str(random.randint(0, 9)) for _ in range(11)])

nome = "Gabriel"
idade = random.randint(20, 40)
altura = random.uniform(1.5, 2.0)
is_programmer = random.choice([True, False])
saldo = calcula_saldo_inicial(idade)
cpf = gera_cpf()

print(f"Bem-vindo, {nome}! Sua idade é {idade} anos, altura {altura:.2f}m, e seu saldo inicial é R$ {saldo:.2f}. Seu CPF gerado é {cpf}.")

if idade >= 18 and altura >= 1.60:
    acesso_montanha = "permitido"
else:
    acesso_montanha = "negado"

if 'a' in nome.lower():
    letra_a_no_nome = True
else:
    letra_a_no_nome = False

frase = f"Você tem {idade} anos, e seu acesso à montanha-russa é {acesso_montanha}."
palavras = frase.split()
frase_invertida = " ".join(palavras[::-1])

contador = 0
while contador < idade:
    if contador == 5:
        break
    contador += 1
    if contador % 2 == 0:
        continue
    saldo += Decimal('1.00')

print(f"Sua frase invertida: {frase_invertida}")
print(f"Novo saldo após bônus: R$ {saldo:.2f}")

lista_compras = ['maçã', 'banana', 'laranja']
for i, item in enumerate(lista_compras):
    print(f"Item {i+1}: {item}")

tupla_dados = (nome, idade, altura, is_programmer)
nome, idade, altura, is_programmer = tupla_dados

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura:.2f}m, Programador: {is_programmer}")

dicionario_info = {
    "nome": nome,
    "idade": idade,
    "altura": altura,
    "saldo": saldo,
    "cpf": cpf
}

dict_copy = copy.deepcopy(dicionario_info)
dict_copy.update({"cidade": "São Paulo"})
print(f"Cidade adicionada: {dict_copy['cidade']}")

if dict_copy is not None:
    try:
        divisao = 10 / (random.choice([0, 2, 5]))
    except ZeroDivisionError:
        divisao = "Erro de divisão por zero"
    print(f"Tentativa de divisão: {divisao}")

def calcula_bonificacao(*args):
    return sum(args) / len(args)

bonus = calcula_bonificacao(Decimal('50.0'), Decimal('30.0'), Decimal('20.0'))
saldo += bonus
print(f"Saldo final com bonificação: R$ {saldo:.2f}")

def cria_saudacao(mensagem):
    def saudacao_interna():
        return f"Mensagem secreta: {mensagem}"
    return saudacao_interna

msg_func = cria_saudacao("Parabéns, você concluiu o sistema!")
print(msg_func())

numero_random = random.randint(1, 100)
print(f"Seu número da sorte é: {numero_random}")

print(f"Nome ao contrário: {nome[::-1]}")
