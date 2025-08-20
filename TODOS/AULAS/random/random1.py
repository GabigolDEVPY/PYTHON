import random
import secrets
import string as s


random = secrets.SystemRandom()
random.seed(0)

for x in range(20):
    print(random.randrange(10, 20, 3))

nomes = ["Gabriel", "Gabriela", "Amor", "Morango"] 
random.shuffle(nomes)

novos_nomes = random.sample(nomes, k=2)
print(nomes)   
print(novos_nomes)