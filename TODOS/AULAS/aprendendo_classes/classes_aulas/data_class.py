from dataclasses import dataclass

@dataclass
class Pessoa:
    name: str
    sobrenome: str
    
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    
    
if __name__ == "__main__":
    p1 = Pessoa("luiz", 30)    
    print(p1.idade)