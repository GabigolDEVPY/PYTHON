listas_produtos = [
    [1, 2, 3, 4, 5, 6, 7 , 7, 8, 9],
    [1, 4, 5, 3, 6, 7, 8, 5, 3, 4],
]
numeros_checados = set()
numero_duplicado = -1

for lista in listas_produtos:
    for numero in lista:
        if numero_duplicado != -1:
            ...
        else:
            if numero in numeros_checados:
                numero_duplicado = numero
            else:
                numeros_checados.add(numero)      


        
    print(f'{listas_produtos}{numero_duplicado}')    

