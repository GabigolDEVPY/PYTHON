import os
import time

def verify(list_users):
    while True:
        cpf = input('Type cpf number: ')
        cpf_valid = ''
        for digit in cpf:
            if digit.isdigit():
                cpf_valid += digit
        cpf = cpf_valid        

        if cpf.isdigit():
                if len(str(cpf)) != 11:
                    os.system("cls")
                    print('CPF not contain 11 digits')
                    continue
        else:
            os.system("cls")
            print("Type only numbers")

        users = list_users
        if users:
            for user in users:
                if user["cpf"] == cpf:
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
            print("CPF inválido")
            continue
        return new_cpf
        

