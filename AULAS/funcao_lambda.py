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

print(lista)

def exibir(lista):
    for list in lista:
        print(list)
        print()
    

lista_ordem = sorted(lista, key=lambda list: list['nome'])

exibir(lista_ordem)