import random

def id():
    ID = ""
    for num in range(10):
        ID += str(random.randint(0, 10))
    return ID
    
