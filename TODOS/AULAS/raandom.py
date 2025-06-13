def receber(valor):
    lista = [1, 2, 3, 4]
    for p in valor:
        if len(p) >= 5:
            lista = None
        else:
            lista.append(p)

def cadastrar():
    while True:
        option = input("S para sair, E para cadastrar: ").upper()
        if option == "E":    
            nome = input("nome: ")
            preco = input("preço: ") 
            product = {
                "nome": nome,
                "preco": preco
            }
            products = []
            products.append(product)
            print(products)
        elif option == "S":
            break
        else:
            continue    
cadastrar()