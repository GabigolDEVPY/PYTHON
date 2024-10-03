lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena(item):
    items = item['nome']
    return items

lista.sort(key=ordena)


for list in lista:
    print(list)
print()

def exibir(lista):
    for item in lista:
        print(item)
        print()

l1 = sorted(lista, key=lambda list: list['nome'])

exibir(l1)

