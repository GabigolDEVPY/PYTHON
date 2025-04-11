dados = {"nome": "gabriel", "idade": 18}

def mostrar_dados(nome, idade):
    print(f"O nome {nome} e idade {idade}")
    
    
mostrar_dados(**dados)    