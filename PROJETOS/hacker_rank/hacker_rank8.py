x = int(input())
y = int(input())
z = int(input())
n = int(input())

listas = []
for num in range(x + 1):
    for numm in range(y + 1):
        for nummm in range(z + 1):
            if (num + numm + nummm) == n:
                continue
            listas.append([num, numm, nummm])
print(listas)