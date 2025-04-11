import time
from load import save_file, load_list_scores_lifes, clear

def loja():
    while True:
        clear()
        data = load_list_scores_lifes()
        print(f"SCORE: {data["scores"]}  LIFES: {data["lifes"]}"
            "\n"
            )
        valid = [0,1,2,3,4,5]
        itens = [
            {"LIFE": 1,  "Valor": 10000},
            {"LIFE": 2,  "Valor": 20000},
            {"LIFE": 3,  "Valor": 30000},
            {"LIFE": 4,  "Valor": 40000},
            {"LIFE": 5,  "Valor": 50000},
            {"LIFE": 6,  "Valor": 60000}
        ]

        for lista in itens:
            print(f"LIFE: {lista["LIFE"]} COST: {lista["Valor"]}")
        print()      
        option = input("[7]EXIT OR NUMBER OF BUY: ")

        if option.isdigit():
            option = int(option) -1
            if option == 6:
                break

            elif option not in valid:
                print('OPTION INVALID, TYPE TRY')
                time.sleep(3)
                continue
            else:
                if data["scores"] >= itens[option]["Valor"]:
                    data["lifes"] += itens[option]["LIFE"]
                    data["scores"] -= itens[option]["Valor"]
                    save_file(data)
                else:
                    print("\n"
                        'INSUFFICIENT FUNDS')
                    time.sleep(3)
        else:
            print('TYPE ONLY NUMBERS')
            time.sleep(3)            

        
