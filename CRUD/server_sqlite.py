from flask import Flask, make_response, jsonify, request
import sqlite3
from pathlib import Path
from flask_cors import CORS

FILE_PATH = Path(__file__).parent
DB_FILE = "db.sqlite3"
DB_LOCAL = FILE_PATH / DB_FILE

def get_connection():
    connect = sqlite3.connect(DB_LOCAL)
    return connect

def curl(comando, params=None):
    connection = get_connection()
    cursor = connection.cursor()

    if params:
        cursor.execute(comando, params,)
        result = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return result
    
    cursor.execute(comando)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

# classe users
class User:
    @staticmethod
    def listar_todos():
        return curl(comando="SELECT * FROM usuarios")
    
    @staticmethod
    def add_users(user_data):
        params = (user_data['nome'], user_data["idade"], user_data['telefone'])
        comando = "INSERT INTO usuarios (nome, idade, telefone) VALUES (?, ?, ?)"
        return curl(comando, params)
    
    @staticmethod
    def listar_id(id):
        params = (id,)
        print(params)
        comando = "SELECT * FROM usuarios WHERE id_user = ?"
        return curl(comando, params)
    
    @staticmethod
    def delete(id):
        params = (id,)
        comando = "DELETE FROM usuarios WHERE id_user = ?"
        return curl(comando, params)
    
    @staticmethod
    def update(id, params):
        id_user = (id,)
        user_data = (curl("SELECT * FROM usuarios WHERE id_user = ?", id_user))[0]
        user_update = params
        user_data = {
            "nome": user_data[1],
            "idade": user_data[2],
            "telefone": user_data[3]
        }
        user_data.update(user_update)
        params = (user_data['nome'], user_data['idade'], user_data['telefone'], id)
        print(params)
        user_updated =  curl("UPDATE usuarios SET nome = ?, idade = ?, telefone = ? WHERE id_user = ?", params)
        return ("este é o user, atualizado", user_data)

app = Flask(__name__)
CORS(app)



# CRIANDO AS ROTAS DA APLICAÇÃO 
@app.route("/listar/id/<int:id>", methods=["GET"])
def listar(id):
    return make_response(jsonify(User.listar_id(id)))

@app.route("/add", methods=["POST"])
def add():
    user_data = request.get_json()
    return make_response(jsonify(User.add_users(user_data)))

@app.route("/listar-todos", methods=["GET"])
def listar_todos():
    return make_response(jsonify(User.listar_todos()))

@app.route("/deletar/id/<int:id>", methods=["DELETE"])
def delete(id):
    return make_response(jsonify(User.delete(id)))

@app.route("/update/id/<int:id>", methods=["PUT", "GET"])
def update(id):
    params = request.get_json()
    print(params)
    return make_response(jsonify(User.update(id, params)))


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)