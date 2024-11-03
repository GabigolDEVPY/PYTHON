import random
import time
from load import list, clear, load_list_scores_lifes, save_file

def game_forca(list):
    while True:
        clear()
        data = load_list_scores_lifes()
        print(f"SCORE: {data["scores"]}              LIFES: {data["lifes"]}"
        "\n")

        option = input("[1]Play [2]Exit: ")
        if option == "2":
            save_file(data)
            break

        elif option == "1":
            word_selected = random.choice(list)
            secret_word = word_selected["complemento"]
            tip = word_selected["item"]
            correct_letters = ''
            lifes = 10

            while True:
                if lifes == 0:
                    save_file(data)
                    clear()
                    print('You Defeat')
                    time.sleep(3)
                    break
                formed_word = ''
                for letter in secret_word:
                    if letter in correct_letters:
                        formed_word += letter
                    else:
                        formed_word += " _ "
                if formed_word == secret_word:
                    data["scores"] += 10000
                    save_file(data)
                    clear()
                    print('Congragulations, You Win!!!')
                    next = input('Press any button to continue')
                    clear()
                    break        
                clear()
                print(f"SCORE: {data["scores"]}              LIFES: {data["lifes"]}"
                "\n")
                print(
                    f"TIP :{tip} LIFES: {lifes}\n"
                    f"{formed_word}"
                    )
                
                letter = input("[2]Use life [1]Exit type a letter: ")
                if letter == "1":
                    save_file(data)
                    break
                if letter == '2':
                    if data['lifes'] == 0:
                        print("\n"
                            'you not have lifes'.upper()
                            )
                        time.sleep(3)
                        continue
                    else:
                        data["lifes"] -= 1
                        lifes += 1
                        continue

                if len(letter) >1:
                    print('type just one letter')
                    continue

                if letter in secret_word:
                    correct_letters += letter

                else:
                    lifes -= 1    

                
                print(formed_word)





