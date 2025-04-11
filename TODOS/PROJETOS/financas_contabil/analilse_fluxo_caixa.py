meses = [{"mes": "janeiro", "valor": 1000},{"mes": "fevereiro", "valor": -1000},{"mes": "março", "valor": 1400},{"mes": "abriu", "valor": 2200}]


def visualizar_meses(lista):
    total = 0
    for _ in lista:
        total += _["valor"]
        if _["valor"] < 0:
            print(f"O mês {_["mes"]} teve um prejuízo de {_["valor"]}")
        elif _["valor"] == 0:
                print(f"O mês {_["mes"]} não teve lucro e nem prejuízo")
        else:
            print(f"O mês {_["mes"]} teve um lucro de {_["valor"]}")
    if total == 0:
        print(f"Não teve lucro e nem prejuízo")                
    elif total < 0:
        print(f"Teve um prejuízo de {total}")
    else:
        print(f"Teve um lucro de {total}")

visualizar_meses(meses)        

