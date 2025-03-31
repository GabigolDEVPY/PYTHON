def door(n, m):
    for i in range(1, n, 2):
        print((".|." * i).center(m, "-"))
    print("WELCOME".center(m, "-"))
    for i in range(n-2, 0, -2):
        print((".|." * i).center(m, "-"))
n, m = map(int, input().split())
door(n, m)            