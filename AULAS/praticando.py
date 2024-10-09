

def somar(numero, numero2):
        return numero + numero2
        
def inteiros(numero, numero3):
    valor = numero + numero3
    def somas2():
        return valor + 4
    
    return somas2
        







resultado_somar = somar(2,5)
resultado = inteiros(4,5)()
print(resultado_somar + resultado)
