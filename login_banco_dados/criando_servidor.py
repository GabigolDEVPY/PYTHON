from flask import Flask, jsonify
from acessar_banco import save_data, load_data

app = Flask(__name__)

users = load_data()

@app.route("/inicio")
def incio():
    return "BEM VINDO ao LIXOSITE"

@app.route("/inicio/login=<login>&senha=<senha>")
def logar(login, senha):
    print(users)
    for user in users:
        if user["login"] == login and user["senha"]:
            return jsonify(user["itens"])
            
if __name__ == "__main__":
    app.run(port=5000, host="localhost", debug=True)        