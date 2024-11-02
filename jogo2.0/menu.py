from game_strength import game_forca
from load import save_file, load_list_scores_lifes, list


while True:
    data = load_list_scores_lifes()
    print(f"SCORE: {data["scores"]}              LIFES: {data["lifes"]}"
        "\n")
    option = input('[1]Loja [2]Forca [3]Sair: ')

    if option == "2":
        game_forca(list)
    elif option == "3":
        break

    