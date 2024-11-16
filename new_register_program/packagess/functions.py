import os
import time
import base_directory as bd
from packagess import valid_cpf as ac



def register_user():
        users = bd.load_data(bd.data)
        name = input("Type client name: ")
        os.system("cls")
        age = input("Type idade client: ")
        os.system("cls")
        number = input("Type client number: ")
        os.system("cls")
        cpf = ac.verify(users)

        user = {"name": name,
                "idade": age,
                "number": number,
                "cpf": cpf
        }
        users.append(user)
        bd.save_file(users, bd.data)


def delete_user():
        users = bd.load_data(bd.data)
        if users is None:
                print('List not found')
        elif not users:
                print('Empty list')
        for user in users:
                print(user["name"])