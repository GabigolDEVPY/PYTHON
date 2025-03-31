alunos = {
    "ramdom": [1, 2, 3, 4, 5, 6, 7]
}
alunos["ramdom"].append(8)
print(alunos["ramdom"])

# Dicionário com tuplas como chaves

cordenadas = {
    (1, 5): "one point five",
    (1, 7): "one point seven",
    (1, 2): "one point two",
    (1, 3): "one point three"
}

print(cordenadas[(1, 5)])


languages = {
    "ramdom": {"python", "C", "C#"},
    "ramdom2": {"go", "ada", "Assembly"}
}

languages["ramdom"].add("java")

print(languages["ramdom"])


# Dicionário com outros dicionários como valores
empresa = {
    "Gabigordo": {"idade": 25, "cargo": "Dev", "linguagens": ["Python", "Java"]},
    "Moranguinha": {"idade": 24, "cargo": "Futura Perita", "linguagens": ["R", "Python"]}
}

# Acessando informações específicas
print(empresa["Gabigordo"]["linguagens"])  # Saída: ['Python', 'Java']


# Lista de dicionários
usuarios = [
    {"nome": "Gabigordo", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Moranguinha", "idade": 24, "cidade": "Rio de Janeiro"}
]

# Iterando pela lista
for usuario in usuarios:
    print(f"{usuario['nome']} mora em {usuario['cidade']}.")
# Saída:
# Gabigordo mora em São Paulo.
# Moranguinha mora em Rio de Janeiro.



# Dicionário com combinações de listas, sets e tuplas
dados = {
    "alunos": ["Gabigordo", "Moranguinha"],
    "notas": {
        "Gabigordo": {9.0, 8.5, 10.0},
        "Moranguinha": {10.0, 10.0, 9.5}  # Sets removem duplicatas automaticamente
    },
    "coordenadas": [(0, 0), (1, 2), (-1, -1)]  # Lista de tuplas
}

# Acessando diferentes tipos de dados
print(dados["alunos"])        # Saída: ['Gabigordo', 'Moranguinha']
print(dados["notas"]["Gabigordo"])  # Saída: {9.0, 8.5, 10.0}
print(dados["coordenadas"])   # Saída: [(0, 0), (1, 2), (-1, -1)]

