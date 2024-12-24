import os


def verify(cpf):

    cpf_valid = ''
    for digit in cpf:
        if digit.isdigit():
            cpf_valid += digit
        else:
            return 2
    cpf = cpf_valid        

    if cpf.isdigit():
            if len(str(cpf)) != 11:
                return 1


    first_digit = cpf[:9]
    accountant = 10
    digit_1 = 0
    for digit in first_digit:
        digit_1 += int(digit) * accountant
        accountant -= 1
    digit_1 = (digit_1 * 10) % 11
    digit_1 = digit_1 if digit_1 <= 9 else 0

    second_digit = cpf[:10]
    accountant = 11
    digit_2 = 0
    for digit in second_digit:
        digit_2 += int(digit) * accountant
        accountant -= 1
    digit_2 = (digit_2 * 10) % 11
    digit_2 = digit_2 if digit_2 <= 9 else 0

    new_cpf = (f"{first_digit}{digit_1}{digit_2}")

    if new_cpf != cpf:
        os.system("cls")
        return 3

    return 4
        

