from flask import Flask, jsonify
from local_dados import save_data, load_data

app = Flask(__name__)

dados = load_data()

@app.route("/buscar=<nome>", methods=["GET"])
def buscar(nome):
    for chave, dado in dados.items():
        if chave == nome:
                return ({chave: dado})

if __name__ == "__main__":
    app.run(port=5000, host="localhost", debug=True)