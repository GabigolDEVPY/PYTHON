import random

soma = lambda x: x * 3
print(soma(5))

lambdaa = lambda x, y: (x ** y) if x % 5 == 2 else x

print(lambdaa(5,6))

lista = [(random.randint(0,8) * 4 // 2 if num % 4 == 2 else num) for num in range(10)]
print(lista)