import random
from perguntas import perguntas

perguntas = perguntas

perguntas_atualizadas = []

for pergunta in perguntas:
    resposta_correta = pergunta["alternativas"][pergunta["resposta_correta"]]
    nova_lista = pergunta["alternativas"]
    random.shuffle(nova_lista)
    indice = -1
    for alternativa in nova_lista:
        indice +=1
        if alternativa == resposta_correta:
            break

    nova_pergunta = {
        "pergunta": pergunta["pergunta"],
        "alternativas": nova_lista,
        "resposta_correta": indice,
        "modulo": pergunta["modulo"]
    }
    perguntas_atualizadas.append(nova_pergunta)


print(perguntas_atualizadas)
