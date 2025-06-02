<<<<<<< HEAD
class camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    def filmar(self):
        if self.filmando:
            return print("Já está filmando")
        self.filmando = True
        print(self.filmando)
        print(f"a {self.nome} está filmando")
    def parar_filmar(self):
        if not self.filmando:
            print(f"a {self.nome} não está filmando")
            return
        print(f"a {self.nome} está parando de filmar")
        self.filmando = False
    def fotografar(self):
        if self.filmando:
            print("não é possível fotografar quando estiver filmando")
            return
        print(self.nome, "Está fotografando!")
    
        
camera1 = camera("camera1")
print(camera1.filmando)
camera1.filmar()
camera1.filmar()
camera1.fotografar()
camera1.parar_filmar()
camera1.fotografar()
=======
class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()    

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco 

carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())
>>>>>>> 6b5cb26 (add files corrupted)
