estados = [
    {"MG": ["divi", "moema", "itauna"]},
    {"SP": ["gut", "lufi", "sufe"]}
    ]

estacao_guarulhos = estados[1]["SP"][1],estados[1]["SP"][2]
estacao_guarame = estados[1]["SP"][1],estados[1]["SP"][2],estados[0]["MG"][2],estados[0]["MG"][1]
estados.append({"PR": ["nordeste", "affs", "raiva"]})
estados_add = estados[0]["MG"]
estados_add.append("jaraguara")
print(estacao_guarame)

list_comprehension = [num * 4 + (10 + 40 / (100000 // 100) + (13 ** 5)) * 10 // 2 if num // 2 == 0 and num - 4 and num != 1000 else 1000 for num in range(len(estacao_guarame))]


print(list_comprehension)
print(estados)