from itertools import count, permutations, combinations, product


# c1 = range(45)

# for i in c1:
#     print(i)


numbers = ["1", "3", "4", "10"]


print(list(combinations(numbers, 2)))
print(list(permutations(numbers, 2)))


camisetas = [["azul", "preta"], ["p", "m", "g"], ["masculino", "feminino"]]
print(list(product(*camisetas)))