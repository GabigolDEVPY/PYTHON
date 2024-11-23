import os
import time
import base_directory as bd
from packagess import valid_cpf as ac, generate_ID as gen





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

                user = {
                        "ID": gen.gen_ID(),
                        "name": name,
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
                print(f"{i+1}: Name: {user["name"]} ID: {user["ID"]} CPF: {user["cpf"]} NUMBER: {user["number"]} AGE: {user["idade"]}")
                
        option = input("[1] Delete for indice [2] Delete by ID: ")
        if option == "2":
                os.system("cls")
                id_user = input("Enter the client ID: ")
                interact = 0
                for user in users:
                        if user["ID"] == id_user:
                                del users[interact]
                                bd.save_file(users, bd.data)
                                return
                        else:
                                interact += 1
                                
                print('Cliente not found')                
                return
        os.system("cls")
        for i, user in enumerate(users):
                print(f"{i+1}: Name: {user['name']} ID: {user['ID']}\n"
                f"CPF: {user["cpf"]}"
                )
                print()

        option = int(input('[0]Sair ,Type indice the want user delete: ')) - 1
        if option == -1:
                return
        del users[option]
        bd.save_file(users, bd.data)
        
        

def search_user():
        users = bd.load_data(bd.data)
        if users is None:
                print('List not found')
                time.sleep(3)
                return
        elif not users:
                print('Empty list')
                time.sleep(3)
                return
        
        option = input('enter the name of the user you want to find: ')
        encontred_users = 0
        for i, user in enumerate(users):
                if user["name"][:3] == option[:3]:
                        print(f"{i+1}: Name: {user['name']} ID: {user['ID']}")
                        encontred_users += 1
        if encontred_users == 0:
                print("No users were found")                
        is_continue = input('Press ENTER to coninue: ')  
        


def update_user():
        users = bd.load_data(bd.data)
        if users is None:
                print('List not found')
                time.sleep(3)
                return
        elif not users:
                print('Empty list')
                time.sleep(3)
                return
        
        option = input('Enter the ID of the user you want to update: ')
        for user in users:
                if user["ID"] == option:
                        os.system("cls")
                        option_update = input('[1]name [2] age [3] number [4] cpf: ')
                        if option_update == "1":
                                os.system("cls")
                                user["name"] = input('press a updated name: ')
                        if option_update == "2":
                                os.system("cls")
                                user["idade"] = input('press a updated age: ')
                        if option_update == "3":
                                os.system("cls")
                                user["number"] = input('press a updated number: ')
                        if option_update == "4":
                                os.system("cls")
                                user["cpf"] = ac.verify(users)
                                
                        os.system("cls")
                        bd.save_file(users, bd.data)
                        break
                        
        print("No users were found")                
        