from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys

app = QApplication(sys.argv)
window = QMainWindow()
layout = QGridLayout()
central_widget = QWidget()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

lista = QListWidget()
linha = QLineEdit()
linha.setPlaceholderText("Type name")
button = QPushButton("BOTAO")


layout.addWidget(button)
layout.addWidget(lista)
layout.addWidget(linha)


def add_nome():
    nome = linha.text()
    lista.addItem(nome)

button.clicked.connect(add_nome)

window.show()
app.exec()