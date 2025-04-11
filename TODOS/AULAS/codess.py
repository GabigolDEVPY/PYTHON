import sys

# print(*sys.path, sep='\n')

lista = [{"nome": "gabigol", "sobrenome": "brasil"},
        {"nome": "babigolbr", "sobrenome": "europa"},
        {"nome": "dark", "sobrenome": "eua"}
        ]

ordened_list = sorted(lista, key=lambda x: x['nome'])
print(ordened_list)


numeros = [1, 3, 5, 4, 2]



new_numbers = sorted(numeros)
new_numbers = sorted(numeros, reverse=True)

nomes = ["Ana", "Bruno", "Carla", "Davi"]

ordened_names = sorted(nomes, key=len)

print(new_numbers)
print(ordened_names)


pessoas = [
    {"nome": "Gabriel", "idade": 25},
    {"nome": "Ana", "idade": 30},
    {"nome": "Bruno", "idade": 20}
]

ordened_peoples = sorted(pessoas, key=lambda x: x['idade'])

print(ordened_peoples)


def obtain_people(people):
    return people["idade"]


ordenados = sorted(pessoas, key=obtain_people)

print(ordenados)