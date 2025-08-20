from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'produtos.csv'

print(CAMINHO_CSV)

with open(CAMINHO_CSV, "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)    

lista_clientes = [
    {"Nome": "Gabriel", "Idade": 20},
    {"Nome": "Gabigol", "Idade": 20},
    {"Nome": "Biel", "Idade": 20}
]

lista_clientes2 = [
    ["Gabriel", 20],
    ["Gabigol", 25],
    ["Biel", 30]
]

with open(CAMINHO_CSV, "w") as arquivo:
    colums = lista_clientes[0].keys()
    # nome_colunas = ["Nome", "Endereço"]
    escritor = csv.DictWriter(arquivo, fieldnames=colums)
    # escritor = csv.writer(arquivo)
    # escritor.writerow(nome_colunas)
    # for cliente in lista_clientes2:
    #     escritor.writerow(cliente)
    escritor.writeheader()
    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)
    print(colums)