import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gabrielrochadias12",
        database="banco"
    )

connection = get_connection()
cursor = connection.cursor(dictionary=True)
comand = ("SELECT * FROM users")
cursor.execute(comand)
result = cursor.fetchone()
print(result)