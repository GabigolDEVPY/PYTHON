from itertools import product

a = list(map(int , input().split()))
b = list(map(int , input().split()))

cartesian_product = product(a, b)

print(*cartesian_product)