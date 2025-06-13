from flask import Flask, make_response, jsonify, request
import mysql.connector

def get_connection():
    connect = mysql.connector.connect(
        host="localhost",
        user="Gabriel",
        password="Gabrielrochadias12",
        database="usuarios"
    )
    return connect

def curl(comando, params=None):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

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
        params = (user_data['nome'], int(user_data["idade"]), user_data['telefone'])
        comando = "INSERT INTO usuarios (nome, idade, telefone) VALUES (%s, %s, %s)"
        return curl(comando, params)
    
    @staticmethod
    def listar_id(id):
        params = (id,)
        print(params)
        comando = "SELECT * FROM usuarios WHERE id_user = %s"
        return curl(comando, params)
    
    @staticmethod
    def delete(id):
        params = (id,)
        comando = "DELETE FROM usuarios WHERE id_user = %s"
        return curl(comando, params)
    
    @staticmethod
    def update(id, params):
        id_user = (id,)
        user_data = (curl("SELECT * FROM usuarios WHERE id_user = %s", id_user))[0]
        user_update = params
        user_data.update(user_update)
        params = (user_data['nome'], user_data['idade'], user_data['telefone'], id)
        print(params)
        user_updated =  curl("UPDATE usuarios SET nome = %s, idade = %s, telefone = %s WHERE id_user = %s", params)
        return ("este é o user, atualizado", user_data)

app = Flask(__name__)

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
    app.run(debug=True, host="localhost", port=3000)