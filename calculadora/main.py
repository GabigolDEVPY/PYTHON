from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys


def janela():
    window = QMainWindow()
    central_widget = QWidget()
    window.setCentralWidget(central_widget)
    layout_principal = QVBoxLayout()
    central_widget.setLayout(layout_principal)
    
    visor = QLabel("text")
    visor.setStyleSheet("border-radius: 5px; color: #800000; border: 2px solid #400080;font-size: 36px;")
    visor.setFixedSize(300, 33)
    layout_principal.addWidget(visor)
    botao1 = QPushButton("1")
    layout_principal.addWidget(botao1)
    
    botao1.clicked.connect(lambda: visor.setText("1"))
    
    window.show()
    app.exec()
    
app = QApplication(sys.argv)
janela()
    