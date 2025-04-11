import random
import time
from desenho import stages, op_print
from load import list, clear, load_list_scores_lifes, save_file

def game_forca(list):
    while True:
        clear()
        data = load_list_scores_lifes()
        print(f"SCORE: {data["scores"]}     LIFES: {data["lifes"]}"
        "\n")

        option = input("[1]PLAY [2]EXIT: ")
        if option == "2":
            save_file(data)
            break

        elif option == "1":
            word_selected = random.choice(list)
            secret_word = (word_selected["complemento"]).lower()
            tip = word_selected["item"]
            correct_letters = ''
            lifes = 10
            words_typed = ''

            while True:
                if lifes == 0:
                    save_file(data)
                    clear()
                    print('GAME OVER')
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
                    print("           .-\"\"\"\"\"\"-.")
                    print("         .'            '.")
                    print("        /   O      O     \\")
                    print("       :           `      :")
                    print("       |    \\       /    |")
                    print("       |     .-----.'     |")
                    print("       |    /       \\    |  CONGRATULATIONS,")
                    print("       :   |         |   :   YOU WIN!!!")
                    print("        \\   \\       /   /")
                    print("         '.  '.___.'  .'")
                    print("           '-.......-'")

                    next = input('PRESS ANY BUTTON TO CONTINUE')
                    clear()
                    break        
                clear()
                print(f"SCORE: {data["scores"]}                              LIFES: {data["lifes"]}"
                "\n")
                print(
                    f"TIP :{tip} LIFES: {lifes}     WORDS TYPED: {words_typed}\n"
                    "\n"
                    "\n"
                )
                op_print(lifes, formed_word)
                print(
                "\n"
                "\n"
                )

                letter = input("[2]USE LIFE [1]EXIT TYPE A LETTER: ")
                if letter == "1":
                    save_file(data)
                    break
                if letter == '2':
                    if lifes == 10:
                        print('FULL LIFE')
                        time.sleep(2)
                        continue
                    if data['lifes'] == 0:
                        print("\n"
                            'YOU DO NOT HAVE LIVES'
                            )
                        time.sleep(3)
                        continue
                    else:
                        data["lifes"] -= 1
                        lifes += 1
                        continue

                if letter.isalpha():
                    if len(letter) >1:
                        print('TYPE JUST ONE LETTER')
                        continue
                    if letter in words_typed:
                        print("\n"
                            'LETTER ALREADY TYPED')
                        time.sleep(3)
                        continue
                    words_typed += letter
                else:
                    print("TYPE ONLY WORDS")
                    time.sleep(2)
                    continue

                if letter in secret_word:
                    correct_letters += letter

                else:
                    lifes -= 1    

                
                print(formed_word)





