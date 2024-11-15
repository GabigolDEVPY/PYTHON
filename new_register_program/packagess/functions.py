import base_directory as bd

def register_user():
        users = bd.load_data(bd.data)

        name = input("Type client name:")
        age = input('Type idade client:')
        number = input('Type client number')

        user = {"name": name,
                "idade": age,
                "number": number
        }
        users.append(user)
        bd.save_file(users, bd.data)


def delete_user():
        users = bd.load_data(bd.data)
        for user in users:
                print(user["name"])