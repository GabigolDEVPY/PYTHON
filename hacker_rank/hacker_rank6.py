number = int(input())

if number > 0:
    for _ in range(number + 1):
        if _ == 0:
            continue
        acumulate = ''
        acumulate += (str(_) *_)
        print(acumulate)
        
