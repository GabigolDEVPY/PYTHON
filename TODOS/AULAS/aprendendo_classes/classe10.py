from flask import Flask, render_template, request, session
app = Flask(__name__)

clientes = [
    {"id": 1, "nome": "gabriel", "idade": 20,  "login": "gabgab", "senha": "12345678", "value": 1000},
    {"id": 2, "nome": "pele", "idade": 25,  "login": "pele55", "senha": "12345678", "value": 2000}
]

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar_idade(self):
        print(self.idade)


class Client():
    def __init__(self, id):
        for cliente in clientes:
            if id == cliente["id"]:
                self.nome, 
            
    class Pessoa():
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    def __init__(self, id,  nome, idade, login, senha, value):
        super().__init__(nome, idade)
        self.login = login
        self.senha = senha
        self.value = value
        self.id = id


@app.route("/login2", methods=["POST"])
def return_user2():
    dados = request.get_json()
    print(dados)
    for cliente in clientes:
        if dados['id'] == cliente["id"]:
            cliente = Client(**cliente)
            return f"Esse é o cliente: {cliente.nome}, {cliente.value}" 
    return "error"    

app.run(debug=True)    


class Carro:
    class Motor:
        def __init__(self, potencia):
            self.potencia = potencia

    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Carro.Motor(potencia_motor)

carro = Carro("Fusca", 50)
print(carro.motor.potencia)  # 50