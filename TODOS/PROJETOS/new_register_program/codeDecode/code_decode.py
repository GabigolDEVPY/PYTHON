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
    if users == []:
        return []
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

    
        new_number = ''
        for number in user["number"]:
            for digit in utf:
                if number == digit["Caractere"]:
                    new_number += digit['UTF-8']
        user["number"] = new_number

        return users    
        
users = [{"ID": "3231333236353130373034", "name": "6761627269656c", "idade": "3139", "number": "393938373337323236", "cpf": "3730333534303236363734"}]

def decode(users):
    if users == []:
        return []
    for user in users:
        string_text = user["ID"]
        new_id = ''
        two = ""
        for number in range(0, len(string_text), 2):
            two = string_text[number:number+2]
            for digit in utf:
                if two == digit["UTF-8"]:
                    new_id += digit['Caractere']
        user["ID"] = new_id
        
        string_text = user["name"]
        new_name = ''
        two = ""
        for number in range(0, len(string_text), 2):
            two = string_text[number:number+2]
            for digit in utf:
                if two == digit["UTF-8"]:
                    new_name += digit['Caractere']
        user["name"] = new_name
        
        string_text = user["idade"]
        new_idade = ''
        two = ""
        for number in range(0, len(string_text), 2):
            two = string_text[number:number+2]
            for digit in utf:
                if two == digit["UTF-8"]:
                    new_idade += digit['Caractere']
        user["idade"] = new_idade
        
        string_text = user["number"]
        new_number = ''
        two = ""
        for number in range(0, len(string_text), 2):
            two = string_text[number:number+2]
            for digit in utf:
                if two == digit["UTF-8"]:
                    new_number += digit['Caractere']
        user["number"] = new_number
        
        string_text = user["cpf"]
        new_cpf = ''
        two = ""
        for number in range(0, len(string_text), 2):
            two = string_text[number:number+2]
            for digit in utf:
                if two == digit["UTF-8"]:
                    new_cpf += digit['Caractere']
        user["cpf"] = new_cpf
        return users
    

