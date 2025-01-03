import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# obs: SEU MORANGO GOSTARIA DE UMA LISTA MAIS ORGANIZADA
lista_produtos = [{"nome": produto["nome"], "preco": produto["preco"]} for produto in produtos]
print(lista_produtos)

def aumenta_preco(lista):
    novos_produtos = lista.copy()
    produtos_por_nome = lista.copy()
    for produtos in novos_produtos:
        produtos["preco"] = (produtos["preco"] * 1.10)
    novos_produtos.sort(key=lambda produto: produto["preco"])
    produtos_por_nome.sort(key=lambda produto: produto["nome"])
    produtos_por_nome.reverse()
    print(novos_produtos)
    print(produtos_por_nome)
    return produtos_por_nome


aumenta_preco(produtos)

copia_profunda = copy.deepcopy(aumenta_preco(lista_produtos))
print(*copia_profunda, sep="\n")


outra = [{**p, 'preco': round(p['preco'] * 1.1, 2)} for p in copy.deepcopy(produtos)]

print(*outra, sep="\n")