import os
import time
from packagess import functions as ft

def select_option():
        os.system("cls")
        print("[1] register [2] delete [3] search [4] Exit"
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
        os.system("cls")
        ft.register_user()
    elif x == 2:
        os.system("cls")
        ft.delete_user()
    elif x == 3:
        os.system("cls")
        ft.search_user()



#comentário


while True:
    value = select_option()
    if value == 4:
        break
    interact_display(value)

