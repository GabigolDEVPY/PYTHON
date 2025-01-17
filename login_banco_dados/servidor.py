from flask import Flask, jsonify, request
from acessar_banco import save_data, load_data



app = Flask(__name__)


@app.route("/inicio", methods=["GET"])
def incio():
    return "BEM VINDO AO LIXOSITE"

@app.route("/login/login=<login>&senha=<senha>")
def logar(login, senha):
    users = load_data()
    print(users)
    for user in users:
        if user["login"] == login and user["senha"] == senha:
            return jsonify(user["saldo"])
    return jsonify({"error": "Usuário não encontrado"}), 404
    
@app.route("/register", methods=["PUT"])
def register():
    users = load_data()
    dados = request.json
    users.append(dados)
    save_data(users)

            
if __name__ == "__main__":
    app.run(port=5000, host="localhost", debug=True)        