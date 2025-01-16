from flask import Flask

app = Flask(__name__)

dados = {
    "Gabriel": "sao paulo",
    "Gabriela": "sao paulo",
    "ramdom": "sao paulo"
}
lista = ["gabriel", "eu"]

@app.route("/buscar/nome=<nome>", methods= ["GET"])
def buscar(nome):
    if nome in dados:
        return lista
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')    
    