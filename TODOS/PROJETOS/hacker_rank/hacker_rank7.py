amount = int(input())
stack = sorted(list(map(int, input().split())))

verificados = set()
nova_lista = []
for num in stack:
    if num in verificados:
        continue
    verificados.add(num)
    nova_lista.append(num)
bigger_number = nova_lista[-2]
print(bigger_number)    


