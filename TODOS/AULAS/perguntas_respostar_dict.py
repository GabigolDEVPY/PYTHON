import os

dict =[
    {
    "Pergunta": "quem descobriu o Brasil?",
    "alternativas": {"A": "Pedro Álvares Cabral", "B": "Dom Pedro I"},
    "resposta": "Pedro Álvares Cabral"
    },
    {
    "Pergunta": "quem descobriu o Brasil?",
    "alternativas": {"A": "Pedro Álvares Cabral", "B": "Dom Pedro I"},
    "resposta": "Pedro Álvares Cabral"
    },
    {
    "Pergunta": "quem descobriu o Brasil?",
    "alternativas": {"A": "Pedro Álvares Cabral", "B": "Dom Pedro I"},
    "resposta": "Pedro Álvares Cabral"
    }
]

for perguntas in dict:
    print(dict[0]["Pergunta"])
    for chave, alternativa in perguntas["alternativas"].items():
        print(chave, alternativa)
    tentativa = input("qual a alternativa ?").upper()
    os.system("cls")
    if perguntas["alternativas"][tentativa] == perguntas["resposta"]:
        print("Acertou")
        print()
    else:
        print("errou")
        print()
