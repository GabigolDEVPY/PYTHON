import random
from perguntas import perguntas as pr
import json
import os
import copy

local = os.path.join((os.path.abspath(os.path.dirname(__file__))), "dados.json")


perguntas = copy.deepcopy(pr)
perguntas_atualizadas = []

for pergunta in perguntas:
    resposta_correta = pergunta["opcoes"][pergunta["resposta_correta"]]
    nova_lista = pergunta["opcoes"]
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



with open(local, "w", encoding="UTF-8") as f:
    json.dump(perguntas_atualizadas, f, ensure_ascii=False, indent=4)