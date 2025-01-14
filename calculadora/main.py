from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys

if __name__ == '__main__':
    def janela():
        window = QMainWindow()
        central_widget = QWidget()
        window.setCentralWidget(central_widget)
        layout_principal = QVBoxLayout()
        central_widget.setLayout(layout_principal)
        
        visor = QLabel("text")
        visor.setStyleSheet("border-radius: 5px; color: #808080; border: 2px solid #e44501;font-size: 32px;")
        visor.setFixedSize(300, 33)
        layout_principal.addWidget(visor)
        botao1 = QPushButton("1")
        layout_principal.addWidget(botao1)
        
        botao1.clicked.connect(lambda: visor.setText("1"))
        
        window.show()
        app.exec()
        
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    janela()
    