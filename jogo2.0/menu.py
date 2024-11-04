from game_strength import game_forca
from load import save_file, load_list_scores_lifes, list, clear
from shop import loja
import time


while True:
    clear()
    data = load_list_scores_lifes()
    print(f"SCORE: {data["scores"]}              LIFES: {data["lifes"]}"
        "\n")
    option = input('[1]SHOP [2]STRENGTH [3]EXIT: ')

    if option == "2":
        game_forca(list)

    elif option == "3":
        break

    elif option == "1":
        loja()

    else:
        print('TYPE VALID OPTION')
        time.sleep(3)    

    