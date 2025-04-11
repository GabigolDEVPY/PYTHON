from flask import Flask, jsonify, request

app = Flask(__name__)

vagas = [
    {"nome": "vaga 1", "estado": "vazia"},
    {"nome": "vaga 2", "estado": "vazia"},
    {"nome": "vaga 3", "estado": "vazia"},
    {"nome": "vaga 4", "estado": "vazia"},
]


@app.route("/inicio", methods=["GET", "PUT"])
def return_vagas():
    if request.method == "PUT":
        marcar = request.get_json()
        print(marcar)
        for vaga in vagas:
            if marcar["nome"] == vaga["nome"]:
                if vaga["estado"] == "ocupado":
                    return "Esse lugar já está ocupado"
                else:
                    vaga["estado"] = "ocupado"
                    
    return jsonify(vagas)



if __name__ == "__main__":
    app.run(debug=True)