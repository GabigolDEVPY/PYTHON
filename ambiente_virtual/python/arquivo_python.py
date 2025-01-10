import time

def math_door(n, m):
    for i in range(1, n, 2):
        print((".|." * i).center(m,"-"))
        time.sleep(0.01)
    print("WELCOME".center(m, "_"))
    for i in range(n-2, 0, -2):
        print((".|." * i).center(m, "-"))
        time.sleep(0.01)
n, m = map(int, input().split())

for i in range(1000):
    math_door(n, m)    



