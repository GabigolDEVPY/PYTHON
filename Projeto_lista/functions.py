import os

def limpar():
    os.system('cls')


def validador():
    digitosnecessarios = 11

    cpf = input('Digite um CPF: ')
    limpar()
    while len(cpf) != digitosnecessarios:
        limpar()
        cpf = input('Digite o CPF novamente: ')
    if len(cpf) == 11:
        nove_digitos = cpf[:9]
        contador_regressivo = 10

        digito_1 = 0
        for digito in nove_digitos:
            digito_1 += int(digito) * contador_regressivo
            contador_regressivo -= 1
        digito_1 = (digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0 

        dez_digitos = cpf[:10]
        contador_regressivo = 11

        digito_2 = 0
        for digito in dez_digitos:
            digito_2 += int(digito) * contador_regressivo
            contador_regressivo -= 1
        digito_2 = (digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0 

        valido = str(digito_1) + str(digito_2)
        cpf2 = str(cpf[-2]) + str(cpf[-1])
        limpar()
        if valido == cpf2:
            ...
        else:
            print('CPF inválido')
        return cpf    


def validnome():
    while True:
        nome = input('Digite nome do cliente: ')
        if nome.isalpha():
            if len(nome) < 3:
                limpar()
                print('Nome muito curto!')
                continue
            if len(nome) > 14:
                limpar()
                print('Nome muito extenso!')
                continue
            else:
                return nome                        
        else:
            limpar()
            print('O nome deve conter apenas letras. Tente novamente.')


    


def idadevalid():
    idade = int(input('Digite a idade do cliente: '))
    while idade <= 8 or idade >= 110:
        limpar()
        print('Idade inválida, digite novamente:')
        idade = int(input("Idade: "))
    idade = str(idade)
    return idade    






