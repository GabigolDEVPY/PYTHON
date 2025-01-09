num = int(input())

if num > 0:
    lista = ""
    for _ in range(num + 1):
        if _ == 0:
            continue
        lista += str(_)


print(lista)        