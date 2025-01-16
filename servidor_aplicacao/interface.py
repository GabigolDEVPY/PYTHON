from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
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
        return "nada"
        




    # Exibindo a janela
    window.setWindowTitle("Busca no Servidor")
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec())


janela()