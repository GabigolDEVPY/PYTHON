import random
import os
import json

listt = [1, 2, 4, 3, 6, 5, 8, 7, 9, 10]

listt.sort()

def binary_search(list, search):
    left_poiter = 0
    right_pointer = len(list) - 1
    # while my left pointer is smaller than my right pointer
    while left_poiter <= right_pointer:
        quite = (right_pointer + left_poiter) // 2 
        
        if search == list[quite]:
            return quite
        
        elif search < quite:
            right_pointer = quite
        
        elif search > quite:
            left_poiter = quite
            
        else:
            print("Number not found")
            
result = binary_search(listt, 9)   
print(result)                 


list = [(num * 2 // 2 ** num if num < 2 else num ) for num in range(random.randint(1, 10))]
list = [(num * 8 // 2 ** num if num < 2 else num * 10 ) for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

print(list)


FILE_DIREECTORY = os.path.dirname(os.path.abspath(__file__))
DADOS_LOAD = os.path.join(FILE_DIREECTORY, "dados.json")

def load_list():
    try:
        with open(DADOS_LOAD, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
LOAD_DATA = load_list()
print(LOAD_DATA)    