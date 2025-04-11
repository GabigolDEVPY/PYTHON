from flask import Flask
from outro_modulo import saber_name_modulo

app = Flask(__name__)
print(__name__)
saber_name_modulo()

@app.route("/")
def pagina_inicial():
    return(saber_name_modulo())

@app.route("/lista")
def pagina_listas():
    return("Era pra ser uma lista")

if __name__ == "__main__":
    app.run(debug=True)