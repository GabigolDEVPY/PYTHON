import copy
import time  # Importando o módulo time
from binary_search.nomes_unicos_20000 import nomes

list_names = sorted(nomes)


def binary_search(lista, name):
    left_pointer = len(lista) - len(lista)
    right_pointer = len(lista) - 1 
    searches = 0

    while left_pointer <= right_pointer:
        searches += 1
        mid = (left_pointer + right_pointer) // 2
        kick = lista[mid]
        if name == kick:
            return mid
        
        elif kick > name:
            right_pointer = mid

        elif kick < name:
            left_pointer = mid 
        
        else:
            print("result not found")

def search_with_for(lista, name):
    searches = 0
    for _ in lista:
        if _ == name:
            return searches
        searches += 1


# Medir o tempo da busca linear
start_time_for = time.time()  # Marca o tempo de início da busca linear
with_for = search_with_for(list_names, "Larissa Costa 171")  
end_time_for = time.time()  # Marca o tempo de término da busca linear
print(f"with_for {with_for}")  
print(f"Tempo da busca linear: {end_time_for - start_time_for:.8f} segundos")

# Medir o tempo da busca binária
start_time_binary = time.time()  # Marca o tempo de início da busca binária
with_binary = binary_search(list_names, "Larissa Costa 171")  
end_time_binary = time.time()  # Marca o tempo de término da busca binária
print()
print(f"with binary search {with_binary}")
print(f"Tempo da busca binária: {end_time_binary - start_time_binary:.8f} segundos")
