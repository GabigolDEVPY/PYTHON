from itertools import zip_longest

# print(min(["z", "b", "c", "d", "f", "g", "s", "e"]))



l1 = ["salvador", "ubatuba", "belo horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]

print(list(zip_longest(l1, l2)))