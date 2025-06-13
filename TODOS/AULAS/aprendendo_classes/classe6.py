class Pessoa:
    def __init__(self, nome, sobrenome, tipo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.tipo = tipo

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, tipo, permissao, vip, ltv):
        super().__init__(nome, sobrenome, tipo)
        self.vip = vip
        self.permissao = permissao
        self.ltv = ltv
    ...


cliente = Cliente("gabriel", "sobrenome", "humano", "0", 1, 5)    
print(cliente.nome, cliente.tipo, cliente.vip, cliente.permissao, cliente.ltv)