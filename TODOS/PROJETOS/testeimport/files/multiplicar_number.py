import random


def multi_number(x):
    return [random.randint(0, 6) * x // 4 for num in range(10)]


print("The name of this module is", __name__)