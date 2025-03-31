import random
import os

file_path = r"C:\teste"

if os.path.exists(file_path):
    try:
        if random.randint(0, 2) == 1:
            os.remove(file_path)
            print(f"{file_path} foi removido.")
        else:
            print("Nenhuma ação foi tomada.")
    except PermissionError as e:
        print(f"Erro de permissão: {e}")
else:
    print(f"O arquivo {file_path} não existe.")

