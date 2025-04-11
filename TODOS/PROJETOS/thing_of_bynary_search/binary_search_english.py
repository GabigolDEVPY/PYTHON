    # 0  1  2  3  4  5  6  7 
list = [1, 2, 3, 4, 5, 6, 7]

def binary_search(lista, search):
    left_pointer = 0 
    right_pointer = len(lista) - 1 
    
    while left_pointer <= right_pointer:
        quite =  (left_pointer + right_pointer) // 2
        
        if search == lista[quite]:
            return quite
        
        elif quite < search:
            left_pointer = quite
            
        elif quite > search:
            right_pointer = quite
            
        else:
            print('The number was not found')        

search = int(input(f"{list}\n"
    "\n"
    "Enter the number you want to find: "))            
result = binary_search(list, search)            



print(f"The search result was {result}")
