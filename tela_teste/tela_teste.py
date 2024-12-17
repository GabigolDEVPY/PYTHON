from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import sys
from backend import teste_base_dir as tb


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
    users = tb.load_file()
    nome = {"Nome":linha.text()}
    lista.addItem(f"Nome: {nome["Nome"]}")
    users.append(nome)
    tb.save_file(users)

button.clicked.connect(add_nome)

def charge_names():
    users = tb.load_file()
    for user in users:
        lista.addItem(f"Nome: {user["Nome"]}")

charge_names()
window.show()
app.exec()