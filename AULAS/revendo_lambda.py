



quadrado = lambda x: x ** 2
print(quadrado(4))  # Saída: 16




def quadrado(x):
    return x ** 2

print(quadrado(4))  # Saída: 16


soma = lambda x, y: [num * (y - x) for num in range(10)]
result = soma(10, 17)
print(result)  



# Ordenar uma lista de tuplas pelo segundo elemento
lista = [(1, 3), (4, 1), (2, 2)]
lista.sort(key=lambda x: x[1])
print(lista)  # Saída: [(4, 1), (2, 2), (1, 3)]



numeros = [1, 2, 3, 4]
nova_lista = list(map(lambda x: x ** 4, numeros))
print(nova_lista)  # Saída: [1, 4, 9, 16]


numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4]



# Lista de pessoas com idade
pessoas = [
    {"nome": "Gabigordo", "idade": 23},
    {"nome": "Moranguinha", "idade": 20},
    {"nome": "Python", "idade": 32}
]

# Filtrar maiores de 21 e extrair os nomes
maiores = list(map(lambda p: p["nome"], filter(lambda p: p["idade"] > 21, pessoas)))

print(maiores)  # Saída: ['Gabigordo', 'Python']
