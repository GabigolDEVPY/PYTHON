def criar_divisor(dividir):
    def divisor(number):
        x = 4
        return number / dividir
    return divisor
    
tal = criar_divisor(4)(12) # resultado da função = 3


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        global x
        x = 4        
        return numero * multiplicador
    return multiplicar


strong = criar_multiplicador(4)(6) # resultado da função = 24


somma = strong * tal # essa variável soma os resultados/ retorno das duas funções 
print(somma)