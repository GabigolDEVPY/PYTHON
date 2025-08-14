import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "usuarios"
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT'
    ')'
)

sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(nome)'
    'VALUES'
    '(?)'
)

cursor.execute(sql, ("gabriel",))

cursor.executemany(sql, (("gabriel",), ("gabigol",), ("gabigolas",)))

sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(nome)'
    'VALUES'
    '(:nome)'
)
cursor.execute(f'DELETE FROM {TABLE_NAME}')
connection.commit()

cursor.executemany(sql, (
    {'nome': "Gabriel1"},
    {'nome': "Gabriel2"},
    {'nome': "Gabriel3"},
))
    
connection.commit()

cursor.execute(f'SELECT * FROM {TABLE_NAME} LIMIT 2')
result = cursor.fetchall()
print(result)

cursor.execute(f'SELECT * FROM {TABLE_NAME}')
row = cursor.fetchone()
print(row)

cursor.execute(f"DELETE FROM {TABLE_NAME}")
connection.commit()

cursor.execute(f"SELECT * FROM {TABLE_NAME}")
result = cursor.fetchall()
print(result)

cursor.executemany(f"INSERT INTO {TABLE_NAME} (nome) VALUES (:nome)", ({"nome": "Gabigooolas"},{"nome": "gabriel"}))
cursor.execute(f"UPDATE {TABLE_NAME} SET nome = ? WHERE id = 153", ("Gabigolllllllllllllllllllllllllllllllllll",))
cursor.execute(f"UPDATE {TABLE_NAME} SET nome = ? WHERE id = 153", ("Gabigolllllllllllllllllllllllllllllllllll",))
connection.commit()












cursor.close()
connection.close()





