print("Usando LIST______________________________________________________________")

lista = [1, 2, 3, 4, 8, 6, 7]

lista.append(5)

lista[len(lista):] = [5]

lista.insert(2, 5)

print(lista)

lista.remove(lista[0])

print(lista)

lista.pop(2)

print(lista)

#del lista[:]
#list.clear()

print (lista.count(5))

lista.sort(key=None, reverse=True)

print(lista)

lista.sort(key=None, reverse=False)

print(lista)

lista.reverse()

print(lista)

copyy = lista[:]

listacopia = (lista.copy() + [11, 12, 14])

print(listacopia)

print(copyy)

print("Usando Stack______________________________________________________________")
stack = [3, 4, 5]

print(stack)

stack.append(6)

stack.append(7)

print(stack)

[3, 4, 5, 6, 7]

stack.pop()

print(stack)

stack.pop()

stack.pop()

print(stack)

print("USANDO LISTAS COMO FILAS_________________________________________________________________________________")


from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)

queue.append("Terry") 
print(queue)       

queue.append("Graham") 
print(queue)     

queue.popleft()                
print(queue)

queue.popleft()
print(queue)   


print("List Comprehensions de verdade____________________________________________________________________________________________________________________________________")

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


squares = list(map(lambda x: x**2, range(10)))