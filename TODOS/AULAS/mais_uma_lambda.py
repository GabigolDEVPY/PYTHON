def secondnumlambda(num):
    return num + 10 
    

def multiplica(x, y, quantidade):
    result = x - y
    lista = [(num * result) - 10 for num in range(quantidade - 200)]
    print(lista)
    print(result, quantidade)
    
multiplica((lambda x, y: x - y )(5, 10), 10, (lambda x, y: x * y - 4 + 30)(10, secondnumlambda(10)))    

