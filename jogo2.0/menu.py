from game_strength import game_forca
from load import data


while True:
    print(f"SCORE: {data["scores"]}              LIFES: {data["lifes"]}"
        "\n")
    option = input('[1]Loja [2]Forca [3]Sair: ')

    if option == "2":
        game_forca(list)
    elif option == "3":
        break

    