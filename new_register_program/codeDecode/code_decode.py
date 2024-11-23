import sys
import os
import json


Base_dir = os.path.dirname(os.path.abspath(__file__))
utf = os.path.join(Base_dir, "utf-8_list.json")


def load_utf():
    try:
        with open(utf, "r" , encoding="utf-8") as f:
            return json.load(f)
    except (FileExistsError, FileNotFoundError):
        print('ERROR')

utf = load_utf()

def code(users):
    for user in users:
        new_id = ''
        for number in user["ID"]:
            for digit in utf:
                if number == digit["Caractere"]:
                    new_id += digit['UTF-8']
        user["ID"] = new_id
        
        new_name = ''
        for number in user["name"]:
            for digit in utf:
                if number == digit["Caractere"]:
                    new_name += digit['UTF-8']
        user["name"] = new_name
        
        new_idade = ''
        for number in user["idade"]:
            for digit in utf:
                if number == digit["Caractere"]:
                    new_idade += digit['UTF-8']
        user["idade"] = new_idade
        
        new_cpf = ''
        for number in user["cpf"]:
            for digit in utf:
                if number == digit["Caractere"]:
                    new_cpf += digit['UTF-8']
        user["cpf"] = new_cpf
        return users
        
        
def decode(users):
    for user in users:
        new_id = ''
        for number[:2] in user["ID"]:
            for digit in utf:
                if number == digit["UTF-8"]:
                    new_id += digit['Caractere']
        user["ID"] = new_id
        
        new_name = ''
        for number[:2] in user["name"]:
            for digit in utf:
                if number[:2] == digit["UTF-8"]:
                    new_name += digit['Caractere']
        user["name"] = new_name
        
        new_idade = ''
        for number[:2] in user["idade"]:
            for digit in utf:
                if number[:2] == digit["UTF-8"]:
                    new_idade += digit['Caractere']
        user["idade"] = new_idade
        
        new_cpf = ''
        for number[:2] in user["cpf"]:
            for digit in utf:
                if number == digit["UTF-8"]:
                    new_cpf += digit['Caractere']
        user["cpf"] = new_cpf
        return users

