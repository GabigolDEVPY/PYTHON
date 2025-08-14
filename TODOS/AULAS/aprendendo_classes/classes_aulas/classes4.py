class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor
        self.fabricante = fabricante

    def exibir_infos(self):
        print(self.nome)
        print(self.motor.nome)
        print(self.fabricante.nome)

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

motor = Motor("V12")
fabricante1 = Fabricante("FIAT")
gol = Carro("gol", motor, fabricante1)

gol.exibir_infos()