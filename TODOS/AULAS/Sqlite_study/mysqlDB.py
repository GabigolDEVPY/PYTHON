import pymysql
from dotenv import load_dotenv 
import os

load_dotenv()

connection = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER")
)

TABLE_NAME = "customers"


with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS customers ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL,'
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
    

with connection:
    with connection.cursor() as cursor:
        sql = (
            f"INSERT INTO {TABLE_NAME}"
            "(nome, idade) "
            "VALUES "
            "(%(nome)s , %(idade)s)"
        )
        data = {
            "nome": "Gabigol",
            "idade": 20,
        }
        result = cursor.execute(sql, data)
        print(result)
    connection.commit()
