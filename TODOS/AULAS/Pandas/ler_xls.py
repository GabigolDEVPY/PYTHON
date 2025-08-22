import pandas as pd
import re
from decimal import Decimal

resultado = {}
resultado2 = {}
ordens = []

caminho = str(input("Digite o nome do arquivo:"))

dados = pd.read_excel(caminho)
df = pd.DataFrame(dados)
colunas = (['Unnamed: 0', 'Status conciliação', 'Data', 'Lançamento automático', 'Contrapartida', 'Descrição', 'Valor', 'Histórico', 'Descrição histórico', 'Saldo', 'Observação'])
num_linhas = df.shape[0]
for linha_indice in range(num_linhas):
    linha = df.loc[linha_indice].to_dict()
    valor = Decimal(str(linha["Valor"]))
    name = re.findall(r"\((.*?)\)", linha["Descrição histórico"])
    name = name[0]
    if name not in resultado:
        resultado[name] = Decimal("0")
        resultado2[name] = [] 
        ordens.append(name)   
    resultado[name] += valor 
    resultado2[name].append(valor)


for funcionario in range(len(ordens)):
    print()
    print("Funcionário:", ordens[funcionario])
    valores = resultado2[ordens[funcionario]]
    soma_total = sum(valores, Decimal("0"))
    print(soma_total)

    






