extras = {"Cidade": "São paulo", "Estado": "SP", "dados": {"altura": 159, "habilidade": "cozinhar"}}
pessoa = {"nome": "Moranguinha", **extras, "idade": 23, **extras["dados"]}

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")