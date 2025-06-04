lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4, 5, 7]
        # 2  4  6  8  10  13
        
def soma_lista(first, second):
    menor = None
    maior = None
    if len(first) > len(second):
        menor = second
        maior = first
    else:
        menor = first
        maior = second
        
    new_list = []
    indice = 0
    for num in menor:
        new_list.append(num + maior[indice])    
        indice += 1
    
    print(new_list)
    
soma_lista(lista1, lista2)

# second solution 

new_list2 = []
for i in range(len(lista2)):
    new_list2.append(lista1[i] + lista2[i])
    
    
print(new_list2)


for i, _ in enumerate(lista1):
    print(i, _)
    
# solução com list comprehenssion


new_list3 = [x + y for x, y in zip(lista1, lista2)]        

print(new_list3)


listass = list(zip(lista1, lista2))
print(listass)