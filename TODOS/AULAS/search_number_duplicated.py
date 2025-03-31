list= [
    [1, 4, 4, 6, 7, 5, 8, 9, 11, 23, 11,],
    [1, 4, 5, 6, 7, 5, 8, 9, 11, 23, 11,],
    [1, 4, 6, 6, 7, 5, 8, 9, 11, 23, 11,],
    [1, 4, 1, 6, 7, 5, 8, 9, 11, 23, 11,]
]

def return_fist_duplicated(list):
    numero_duplicado = '*'
    checked_numbers = set()

    for numero in list:
        if numero in checked_numbers:
            numero_duplicado = numero
            return numero_duplicado
        
        checked_numbers.add(numero)

for lista in list:
    print(lista, return_fist_duplicated(lista))    


