import random

soma = lambda x, y: (x * y) // 2 + (10 ** 4) if y % 4 == 0 else x
print(soma(8, 9))

lambdaa = lambda x, y: (x ** y) if x % 5 == 2 else x
vx = 12
vy = 5
print(lambdaa(vx, vy))

lista = [(random.randint(0,8) * 4 // 2 if num % 4 == 2 else num) for num in range(10)]
print(lista)


list1 = [(random.randint(1, 10)) ** 10 // 2 if num % 2 == 0 else num + 2 for num in [random.randint(1, 10) for _ in range(10)]]


print(list1)

print(vx ** vy)



macro = [(num - 2) * 10 // 4 if num % 2 == 0 else num for num in [random.randint(1, 10) for _ in range(10)]]


print(macro)