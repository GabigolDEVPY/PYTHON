class animal:
    def __init__(self, altura, peso, nome):
        self.nome = nome
        self.altura = altura
        self.peso = peso
    
    def cagar(self):
        print(f"o {self.nome} está cagando")

class gato(animal):
    def __init__(self, altura, peso, nome, raca, cor):
        super().__init__(altura, peso, nome)
        self.raca = raca
        self.cor = cor
        
    def miar(self):
        print(f"o {self.nome} está miando")




gato = gato(1.40, 20, "sandy", "vira-lata", "branco")
print(gato.nome)                