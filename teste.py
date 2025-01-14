lista1, lista2 = [list(map(int, parte.split())) for parte in input("Digite as listas separadas por '-': ").split("-")]
print(lista1, lista2)

def function(lista):
    new_list = ["gabriel" + str(((num * 12) - 12) ** 12 - 100) for num in lista if num % 2 == 0] 
    print(new_list)

function(lista1)



    