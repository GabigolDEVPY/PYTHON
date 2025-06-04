<<<<<<< HEAD
class Pessoa():
    def __init__(self, nome, sobrenome, idade, peso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.peso = peso
        
    def deixa_maiusculo(self):
        return self.nome.upper()


pessoa1 = Pessoa("gabriel", "rocha", 18, 79)

=======
class Pessoa():
    def __init__(self, nome, sobrenome, idade, peso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.peso = peso
        
    def deixa_maiusculo(self):
        return self.nome.upper()


pessoa1 = Pessoa("gabriel", "rocha", 18, 79)

>>>>>>> 6b5cb26 (add files corrupted)
print(pessoa1.deixa_maiusculo())