import random


def gen_ID():
    ID = ""
    for num in range(10):
        ID += str(random.randint(0,10))
    return ID    
        
        
result = gen_ID()

print(result)        