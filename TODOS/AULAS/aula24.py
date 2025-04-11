import os
digitosnecessarios = 11

while True:
    sair = input('deseja sair ?').lower().startswith('s')
    if sair:
        break
    else:
            os.system('cls')
            cpf = input('Digite um CPF apenas em números: ')
    os.system('cls')
    while len(cpf) != digitosnecessarios:
        os.system('cls')
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
        os.system('cls')
        if valido == cpf2:
            print('CPF válido')
        else:
            print('CPF inválido')  








