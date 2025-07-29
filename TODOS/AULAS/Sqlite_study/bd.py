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

connection.commit()

cursor.execute(
    f'INSERT INTO {TABLE_NAME} (nome)'
    'VALUES (?)',
    ('Gabriel',)
)

cursor.execute('UPDATE usuarios SET nome = ? WHERE id = ')

connection.commit()

cursor.execute(f"SELECT * FROM {TABLE_NAME}")
result = cursor.fetchall()
print(result)