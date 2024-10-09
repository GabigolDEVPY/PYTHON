lista = [
{"nome": "Gabriel","cpf": "70354054434"},
{"nome": "Ruan", "cpf": "89057389396"}
]

lista1 = lista[1]

if lista1["nome"] == "Ruan":
    print("nomess")


print(lista1["nome"])


for i, pessoa in enumerate(lista):
    print(f'{i+1}. NOME: {pessoa["nome"]}')