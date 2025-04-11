number = int(input())

if number % 2 != 0:
    print("Weird")
elif number > 1 and number < 6:
    print("Not Weird")
elif number > 5 and number < 21:
    print("Weird")
elif number > 20:
    print("Not Weird")