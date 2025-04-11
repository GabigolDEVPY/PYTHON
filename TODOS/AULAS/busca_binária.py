#       0  1  2  3  4  5  6  7  8  9   10
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def binary_search(lista, search):
    pointer_left = 0
    pointer_right = len(lista) - 1
    
    while pointer_left <= pointer_right:
        quite = (pointer_left + pointer_right) // 2
        kick = list[quite]
        
        if kick == search:
            return quite
        
        elif kick < search:
            pointer_left = quite
        
        elif kick < search:
            pointer_right = quite
        
        else:
            return 0
        
        
search = 8        
result = binary_search(list, search)        
print(f"o resultado foi {result}")

