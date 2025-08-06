from flask import Flask, render_template, request, session
app = Flask(__name__)
app.config['SECRET_KEY'] = "amor de morango 123"

clientes = [
    {"id": 1, "nome": "gabriel", "idade": 20,  "login": "gabgab", "senha": "12345678", "value": 1000},
    {"id": 2, "nome": "pele", "idade": 25,  "login": "pele55", "senha": "12345678", "value": 2000}
]

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Client(Pessoa):
    def __init__(self,  nome, idade, login, senha, value, id):
        super().__init__(nome, idade)
        self.login = login
        self.senha = senha
        self.value = value
        self.id = id

def return_cliente(id_cliente):
    for cliente in clientes:
        if id_cliente['id'] == cliente["id"]:
            session['id'] = cliente['id']
            cliente = Client(**cliente)
            return cliente

@app.route("/login", methods=["POST"])
def return_user():
    id_cliente = request.get_json()
    cliente = return_cliente(id_cliente)
    return (cliente.__dict__)

app.run(debug=True, port=5020, host='0.0.0.0')    
