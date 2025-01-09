def valid_uid(nums):
    valids = []
    for num in range(nums):
        uid = input()
        lista = list(uid)
        uppers = 0
        digits = 0
        checados = ""
        if_e = 0
        for char in lista:
            if char in checados:
                valids.append("Invalid")
                if_e = 1
                break
            if char.isupper():
                uppers += 1
            elif char.isdigit():
                digits += 1
            checados += char
        if if_e == 1:
            continue
        elif uppers >= 2 and digits >= 3 and len(uid) == 10 and uid.isalnum():
            valids.append("Valid")
        else:
            valids.append("Invalid")
        checados = ""        
    for _ in valids:
        print(_)    



valid_uid(int(input()))


