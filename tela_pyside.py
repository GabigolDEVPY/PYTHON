from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

lista_user = [
    {"nome": "gabriel", "cpf": "56453"},
    {"nome": "gabi", "cpf": "44534"},
]


app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.resize(400, 500)

botao1 = QPushButton("Botao")
botao1.setStyleSheet('font-size: 40px; color: black;')
lista = QListWidget()

linha = QLineEdit()
linha.setPlaceholderText("Type thing here")

layout = QGridLayout()
central_widget.setLayout(layout)

def add_frase():
    texto = linha.text()
    lista.addItem(texto)

botao1.clicked.connect(add_frase)

for user in lista_user:
    lista.addItem(f"Name: {user["nome"]}    CPF: {user["cpf"]}")
    

layout.addWidget(botao1)
layout.addWidget(lista)
layout.addWidget(linha)


window.show()
app.exec()

