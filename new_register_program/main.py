import os
import time


def select_option():
        print("[1] register [2] delete [3] search [4] cancel"
            "\n"
            "\n"
            "\n")
        option = input("What do you want?")
        try:
            if option.isalnum:
                return int(option)

        except:
            print("Type only numbers!")
            time.sleep(3)




def interact_display(x):
    if x == 1:
        print("cadastrar")
        time.sleep(4)



while True:
    value = select_option()
    interact_display(value)

