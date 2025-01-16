from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulando um banco de dados
dados = {
    "Gabriel": {"idade": 25, "cidade": "São Paulo"},
    "Gabi": {"idade": 22, "cidade": "Rio de Janeiro"},
    "Moranguinha": {"idade": 23, "cidade": "Curitiba"},
}

@app.route('/buscar', methods=['GET'])
def buscar():
    nome = request.args.get('nome')  # Pega o nome na URL
    if nome in dados:
        return jsonify({nome: dados[nome]})  # Retorna o resultado em JSON
    else:
        return jsonify({"erro": "Nome não encontrado!"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

