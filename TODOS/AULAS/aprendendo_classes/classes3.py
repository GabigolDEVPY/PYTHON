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
