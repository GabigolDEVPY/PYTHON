from flask import Flask, jsonify, request
import retornandolista

app = Flask(__name__)
dados = []

@app.route('/calcular/<int:valor>&<int:numero>', methods= ['GET'])
def inicio(valor, numero):
    return jsonify(retornandolista.retornar(valor, numero))

@app.route('/cadastrar/<nome>', methods=['PUT'])
def cadastrar(nome):
    result = request.json
    dados.append(str(result))
    return f"nome {nome} cadastrado"

@app.route('/consultar/nome=<nome>', methods= ['GET'])
def consultar(nome):
    if nome in dados:
        return "Nome existe na lista"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)