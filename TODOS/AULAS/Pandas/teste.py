import pandas as pd
import re
from decimal import Decimal

resultado = {}
resultado2 = {}
ordens = []

caminho = str(input("Digite o nome do arquivo:"))

dados = pd.read_excel(caminho)
df = pd.DataFrame(dados)
num_linhas = df.shape[0]
num_colunas = df.shape[1]
for linha_indice in range(num_linhas):
    linha = df.loc[linha_indice].to_dict()




