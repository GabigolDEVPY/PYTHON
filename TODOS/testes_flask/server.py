from flask import Flask

app = Flask(__name__)

dados = {
    "Gabriel": "sao paulo",
    "Gabriela": ["sao pauloooooo"],
    "ramdom": "sao paulo"
}
lista = ["gabriel", "eu"]

@app.route("/buscar/nome=<nome>", methods= ["GET"])
def buscar(nome):
    return dados.get(nome, "USUÁRIO NÃO ENCONTRADO")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')    
    