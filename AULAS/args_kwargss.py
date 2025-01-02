def somar(*args):
    return sum(args)

print(somar(1, 2, 3))  # Saída: 6
print(somar(10, 20, 30, 40))  # Saída: 100


def mostrar_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"chave {chave} valor {valor}")

mostrar_dados(nome="gabriel", idade= 19, altura=1.79)

def misturados(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    for chave, valor in kwargs.items():
        print(chave, valor)
    
misturados(1, 2, 3, 4, 5, 6, nome = "gabriel", idade = "19", altura = "1.79")
# * desempacotando lista
numeros = [1, 2, 3]
print(somar(*numeros))  # Saída: 6

dados = {"nome": "Gabigordo", "idade": 25}
mostrar_dados(**dados)