from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import requests
import sys


def janela():
    app = QApplication(sys.argv)
    app.setStyle("Windows11")

    # Configurando a janela principal
    window = QMainWindow()
    central_Widget = QWidget()
    window.setCentralWidget(central_Widget)
    layout_central = QVBoxLayout()  # Layout central
    central_Widget.setLayout(layout_central)

    # Criando widgets
    busca = QLineEdit()
    busca.setMinimumSize(300, 25)
    buton = QPushButton("Buscar")
    buton.setMinimumSize(310, 40)
    resultados = QListWidget()

    # Adicionando widgets ao layout
    layout_central.addWidget(busca)
    layout_central.addWidget(resultados)
    layout_central.addWidget(buton)


    def conectar_servidor():
        print("deu certo")
        nome = busca.text()
        print(nome)
        if not nome:
            return resultados.addItem("digite um nome")
        url = f"http://localhost:5000/buscar={nome}"
        result = requests.get(url)
        print(result)
        resultados.addItem(result.text)
        

    buton.clicked.connect(lambda: conectar_servidor())



    # Exibindo a janela
    window.setWindowTitle("Busca no Servidor")
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())


janela()