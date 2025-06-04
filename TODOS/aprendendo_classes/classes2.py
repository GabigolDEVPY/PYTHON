class animal:
    comida= "carne"    
    def __init__(self, nome):
        self.nome = nome
    def acao(self):
        print(f"O {self.nome} está comendo {self.comida}")
    def escolher(self, comida):
        print(f"O {self.nome} está comendo {comida}")
        
animal1 = animal("carneiro")
animal1.acao()  
animal1.escolher("feijão")      