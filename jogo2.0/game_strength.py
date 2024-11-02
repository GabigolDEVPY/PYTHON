import random
from load import list, clear

def game_forca(list):
    while True:
        option = input("[1]Play [2]Exit [3]Use-life: ")

        if option == "1":
            word_selected = random.choice(list)
            secret_word = word_selected["complemento"]
            tip = word_selected["item"]
            correct_letters = ''

            while True:
                formed_word = ''
                for letter in secret_word:
                    if letter in correct_letters:
                        formed_word += letter
                    else:
                        formed_word += " _ "
                if formed_word == secret_word:
                    clear()
                    print('Congragulations, You Win!!!')
                    next = input('Press any button to continue')
                    clear()
                    break        
                clear()
                print(
                    f"TIP :{tip}\n"
                    f"{formed_word}"
                    )

                letter = input("[1]Exit type a letter: ")
                if letter == "1":
                    break

                if len(letter) >1:
                    print('type just one letter')
                    continue

                if letter in secret_word:
                    correct_letters += letter

                
                print(formed_word)


game_forca(list)


