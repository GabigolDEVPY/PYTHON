import time

def multipli_age():
    while True:
        age = int(input("Type your age: "))
        if age >= 18:
            print('Your age is valid')
            return age
        print('Your age is not valid, Retry')
        time.sleep(3)