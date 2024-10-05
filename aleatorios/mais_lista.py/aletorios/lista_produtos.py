lista = []


def adiciona_produto():
    codigo = input('Digite o código do produto: ')
    nome = input('Digite o nome do produto: ')
    quantidade = input('Digite a quantidade do produto em estoque: ')
    valor = input('Digite o valor inutário do produto: ')

    produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "valor": valor
    }

    lista.append(produto)

    print(
        f'codigo: {lista[0]["codigo"]}\n'
        f'nome: {lista[0]["nome"]}\n'
        f'quantidade: {lista[0]["quantidade"]}\n'
        f'valor: {lista[0]["valor"]}\n'
        )



adiciona_produto()    