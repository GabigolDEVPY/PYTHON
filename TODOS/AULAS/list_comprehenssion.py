nome = input("type name")

lista = [num ** 2 for num in range(len(nome)) if num // 2 > 0.5]

print(lista)
