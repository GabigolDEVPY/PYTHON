import os
import time
import base_directory as bd
from packagess import valid_cpf as ac


        

def register_user():
        while True:
                users = bd.load_data(bd.data)
                name = input("Type client name: ")
                os.system("cls")
                age = input("Type client age: ")
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

        option = int(input('[0]Sair ,Type indice the want user delete: ')) - 1
        if option == -1:
                return
        del users[option]
        bd.save_file(users, bd.data)
        time.sleep(4)

def search_user():
        users = bd.load_data(bd.data)
        option = input('enter the name of the user you want to find: ')
        encontred_users = 0
        for i, user in enumerate(users):
                if user["name"][:3] == option[:3]:
                        print(f"{i+1}: {user["name"]}")
                        encontred_users += 1
        if encontred_users == 0:
                print("No users were found")                
        is_continue = input('Press ENTER to coninue: ')                

