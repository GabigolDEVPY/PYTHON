import os
import time
import base_directory as bd
from packagess import valid_cpf as ac



def register_user():
        while True:
                users = bd.load_data(bd.data)
                name = input("Type client name: ")
                os.system("cls")
                age = input("Type idade client: ")
                os.system("cls")
                number = input("Type client number: ")
                os.system("cls")
                cpf = ac.verify(users)
                if cpf == 1:
                        print("This user is already registered")
                        time.sleep(3)
                        break

                user = {"name": name,
                        "idade": age,
                        "number": number,
                        "cpf": cpf
                }
                users.append(user)
                bd.save_file(users, bd.data)
                break


def delete_user():
        users = bd.load_data(bd.data)
        if users is None:
                print('List not found')
                time.sleep(3)
                return
        elif not users:
                print('Empty list')
                time.sleep(3)
                return
        for i, user in enumerate(users):
                print(f"{i+1}: NAME: {user["name"]}\n"
                f"CPF: {user["cpf"]}"
                )
                print()

        option = int(input('Type indice the want user delete')) - 1
        del users[option]
        bd.save_file(users, bd.data)
        print(users)
        time.sleep(4)        