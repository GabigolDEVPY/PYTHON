import random

quantidade = int(input('Quantos CPFs deseja gerar ?'))

for CPF in range(quantidade):
    
    cpf_gerado = ''

    for digito in range(9):
        cpf_gerado += str(random.randint(0,9))

    primeiro_digito = 0
    contador_regressivo = 10

    for digito in cpf_gerado:
        primeiro_digito += int(digito) * contador_regressivo
        contador_regressivo -= 1
    primeiro_digito = (primeiro_digito * 10) % 11  
    primeiro_digito = primeiro_digito if primeiro_digito < 10 else 0    
        

    cpf_gerado = cpf_gerado + str(primeiro_digito)

    segundo_digito = 0
    contador_regressivo = 11

    for digito in cpf_gerado:
        segundo_digito += int(digito) * contador_regressivo
        contador_regressivo -= 1
    segundo_digito = (segundo_digito * 10) % 11  
    segundo_digito = segundo_digito if segundo_digito < 10 else 0 

    cpf_gerado = cpf_gerado + str(segundo_digito)


    print(cpf_gerado)