import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="Gabriel",
        password="Gabrielrochadias12",
        database="data_base"
    )

connection = get_connection()
cursor = connection.cursor(dictionary=True)
comand = ("SELECT * FROM usuarios")
cursor.execute(comand)
result = cursor.fetchone()
print(result)