from unittest import result
import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gabrielrochadias12",
        database="teste"
    )
    return conn


def execute_comand(comand, *args):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(comand, (args))
    rows = cursor.rowcount
    result = cursor.fetchall()
    conn.commit()
    cursor.close
    conn.close
    if rows:
        return rows
    if result:
        return result
