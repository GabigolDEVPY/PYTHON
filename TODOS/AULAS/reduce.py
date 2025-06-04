from functools import reduce

def mostrar(x, y):
    print(f"x: {x}, y: {y}")
    return x + y

total = reduce(mostrar, [1,2, 3, 4 ])
print(total)