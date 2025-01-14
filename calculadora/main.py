from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    
    label1 = QLabel("o meu text")
    label1.setStyleSheet('font-size: 40px;')
    window.addWidgetToVLayout(label1)
    window.adjustFixedSize()
    
    window.show()
    app.exec()