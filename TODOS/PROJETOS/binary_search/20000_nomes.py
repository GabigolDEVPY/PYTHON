import random
from itertools import product
import json

# Listas de primeiros e últimos nomes
primeiros_nomes = [
    "Gabriel", "Ana", "Lucas", "Julia", "Pedro", "Mariana", "Beatriz", 
    "Rafael", "Carlos", "Fernanda", "Daniel", "Sofia", "Felipe", "Larissa", "João"
]

ultimos_nomes = [
    "Silva", "Santos", "Oliveira", "Souza", "Pereira", "Costa", "Almeida", 
    "Gomes", "Martins", "Barros", "Ferreira", "Lima", "Mendes", "Vieira", "Ribeiro"
]

# Gerar combinações únicas de primeiros e últimos nomes
nomes_combinados = [f"{primeiro} {ultimo}" for primeiro, ultimo in product(primeiros_nomes, ultimos_nomes)]

# Garantir que sejam 20.000 nomes adicionando números únicos quando necessário
nomes = set(nomes_combinados)  # Começa com combinações únicas
while len(nomes) < 20000:
    primeiro = random.choice(primeiros_nomes)
    ultimo = random.choice(ultimos_nomes)
    numero = random.randint(1, 10000)  # Adiciona um número aleatório
    nomes.add(f"{primeiro} {ultimo} {numero}")

# Converter para lista
nomes = list(nomes)

# Salvando a lista em um arquivo JSON
file_path_json = "nomes_unicos_20000.json"
with open(file_path_json, "w") as file:
    json.dump(nomes, file)

print(f"Arquivo salvo em: {file_path_json}")
