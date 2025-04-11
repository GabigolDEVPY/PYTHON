from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

lista_user = [
    {"nome": "gabriel", "cpf": "56453"},
    {"nome": "gabi", "cpf": "44534"},
]


app = QApplication(sys.argv) # inicia a aplicação, que vai ficar no loop

window = QMainWindow() # inicia a janela que vai ficar rodando

layout = QGridLayout() # cria um layout

central_widget = QWidget() # cria um widget central

central_widget.setLayout(layout)  # seleciona o layout do cetral widget passando layout como argumento

window.setCentralWidget(central_widget) # passa o central widget passando o central_widget como widget central, argumento

window.resize(400, 500)   # cria o tamanho ja janela quando o aplicativo for iniciado

botao1 = QPushButton("Botao") # cria um botão

botao1.setStyleSheet('font-size: 40px; color: black;')  # faz alteração de tamanho de fonte e cor da fonte do botão!

lista = QListWidget() # cria uma QlistWidget

linha = QLineEdit() #cria uma QLineEdit

linha.setPlaceholderText("Type thing here") # define oque será escrito na linha 


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

