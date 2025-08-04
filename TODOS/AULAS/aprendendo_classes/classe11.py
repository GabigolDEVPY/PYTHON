class Carro():
    def __init__(self, cor, peso):
        self.cor = cor
        self.peso = peso
        self.motor = False

    def andar(self, km):
        if self.motor == True:
            return print(f"O carro andou {km} KM")    
        print("O Motor está deslidago, não é possível andar")

    
    def ligar(self):
        self.motor = True
        print("Motor Ligado!")

    def desligar(self):
        self.motor = False
        print("Motor Desligado!")

    def statusMotor(self):
        if self.motor == True:
            return print("Motor está ligado")
        print("Motor está desligado")


carro = Carro("Amarelo", 1400)
print(carro.cor)
print(carro.peso)
carro.statusMotor()
carro.ligar()
carro.desligar()







