class Pessoa():
    def __init__(self, nome, sobrenome, idade, peso):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.peso = peso
        

    
Pessoa1 = Pessoa("gabriel", "rocha", 18, 78 )
pessoa2 = Pessoa("não", "sei", 18, None)

print(Pessoa1.nome)    
print(pessoa2.peso)    
