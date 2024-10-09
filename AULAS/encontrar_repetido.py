listas_produtos = [
    [1, 2, 3, 4, 5, 6, 7 , 7, 8, 9],
    [1, 4, 5, 3, 6, 7, 8, 5, 3, 4],
]

def encontrar_duplicado(lista):
    numeros_checados = set()
    for numero in lista:
        if numero in numeros_checados:
            return numero  # Retorna o primeiro duplicado encontrado
        numeros_checados.add(numero)
    return -1  # Retorna -1 se não houver duplicados

for lista in listas_produtos:
    numero_duplicado = encontrar_duplicado(lista)
    print(f'Lista: {lista}, Número duplicado: {numero_duplicado}')
