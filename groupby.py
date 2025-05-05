from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos_agrupados = sorted(alunos, key= lambda b: b["nota"])
grupos = groupby(alunos_agrupados, key= lambda b: b["nota"])

# print(grupos)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)