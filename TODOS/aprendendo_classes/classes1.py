class Pessoa():
    def __init__(self, nome, sobrenome, idade, peso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.peso = peso
        
    def deixa_maiusculo(self):
        return self.nome.upper()


pessoa1 = Pessoa("gabriel", "rocha", 18, 79)

print(pessoa1.deixa_maiusculo())